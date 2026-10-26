# -*- coding: utf-8 -*-
"""진도표 데이터에 1~9 칸 · 담당 · 상태 · 메모를 붙입니다 (2026-10-26 구조 개편)."""
import json, io, collections, re

P = 'gsmch-1f-plan.json'
d = json.load(io.open(P, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)

CATS = [
  {"n":1, "name":"주문 · 결제 시스템", "who":"잇다 · 단장님"},
  {"n":2, "name":"공사 · 현장",       "who":"건축위"},
  {"n":3, "name":"구매 · 발주",       "who":"단장님 · 매니저"},
  {"n":4, "name":"서점 준비",         "who":"서점 매니저"},
  {"n":5, "name":"카페 준비",         "who":"단장님 · 카페 매니저"},
  {"n":6, "name":"디자인 · 제작물",   "who":"나 · 디자인 간사"},
  {"n":7, "name":"사람",             "who":"단장님"},
  {"n":8, "name":"오픈 · 홍보",       "who":"사업단"},
  {"n":9, "name":"행정 · 인수인계",   "who":"나"},
]
WHO = ["나", "단장님", "잇다", "건축위", "매니저"]

# 항목 → (칸, 기본 담당)
MAP = {
 'a-decision':(1,'단장님'), 's-contract':(1,'단장님'), 's-temppos':(1,'잇다'), 's-trainplan':(1,'나'),
 'b-train':(1,'잇다'), 'cafe-train':(1,'잇다'), 'cafe-menu-pos':(1,'매니저'), 's-install':(1,'잇다'), 's-test':(1,'잇다'),
 'c-entry':(2,'건축위'), 'c-watch':(2,'단장님'), 'c-book':(2,'나'), 'c-cafe':(2,'나'), 'c-fix':(2,'나'), 'c-done':(2,'건축위'),
 'cafe-equip':(3,'단장님'), 'cafe-order':(3,'단장님'), 'b-order':(3,'매니저'), 'cafe-in':(3,'매니저'),
 'b-mix':(4,'매니저'), 'b-list':(4,'매니저'), 'b-stock':(4,'매니저'), 'b-mix2':(4,'매니저'), 'b-stock2':(4,'매니저'), 'b-in':(4,'매니저'),
 'cafe-cup-review':(5,'단장님'), 'cafe-bean':(5,'단장님'), 'cafe-menu-fix':(5,'단장님'), 'cafe-cup':(5,'단장님'),
 'cafe-menu':(5,'매니저'), 'cafe-cup-set':(5,'매니저'),
 'c-sign':(6,'나'), 'm-scope':(6,'단장님'), 'm-order':(6,'나'), 'cafe-board':(6,'나'), 'cafe-apron':(6,'매니저'), 'm-recv':(6,'나'),
 's-train':(7,'단장님'), 'a-staff':(7,'단장님'), 'all-rehearsal':(7,'단장님'),
 'a-promo':(8,'나'), 'a-event':(8,'나'), 'open':(8,'단장님'),
 'a-ops':(9,'나'), 'a-manual':(9,'나'), 'a-close':(9,'나'), 'a-handover1':(9,'나'), 'a-handover2':(9,'나'),
 'bk-plan':(9,'나'), 'bk-part4':(9,'나'), 'bk-forms':(9,'나'), 'bk-fin':(9,'나'), 'bk-typeset':(9,'나'),
 'bk-print':(9,'나'), 'bk-hand':(9,'나'), 'bk-contact':(9,'나'),
}

# 확실히 아는 항목은 할 일을 다시 씁니다 (t, who, st, date, memo)
def T(t, who, st='todo', date='', memo=''):
    return collections.OrderedDict([('t',t),('who',who),('st',st),('date',date),('memo',memo),('done',st=='done')])

REWRITE = {
 'a-decision': [
   T('도입안 작성 · 서점 · 카페 비용 산출','나','done','10/19'),
   T('잇다에 견적 요청서 발송','나','done','10/20'),
   T('확정 견적서 받기','나','done','10/21','하드웨어 6,953,100원 · 월 152,790원 (부가세 포함)'),
   T('사업단 의사결정','단장님','wait','10/28','10/20~21 예정이었음 — 결과 확인'),
   T('결정 결과 회신 · 집행 근거 보관','나'),
 ],
 's-contract': [
   T('키오스크 장비 선택','단장님','done','10/20','서점 · 카페 모두 안드로이드 · 데스크형'),
   T('카페 제조대 화면 — 태블릿 KDS로 결정','단장님','done','10/21','1대 42만 원 · 3인 요금에 포함'),
   T('잇다에 계약 서류 보내기','단장님','wait','10/26','오늘 발송 예정 — 준비됐는지 확인'),
   T('선금 비율 결정','단장님','wait','10/28','교회 · 조은진 장로님 협의 · 50% 3,476,550 / 30% 2,085,930'),
   T('선금 입금','나','todo','','결정 뒤'),
   T('서점 외벽 디스플레이 — 사이니지 스틱 / USB 선택','단장님','todo','','스틱은 POS에 연결 · 나중에 추가 구매 가능'),
   T('무선 링스캐너 구매 여부','단장님','todo','','145,000원 (부가세 별도)'),
   T('계약서 조건 확인 (약정 없음 · 무상 A/S)','나'),
   T('하드웨어 발주 · 납기 확인','잇다'),
   T('설치일 확정','잇다','todo','','11/14 준공 이후 설치'),
 ],
 's-temppos': [
   T('입고 · 테스트 일정 잡기','잇다','todo','','선금 입금 뒤 · 임시서점(5층)에서'),
   T('전원 · 인터넷 확인','나'),
   T('서점 기초 자료 등록','매니저'),
 ],
 'cafe-equip': [
   T('기물 리스트 확정','단장님','done'),
   T('견적 3곳 비교','단장님','done','','제이엔지니어스 · 기정인터내셔날 · 제이크리'),
   T('업체 선정 · 계약 체결','단장님','done','10/20','50% 선입금 · 설치 후 50%'),
   T('계약서 사본 받기','단장님','wait','10/28','미수령'),
   T('납기 확인 — 11/13 전 입고','단장님'),
   T('입금 조건 · 시점 확인','단장님'),
   T('집행 근거 보관 (견적서 3부 · 계약서 · 선정 사유)','나'),
 ],
 'cafe-bean': [
   T('후보 조사 — 히즈빈스 · 마데톨미 등','단장님','wait','10/26','기존 파블로스와 비교'),
   T('시음 — 아메리카노 · 라떼','단장님'),
   T('한 잔 원가 · 최소 주문량 · 납기 · 교육 지원 비교','단장님'),
   T('결정 — 메뉴 포스 셋업(11월 첫 주) 전','단장님','todo','','가격 500원 인상 · 오픈 이벤트와 연결'),
 ],
 'cafe-cup': [
   T('업체 대표 미팅 (+지속환경국)','단장님','wait','10/27'),
   T('운영 업체 선정','단장님'),
   T('월 비용 · 컵 단가 확정','단장님'),
   T('세척기 · 반납 키오스크 사양 확정','단장님'),
   T('계약 조건 정리','나'),
 ],
}

def clean(t):
    # 예전 할 일 문장 끝의 담당 · 날짜 꼬리 정리
    return re.sub(r'\s*—\s*(단장님|잇다|건축위)[^—]*$', '', t).strip()

for it in d['items']:
    cat, owner = MAP[it['id']]
    it['cat'] = cat
    it['owner'] = owner
    wk = next(w for w in d['weeks'] if w['id'] == it['week'])
    it['due'] = wk['to'][5:].replace('-', '/').lstrip('0').replace('/0', '/')
    if it['id'] in REWRITE:
        it['todo'] = REWRITE[it['id']]
        continue
    new = []
    for t in it.get('todo', []):
        who = owner
        txt = t['t']
        if '건축위' in txt and ('전달' in txt or '확인' in txt): who = '건축위' if it['id'] != 'c-cafe' else '나'
        if '업체에 1:1 교육 요청' in txt: who = '나'
        if '교육일 확정' in txt: who = '나'
        new.append(T(clean(txt), who, 'done' if t.get('done') else 'todo'))
    it['todo'] = new

d['cats'] = CATS
d['who'] = WHO
d['updated'] = '2026-10-26'
json.dump(d, io.open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

c = collections.Counter(i['cat'] for i in d['items'])
print('칸별 항목:', dict(sorted(c.items())))
w = collections.Counter(t['who'] for i in d['items'] for t in i['todo'])
s = collections.Counter(t['st'] for i in d['items'] for t in i['todo'])
print('담당:', dict(w)); print('상태:', dict(s))
