import re
b=open('templates/base.html').read()
if 'card3d' not in b:
    logo=re.search(r'<a class="logo"[^>]*>(.*?)</a>',b,re.S).group(1).replace('id="lg"','id="lg2"').replace('url(#lg)','url(#lg2)').replace('class="mark"','class="mark big"')
    new='<div id="loader"><div class="ld"><div class="ldlogo">'+logo+'</div><div class="scene"><div class="card3d"><div class="face fr"></div><div class="face bk"></div></div><div class="gl"></div></div><p class="ldt">Building Excellence &amp; Infrastructure</p></div></div>\n'
    b=re.sub(r'<div id="loader">.*?</div>\n',lambda m:new,b,count=1,flags=re.S)
if 'data-home' not in b:
    b=b.replace('<body>','<body data-home="{{ \'1\' if request.endpoint == \'home\' else \'\' }}">')
open('templates/base.html','w').write(b)
j=open('static/js/main.js').read()
if 'dataset.home' not in j:
    line="addEventListener('load',()=>{const l=document.getElementById('loader');setTimeout(()=>{l.classList.add('hide');setTimeout(()=>l.style.display='none',900)},document.body.dataset.home?4800:600)});"
    j=re.sub(r"(?:window\.)?addEventListener\('load',\(\)=>setTimeout\(.*?\),\d+\)\);",lambda m:line,j,count=1)
open('static/js/main.js','w').write(j)
c=open('static/css/style.css').read()
if '.card3d' not in c:
    c+='''
.ld{display:flex;flex-direction:column;align-items:center;gap:34px;text-align:center;padding:0 20px}
.ldlogo{display:flex;align-items:center;gap:16px;animation:rise .9s both}.ldlogo .mark{width:84px;height:84px}.ldlogo .lt b{font-size:1.7rem;color:#f3dca0;letter-spacing:4px}.ldlogo .lt i{color:#e0bd7f}.ldlogo .lt small{font-size:.7rem;color:#b9c9c2}
.scene{perspective:1100px;width:min(78vw,340px);height:min(45vw,197px);animation:rise 1s .5s both}
.card3d{width:100%;height:100%;position:relative;transform-style:preserve-3d;animation:spin 7s linear infinite}
.card3d::before{content:"";position:absolute;inset:0;border-radius:8px;background:#c9a45c}
.face{position:absolute;inset:0;border-radius:8px;background-size:cover;background-position:center;backface-visibility:hidden;box-shadow:0 0 45px rgba(227,195,123,.28)}
.fr{background-image:url(../img/card/front.jpg);transform:translateZ(2px)}.bk{background-image:url(../img/card/back.jpg);transform:rotateY(180deg) translateZ(2px)}
.gl{width:70%;height:20px;margin:42px auto 0;background:radial-gradient(ellipse,rgba(227,195,123,.35),transparent 70%)}
.ldt{letter-spacing:4px;font-size:.75rem;color:#e0bd7f;animation:rise 1s 1.3s both}
@keyframes spin{from{transform:rotateX(-8deg) rotateY(0)}to{transform:rotateX(-8deg) rotateY(360deg)}}
@keyframes rise{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}
@media(max-width:600px){.ldlogo .lt b{font-size:1.15rem}.ldlogo .mark{width:60px;height:60px}.ldlogo .lt small{display:none}}
'''
if 'LOADER-BLACK' not in c:
    c+='''
/* LOADER-BLACK */
#loader{display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 35%,#1d1d22,#050506 75%);color:#fff}
.ld{width:100%;margin:auto}
'''
open('static/css/style.css','w').write(c)
print("patched")
