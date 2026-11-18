import os
d=os.path.dirname(os.path.abspath(__file__))
r=lambda f:open(os.path.join(d,f),encoding='utf-8').read()
s=r('src.html').replace('{{BADGE_STYLE}}',r('badge_style.part').replace('<style>','').replace('</style>','').strip()).replace('{{BADGE_LINK}}',r('badge_link.part').strip())
open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(s)
