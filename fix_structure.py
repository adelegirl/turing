# -*- coding: utf-8 -*-
import io, re, shutil, os

src = r'C:/Users/ASUS/VSCODE/途灵Pro.html'
bak = r'C:/Users/ASUS/VSCODE/途灵Pro_backup3.html'
shutil.copy2(src, bak)

with io.open(src, 'r', encoding='utf-8') as f:
    lines = f.readlines()

tag_re = re.compile(r'(<div\b[^>]*>|</div>)')
stack = []   # {'indent': int, 'tag': str, 'line': int}
new_lines = []
fix_log = []

def indent_of(s):
    return len(s) - len(s.lstrip(' '))

for line in lines:
    stripped = line.strip()
    if stripped.startswith('<!--') or stripped == '-->':
        new_lines.append(line)
        continue

    matches = list(tag_re.finditer(line))
    ind = indent_of(line)

    # 行前补闭合：新块缩进 <= 栈顶 div 缩进，说明栈顶 div 应已闭合
    if matches:
        first = matches[0].group(1)
        if first.startswith('<div') and not first.startswith('</div'):
            if stack and ind <= stack[-1]['indent']:
                while stack and stack[-1]['indent'] >= ind:
                    t = stack.pop()
                    fix_log.append('补闭合 line%d 缩进%d %s' % (t['line'], t['indent'], t['tag'][:44]))
                    new_lines.append(' ' * t['indent'] + '</div>\n')
    else:
        if (stripped.startswith('</section>') or stripped.startswith('</footer>')
            or stripped.startswith('</ul>') or stripped.startswith('<section')
            or stripped.startswith('<footer') or stripped.startswith('<h2')
            or stripped.startswith('<h3') or stripped.startswith('<p')
            or stripped.startswith('<ul') or stripped.startswith('<span')):
            if stack and ind <= stack[-1]['indent']:
                while stack and stack[-1]['indent'] >= ind:
                    t = stack.pop()
                    fix_log.append('补闭合 line%d 缩进%d %s' % (t['line'], t['indent'], t['tag'][:44]))
                    new_lines.append(' ' * t['indent'] + '</div>\n')

    # 处理本行 div 标签，更新栈
    for m in matches:
        tag = m.group(1)
        if tag.startswith('</div>'):
            if stack:
                stack.pop()
        else:
            stack.append({'indent': ind, 'tag': tag, 'line': len(new_lines) + 1})

    new_lines.append(line)

# 文件末尾兜底
while stack:
    t = stack.pop()
    fix_log.append('文件尾补闭合 line%d %s' % (t['line'], t['tag'][:44]))
    new_lines.append(' ' * t['indent'] + '</div>\n')

with io.open(src, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('==== 共补全闭合标签 %d 个 ====' % len(fix_log))
for s in fix_log:
    print(s)
print('剩余未闭合 div: 0' if not stack else '剩余未闭合 div: %d' % len(stack))
print('写入完成, 文件大小:', os.path.getsize(src), '字节')
