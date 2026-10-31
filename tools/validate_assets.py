#!/usr/bin/env python3
"""Technical fixed-grid contract validation, not an artistic-quality certificate."""
import argparse,hashlib,json,re,sys
from pathlib import Path
from PIL import Image

CORE=['hero','vera','max','anya','lev','polina','artem','denis']
FULL=CORE+['sonya','timur','oleg','nika','irina']
PROPS=['floor-oak','floor-tile','floor-carpet','wall-office','desk-main','chair-north','chair-south','meeting-glass','door-office','coffee-machine','printer','locker','sofa','plant-small','plant-large','whiteboard','interaction-icons','dialogue-panel','workstation-panel']
REQUIRED={}
for state,count in [('idle',4),('walk',6),('talk',4)]:
    for facing in ['south','west','east','north']:REQUIRED[state+'-'+facing]=count
REQUIRED.update({'sit-type-north':6,'sit-type-south':6,'drink-south':6,'interact-south':4,'react-south':4})

def contained(root,relative):
    if not isinstance(relative,str) or not relative or Path(relative).is_absolute() or '\\' in relative:
        raise ValueError('nonempty relative forward-slash path required')
    root=root.resolve(); target=(root/relative).resolve()
    if not target.is_relative_to(root):raise ValueError('path escapes root')
    return target

