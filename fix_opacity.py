# -*- coding: utf-8 -*-
import io, os

src = r'C:/Users/ASUS/VSCODE/途灵Pro.html'

with io.open(src, 'r', encoding='utf-8') as f:
    content = f.read()

old = 'box-shadow:0 30px 70px -30px rgba(0,0,0,.6); opacity:.88;"'
new = 'box-shadow:0 30px 70px -30px rgba(0,0,0,.6); opacity:.75;"'

if old in content:
    content = content.replace(old, new, 1)
    print('透明度调至 0.75: OK')
else:
    print('未匹配当前透明度值!')

with io.open(src, 'w', encoding='utf-8') as f:
    f.write(content)
print('写入完成, 文件大小:', os.path.getsize(src))
