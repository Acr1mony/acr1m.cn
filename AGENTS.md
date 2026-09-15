# 仓库贡献指南

## 项目结构与模块组织

本仓库是一个基于 Hexo 8 的静态博客。站点全局配置位于 `_config.yml`，主题专用配置应放在 `themes/prince/_config.yml`。已发布文章以 Markdown 格式存放在 `source/_posts/`，文章头部信息应遵循 `scaffolds/post.md` 中的模板。可复用的内容模板位于 `scaffolds/`。本地 `prince` 主题的 Jade 模板位于 `themes/prince/layout/`，浏览器脚本和样式位于 `themes/prince/source/`，翻译文件位于 `themes/prince/languages/`，Hexo 辅助脚本位于 `themes/prince/scripts/`。生成目录 `public/`、缓存文件 `db.json` 和依赖目录 `node_modules/` 不属于源代码，请勿提交。

## 构建、测试与本地开发命令

- `npm ci`：按照 `package-lock.json` 安装确切版本的依赖。
- `npm run server`：启动 Hexo 本地预览服务，默认地址为 `http://localhost:4000`。
- `npm run clean`：清除生成文件和缓存；排查输出未更新等问题时先执行此命令。
- `npm run build`：将生产站点生成到 `public/`，是提交前必须执行的验证命令。
- `npm run deploy`：执行 Hexo 部署；当前 `_config.yml` 尚未配置部署目标，配置完成后方可使用。

## 编码风格与命名约定

YAML 和 Jade 文件使用两个空格缩进；JavaScript 与 CSS 应保持所在文件的现有风格。Hexo 定义的 YAML 键名使用小写。新文章应采用简洁、稳定的 `.md` 文件名，并包含 `title`、`date` 和 `tags` 头部字段。共享布局逻辑应提取到 Jade mixin，避免重复标记。不要直接修改 `bootstrap.min.js`、`jquery-3.2.1.min.js` 等第三方压缩文件。项目未配置格式化或代码检查工具，因此提交前应检查差异，避免无关的空白变更。

## 测试规范

本项目暂未配置自动化测试或覆盖率要求。每次修改文章、配置或主题后，都应运行 `npm run build`，并将警告或渲染失败视为需要修复的问题。修改布局、CSS 或 JavaScript 后，还应运行 `npm run server`，手动检查首页、文章页、归档、标签、图片和响应式布局，并确认站内链接与代码块渲染正常。

## 提交与拉取请求规范

当前工作副本不包含 Git 历史，因此无法推断仓库原有的提交规范。请使用简短、祈使语气的提交标题，例如 `添加物流阅读笔记` 或 `修复移动端文章导航`，并将无关修改拆分提交。拉取请求应说明用户可见的变化、列出已执行的验证、关联相关问题，并为主题视觉调整提供修改前后截图。禁止提交密钥、部署凭据、生成的 `public/` 内容、日志或本地缓存文件。
