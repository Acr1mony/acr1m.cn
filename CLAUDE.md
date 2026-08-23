# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概览

基于 **Hexo 8** 的静态博客站点（`package.json` 中 `hexo.version` 为 8.1.2），站点名「Logiac/AC的物流分享」。内容以物流/建站相关中文 Markdown 文章为主，主题为本地 vendored 的 `prince`（非 npm 主题包）。

本仓库从 `E:\Blog\acr1m.cn` 导入；`node_modules/`、`public/`、`db.json` 被 `.gitignore` 忽略，需本地安装与生成。

## 常用命令

在仓库根目录执行：

```bash
npm install          # 安装依赖（首次或 lock 变更后）
npm run server       # 本地预览：hexo server（默认 http://localhost:4000）
npm run build        # 生成静态站点到 public/：hexo generate
npm run clean        # 清空 Hexo 缓存与 public/：hexo clean
npm run deploy       # hexo deploy（当前 _config.yml 中 deploy.type 为空，未配置部署目标）
```

文章相关（需已 `npm install`，可直接用 npx）：

```bash
npx hexo new "文章标题"           # 按 scaffolds/post.md 在 source/_posts/ 创建文章
npx hexo new page "页面名"        # 创建页面
npx hexo new draft "草稿标题"     # 创建草稿
npx hexo publish "草稿标题"       # 发布草稿
npx hexo generate --watch         # 监听变更并持续生成
```

本仓库 **没有** 配置 lint、单元测试或 CI 测试脚本；主题 `themes/prince/package.json` 中的 `npm test` 仅为占位。

## 架构

```
_config.yml                 # 站点级 Hexo 配置（title/url/permalink/theme/deploy 等）
package.json                # 依赖与 npm scripts；构建链全部经 hexo CLI
source/_posts/*.md          # 文章源（front matter + Markdown/HTML）
scaffolds/{post,page,draft}.md
themes/prince/              # 当前启用主题（_config.yml 中 theme: prince）
  _config.yml               # 主题配置：导航、关于我、GitHub、GA 等
  layout/**/*.jade          # Jade 模板（依赖 hexo-renderer-jade）
  languages/{default,zh-CN}.yml
  scripts/customGist.js     # 注册 hexo tag: {% gist id [file] %}
  source/                   # 主题静态资源（css/js/fonts/图片），生成时合并进站点
public/                     # 生成产物（gitignore，勿手改）
.github/dependabot.yml      # npm 依赖每日更新
```

数据流：`source/` 文章 + `themes/prince` 模板/资源 → `hexo generate` → `public/`。

### 双配置文件

| 文件 | 作用 |
|------|------|
| 根目录 `_config.yml` | 站点元数据、`source_dir`/`public_dir`、permalink、分页、**启用主题名**、deploy |
| `themes/prince/_config.yml` | 顶栏名称/描述、`nav`、摘录链接、about 图、GitHub、主题页链接、GA |

改导航、侧栏「关于我」、favicon 路径等应改主题配置；改 URL 结构、语言、生成器行为改站点配置。

### 主题与渲染

- 启用主题：`theme: prince`。`hexo-theme-landscape` 仍在 `package.json` 依赖中，但未启用；根目录 `_config.landscape.yml` 为空文件。
- 布局为 **Jade**（`layout/*.jade`、`_partial/`、`mixins/`），不是 EJS/Swig。改页面结构时编辑这些 `.jade` 文件。
- Markdown 由 `hexo-renderer-marked` 渲染；样式相关还有 `hexo-renderer-stylus`（主题当前以预置 CSS 为主）。
- `themes/prince/scripts/customGist.js` 在 Hexo 加载主题时注册自定义 tag `gist`。

### 文章约定

- 路径：`source/_posts/*.md`
- 常见 front matter：`title`、`date`、`categories`、`tags`、`description`；个别文件可能含非标准字段（如错误的 `layout:` 值），生成时需注意
- 正文可为 Markdown，并夹杂 HTML（如 `<font>`、`<table>`、`<center>`）
- 新文章文件名默认：`new_post_name: :title.md`（见站点 `_config.yml`）
- permalink：`:year/:month/:day/:title/`

### 当前配置注意点

- `url` 已设为 `https://acr1m.cn`（若实际域名不同需同步修改）。
- 站点 `language: zh-CN`，与主题 `zh-CN.yml` 及中文正文一致。
- `deploy.type` 为空；历史文章提到过 Netlify + GitHub + Cloudflare，但本仓库未包含对应 deploy 插件或工作流。
- 主题 `favicon: /favicon.ico`，与 `themes/prince/source/favicon.ico` 一致。

## 修改时的习惯位置

- 写文章 / 改内容 → `source/_posts/`
- 站点标题、链接形态、部署 → `_config.yml`
- 导航、侧栏、主题文案 → `themes/prince/_config.yml`
- 页面 HTML 结构 → `themes/prince/layout/`
- 主题样式/脚本/图片 → `themes/prince/source/`
