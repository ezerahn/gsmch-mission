#!/usr/bin/env python3
# gsmch-1f-plan.json 내용을 두 html 안에 사본으로 심는다.
# 웹(github.io)에서는 json을 먼저 읽고, 못 읽으면 이 사본을 쓴다.
import io, json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
src  = os.path.join(BASE, 'gsmch-1f-plan.json')
data = io.open(src, encoding='utf-8').read()
json.loads(data)                      # 형식 검증
data = data.replace('</', '<\\/')     # 스크립트 조기 종료 방지

TAG = '<script id="planData" type="application/json">%s</script>' % data
PAT = re.compile(r'<script id="planData" type="application/json">.*?</script>', re.S)
MARK = '<!--PLANDATA-->'

for f in ['gsmch-1f-plan.html', 'gsmch-1f.html']:
    p = os.path.join(BASE, f)
    s = io.open(p, encoding='utf-8').read()
    if PAT.search(s):
        s = PAT.sub(lambda m: TAG, s, count=1)
    elif MARK in s:
        s = s.replace(MARK, MARK + '\n' + TAG, 1)
    else:
        raise SystemExit('표식(<!--PLANDATA-->)이 %s 에 없습니다' % f)
    io.open(p, 'w', encoding='utf-8').write(s)
    print('심음:', f)
