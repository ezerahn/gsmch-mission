# 공통 유틸
INK='#2c2a26';MUT='#6e6860';RED='#c0392b';GO='#b8860b';BL='#2a5db0';G='#07913B';WOOD='#d9b98a';TILE='#cfe3d0';STONE='#9a948a'
def mk(W,H,title,sub):
    o=[];o.append(f'<rect width="{W}" height="{H}" fill="#fbf8f2"/>')
    o.append(f'<text x="50" y="60" font-size="34" font-weight="900" fill="{INK}">{title}</text>')
    o.append(f'<text x="50" y="94" font-size="17" fill="{MUT}">{sub}</text>')
    return o
def save(o,W,H,name):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Noto Sans CJK KR, sans-serif">'+''.join(o)+'</svg>'
    open(name,'w').write(svg)
def T(o,x,y,t,sz=14,w=700,c=INK,anc='middle',rot=0):
    tr=f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot else ''
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{sz}" font-weight="{w}" fill="{c}" text-anchor="{anc}"{tr}>{t}</text>')
def R(o,x,y,w,h,fill,stroke=INK,sw=1.5,rx=0,dash=''):
    o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{" stroke-dasharray=%s"%dash if dash else ""}/>')
def DIM(o,x1,y1,x2,y2,t,c=BL,off=18,sz=14):
    o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="1.4"/>')
    if y1==y2:
        for xx in (x1,x2): o.append(f'<line x1="{xx:.1f}" y1="{y1-6}" x2="{xx:.1f}" y2="{y1+6}" stroke="{c}" stroke-width="1.4"/>')
        T(o,(x1+x2)/2,y1+off,t,sz,800,c)
    else:
        for yy in (y1,y2): o.append(f'<line x1="{x1-6}" y1="{yy:.1f}" x2="{x1+6}" y2="{yy:.1f}" stroke="{c}" stroke-width="1.4"/>')
        T(o,x1-off,(y1+y2)/2+5,t,sz,800,c,'end')
def NOTES(o,y,rows,W):
    R(o,50,y,W-100,40*len(rows)+40,'#fff','#e3d9c6',1,12)
    for k,(c,l) in enumerate(rows): T(o,74,y+40+k*40,l,15,700,c,'start')

# ---- 덧그리기(overlay): 사람 · 컵 · 상자 — 환경변수 OVL(JSON 목록) 또는 호출 인자
# 항목: {"view":"el2|el2b|el4|el3|front|plan", "type":"person|cup|box|label", "x":mm, "y":mm(바닥/위쪽 기준 0), "h":mm, "w":mm, "label":"", "color":""}
import os, json
def person(o,X,Y,x,h,label='',color='#2c2a26',apron=None):
    # 입면: 바닥 y=0 기준 · x = 발 위치(mm) · h = 키(mm). 머리 지름 ≈ h/7.5
    hd=h/7.5; S=(X(1)-X(0))
    cx=X(x); top=Y(h)
    o.append(f'<circle cx="{cx:.1f}" cy="{top+hd*S/2:.1f}" r="{hd*S/2:.1f}" fill="#f1d9c0" stroke="{color}" stroke-width="1.5"/>')
    sh=top+hd*S*1.1; hip=Y(h*0.5); ft=Y(0)
    o.append(f'<path d="M {cx-hd*S*0.9:.1f} {sh:.1f} L {cx+hd*S*0.9:.1f} {sh:.1f} L {cx+hd*S*0.75:.1f} {hip:.1f} L {cx-hd*S*0.75:.1f} {hip:.1f} Z" fill="{color}" stroke="{color}" stroke-width="1"/>')
    if apron: o.append(f'<path d="M {cx-hd*S*0.7:.1f} {Y(h*0.72):.1f} L {cx+hd*S*0.7:.1f} {Y(h*0.72):.1f} L {cx+hd*S*0.7:.1f} {Y(h*0.3):.1f} L {cx-hd*S*0.7:.1f} {Y(h*0.3):.1f} Z" fill="{apron}" stroke="#000" stroke-width="0.8"/>')
    for dx in (-0.35,0.35): o.append(f'<line x1="{cx+dx*hd*S:.1f}" y1="{hip:.1f}" x2="{cx+dx*hd*S:.1f}" y2="{ft:.1f}" stroke="{color}" stroke-width="{max(2,hd*S*0.3):.1f}"/>')
    for dx in (-1.05,1.05): o.append(f'<line x1="{cx+dx*hd*S*0.85:.1f}" y1="{sh+2:.1f}" x2="{cx+dx*hd*S*0.85:.1f}" y2="{Y(h*0.45):.1f}" stroke="{color}" stroke-width="{max(2,hd*S*0.25):.1f}"/>')
    if label: T(o,cx,top-8,label,11,800,RED)
