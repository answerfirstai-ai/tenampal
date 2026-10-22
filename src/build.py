import json, html
R='/workspace/sites/tenampal/'; B='/tenampal/'; SITE='https://answerfirstai-ai.github.io/tenampal/'
NAME='Tenampal'; TEL='tel:+13235268172'; PHONE='(323) 526-8172'
ADDR='1859 E 1st St'; CITY='Los Angeles, CA 90033'
IG='https://www.instagram.com/tenampal/'; IGH='@tenampal'
DIR='https://www.google.com/maps/dir/?api=1&destination=1859+E+1st+St+Los+Angeles+CA+90033'
MAPS='https://www.google.com/maps/search/?api=1&query=Tenampal+1859+E+1st+St+Los+Angeles+CA+90033'
EATER='https://la.eater.com/venue/104678/tenampal'
PRICE_LINE=f'Prices: call {PHONE} or ask at the counter.'
MENU=[('Plates',['Chilaquiles','Huevos Rancheros','Huarache Azul','Tacos Dorados','Enchiladas','Chorizo Torta','Burrito de Suadero','Wet Burrito','Smashburger']),
      ('Drinks & sweet',['Café de Olla','Coffee / iced coffee','Limonada / Jamaica','Sodas','Flan con Pecanas']),
      ('Sides',['Papas','Frijoles','Mole Poblano con Totopos'])]
ICON={'call':'<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8Z"/>',
 'pin':'<path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/>',
 'ig':'<path d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3Zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6Zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0ZM12 3.6c2.7 0 3 0 4.1.1 2.7.1 4 1.4 4.1 4.1.1 1.1.1 1.4.1 4.1s0 3-.1 4.1c-.1 2.7-1.4 4-4.1 4.1-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-2.7-.1-4-1.4-4.1-4.1C3.7 15 3.6 14.7 3.6 12s0-3 .1-4.1C3.8 5.2 5.1 3.9 7.9 3.7 9 3.6 9.3 3.6 12 3.6ZM12 2c-2.7 0-3.1 0-4.2.1C4.2 2.2 2.2 4.2 2.1 7.8 2 8.9 2 9.3 2 12s0 3.1.1 4.2c.2 3.6 2.2 5.6 5.7 5.7 1.1.1 1.5.1 4.2.1s3.1 0 4.2-.1c3.6-.2 5.6-2.2 5.7-5.7.1-1.1.1-1.5.1-4.2s0-3.1-.1-4.2c-.2-3.6-2.2-5.6-5.7-5.7C15.1 2 14.7 2 12 2Z"/>'}
I=lambda n:f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor">{ICON[n]}</svg>'
call=lambda c='btn btn-ancho',t=None:f'<a class="{c}" href="{TEL}">{I("call")}{t or "Call "+PHONE}</a>'
dirb=lambda c='btn btn-line':f'<a class="{c}" href="{DIR}" target="_blank" rel="noopener">{I("pin")}Directions<span class="sr"> (opens Google Maps)</span></a>'
igb=lambda c='btn btn-line',t='Instagram':f'<a class="{c}" href="{IG}" target="_blank" rel="noopener">{I("ig")}{t}<span class="sr"> (opens Instagram)</span></a>'
LD={"@context":"https://schema.org","@type":"Restaurant","@id":SITE+"#kitchen","name":NAME,"url":SITE,"telephone":"+1-323-526-8172","image":SITE+"assets/img/og.jpg","servesCuisine":"Mexican","hasMenu":SITE+"menu/",
 "address":{"@type":"PostalAddress","streetAddress":ADDR,"addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90033","addressCountry":"US"},"areaServed":"Boyle Heights, Los Angeles","hasMap":MAPS,"sameAs":[IG]}
