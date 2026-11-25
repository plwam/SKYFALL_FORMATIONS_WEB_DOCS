p = r'D:\smarta\gesi formation\module-django-gesibiblio\preamble.tex'
s = open(p, encoding='utf-8').read()
s = s.replace('''\\lstdefinestyle{html}{
  style=base,
  language=HTML,
  moredelim=[is][\\color{teal}\\bfseries]{\\{\\%}{\\%\\}},
  moredelim=[is][\\color{purple}]{\\{\\{}{\\}\\}}
}''', '''\\lstdefinestyle{html}{
  style=base,
  language=HTML
}''')
open(p,'w',encoding='utf-8').write(s)
print('done')
