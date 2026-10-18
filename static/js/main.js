addEventListener('load',()=>{const l=document.getElementById('loader');setTimeout(()=>{l.classList.add('hide');setTimeout(()=>l.style.display='none',900)},document.body.dataset.home?4800:600)});
const nav=document.getElementById('nav');addEventListener('scroll',()=>nav.classList.toggle('s',scrollY>40));
document.getElementById('burger').onclick=()=>document.getElementById('menu').classList.toggle('open');
const cur=document.getElementById('cursor');addEventListener('mousemove',e=>{cur.style.left=e.clientX+'px';cur.style.top=e.clientY+'px'});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;e.target.classList.add('in');
const b=e.target.querySelector('[data-n]');if(b){let n=+b.dataset.n,i=0;const t=setInterval(()=>{i+=Math.ceil(n/50);if(i>=n){i=n;clearInterval(t)}b.textContent=i},30)}
io.unobserve(e.target)}),{threshold:.15});
document.querySelectorAll('.reveal').forEach((el,i)=>{el.style.transitionDelay=(i%4)*.1+'s';io.observe(el)});
document.querySelectorAll('.tilt').forEach(c=>{c.addEventListener('mousemove',e=>{c.style.transitionDelay='0s';const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
c.style.transform=`perspective(800px) rotateY(${x*14}deg) rotateX(${-y*14}deg) translateY(-6px)`});c.addEventListener('mouseleave',()=>c.style.transform='')});
const cv=document.getElementById('bg'),R=new THREE.WebGLRenderer({canvas:cv,alpha:true,antialias:true});
R.setPixelRatio(Math.min(devicePixelRatio,2));const S=new THREE.Scene(),C=new THREE.PerspectiveCamera(60,1,.1,100);C.position.z=12;
const mat=new THREE.LineBasicMaterial({color:0xd9b25f});
function house(){const g=new THREE.Group();
g.add(new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(2,1.5,2)),mat));
const roof=new THREE.Mesh(new THREE.ConeGeometry(1.7,1.1,4),new THREE.MeshBasicMaterial({color:0xd9b25f,wireframe:true}));roof.position.y=1.3;roof.rotation.y=Math.PI/4;g.add(roof);return g}
const hs=[];for(let i=0;i<9;i++){const h=house();h.position.set((Math.random()-.5)*26,(Math.random()-.5)*16,(Math.random()-.5)*12-3);h.scale.setScalar(.5+Math.random()*1.2);h.userData={s:Math.random()*.01+.003,f:Math.random()*2};S.add(h);hs.push(h)}
const pg=new THREE.BufferGeometry(),pa=[];for(let i=0;i<700;i++)pa.push((Math.random()-.5)*40,(Math.random()-.5)*30,(Math.random()-.5)*30);
pg.setAttribute('position',new THREE.Float32BufferAttribute(pa,3));const pts=new THREE.Points(pg,new THREE.PointsMaterial({color:0xc8ced6,size:.05}));S.add(pts);
let mx=0,my=0,sy=0;addEventListener('mousemove',e=>{mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5});addEventListener('scroll',()=>sy=scrollY);
function rs(){R.setSize(innerWidth,innerHeight);C.aspect=innerWidth/innerHeight;C.updateProjectionMatrix()}rs();addEventListener('resize',rs);
(function loop(t){requestAnimationFrame(loop);t*=.001;hs.forEach(h=>{h.rotation.y+=h.userData.s;h.position.y+=Math.sin(t+h.userData.f)*.003});
pts.rotation.y=t*.02;C.position.x+=(mx*3-C.position.x)*.04;C.position.y+=(-my*2-sy*.004-C.position.y)*.04;C.lookAt(0,-sy*.004,0);R.render(S,C)})(0);

document.querySelectorAll('.f').forEach(b=>b.onclick=()=>{document.querySelectorAll('.f').forEach(x=>x.classList.remove('on'));b.classList.add('on');
document.querySelectorAll('.photo').forEach(c=>{c.style.display=(b.dataset.f==='all'||c.dataset.cat===b.dataset.f)?'':'none'})});
const lb=document.createElement('div');lb.id='lb';lb.innerHTML='<button class="x">✕</button><button class="pv">‹</button><img><button class="nx">›</button>';document.body.appendChild(lb);
const its=[...document.querySelectorAll('[data-full]')];let ci=0;
function show(i){ci=(i+its.length)%its.length;lb.querySelector('img').src=its[ci].dataset.full;lb.classList.add('on')}
its.forEach((e,i)=>e.addEventListener('click',()=>show(i)));
lb.onclick=e=>{if(e.target.tagName!=='IMG'&&!e.target.classList.contains('pv')&&!e.target.classList.contains('nx'))lb.classList.remove('on')};
lb.querySelector('.pv').onclick=()=>show(ci-1);lb.querySelector('.nx').onclick=()=>show(ci+1);
addEventListener('keydown',e=>{if(!lb.classList.contains('on'))return;if(e.key==='Escape')lb.classList.remove('on');if(e.key==='ArrowLeft')show(ci-1);if(e.key==='ArrowRight')show(ci+1)});