FONTS=f'@font-face{{font-family:"Fraunces";src:url({B}assets/fonts/fraunces-600-800.woff2) format("woff2");font-weight:600 800;font-display:swap}}@font-face{{font-family:"Instrument Sans";src:url({B}assets/fonts/instr-400.woff2) format("woff2");font-weight:400 600;font-display:swap}}'
def page(path,title,desc,body,cur='',extra=''):
  can=SITE+path
  nav=lambda h,t:f'<a href="{B}{h}"{" aria-current=\"page\"" if cur==h else ""}>{t}</a>'
  links=nav('menu/','Menu')+nav('#hours' if not cur else 'visit/#hours','Hours')+nav('visit/','Visit')
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{can}">
<meta name="theme-color" content="#1F1A17"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{can}"><meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{B}assets/img/favicon.svg" type="image/svg+xml"><link rel="preload" href="{B}assets/fonts/fraunces-600-800.woff2" as="font" type="font/woff2" crossorigin>{extra}
<style>{FONTS}</style><link rel="stylesheet" href="{B}assets/css/site.css">
<script type="application/ld+json">{json.dumps(LD,ensure_ascii=False)}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="nav-in"><a class="mark" href="{B}" aria-label="{NAME} home"><i aria-hidden="true"></i>Tenampal</a>
<nav aria-label="Main"><div class="links">{links}<a href="{IG}" target="_blank" rel="noopener">{IGH}</a></div><details class="mnav"><summary aria-label="Open menu">Menu</summary><div class="mpanel"><a href="{B}">Home</a>{links}<a href="{TEL}">Call {PHONE}</a><a href="{IG}" target="_blank" rel="noopener">Instagram {IGH}</a></div></details></nav>
{call("btn btn-ancho btn-sm nav-call")}</div></header>
<main id="main">{body}</main>
<footer class="foot"><div class="wrap"><p class="hr" aria-hidden="true">4</p><p class="hr-cap">4 PM · closing</p><div>
<p class="f-name">Tenampal</p><p>{ADDR}, Boyle Heights, {CITY}. <a href="{TEL}">{PHONE}</a>.</p>
<p>Hours per Google Maps: Wed 11-4, Thu-Sun 10-4, closed Mon-Tue. Call to confirm.</p>
<div class="ctas">{call("btn btn-ancho btn-sm")}{dirb("btn btn-line btn-sm")}{igb("btn btn-line btn-sm",IGH)}</div>
<p class="fine">The comal image is an AI-generated illustrative scene, not a photo of Tenampal's kitchen. Photos: @tenampal, from the kitchen's own Instagram. Menu item names come from public listings and may change. Demo site, © 2026 Tenampal.</p></div></div></footer>
<div class="mbar" aria-label="Quick actions">{call("btn btn-ancho btn-sm","Call")}{dirb("btn btn-line btn-sm")}</div>
<script src="{B}assets/js/site.js" defer></script></body></html>'''
def pic(name,alt,d=True):
  m=f'<source media="(max-width:760px)" type="image/avif" srcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" sizes="100vw"><source media="(max-width:760px)" type="image/webp" srcset="{B}assets/img/hero-m-800.webp 800w, {B}assets/img/hero-m-1200.webp 1200w, {B}assets/img/hero-m-1600.webp 1600w" sizes="100vw">'
  return f'<picture>{m}<source type="image/avif" srcset="{B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" sizes="100vw"><img src="{B}assets/img/hero-d-1920.webp" srcset="{B}assets/img/hero-d-1280.webp 1280w, {B}assets/img/hero-d-1920.webp 1920w, {B}assets/img/hero-d-2880.webp 2880w" sizes="100vw" width="2880" height="1620" alt="{alt}" {"fetchpriority=\"high\"" if d else "loading=\"lazy\" decoding=\"async\""}></picture>'
ALT="Illustrative: an empty black cast-iron comal on a gas burner in morning light with steam and a ball of masa. AI-generated, not a photo of Tenampal's kitchen."
PRE=f'<link rel="preload" as="image" type="image/avif" media="(max-width:760px)" imagesrcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" imagesizes="100vw" fetchpriority="high"><link rel="preload" as="image" type="image/avif" media="(min-width:761px)" imagesrcset="{B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" imagesizes="100vw" fetchpriority="high">'
import sys as _s;_s.path.insert(0,'/workspace/sites/_kit');from social import export,pic as spic,grade_warm
SP='/workspace/clients/la-rest-tenampal/photos/social/';OD=R+'assets/img/ig'
G=lambda im:grade_warm(im,lift=10,warm=4)
P={k:export(SP+f'tenampal_{n}.jpg',OD,'t'+n,w,crop=c,grade=G) for k,n,w,c in [('lead','02',520,None),('ench','01',600,(0,.16,1,.83)),('nop','05',260,None),('cab','03',560,(.1,0,.9,1)),('squ','04',360,None),('tor','09',600,(0,.12,1,.79))]}
def fig(k,cap,cls,sizes=None,lazy=True,alt=None): return f'<figure class="print rv {cls}">{spic(B,"assets/img/ig",P[k],(alt or cap)+". Photo from Tenampal\'s own Instagram, @tenampal.",lazy=lazy,sizes=sizes)}<figcaption>{cap}</figcaption></figure>'
def menu_html(h='h2'):
  cols=f'<div class="mcol">{grp(*MENU[0])}</div><div class="mcol">{grp(*MENU[1])}{grp(*MENU[2])}</div>'
  return f'<div class="board"><div class="board-head"><{h} id="menu-h">Menu</{h}><p>{PRICE_LINE}</p></div><div class="mcols">{cols}</div><p class="fine-b">Item names per public menu listings (MenuPix, Fantuan). Ask at the counter for today\'s board.</p></div>'
grp=lambda t,items:f'<section class="mg" aria-label="{html.escape(t)}"><h3>{html.escape(t)}</h3><ul>{"".join(f"<li>{html.escape(i)}</li>" for i in items)}</ul></section>'
DAYS=[('Mon',None),('Tue',None),('Wed',(11,16)),('Thu',(10,16)),('Fri',(10,16)),('Sat',(10,16)),('Sun',(10,16))]
bar=''.join(f'<li data-d="{i}" class="{"open" if h else "closed"}"><b>{d}</b><span>{f"{h[0]}-{h[1]-12}" if h else "Closed"}</span></li>' for i,(d,h) in enumerate(DAYS))
home=f'''<section class="hero" aria-labelledby="h1"><div class="hero-img">{pic("hero",ALT)}</div><span class="ill">Illustrative scene · not Tenampal's kitchen</span>
<div class="hero-in"><p class="hr hr-10" aria-hidden="true">10</p><p class="hr-cap hr-cap-10">10 AM · doors open Thu–Sun</p><h1 id="h1">Tenampal</h1>
<p class="sub">Kitchen at {ADDR}, Boyle Heights. Wed–Sun, until 4 PM.</p>
<div class="ctas">{call()}{dirb()}{igb()}</div></div></section>
<section class="sec sec-12" aria-labelledby="menu-h"><p class="hr" aria-hidden="true">12</p><p class="hr-cap">12 PM · the menu</p><div class="wrap noon"><div>{menu_html()}{fig("ench","Enchiladas verdes","p-ench","(max-width:760px) 88vw, 600px")}<div class="ctas">{call()}<a class="btn btn-line" href="{B}menu/">Full menu page</a></div></div><div class="lead-col"><div class="stack">{fig("lead","Burrito de suadero with mole","lead","(max-width:760px) 88vw, 520px",False)}{fig("nop","Huevos con nopales","p-nop","(max-width:760px) 50vw, 260px")}</div><p class="credit">Photos: {IGH}</p></div></div></section>
<section class="sec sec-2" aria-labelledby="fam-h"><p class="hr" aria-hidden="true">2</p><p class="hr-cap">2 PM · seasonal plates</p><div class="wrap two">
<div><h2 id="fam-h">Family-owned, per Eater LA</h2><p class="lede">Eater LA lists Tenampal as a family-owned kitchen on E 1st St. <a href="{EATER}" target="_blank" rel="noopener">Read the Eater LA listing</a>.</p></div>
<div class="mosaic">{fig("cab","Seasonal plate · Photo: @tenampal","p-cab","(max-width:760px) 88vw, 560px",alt="A seasonal plate")}{fig("squ","Seasonal plate · Photo: @tenampal","p-squ","(max-width:760px) 64vw, 360px",alt="A seasonal plate")}{fig("tor","From @tenampal","p-tor","(max-width:760px) 88vw, 600px",alt="A toasted sandwich cut in half")}<p class="credit">Seasonal plates from {IGH}</p></div></div></div></section>
<section class="sec sec-3" id="hours" aria-labelledby="hours-h"><p class="hr" aria-hidden="true">3</p><p class="hr-cap">3 PM · the hours</p><div class="wrap">
<h2 id="hours-h">Hours, per Google Maps</h2><p class="today" data-today aria-live="polite">Wed 11 AM-4 PM, Thu-Sun 10 AM-4 PM. Closed Monday and Tuesday.</p>
<ol class="light" aria-label="Weekly hours">{bar}</ol><p class="muted">Per Google Maps and The LA Local listings. <a href="{TEL}">Call {PHONE}</a> to confirm.</p></div></section>'''
menu=f'''<section class="phero"><div class="wrap"><p class="eyebrow">Menu</p><h1>The board</h1><p class="lede">{PRICE_LINE}</p><div class="ctas">{call()}{dirb()}</div></div></section>
<section class="sec sec-12" style="padding-top:2rem"><div class="wrap">{menu_html()}<div class="mpair">{fig("ench","Enchiladas verdes","p-ench","(max-width:760px) 88vw, 600px")}{fig("nop","Huevos con nopales","p-nop","(max-width:760px) 50vw, 260px")}</div><p class="credit">Photos: {IGH}</p></div></section>'''
rows=''.join(f'<tr><th scope="row">{d}</th><td>{f"{h[0]} AM - {h[1]-12} PM" if h else "Closed"}</td></tr>' for d,h in [("Monday",None),("Tuesday",None),("Wednesday",(11,16)),("Thursday",(10,16)),("Friday",(10,16)),("Saturday",(10,16)),("Sunday",(10,16))])
visit=f'''<section class="phero"><div class="wrap"><p class="eyebrow">Visit</p><h1>1859 E 1st St</h1><address>{NAME}<br>{ADDR}<br>Boyle Heights, {CITY}<br><a href="{TEL}">{PHONE}</a></address><div class="ctas">{dirb("btn btn-ancho")}{call("btn btn-line")}{igb()}</div></div></section>
<section class="sec" id="hours"><div class="wrap two"><div class="card"><h2>Hours</h2><table class="hours"><thead><tr><th scope="col">Day</th><th scope="col">Listed hours</th></tr></thead><tbody>{rows}</tbody></table><p class="muted">Per Google Maps and The LA Local. Call to confirm.</p></div>
<div class="card"><h2>Getting here</h2><p>On E 1st St in Boyle Heights (ZIP 90033).</p><p>Parking: call to ask.</p><p><a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></p></div></div></section>'''
nf=f'<section class="phero"><div class="wrap"><p class="eyebrow">404</p><h1>Kitchen\'s closed here</h1><p>That page doesn\'t exist.</p><div class="ctas"><a class="btn btn-line" href="{B}">Back home</a>{call()}</div></div></section>'
open(R+'index.html','w').write(page('','Tenampal | Kitchen on E 1st St, Boyle Heights','Tenampal, family kitchen at 1859 E 1st St, Boyle Heights. Listed hours Wednesday to Sunday until 4. Call (323) 526-8172.',home,'',PRE))
open(R+'menu/index.html','w').write(page('menu/','Menu | Tenampal, Boyle Heights','Tenampal menu items: chilaquiles, huevos rancheros, huarache azul, tacos dorados and more. Prices: call (323) 526-8172 or ask at the counter.',menu,'menu/'))
open(R+'visit/index.html','w').write(page('visit/','Hours & Directions | Tenampal, Boyle Heights','Tenampal is at 1859 E 1st St, Los Angeles 90033. Listed hours Wed 11-4, Thu-Sun 10-4. Call (323) 526-8172 to confirm.',visit,'visit/'))
open(R+'404.html','w').write(page('404.html','Page not found | Tenampal','Page not found.',nf).replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="x-canonical"'))
open(R+'sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>' for p in ['','menu/','visit/'])+'</urlset>')
open(R+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n'); open(R+'.nojekyll','w').write('')
print('ok')
