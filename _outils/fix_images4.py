p = r'D:\smarta\gesi formation\_outils\images.py'
s = open(p, encoding='utf-8').read()
s = s.replace('ms=13, z=2, shrinkA=1, shrinkB=1):', 'ms=13, z=4, shrinkA=1, shrinkB=1):')
open(p,'w',encoding='utf-8').write(s)
print('ok')
