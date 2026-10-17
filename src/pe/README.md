# PE 自由安装 Windows · PE 模块

打开上一级目录中的 `PE-Installation-Tutorial.html`（单文件离线版），或者本目录的 `index.html`。

固定虚拟环境：Samsung 500 GB、WD 1 TB 两块硬盘，以及装有 Windows ISO/WIM/ESD 的 Ventoy U 盘。PE 桌面仍采用 FirPE 风格。无场景选择、无资料保留评分；目标硬盘可自行删除、快速分区、格式化和安装。

操作提示：
1. DiskGenius 中查看硬盘，F6 快速分区。自定单选项可直接点击，再选择分区数量。
2. Dism++ → 文件 → 释放映像，先浏览加载镜像，再选择目标映像版本和安装分区。
3. 释放进度显示在软件底部状态栏；释放开始前确认“写入ESP分区磁盘1分区1”，确认后释放映像并写入引导。
4. 重启选择内置盘，进入 Windows OOBE 起始画面。

所有磁盘操作仅修改页面内虚拟状态。可随时在空闲时“重置虚拟环境”。不依赖网络 CDN 或后端，已接入 Windows 安装教程：Ventoy 镜像选择或左侧安装方式菜单可进入 PE；成功启动后继续原 OOBE。

源文件：`model.js`（虚拟磁盘）、`pe.js`（界面和流程）、`pe.css`（样式）、`dg-assets.js`（内嵌图标）。

验证：`node test-model.cjs`。依据及边界见 [RESEARCH.md](RESEARCH.md)。
