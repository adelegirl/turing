# -*- coding: utf-8 -*-
"""临时脚本：从技术原理动画.html 提取途灵logo(base64) 并替换途灵Pro.html 两处图标"""
import re, shutil, os, sys

vscode = r'C:\Users\ASUS\VSCODE'
src_path = os.path.join(vscode, '技术原理动画.html')
dst_path = os.path.join(vscode, '途灵Pro.html')
bak_path = os.path.join(vscode, '途灵Pro_backup5.html')

# 1. 备份
shutil.copy2(dst_path, bak_path)
print('BACKUP OK:', bak_path, os.path.getsize(bak_path))

# 2. 提取 base64
src = open(src_path, encoding='utf-8').read()
m = re.search(r'<div class="logo-dot"><img src="(data:image/jpeg;base64,[^"]+)"', src)
if not m:
    print('ERROR: logo base64 not found'); sys.exit(1)
data = m.group(1)
print('LOGO base64 length:', len(data))

# 3. 替换两处 span
html = open(dst_path, encoding='utf-8').read()
old = '<span class="logo">🧭</span>'
img_html = '<span class="logo"><img src="' + data + '" alt="途灵logo" style="width:100%;height:100%;border-radius:9px;object-fit:cover;display:block;"></span>'
cnt = html.count(old)
print('OCCURRENCES:', cnt)
if cnt != 2:
    print('ERROR: expected 2 occurrences, got', cnt); sys.exit(1)
html2 = html.replace(old, img_html)

# 4. 写回
open(dst_path, 'w', encoding='utf-8').write(html2)
print('WRITTEN OK, new size:', os.path.getsize(dst_path))
print('DONE')
