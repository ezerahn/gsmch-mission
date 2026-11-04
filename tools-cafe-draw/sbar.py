from gen import *
import base64
W,H=2100,1500
o=mk(W,H,'④ 로뎀카페 서비스바 (안) — 11/3 도면 4,200 · 11/4 구성','단위 mm · 길이 4,200(도면) · 폭 700(스케치) / 600(업체) · 세척 2구 → 음료 버림 → 쓰레기 3 (일반 · 종이 · 플라스틱) · 끝에 더그리트 반납함 WIDE 2대 (790×620×1,100 · 바닥 거치) · 아이스크림 냉동고는 뺌 · 빨간 글씨 = 정할 것')
S=0.33;OX=150;OY=230;L=4200;D=700
X=lambda mm:OX+mm*S;Y=lambda mm:OY+mm*S
T(o,X(0),Y(-90),'① 위에서 본 모습',20,900,INK,'start');T(o,X(L/2),Y(-40),'↑ 앞 바 쪽 (주문 · 픽업) — 사이 1,600',13,700,BL)
R(o,X(0),Y(0),L*S,D*S,'#fff7e2',GO,3)
segs=[(0,900,'텀블러 세척 2구 (확정)','#fdf3dc'),(900,500,'음료 버리는 곳','#e6f0fa'),(1400,1800,'쓰레기 투입구 3 — 일반 · 종이 · 플라스틱','#fffaf0'),(3200,1000,'셀프 코너 · 여유 (상판)','#fffaf0')]
for x,w,lab,f in segs:
    R(o,X(x),Y(0),w*S,D*S,f,GO,1.2,0,'6 4');T(o,X(x+w/2),Y(D+60),lab,12,800,'#8a6a1a')
    DIM(o,X(x),Y(D+110),X(x+w),Y(D+110),f'{w:,}',RED,16,11)
# 세척 2구
R(o,X(100),Y(100),700*S,500*S,'#e8eef5',INK,1.5,8)
for cx in (280,620): o.append(f'<circle cx="{X(cx)}" cy="{Y(350)}" r="{90*S}" fill="#fff" stroke="{INK}" stroke-width="2"/>')
# 음료 버림
o.append(f'<circle cx="{X(1150)}" cy="{Y(350)}" r="{120*S}" fill="#fff" stroke="{INK}" stroke-width="2"/><circle cx="{X(1150)}" cy="{Y(350)}" r="{70*S}" fill="#cfe0f3" stroke="{INK}" stroke-width="1"/>')
# 쓰레기 3
for k,(lab,f) in enumerate((('일반','#e8e8e8'),('종이','#efe3cf'),('플라스틱','#dff3ee'))):
    x=1400+100+k*570;R(o,X(x),Y(90),450*S,520*S,f,INK,1.5,8);R(o,X(x+115),Y(280),220*S,110*S,'#2b2b2b','none',0,6);T(o,X(x+225),Y(560),lab,11,800,INK)
# 더그리트 반납함 WIDE 2대 — 서비스바 끝 옆 바닥 거치 (790 × 620 × 1,100)
for k in range(2):
    x=L+100+k*(790+60);R(o,X(x),Y(D-620),790*S,620*S,'#2b2b2b',INK,1.5,6);R(o,X(x+200),Y(D-620+200),390*S,160*S,'#666','none',0,6);T(o,X(x+395),Y(D-620+480),'반납함 WIDE',11,800,'#fff');T(o,X(x+395),Y(D-620+560),'790 × 620',9.5,600,'#ccc')