def validate(repo,manifest,gate):
    errors=[];warnings=[]
    def fail(msg):errors.append(msg)
    try:
        path=contained(repo,manifest); data=json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:return {'passed':False,'errors':['manifest: '+str(exc)],'warnings':[]}
    if data.get('schemaVersion')!=1:fail('schemaVersion must be1')
    if data.get('contractVersion')!='1.0.0':fail('unsupported contractVersion')
    if data.get('gate')!=gate:fail('manifest gate differs from requested gate')
    entries=data.get('assets');entries=entries if isinstance(entries,list) else []
    if not entries:fail('assets must be a nonempty array')
    ids=[];byid={};image_root=repo/'public/assets'
    for index,a in enumerate(entries):
        if not isinstance(a,dict):fail(f'entry{index}: object required');continue
        aid=a.get('id',f'entry-{index}');ids.append(aid);byid[aid]=a
        try:
            if not isinstance(aid,str) or not re.fullmatch(r'[a-z][a-z0-9-]*',aid):raise ValueError('invalid ID')
            if a.get('status')!='approved':raise ValueError('status must be approved')
            if a.get('kind') not in ['character','prop','tileset','portrait','ui','effect']:raise ValueError('invalid runtime kind (reference art forbidden)')
            p=contained(image_root,a.get('path'))
            if p.suffix.lower()!='.png':raise ValueError('runtime image must be PNG')
            raw=p.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=a.get('sha256'):raise ValueError('SHA256 mismatch')
            with Image.open(p) as opened:
                if opened.format!='PNG':raise ValueError('file is not actually PNG')
                image=opened.convert('RGBA');image.load()
            if image.size!=(a.get('width'),a.get('height')):raise ValueError('image dimensions mismatch')
            if max(image.size)>2048:raise ValueError('image exceeds2048px atlas budget')
            source=contained(repo,a.get('sourcePath'))
            if not source.is_file():raise ValueError('editable source missing')
            provenance=a.get('provenance',{})
            if not provenance.get('method') or not provenance.get('rightsNote'):raise ValueError('provenance method/rightsNote missing')
            if a.get('kind')!='effect':
                if any(v not in (0,255) for v in image.getchannel('A').getdata()):raise ValueError('fractional alpha outside declared effect')
            if a.get('kind')=='portrait' and image.size!=(96,96):raise ValueError('portrait must be96x96')
            if a.get('kind')=='tileset':
                tile=a.get('tile',{})
                if tile!={'width':16,'height':16,'spacing':0,'margin':0}:raise ValueError('tileset grid must be16x16, spacing/margin0')
                if image.width%16 or image.height%16:raise ValueError('tileset dimensions not divisible by16')
            if a.get('kind')=='character' or 'animations' in a:
                s=a.get('sheet',{});fw=s.get('frameWidth');fh=s.get('frameHeight');cols=s.get('columns');rows=s.get('rows')
                if not all(type(x) is int and x>0 for x in [fw,fh,cols,rows]):raise ValueError('positive integer sheet geometry required')
                if image.size!=(fw*cols,fh*rows):raise ValueError('sheet geometry differs from image')
                animations=a.get('animations',[])
                if not isinstance(animations,list) or not animations:raise ValueError('animation list missing')
                seen=set();frame_entries=0;used=set()
                for anim in animations:
                    key=anim.get('key');frames=anim.get('frames');dur=anim.get('durationsMs')
                    if not isinstance(key,str) or key in seen:raise ValueError('missing/duplicate animation key')
                    seen.add(key)
                    if not isinstance(frames,list) or not frames:raise ValueError(key+': frames missing')
                    if not isinstance(dur,list) or len(dur)!=len(frames):raise ValueError(key+': duration count mismatch')
                    if any(type(d) is not int or d<40 or d>5000 for d in dur):raise ValueError(key+': invalid durations')
                    if type(anim.get('loop')) is not bool:raise ValueError(key+': loop must be boolean')
                    if any(type(f) is not int or f<0 or f>=cols*rows for f in frames):raise ValueError(key+': frame out of bounds')
                    frame_entries+=len(frames);used.update(frames)
                    hashes=[]
                    for f in frames:
                        cell=image.crop(((f%cols)*fw,(f//cols)*fh,(f%cols+1)*fw,(f//cols+1)*fh))
                        if not cell.getchannel('A').getbbox():raise ValueError(key+': empty referenced cel')
                        hashes.append(hashlib.sha256(cell.tobytes()).hexdigest())
                        if a.get('kind')=='character' and len(cell.getcolors(fw*fh) or [])>25:raise ValueError(key+': over24 solid colors plus transparency')
                    if key.startswith('walk-') and len(set(hashes))!=6:raise ValueError(key+': requires6 distinct visual cels')
                    if a.get('kind')=='character' and key in REQUIRED and len(frames)!=REQUIRED[key]:raise ValueError(key+': wrong frame count')
                if a.get('kind')=='character':
                    if (fw,fh,cols,rows)!=(32,48,8,11):raise ValueError('character sheet must be32x48,8x11')
                    if a.get('origin')!={'x':0.5,'y':1} or a.get('footAnchor')!={'x':16,'y':44}:raise ValueError('character origin/footAnchor mismatch')
                    if a.get('collider')!={'width':12,'height':8,'anchor':'foot'}:raise ValueError('character foot collider mismatch')
                    if set(REQUIRED)!=seen:raise ValueError('character animation key set differs from contract')
                    if frame_entries!=82:raise ValueError('character must declare82 frame entries')
                    for f in range(82,88):
                        if image.crop(((f%cols)*fw,(f//cols)*fh,(f%cols+1)*fw,(f//cols+1)*fh)).getchannel('A').getbbox():raise ValueError('trailing6 cells must be transparent')
                    if not image.getchannel('A').getextrema()[0]==0:raise ValueError('character sheet lacks transparency')
        except Exception as exc:fail(f'{aid}: {exc}')
    if len(ids)!=len(set(ids)):fail('duplicate asset IDs')
    chars=FULL if gate=='full' else CORE
    required=chars+PROPS+['portrait-'+c for c in chars]
    missing=sorted(set(required)-set(ids))
    if missing:fail('missing required IDs: '+', '.join(missing))
    for c in chars:
        if c in byid and byid[c].get('kind')!='character':fail(c+': required character has wrong kind')
    if gate=='full':warnings.append('Full-area story coverage requires separate visual/content inventory review; this validator checks declared files and cast, not semantic completeness.')
    warnings.append('Manual pixel-art, pose, timing, editability, rights and in-engine review still required.')
    return {'passed':not errors,'gate':gate,'assetCount':len(entries),'errors':errors,'warnings':warnings}

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--manifest',default='public/assets/manifest.json');p.add_argument('--gate',choices=['core','full'],default='core');a=p.parse_args()
    result=validate(a.repo,a.manifest,a.gate);print(json.dumps(result,indent=2));return 0 if result['passed'] else 1

if __name__=='__main__':sys.exit(main())
