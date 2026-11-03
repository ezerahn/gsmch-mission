from gen import *
# ② 고객이 바라보는 카페 모습 — 출입구에서 바 쪽을 본 투시 (11/4 단장님 스케치 기준)
W,H=1900,1250
o=mk(W,H,'② 고객이 바라보는 카페 모습 — 출입구에서 본 투시 (11/4 스케치 기준)','단위 mm · 출입구에서 들어서면 앞 바 · 뒤 바가 안쪽으로 길게 뻗어 보임 · 끝에 루버 벽과 간이주방 문 · 주문현황판은 등 뒤(정면 벽 가운데 위) · 높이는 미정')
# 1점 투시: 소실점
VX,VY=1000,520
# 바닥 기준 근경 좌표 → 원경으로 수렴
def P(x,y,d):  # x: 화면 가로(근경), y: 세로(근경), d: 깊이 0~1
    return (x+(VX-x)*d, y+(VY-y)*d)
def poly(pts,fill,stroke=INK,sw=1.5,dash=''):
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{" stroke-dasharray=%s"%dash if dash else ""}/>')
FL=1060;DEEP=0.78   # 바닥선 · 바 끝 깊이
# 바닥 · 벽
poly([(60,FL),(1840,FL),P(1840,FL,DEEP),P(60,FL,DEEP)],'#f1ece2','none')
# 왼쪽 벽 (뒤 바 뒤 타일벽 + 루버 상부)
poly([(60,FL),P(60,FL,DEEP),P(60,200,DEEP),(60,200)],'#e4d8c4','none')
# 끝 벽 (루버) + 간이주방 문
ex0,ey0=P(60,FL,DEEP);ex1,ey1=P(1840,FL,DEEP);ty=P(60,200,DEEP)[1]
R(o,ex0,ty,ex1-ex0,ey0-ty,'#e5cfa6',INK,1.2)
for k in range(int(ty),int(ey0),9): o.append(f'<line x1="{ex0}" y1="{k}" x2="{ex1}" y2="{k}" stroke="#b58d55" stroke-width="0.6"/>')
T(o,(ex0+ex1)/2,ty-10,'끝 벽 — 우드 루버 (지하 본당 소나무 루버 재활용)',12,700,'#6e5a3a')
dw=(ex1-ex0)*0.16;R(o,ex0+(ex1-ex0)*0.06,ey0-(ey0-ty)*0.72,dw,(ey0-ty)*0.72,'#f7f3ea',INK,1.5);T(o,ex0+(ex1-ex0)*0.06+dw/2,ey0-(ey0-ty)*0.36,'간이주방 문',10,800,INK)
# 뒤 바 (왼쪽 벽에 붙음) — 근경 폭 775*s
s=0.42;BH=900
def bar(x0,wmm,hmm,fill,label,c):
    w=wmm*s;h=hmm*s
    # 윗면
    poly([(x0,FL-h),(x0+w,FL-h),P(x0+w,FL-h,DEEP),P(x0,FL-h,DEEP)],WOOD,INK,1.5)
    # 안쪽 긴 옆면(통로 쪽)
    poly([(x0+w,FL),(x0+w,FL-h),P(x0+w,FL-h,DEEP),P(x0+w,FL,DEEP)],fill,INK,1.5)
    # 근경 정면
    R(o,x0,FL-h,w,h,fill,INK,2)
    T(o,x0+w/2,FL-h/2+5,label,12,900,c)
bar(60,775,BH,'#efe3cf','뒤 바','#8a6a1a')
gx=60+775*s+1000*s   # 통로 1,000 (도면 기준 바 사이)
bar(gx,875,1000,'#d9d2c4','앞 바','#55534e')
T(o,gx+875*s/2,FL-1000*s-18,'앞 바 6,295 × 875 (도면) · 높이 미정',12,800,RED)
T(o,60+775*s/2,FL-BH*s-18,'뒤 바 약 6,300 × 775',12,800,'#8a6a1a')
T(o,60+775*s+1000*s/2,FL-30,'바 안 통로 약 1,000',10.5,700,MUT)
# 쇼케이스 = 앞 바 근경 끝 (출입구 쪽)
R(o,gx+6,FL-1000*s+6,875*s-12,1000*s-12,'#dbe9f7',BL,1.2,3);T(o,gx+875*s/2,FL-1000*s/2+5,'쇼케이스 (근경 끝)',10,800,BL)
# 앞 바 위 기기 (통로 쪽 옆면 위 표시)
for d,lab in [(0.18,'주문 · POS'),(0.38,'커피 · 음료'),(0.56,'제빙기'),(0.70,'픽업')]:
    x,y=P(gx+875*s,FL-1000*s,d);T(o,x+8,y-6,lab,10,700,'#8a4b12','start')
# 뒤 바 위 메뉴판 3대 (왼쪽 벽 상부, 안쪽으로 갈수록 작아짐)
for k,d in enumerate([0.12,0.33,0.52]):
    x1,y1=P(60,FL-2050*s*0.9,d);x2,y2=P(60,FL-2600*s*0.9,d+0.14)
    poly([(x1,y1),(x2,y1-(y1-y2)*0),(x2,y2),(x1,P(60,FL-2600*s*0.9,d)[1])],'#1f2a3a',INK,1.5)
    T(o,(x1+x2)/2,(y1+y2)/2+4,f'메뉴판 {k+1}',10,800,'#fff')
T(o,60+8,FL-2650*s*0.9-10,'뒤 바 위 상부 — 메뉴판 43˝ 3대 (거는 높이 미정)',12,700,RED,'start')
# 홀 (오른쪽)
T(o,1500,FL-300,'홀 · 테이블 (건축위 구매)',13,700,MUT);T(o,1500,FL-270,'서비스바는 반대쪽 벽',11,600,MUT)
T(o,950,FL+40,'← 출입구(자동문)에서 들어서서 본 모습 · 주문현황판 43˝은 등 뒤 정면 벽 가운데 위',13,800,INK)
NOTES(o,FL+70,[(BL,'11/4 단장님 스케치: 들어서면 앞 바 · 뒤 바가 안쪽으로 길게 뻗어 보이고, 끝에 루버 벽 — 앞 바 바깥은 회색 자연석, 상판 우드톤'),
 (RED,'확인할 것: 앞 바 · 뒤 바 높이 · 바 사이 통로 폭 · 메뉴판 거는 높이 · 커피머신 어느 바 · 끝 벽 문 위치(간이주방)')],W)
save(o,W,H,'cust.svg')
