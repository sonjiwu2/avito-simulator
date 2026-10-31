#!/usr/bin/env python3
import json,sys,fnmatch
from pathlib import Path

def check(path):
    d=json.loads(Path(path).read_text(encoding='utf-8'));errors=[];events=d.get('events',[]);days=d.get('days',[]);ids=[e.get('id') for e in events];byid={e['id']:e for e in events};choiceids=[];callbacks=[];shortlinks=0
    if d.get('contentStatus')!='planning-seed-not-runtime-content':errors.append('seed must honestly declare planning status')
    if len(days)!=30 or [x.get('day') for x in days]!=list(range(1,31)):errors.append('campaign day sequence must be1..30')
    if len(events)!=120 or len(set(ids))!=120:errors.append('expected120 unique event IDs')
    for day in days:
        for eid in day.get('anchorEventIds',[]):
            if eid not in byid:errors.append('unknown anchor '+str(eid))
    for e in events:
        choices=e.get('choices',[])
        if len(choices)!=3:errors.append(e['id']+': expected3 choices')
        for c in choices:
            choiceids.append(c.get('id'))
            if not c.get('label'):errors.append(e['id']+': empty choice')
        for c in e.get('delayedCallbacks',[]):
            callbacks.append(c.get('id'))
            memory=c.get('choiceMemory','')
            if not isinstance(memory,str) or not any(fnmatch.fnmatchcase(ch.get('id',''),memory) for ch in choices):errors.append(e['id']+': unknown choiceMemory reference')
            if c.get('targetEventId') not in byid:errors.append(e['id']+': unknown callback target')
            elif c.get('dueDay')!=byid[c['targetEventId']]['dayWindow'][0]:errors.append(e['id']+': callback day differs from target')
            if c.get('dueDay',0)<=e.get('dayWindow',[0])[0]:errors.append(e['id']+': callback not delayed')
            if 1<=c.get('dueDay',0)-e.get('dayWindow',[0])[0]<=7:shortlinks+=1
    if len(choiceids)!=len(set(choiceids)):errors.append('duplicate choice ID')
    if len(callbacks)<24 or len(callbacks)!=len(set(callbacks)):errors.append('insufficient/duplicate delayed links')
    if shortlinks<24:errors.append('expected at least24 links delayed1–7 days')
    if not any(c.get('dueDay',31)<=3 for e in events for c in e.get('delayedCallbacks',[])):errors.append('slice lacks callback by day3')
    for e in events:
        if e.get('locationHint')=='operations' and e.get('dayWindow',[0])[0]<13:errors.append(e['id']+': operations room locked before day13')
    return {'planningCatalogValid':not errors,'runtimeReady':False,'days':len(days),'events':len(events),'choices':len(choiceids),'delayedLinks':len(callbacks),'linksWithinSevenDays':shortlinks,'errors':errors,'note':'This checks a writing scaffold, not authored runtime dialogue, branch quality, puzzle validity or playability.'}

if __name__=='__main__':
    r=check(sys.argv[1]);print(json.dumps(r,indent=2));sys.exit(0 if r['planningCatalogValid'] else 1)
