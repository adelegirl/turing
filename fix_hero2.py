# -*- coding: utf-8 -*-
import io, shutil, os

src = r'C:/Users/ASUS/VSCODE/途灵Pro.html'
bak = r'C:/Users/ASUS/VSCODE/途灵Pro_backup2.html'
shutil.copy2(src, bak)

with io.open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# 1) 补回 hero-text 缺失的闭合 </div>（在 hero-actions 闭合之后、hero-ip 之前）
old_div = '        <a class="btn btn-ghost" href="#flow">技术原理</a>\n      </div>\n\n\n    <div class="hero-ip">'
new_div = '        <a class="btn btn-ghost" href="#flow">技术原理</a>\n      </div>\n    </div>\n\n    <div class="hero-ip">'
if old_div in content:
    content = content.replace(old_div, new_div, 1)
    print('hero-text 闭合补上: OK')
else:
    print('hero-text 闭合: 未匹配目标位置!')

# 2) 给 IP 图加一点透明度（融入深蓝背景）
old_style = 'style="width:min(340px,80vw); aspect-ratio:1/1; object-fit:contain; border-radius:28px; box-shadow:0 30px 70px -30px rgba(0,0,0,.6);"'
new_style = 'style="width:min(340px,80vw); aspect-ratio:1/1; object-fit:contain; border-radius:28px; box-shadow:0 30px 70px -30px rgba(0,0,0,.6); opacity:.88;"'
if old_style in content:
    content = content.replace(old_style, new_style, 1)
    print('IP 图透明度: OK')
else:
    print('IP 图透明度: 未匹配样式!')

with io.open(src, 'w', encoding='utf-8') as f:
    f.write(content)
print('写入完成, 文件大小:', os.path.getsize(src))
print('备份大小:', os.path.getsize(bak))
