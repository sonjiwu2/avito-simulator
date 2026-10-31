#!/usr/bin/env python3
"""Review actual image frames; no new artwork is generated."""
import argparse,json,sys
from pathlib import Path
from PIL import Image,ImageDraw
from validate_assets import contained

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True,type=Path);p.add_argument('--manifest',default='public/assets/manifest.json');p.add_argument('--asset',required=True);p.add_argument('--animation',required=True);p.add_argument('--out',required=True,type=Path);a=p.parse_args()
    data=json.loads(contained(a.repo,a.manifest).read_text());asset=next(x for x in data['assets'] if x['id']==a.asset);anim=next(x for x in asset['animations'] if x['key']==a.animation)
    source=Image.open(contained(a.repo/'public/assets',asset['path'])).convert('RGBA');s=asset['sheet'];w=s['frameWidth'];h=s['frameHeight'];cols=s['columns'];frames=[]
    for index in anim['frames']:
        frames.append(source.crop(((index%cols)*w,(index//cols)*h,(index%cols+1)*w,(index//cols+1)*h)))
    a.out.mkdir(parents=True,exist_ok=True);name=a.asset+'--'+a.animation
    contact=Image.new('RGBA',(w*len(frames),h),(240,237,226,255))
    for i,f in enumerate(frames):contact.alpha_composite(f,(i*w,0))
    contact.save(a.out/(name+'-contact-1x.png'))
    previews=[]
    for background,color in [('light',(244,238,221)),('dark',(37,42,58)),('checker',None)]:
        output=[]
        for f in frames:
            bg=Image.new('RGBA',(w,h),color+(255,) if color else (230,230,230,255))
            if color is None:
                draw=ImageDraw.Draw(bg)
                for yy in range(0,h,4):
                    for xx in range(0,w,4):
                        if (xx//4+yy//4)%2:draw.rectangle((xx,yy,xx+3,yy+3),fill=(195,195,195,255))
            bg.alpha_composite(f);output.append(bg.convert('RGB').resize((w*4,h*4),Image.Resampling.NEAREST))
        opts={'save_all':True,'append_images':output[1:],'duration':anim['durationsMs'],'disposal':2,'optimize':False}
        if anim['loop']:opts['loop']=0
        gifpath=a.out/(name+'-'+background+'-4x.gif');output[0].save(gifpath,**opts)
        with Image.open(gifpath) as encoded:
            encoded_durations=[]
            for n in range(encoded.n_frames):encoded.seek(n);encoded_durations.append(encoded.info.get('duration',0))
        apngpath=a.out/(name+'-'+background+'-4x.png')
        output[0].save(apngpath,save_all=True,append_images=output[1:],duration=anim['durationsMs'],loop=0 if anim['loop'] else 1,disposal=0,blend=0)
        previews.append({'background':background,'gif':str(gifpath),'gifDurationsMs':encoded_durations,'gifTotalMs':sum(encoded_durations),'apng':str(apngpath),'requestedTotalMs':sum(anim['durationsMs'])})
    print(json.dumps({'asset':a.asset,'animation':a.animation,'frames':len(frames),'requestedDurationMs':sum(anim['durationsMs']),'previews':previews,'note':'GIF has10ms timing granularity and may merge held cels; APNG preserves finer duration values. Runtime uses manifest timing.','output':str(a.out)}))

if __name__=='__main__':main()
