import re, io
p = r'D:\smarta\gesi formation\module-django-gesibiblio\preamble.tex'
s = open(p, encoding='utf-8').read()
# charger fontawesome5 avant les boites
s = s.replace(r'\usepackage[most]{tcolorbox}', '\\usepackage{fontawesome5}\n\\usepackage[most]{tcolorbox}')
# supprimer language= vide dans le style tree
s = s.replace('  language=,\n  numbers=none,', '  numbers=none,')
# remplacer les mappings literate errones par les vrais caracteres
pairs = {
 r"{\\'e}": "{é}", r"{\\e}": "{è}", r"{\\^e}": "{ê}", r"{\\\"e}": "{ë}",
 r"{\\}": "{à}", r"{\\^a}": "{â}", r"{\\\"a}": "{ä}",
 r"{\\^i}": "{î}", r"{\\\"i}": "{ï}",
 r"{\\^o}": "{ô}", r"{\\\"o}": "{ö}",
 r"{\\u}": "{ù}", r"{\\^u}": "{û}",
 r"{\\c c}": "{ç}", r"{\\oe}": "{œ}", r"{\\OE}": "{Œ}",
 r"{\\'E}": "{É}", r"{\\E}": "{È}", r"{\\^E}": "{Ê}",
 r"{\\A}": "{À}", r"{\\^A}": "{Â}", r"{\\^I}": "{Î}", r"{\\^O}": "{Ô}",
 r"{\\U}": "{Ù}", r"{\\c C}": "{Ç}",
}
for old,new in pairs.items():
    s = s.replace(old,new)
open(p,'w',encoding='utf-8').write(s)
print('ok')
