p = r'D:\smarta\gesi formation\_outils\images.py'
s = open(p, encoding='utf-8').read()
s = s.replace('label(ax, 55, 64, "3. données", fs=8.5)', 'label(ax, 54, 61, "3. données", fs=8.5)')
s = s.replace('label(ax, 46, 39, "5. contexte", fs=8.5, color=PURPLE)', 'label(ax, 47, 41, "5. contexte", fs=8.5, color=PURPLE)')
s = s.replace('label(ax, 48, 38, "HTML", fs=8.5, color=PURPLE)', 'label(ax, 35, 37, "HTML", fs=8.5, color=PURPLE)')
s = s.replace('box(ax, 24, 6, 68, 88, "", fc="#FBFCFD"', 'box(ax, 24, 12, 68, 82, "", fc="#FBFCFD"')
open(p,'w',encoding='utf-8').write(s)
print('ok')
