p = r'D:\smarta\gesi formation\_outils\images.py'
s = open(p, encoding='utf-8').read()
s = s.replace('ax.set_ylim(0, 100 * h / w)', 'ax.set_ylim(0, 100)')
open(p,'w',encoding='utf-8').write(s)
print('ok')
