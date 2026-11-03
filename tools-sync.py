#!/usr/bin/env python3
"""진도표(gsmch-1f-plan.json)를 원본으로, planData가 들어 있는 모든 페이지에 똑같이 다시 넣는다.
사용: python3 tools-sync.py "2026-11-03 22:00" """
import json,re,sys,glob,datetime
d=json.load(open('gsmch-1f-plan.json'))
if len(sys.argv)>1: d['updated']=sys.argv[1]
json.dump(d,open('gsmch-1f-plan.json','w'),ensure_ascii=False,indent=1)
js=json.dumps(d,ensure_ascii=False)
bj=json.dumps(json.load(open('gsmch-1f-buy.json')),ensure_ascii=False)
for f in sorted(glob.glob('*.html')):
  s=open(f).read()
  if 'id="planData"' not in s: continue
  s2=re.sub(r'(<script[^>]*id="planData"[^>]*>)(.*?)(</script>)',lambda m:m.group(1)+js+m.group(3),s,flags=re.S)
  s2=re.sub(r'(<script[^>]*id="buyData"[^>]*>)(.*?)(</script>)',lambda m:m.group(1)+bj+m.group(3),s2,flags=re.S)
  if f=='gsmch-1f-calendar.html' and len(sys.argv)>1:
    t=sys.argv[1].replace('-','.')
    s2=re.sub(r'업데이트 2026\.\d\d\.\d\d \d\d:\d\d','업데이트 '+t,s2)
  open(f,'w').write(s2); print('synced',f)
