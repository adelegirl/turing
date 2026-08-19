# turing 静态站点

这是从 `C:\Users\ASUS\VSCODE` 整理出来的 Turing 项目文件。

## 文件说明

| 文件 | 说明 |
|------|------|
| `index.html` | 网站首页，内容与 `途灵Pro.html` 相同 |
| `途灵Pro.html` | 原始首页 |
| `途灵Pro_backup4.html` | 备份版本 |
| `技术原理动画.html` | 技术原理动画页面 |
| `豆豆.png` | 图片资源 |
| `途灵IP_立牌.jpg` | 图片资源 |
| `途灵小老师_IP形象.png` | 图片资源 |

## 推送到 GitHub 步骤

1. 在 GitHub 新建仓库 `turing`：
   <https://github.com/new?name=turing>

2. 在本机打开 Git Bash，进入本目录：

   ```bash
   cd "C:\Users\ASUS\WorkBuddy\2026-08-20-01-21-42\turing"
   ```

3. 添加远程仓库（把 `YOUR_USERNAME` 换成你的 GitHub 用户名）：

   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/turing.git
   git branch -M main
   git push -u origin main
   ```

4. 启用 GitHub Pages：
   - 打开仓库 → Settings → Pages
   - Source 选择 `Deploy from a branch`
   - Branch 选择 `main`，目录选 `/ (root)`
   - 保存后会得到访问地址：`https://YOUR_USERNAME.github.io/turing/`

> 访问根地址时会自动加载 `index.html`，即 `途灵Pro.html` 的内容。

## 线上地址

- 网站首页：<https://adelegirl.github.io/turing/>
- 仓库地址：<https://github.com/adelegirl/turing>
