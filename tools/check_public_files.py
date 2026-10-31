#!/usr/bin/env python3
import argparse,json,re,subprocess,sys
from pathlib import Path,PurePosixPath

def private(path):
    parts=PurePosixPath(path).parts;name=parts[-1] if parts else ''
    return (any(x in {'.agents','.claude','.codex','.ai-work','node_modules','scratch','tmp','__pycache__','prompts'} for x in parts)
      or name in {'AGENTS.md','CLAUDE.md','.env'} or (name.startswith('.env.') and name!='.env.example')
      or name.endswith(('_PROMPT.md','.log','.pyc')) or bool(re.search(r'(?:MASTER_)?PROMPT',name,re.I)))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True,type=Path);p.add_argument('--staged',action='store_true');a=p.parse_args()
    cmd=['git','-C',str(a.repo),'diff','--cached','--name-only','--diff-filter=ACMR','-z'] if a.staged else ['git','-C',str(a.repo),'ls-files','-z']
    files=subprocess.check_output(cmd).decode('utf-8').split('\0');bad=[f for f in files if f and private(f)]
    print(json.dumps({'passed':not bad,'checked':len([f for f in files if f]),'privateFiles':bad,'note':'Filename hygiene guard; inspect the staged diff for contents and secrets as well.'},indent=2));sys.exit(1 if bad else 0)
