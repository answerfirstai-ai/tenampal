// Signature: the hours bar shows the real LA day/time (open or closed), and the page light warms 10 -> 4 as you scroll.
(()=>{if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver'in window){const r=document.querySelectorAll('.rv:not(.lead)');document.documentElement.classList.add('rv-on');const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting||e.boundingClientRect.top<0){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});r.forEach(x=>io.observe(x));const up=()=>r.forEach(x=>{if(!x.classList.contains('in')&&x.getBoundingClientRect().top<innerHeight){x.classList.add('in');io.unobserve(x)}});addEventListener('load',up);addEventListener('hashchange',()=>requestAnimationFrame(up));addEventListener('scroll',up,{passive:true});addEventListener('beforeprint',()=>r.forEach(x=>x.classList.add('in')));document.querySelector('.rv.lead')?.classList.add('in')}
document.querySelectorAll('.mnav a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
const H={2:[11,16],3:[10,16],4:[10,16],5:[10,16],6:[10,16]};
const p=new Intl.DateTimeFormat('en-US',{timeZone:'America/Los_Angeles',weekday:'short',hour:'numeric',hour12:false}).formatToParts(new Date());
const wd=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(p.find(x=>x.type=='weekday').value),hr=+p.find(x=>x.type=='hour').value%24;
const li=document.querySelector(`.light li[data-d="${wd}"]`);if(li)li.classList.add('now');
const t=document.querySelector('[data-today]');if(t&&wd>=0){const h=H[wd];let s;
 if(h&&hr>=h[0]&&hr<h[1])s=`Listed as open now, until 4 PM. Call to confirm.`;
 else{let n=wd,k=0;do{n=(n+1)%7;k++}while(!H[n]);const nm=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'];const sameDay=h&&hr<h[0];
 s=sameDay?`Listed as opening today at ${h[0]} AM. Call to confirm.`:`Listed as closed now. Next open ${nm[n]} at ${H[n][0]} AM. Call to confirm.`}
 t.textContent=s}
if(!document.body.classList.contains('no-hero')&&!document.querySelector('.hero'))return;
})();
