---
title: ALGS Interactive Replay 功能介绍
date: 2026-08-24 15:00:00
categories: APEX LEGENDS
tags:
  - APEX LEGENDS
description: ALGS Interactive Replay的功能介绍，分析赛事具体信息必备，ALGS数据。
---
# ALGS Interactive Replay 功能介绍

> 工具站点：[Apex Legends Status](https://apexlegendsstatus.com/)  
> 示例对局：[Year 6, Split 2 Pro League - APAC_S - Day 3 B vs. C Game #4](https://apexlegendsstatus.com/algs/game/2dc2c18972ea07b123eeba23737a9314)  
> 文档性质：社区网页工具说明（非 EA/Respawn 官方客户端回放）

---

## 1. 工具是什么

**ALGS Interactive Replay** 是 Apex Legends Status（ALS）提供的**浏览器端 ALGS 对局交互式回放分析工具**。

它不是游戏内录像，而是把职业赛一局的完整事件数据可视化到地图上，让你可以：

- 任意时刻查看战局
- 追踪队伍/选手走位
- 分析交战、物资、圈型、复活与淘汰节奏
- 对照选手 POV 录像（VOD）做同步复盘

覆盖范围通常包括 ALGS 主要赛事与赛区（Pro League、Playoffs 等，Year 3 起逐步完善）。对局结束后数据一般会较快上线。

---

## 2. 页面整体布局

打开一局回放后，界面大致分为 5 个区域：

| 区域 | 位置 | 主要作用 |
|------|------|----------|
| 顶栏 (Topbar) | 顶部 | 对局标题、分享、系列赛结果、冠军/相关战队标识 |
| 事件面板 (EVENTS) | 左侧 | 时间线事件流、事件类型筛选 |
| 地图舞台 (Map) | 中央 | 地图、选手、圈、空投、死亡箱、走位、热力图、绘图 |
| 播放控制条 | 底部 | 播放/暂停、进度、倍速、平滑、走位进度等 |
| 洞察面板 (INSIGHTS) | 右侧 | Live HUD、交战、物品、POI、选手详情、VOD |

左右面板都可折叠/展开，方便专注看地图。

---

## 3. 顶栏功能

### 3.1 对局标题
显示完整赛事上下文，例如：

`Year 6, Split 2 Pro League - APAC_S - Day 3 B vs. C Game #4`

从标题可直接看出：赛季/分赛段、赛事类型、赛区、比赛日、组次、局号。

### 3.2 Share（分享）
生成/复制当前回放链接，便于分享给队友或用于内容创作。  
（加载未完成时按钮可能暂时不可用。）

### 3.3 Series results（系列赛结果）
跳转到该局所属系列赛/比赛日结果页。  
示例：  
`[Year 6, Split 2 Pro League - APAC_S - Day 3 B vs. C Game #4](https://apexlegendsstatus.com/algs/game/2dc2c18972ea07b123eeba23737a9314)`

便于从“单局回放”回到“整轮积分/对阵”上下文。

---

## 4. 左侧 EVENTS（比赛事件流）

### 4.1 作用
按时间列出本局几乎所有关键事件，是“文字版战报 + 可跳转时间轴”。

### 4.2 快速过滤
- **Show all**：显示全部事件
- **Combat only**：只看战斗相关事件
- **Settings**：展开细粒度事件类别开关

### 4.3 可筛选的事件类别
工具支持按类别开关事件，常见包括：

| 类别 | 含义 |
|------|------|
| Kills | 击杀 |
| Damage | 伤害 |
| Downs | 击倒 |
| Weapon switch | 切枪 |
| Ability used | 技能使用 |
| Grenade | 投掷物 |
| Assist | 助攻 |
| Banner | 收旗帜 |
| Pick up / Drop / Use item | 拾取 / 丢弃 / 使用物品 |
| Ammo used | 消耗弹药 |
| Zipline | 滑索 |
| Connected / Disconnected | 连接 / 断线 |
| Character | 选择传奇 |
| Revive | 扶起 |
| Respawn | 重生 |
| Squad eliminated | 小队淘汰 |
| Ring start / Ring end | 毒圈开始收缩 / 收缩结束 |
| Match end | 比赛结束 |

### 4.4 典型用法
- 复盘某次团战前：先在事件流定位 `Downs/Kills/Ability`
- 查资源节奏：看 `Pick up / Use item`
- 查转点时机：结合 `Ring start` 与走位

---

## 5. 中央地图与图层控制

地图基于可缩放交互地图（Leaflet）。支持滚轮/按钮缩放（`+` / `−`）。

### 5.1 选手显示模式
下拉选项：

1. **Full player info on map**：完整信息（名字、状态等更全）
2. **Player names only**：只显示名字
3. **Player arrows only**：只显示方向箭头
4. **All players hidden**：隐藏全部选手

适合从“全局观战”切换到“干净看圈/看走位”。

### 5.2 死亡显示模式
1. **Deathboxes**：死亡箱
2. **Death markers**：死亡标记
3. **Hide deaths**：隐藏死亡信息

### 5.3 圈层（Ring）
- **Next ring**：显示下一圈
- **All rings**：显示全部圈型轨迹/阶段

可用来研究：
- 落点与初圈关系
- 中后期转点是否提前
- 决赛圈站位选择

### 5.4 地图物件
- **Care packages（空投）**  
  可查看空投相关信息（含内容、开启情况等，视数据完整度）
- **Respawn beacons（重生信标）**  
  含地图信标与移动信标；已使用状态通常会有区分

### 5.5 热力图（Heatmap）
总开关：Heatmap  
类型：

- **Fights**：交战热力（伤害/击杀活跃区）
- **Looting**：搜刮热力
- **Healing**：治疗热力（针、包、电池、细胞、凤凰等）

适合快速回答：
- 这局热点在哪
- 某 POI 是否高频交火
- 治疗压力出现在哪些区域

### 5.6 走位（Pathing）
- 总开关：**Pathing**
- **Teams** 按钮：按队伍开关轨迹
  - **Toggle all**：全选/全不选
  - **Toggle top 5**：只看前五名相关轨迹（便于聚焦强队）

示例局队伍（按名次）：

1. VK GAMING  
2. Dogred  
3. CPR  
4. ARAM  
5. Team RRQ  
6. Outside  
7. S8UL  
8. 2c1m  
9. SaWeiQi  
10. MaMa Clubs  
11. Kirisame  
12. UBI CILEMBU  
13. SMP  
14. Bearclaw Gaming  
15. Orange  
16. Relove DCG  
17. TitanEsportsClub  
18. TuBoShu  
19. AELIX  
20. Void Esports OCE  

### 5.7 绘图模式（Draw controls）
用于标注教学/复盘：

| 控件 | 作用 |
|------|------|
| 颜色选择器 | 选择画笔颜色 |
| 线宽滑条 | 1–20 |
| Free draw | 自由绘制 |
| Circle | 画圆 |
| Arrow | 画箭头 |
| Eraser | 擦除 |
| Undo | 撤销上一笔 |
| Clear | 清空全部标注 |

常见用途：标转点路线、圈边危险区、夹击方向、资源点分工。

---

## 6. 底部播放与时间轴

### 6.1 基本播放
- **时间显示**：当前时间 / 总时长（示例局约 `16:39`）
- **Play / Pause**
- **倍速**：`x0.5 / x1 / x2 / x4 / x8`
- 可直接在时间输入框或进度条跳转

### 6.2 时间轴图层开关
时间轴上可切换关注的事件层：

- **RING**：毒圈阶段
- **KILLS**：击杀
- **DOWNS**：击倒
- **ELIMS**：小队淘汰
- **RESPAWN**：重生
- **REVIVE**：扶起
- **FIGHTS**：交战区段
- **PATH**：走位相关

鼠标悬停时间轴刻度可看具体事件摘要，例如：

- `wert6031 killed void.middoh (G7 Scout)`
- `RRQ EzFlashKIDZ revived RRQ Prycyy`
- `Void Esports OCE eliminated`
- `Ring 3 closing`

### 6.3 高级播放选项
- **Smooth**：平滑插值播放（观感更连贯）
- **Pane to ring**：视角跟随/聚焦毒圈（便于看缩圈节奏）
- **Progressive pathings**：走位轨迹随时间逐步绘制（而不是一开始就画完全程）

---

## 7. 右侧 INSIGHTS（洞察面板）

右侧是分析核心，包含多个标签页。

### 7.1 Live HUD（实时状态）
默认最常用页。按队伍展示“当前时间点”的活体状态，例如：

- 队伍名次（`#1`–`#20`）
- 队伍击杀/伤害等汇总信息
- 选手名、传奇
- 血量/护盾（如 `100 / 50`）
- 存活人数（如 `3/3`）

作用：像“上帝视角记分板 + 血条监视器”。

点击战队后，可以只在地图上单独显示该队伍选手；点击选手后，可进一步进入个人细节（Player 标签）。

### 7.2 Fights（交战分析）
列出检测到的交战片段，信息通常包括：

- 搜索框：`Search team in fights...`(在Fights中搜索战队...)
- Fight 编号（如 Fight #35）
- 状态（如 `CONCLUDED意为已结束`）
- 持续时长、发生圈层（Ring 1–5）
- 双方队伍
- 击倒/伤害等摘要
- **Jump**：一键跳到该交战时间点
- 交战时间线明细（谁在 +Xs 用什么武器/技能打了谁，打后血盾变化）
- **View more details**：展开更多细节
  - Player combat stats：统计双方交战KD和伤害承伤数据
    - 击杀丨击倒丨助攻丨伤害丨承伤丨伤害转化率(伤害/承伤)
  - Weapons used：统计存在输出伤害的武器/技能的命中次数和伤害
    - 玩家丨武器/技能丨命中次数丨伤害
  - Healing used：统计战斗中电池和医疗物品的使用次数
    - 小电丨大电丨小血丨大血丨凤凰

适合：
- 复盘关键团战
- 统计某队交战次数
- 看伤害交换是否划算

### 7.3 Items（物品分析）
- 列表展示本局物品相关事件
- 提示：`Hover item rows to highlight pick/drop/use positions on map.`
  - 悬停物品行，可在地图高亮拾取/丢弃/使用位置(高亮颜色绿色为拾取、红色为丢弃、蓝色为使用)
- 排序方式：
  - Most events（事件最多）
  - Name A-Z（按名称A-Z排序）
  - Most picked（最多拾取）
  - Most dropped（最多丢弃）
  - Most used（最多使用）

适合研究：
- 关键武器/配件流转
- 某类物资争抢点
- 治疗物消耗节奏

### 7.4 Map POIs（落点与 POI）
两个子页：

1. **Inventory**  
   - 选手离开落点 POI 边界时的背包快照  (落点POI边界指的是战队降落资源区的划分边界，每个降落区边界具体划分可到：https://apexlegendsstatus.com/algs/map-analytics 的 Metadata/Physical elements 下方的Show POIs查看)
   - 说明文案：  
     `This is the inventory a player has when the player has left its POI boundaries.`
2. **POI Points**  
   - 各队落点/POI 相关统计与位置
> 注：个别地图版本若 POI 数据未配置，会提示类似  
> `POIs not found for mp_rr_desertlands_mu5.`  
> 此时其他回放功能仍可用。

### 7.5 Player（选手详情）
- 需先在 Live HUD 中选择选手
- 展示该选手在当前时间点/本局维度的详细数据
- 常见关联信息（界面表头可见）：
  - Legend / Survive Time
  - Kills / Deaths / Knockdowns / Assists
  - DMG Dealt / DMG Taken / Revives / Grenades
  - Evo Progression：护甲进化进程，如White (50) 2:11指在游戏时间2:11时进化为蓝甲，这里有些选手的数据有误，以实际为准
  - Legend Upgrades：天赋选择，同上
  - Weapon Breakdown：武器分析，显示造成伤害武器的：伤害量/击杀/击倒/命中数
  - Inventory @gametime：当前时间点持有的物品
    - @ 符号后为当前游戏时间节点的统计，如 @10:55 指的是在当局游戏时间10分55秒时该玩家所持有的物品

### 7.6 VODs（同步录像）
- VODS:
    - 把回放时钟与选手 POV 录像对齐，调节正值为选手POV快进时间
主要能力：
- 按战队列出可看 POV（Watch / Open on Twitch）
- **最多同时选择 3 路 POV** 在地图旁观看
- 播放进度跟随回放时间轴
- **Δs（时间偏移）**：给所有 POV 统一加减秒数，校正不同源的时间误差
- 地图联动选项：
  - **Pane to selected teams**：视角跟随所选队伍
  - **Target teams cards only**：仅保留目标队伍卡片，减少干扰

适合：
- “地图上帝视角 + 选手第一视角”双屏复盘
- 教练组对比同一团战的不同视角决策

---

## 8. 数据维度总览

一局回放通常可覆盖这些信息维度：

1. **赛事元数据**：赛季、分赛段、赛区、日次、组次、局号  
2. **队伍与选手**：队名、选手 ID、传奇  
3. **空间信息**：地图坐标、走位轨迹、POI、圈型  
4. **战斗信息**：伤害、击倒、击杀、助攻、武器、技能  
5. **生存信息**：血盾、扶起、重生、淘汰顺序  
6. **经济/物资**：拾取、丢弃、使用、空投  
7. **时间信息**：精确到秒的事件流与可拖动进度  
8. **视频信息**：可同步的POV与VOD  

---

## 9. 使用前须知

1. **需要浏览器**，现代 Chrome / Edge 体验最佳。  
2. 首次进入可能出现 **Cloudflare / 人机验证**，通过后才会加载完整回放数据。  
3. 数据来自赛事日志可视化，细节完整度可能随地图版本、赛事源、功能迭代变化。  
4. 部分子功能（如某地图 POI 库、某些 VOD 源）可能暂时缺失，但不影响主回放。  
5. 这是社区工具，功能持续更新；以页面实际控件为准。

---

## 10. 与“普通观赛”的区别

| 对比项 | 直播/录像观赛 | ALGS Interactive Replay |
|--------|----------------|--------------------------|
| 视角 | 导播/选手 POV | 全局地图 + 可选 POV |
| 时间控制 | 线性为主 | 任意跳转、多倍速 |
| 信息密度 | 受镜头限制 | 全队状态可同时看 |
| 走位研究 | 难 | 轨迹/热力图直接看 |
| 战术标注 | 需外接工具 | 内置绘图 |
| 事件检索 | 靠记忆/拖进度条 | 事件流 + 分类过滤 + Fight 跳转 |

---

## 下载本文

如需离线阅读或二次编辑，可直接下载完整正文：

<div class="post-download">
  <a class="post-download-btn" href="/downloads/algs-interactive-replay.md" download="ALGS-Interactive-Replay功能介绍.md">下载 Markdown（.md）</a>
  <a class="post-download-btn" href="/downloads/algs-interactive-replay.docx" download="ALGS-Interactive-Replay功能介绍.docx">下载 Word（.docx）</a>
</div>