DIM(o,X(L+100),Y(D+60),X(L+100+790),Y(D+60),'790',BL,16,11);DIM(o,X(L+100+850),Y(D+60),X(L+100+850+790),Y(D+60),'790',BL,16,11);DIM(o,X(L+100+1640+60),Y(D-620),X(L+100+1640+60),Y(D),'620',BL,-10,11)
DIM(o,X(L),Y(D+110),X(L+100+1640),Y(D+110),'반납함 2대 + 사이 60 = 1,740 (서비스바 끝에서 100)',RED,16,10)
T(o,X(L+100+820),Y(D-680),'더그리트 반납함 WIDE 2대 — 바닥 거치 · 수거 400~450개 · 서비스바 옆 (결정)',11,800,G)
DIM(o,X(0),Y(D+230),X(L),Y(D+230),'서비스바 4,200 (도면)',BL,18,13);DIM(o,X(0),Y(D+330),X(L+100+1640),Y(D+330),'서비스바 + 반납함 2대 = 5,940 — 홀 자리 확인',RED,18,12);DIM(o,X(-70),Y(0),X(-70),Y(D),'700',BL,10,12);T(o,X(-120),Y(D+40),'폭 600 / 700 — 결정',10,700,RED,'end')
T(o,X(L/2),Y(D+420),'↓ 홀 쪽 (손님 테이블)',13,700,BL)
# ---- 정면 (손님 쪽)
OY2=920;HT=850;Yf=lambda mm:OY2+mm*S
T(o,X(0),Yf(-500),'② 손님 쪽에서 본 모습 (정면)',20,900,INK,'start')
# 셀프 코너 선반 (안) — 위 벽 없음 · 상판 뒤 2단 선반
R(o,X(1400),Yf(-430),1500*S,40*S,WOOD,INK,1);R(o,X(1400),Yf(-230),1500*S,40*S,WOOD,INK,1)
T(o,X(2150),Yf(-460),'셀프 코너 2단 선반 (안) — 냅킨 · 빨대 · 시럽 · 컵홀더 · 깊이 약 250 · 통은 종류별 하나씩 + 그림 라벨',11,800,G)
for k,lab in enumerate(('빨대','냅킨','시럽','스틱','홀더')): R(o,X(1480+k*290),Yf(-230-150),200*S,150*S,'#f4f4f4',INK,1,4);T(o,X(1580+k*290),Yf(-290),lab,8.5,700,INK)
o.append(f'<line x1="{X(-100)}" y1="{Yf(HT)}" x2="{X(L+100)}" y2="{Yf(HT)}" stroke="{INK}" stroke-width="3"/>')
R(o,X(-20),Yf(0),(L+40)*S,40*S,WOOD,INK,1.5);R(o,X(0),Yf(40),L*S,(HT-40)*S,'#efe3cf',INK,1.5)
UNIT(o,X,Yf,0,900,'door2','수납 — 세척기 배관 · 수납',HT)
UNIT(o,X,Yf,900,500,'open1','물통 (음료 버림)',HT);R(o,X(1000),Yf(250),300*S,500*S,'#cfe0f3',INK,1.2,8);T(o,X(1150),Yf(520),'물통',10,800,'#2a4f86')
for k,(lab,f) in enumerate((('일반','#e8e8e8'),('종이','#efe3cf'),('플라스틱','#dff3ee'))):
    x=1400+100+k*570;UNIT(o,X,Yf,1400+k*600,600,'open1','',HT);R(o,X(x),Yf(120),450*S,650*S,f,INK,1.2,8);T(o,X(x+225),Yf(450),lab,11,800,INK);T(o,X(x+225),Yf(520),'통 · 봉지',9,600,MUT)
UNIT(o,X,Yf,3200,1000,'door2','수납',HT)
# 더그리트 제품 사진 (2대 나란히 · 높이 1,100 기준으로 맞춤)
_b=base64.b64encode(open('greet.png','rb').read()).decode();_w=(790*2+60)*S;_h=1100*S*1.18
o.append(f'<image href="data:image/png;base64,{_b}" x="{X(L+100)-_w*0.06:.1f}" y="{Yf(HT-1100)-_h*0.1:.1f}" width="{_w*1.12:.1f}" height="{_h:.1f}" preserveAspectRatio="xMidYMax meet"/>')
R(o,X(L+100),Yf(HT-1100),(790*2+60)*S,1100*S,'none',RED,1.2,0,'6 4')
T(o,X(L+100+820),Yf(HT+30),'더그리트 REUSABLE CONTAINER RETURN BOX — WIDE 2대',10,800,INK)
DIM(o,X(L+100+1640+80),Yf(HT-1100),X(L+100+1640+80),Yf(HT),'1,100',BL,-10,11)
T(o,X(L+100+820),Yf(HT-1180),'높이 1,100 — 서비스바 상판(미정)보다 높을 수 있음 · 투입구는 위쪽 앞면',10,700,RED)
for cx in (280,620): o.append(f'<ellipse cx="{X(cx)}" cy="{Yf(20)}" rx="{90*S}" ry="{12*S}" fill="#fff" stroke="{INK}" stroke-width="2"/>')
o.append(f'<ellipse cx="{X(1150)}" cy="{Yf(20)}" rx="{120*S}" ry="{14*S}" fill="#cfe0f3" stroke="{INK}" stroke-width="2"/>')
for k in range(3): o.append(f'<ellipse cx="{X(1725+k*570)}" cy="{Yf(20)}" rx="{110*S}" ry="{14*S}" fill="#2b2b2b" stroke="{INK}" stroke-width="1"/>')
DIM(o,X(-70),Yf(0),X(-70),Yf(HT),'높이 미정',RED,10,12)
T(o,X(L/2),Yf(HT+60),'투입구는 상판에 · 아래는 통(봉지) · 앞면은 시트지로 표시 · 아이스크림 냉동고는 서비스바에서 뺌 (자리 다시 정하기)',11,700,RED)
NOTES(o,Yf(HT)+110,[(BL,'도면(11/3): SERVICE BAR 4,200 · 앞 바에서 1,600 · 급배수 1곳(세척) · 전원 — 폭은 도면 치수 없음'),
 (G,'11/4 구성: 세척 2구 900 → 음료 버림 500 → 쓰레기 3(일반 · 종이 · 플라스틱) 1,800 → 셀프 · 수납 1,000 = 4,200 — 끝 옆에 더그리트 반납함 WIDE 2대 (790×620×1,100 · 수거 400~450개 · 바닥 거치) — 구간 너비는 안'),
 (RED,'정할 것: 폭 600/700 · 높이 · 반납함 2대 자리(서비스바 끝 옆 1,740 — 홀 테이블과 간격) · 셀프 선반 위치 · 아이스크림 냉동고 새 자리')],W)
apply_overlays(o,'sbar',X,Yf);save(o,W,H,'sbar.svg')
