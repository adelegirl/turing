# -*- coding: utf-8 -*-
import io, shutil, os

src = r'C:/Users/ASUS/VSCODE/途灵Pro.html'
bak = r'C:/Users/ASUS/VSCODE/途灵Pro_backup.html'
shutil.copy2(src, bak)

with io.open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# 1) 补回 hero-actions 缺失的闭合 </div>（在第二个按钮 </a> 之后）
old_btn = '        <a class="btn btn-ghost" href="#flow">技术原理</a>\n'
new_btn = '        <a class="btn btn-ghost" href="#flow">技术原理</a>\n      </div>\n'
if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print('hero-actions 闭合补上: OK')
else:
    print('hero-actions 未匹配!')

# 2) 替换图片引用：旧IP图 -> 新立牌图
old_img = 'src="途灵小老师_IP形象.png"'
new_img = 'src="途灵IP_立牌.jpg"'
if old_img in content:
    content = content.replace(old_img, new_img)
    print('图片替换为立牌图: OK')
else:
    print('旧图未匹配!')

with io.open(src, 'w', encoding='utf-8') as f:
    f.write(content)

print('写入完成, 文件大小:', os.path.getsize(src))
print('备份文件大小:', os.path.getsize(bak))