def cup(o,X,Y,x,y,w=90,h=120,n=1,label='',color='#8fd1c5'):
    S=(X(1)-X(0))
    for k in range(n): R(o,X(x+k*(w+15)),Y(y+h),w*S,h*S,color,INK,1,2)
    if label: T(o,X(x+(n*(w+15))/2),Y(y+h+60),label,10,800,RED)
def apply_overlays(o,view,X,Y,extra=None):
    items=json.loads(os.environ.get('OVL','[]'))+(extra or [])
    for it in items:
        if it.get('view')!=view: continue
        t=it.get('type')
        if t=='person': person(o,X,Y,it['x'],it.get('h',1650),it.get('label',''),it.get('color','#2c2a26'),it.get('apron'))
        elif t=='cup': cup(o,X,Y,it['x'],it.get('y',0),it.get('w',90),it.get('h',120),it.get('n',1),it.get('label',''),it.get('color','#8fd1c5'))
        elif t=='box':
            S=(X(1)-X(0));R(o,X(it['x']),Y(it.get('y',0)+it['h']),it['w']*S,it['h']*S,it.get('color','#fff3b8'),RED,2,3);T(o,X(it['x']+it['w']/2),Y(it.get('y',0)+it['h']/2)+4,it.get('label',''),10,800,RED)
        elif t=='label': T(o,X(it['x']),Y(it.get('y',0)),it.get('label',''),it.get('size',12),800,RED)

def UNIT(o,X,Yf,x,w,kind,label,HT=850,top=40,c='#8a6a1a'):
    """하부장 한 칸. kind: door2(2문 여닫이) door1 drawer3(서랍 3단) drawer2 open1(오픈 1단) open2(오픈 2단 선반) appl(기기 매립) empty"""
    S=X(1)-X(0); y0=Yf(top); h=(HT-top)*S
    R(o,X(x),y0,w*S,h,'#f6efe0',INK,1.2)
    if kind.startswith('door'):
        n=2 if kind=='door2' else 1; dw=w/n
        for k in range(n):
            R(o,X(x+k*dw)+4,y0+4,dw*S-8,h-8,'#efe3cf',INK,1,2)
            o.append(f'<line x1="{X(x+k*dw)+4}" y1="{y0+4}" x2="{X(x+(k+1)*dw)-4}" y2="{y0+h-4}" stroke="{INK}" stroke-width="0.7"/><line x1="{X(x+(k+1)*dw)-4}" y1="{y0+4}" x2="{X(x+k*dw)+4}" y2="{y0+h-4}" stroke="{INK}" stroke-width="0.7"/>')
            o.append(f'<circle cx="{X(x+k*dw+(dw*0.85 if k==0 else dw*0.15))}" cy="{y0+h*0.45}" r="3" fill="{INK}"/>')
    elif kind.startswith('drawer'):
        n=int(kind[-1]); dh=h/n
        for k in range(n):
            R(o,X(x)+4,y0+4+k*dh,w*S-8,dh-8,'#efe3cf',INK,1,2); o.append(f'<line x1="{X(x+w*0.35)}" y1="{y0+k*dh+dh/2}" x2="{X(x+w*0.65)}" y2="{y0+k*dh+dh/2}" stroke="{INK}" stroke-width="2"/>')
    elif kind.startswith('open'):
        n=int(kind[-1])
        for k in range(1,n): o.append(f'<line x1="{X(x)+3}" y1="{y0+h*k/n}" x2="{X(x+w)-3}" y2="{y0+h*k/n}" stroke="{INK}" stroke-width="2"/>')
        R(o,X(x),y0,w*S,h,'none',INK,1.2)
    T(o,X(x+w/2),y0+h+16,label,9.5,800,c)
