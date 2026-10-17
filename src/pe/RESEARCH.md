# PE 安装 Windows：界面依据与实现记录

本模块单独开发，未修改现有 Windows ISO 教程，未上传到 Sites 或 NUC。软件界面均用 HTML/CSS 重建，磁盘、文件、镜像索引、安装进度为虚拟状态，没有执行真实软件或磁盘命令。

## 已实际查看的第一手材料

|对象|材料与截图|落实到实现|
|---|---|---|
|FirPE|[官方装机教程](https://docs.firpe.cn/guide/quickstart/)、[教程桌面截图](https://docs.firpe.cn/assets/20.BnehMHzd.png)|蓝色山峰桌面、左列圆形快捷方式、此电脑 / DiskGenius / Dism++、底部任务栏。壁纸为自行绘制的近似；DiskGenius 快捷方式改用官方截图中的应用图标。|
|DiskGenius|[主界面](https://www.diskgenius.cn/help/interface.php)、[主界面截图](https://www.diskgenius.cn/help/img/interface1.png)|上方分区结构图、左侧物理盘与分区树、右侧分区参数 / 浏览文件、容量与文件系统、当前分区高亮。官方截图标注 V5.3；不声称覆盖所有版本。|
|DiskGenius|[快速分区](https://www.diskgenius.cn/help/fastpart.php)、[对话框截图](https://www.diskgenius.cn/help/img/fast-partition-01.png)|F6、当前物理盘、MBR / GUID、分区数目、各分区大小 / 文件系统 / 卷标、ESP / MSR、对齐选项、删除全盘分区的确认。该命令立即分区并格式化。|
|DiskGenius|[格式化分区](https://www.diskgenius.cn/help/formatpart.php)、[对话框截图](https://www.diskgenius.cn/help/img/dlgformat1.png)|文件系统、簇大小、卷标、单独确认与进度；格式化只作用于所选卷。|
|DiskGenius|[建立新分区](https://www.diskgenius.cn/help/createpartex.php)、[浏览文件](https://www.diskgenius.cn/help/listfile.php)|连续空闲区中新建普通 / ESP / MSR 分区；分区表修改暂存后保存或放弃；通过 Windows / Users / 资料目录判断用途。|
|Dism++|[作者仓库安装文档](https://github.com/Chuyu-Team/Dism-Multi-language/blob/master/www.chuyu.me/zh-Hans/library/Best/使用Dism%2B%2B安装系统.md)、[快速入门](https://github.com/Chuyu-Team/Dism-Multi-language/blob/master/www.chuyu.me/zh-Hans/library/Quickstart.md)|顶部系统会话、文件 → 释放映像、可直接打开 ISO；格式化和添加引导独立选择；隐藏 ESP 无须分配盘符。|
|Dism++|[主界面截图](https://raw.githubusercontent.com/Chuyu-Team/Dism-Multi-language/master/www.chuyu.me/zh-Hans/images/MainUI.png)、[释放映像截图](https://raw.githubusercontent.com/Chuyu-Team/Dism-Multi-language/master/www.chuyu.me/zh-Hans/images/ISOInstallOS.png)|黑色系统标签与蓝色选中状态、左侧功能列表、映像属性表、目标映像下拉、源与目标浏览按钮、底部复选框及确定 / 取消。|
|Dism++|[中文语言资源](https://github.com/Chuyu-Team/Dism-Multi-language/blob/master/Languages/zh-Hans.xml)|核对中文术语、提示和功能名称；这是作者公开的语言资源与文档仓库，**不是 Dism++ 核心引擎源码**。|

查阅日期：2026-10-11。研究时原始 HTML、截图、Markdown 和语言 XML 保存在工作目录 work/pe-research，未将这些软件的源文件冒充本项目代码。

## 可操作范围

- 资源管理器：按虚拟盘符显示卷及容量；双击 / Enter 浏览文件夹；后退、上一级、搜索；U 盘 ISO / WIM / ESD 与工具入口；隐藏 ESP / MSR 和空白磁盘不作为普通卷展示。
- DiskGenius：物理盘选择、容量图、分区参数与文件检查、右键格式化 / 删除、新建 ESP / MSR / 普通分区、快速分区 F6、保存 Ctrl+S、放弃未保存更改、MBR → GPT。
- Dism++：切换离线系统会话、释放映像、读取虚拟 ISO / WIM / ESD、版本索引、目标卷、格式化、Compact、添加引导、映像释放进度、取消、引导修复、错误提示。
- 窗口：拖动、最小化、最大化、关闭、任务栏切换、菜单、对话框键盘操作。操作中的分区状态不会被另一个工具同时修改。
- 结果：目标系统与 EFI 引导分开记录；未找到 ESP 会显示“映像释放完成但添加引导失败”；修复后可进入模拟 OOBE 起始页。选择 Ventoy U 盘启动则返回 PE。

## 自由装机环境

当前界面不再提供练习场景选择，也不判定“无损重装”。默认保留两块虚拟硬盘和 Ventoy U 盘；用户自由选择目标盘并分区、格式化、释放映像。安装目标盘的数据允许清除，操作后的实际虚拟文件变化仍正常保留。

模型中的其他初始布局仅作为内部回归测试数据，不向用户提供模式入口。

## 为避免假装完整软件而明确保留的边界

- 桌面基于 FirPE 官方截图做风格复刻，不是可启动的 FirPE，也不是软件所有版本的像素级复刻。
- 所有硬盘型号、容量、文件、版本索引、系统状态和进度均为预设训练数据；不能导入或解析任意真实 ISO。
- 文件浏览窗口简化为虚拟文件列表。常用磁盘操作对话框保留装机相关字段；无损缩扩容、扇区编辑、恢复搜索、备份、坏道扫描、BitLocker、驱动注入、WIMBoot、WindowsToGo 等未展开或禁用。
- 模拟没有真实分区 GUID / MFT / SMART。起始扇区依据虚拟区间计算；容量图为了能看清 ESP/MSR，对小分区设有最小显示宽度，并非严格等比例。
- 格式化中的簇大小显示保留，不模拟不同簇大小的存储性能；对齐选项影响虚拟分区对齐标志。镜像进度采用短时演示，不模拟真实耗时。
- 安装确认中额外展示物理磁盘型号；针对装机 U 盘和 X: 内存盘设置教学范围限制。真实软件的错误文案、确认时机和可操作目标可能随版本变化。
- 取消长操作时本模拟不提交本次操作；真实工具可能已经写入部分数据，不应据此认为真实取消可以回滚。
- 进入 OOBE 只作为模块出口和结果核验，不接入已有 ISO / OOBE 教程；不发送父页面消息、不访问服务器、不持久化用户数据。

## 验证

运行 `node test-model.cjs` 可检查四条安装路线、数据保留 / 丢失、未保存分区表、介质丢失、损坏映像、错误目标、空间约束和启动结果。浏览器另行核对主界面、释放对话框、格式化确认、进度以及启动结果。


## DiskGenius 界面重做（2026-10-11）

这一版以官方 V5.3 主界面和经典 Win32 对话框为视觉基准，不使用现代卡片布局。

- 工具栏按“保存更改 / 搜索分区 / 恢复文件 / 快速分区 / 新建分区 / 格式化 / 删除分区 / 备份分区 / 系统迁移”排列。九个工具图标、标题栏应用图标、磁盘/卷/文件夹小图标均从官方 [interface1.png](https://www.diskgenius.cn/help/img/interface1.png) 中提取；不是 emoji 或 AI 生成图标。
- 格式化窗口左侧硬盘图来自 [dlgformat1.png](https://www.diskgenius.cn/help/img/dlgformat1.png)，新建分区窗口配图来自 [dlgcreatepart1.png](https://www.diskgenius.cn/help/img/dlgcreatepart1.png)。快速分区锁图标来自 [fast-partition-01.png](https://www.diskgenius.cn/help/img/fast-partition-01.png)。原图局部保存在 assets/dg-*.png，dg-assets.js 内嵌同一批 PNG，支持离线打开。图像权利归原软件权利人所有，来源在此保留。
- 新建分区普通/展开布局对照 [dlgcreatepart1.png](https://www.diskgenius.cn/help/img/dlgcreatepart1.png) 与 [dlgcreatepart2.png](https://www.diskgenius.cn/help/img/dlgcreatepart2.png)；可切换 MB/GB，展开详细参数，选择 ESP/MSR。高级原始参数仅展示，未开发 GUID、属性位和 CHS 直接编辑。
- 浏览文件对照 [listfile1.png](https://www.diskgenius.cn/help/img/listfile1.png)：左侧目录树展开，点击目录联动右侧多列文件列表，支持子目录与返回上一级。虚拟文件没有真实时间戳/文件大小时显示“—”；普通文件使用简化纸张图形，未伪称真实文件关联图标。
- 分区图恢复 NTFS 棕色、FAT32 蓝色的类型条及粉色当前分区边框；目录树采用浅黄色底、虚线连线与加减展开按钮；右侧密集表格展示 CHS、容量与蓝色参数。所有容量/用量/位置从虚拟模型计算，未复制截图中的硬盘数据。
- 菜单、工具栏仍保留安装无关功能的入口外观，未开发的二级功能禁用或明确说明范围。未复制官网广告条、截图中的红色教学标注，也不声称不同版本完全一致。

本轮浏览器验证：主窗口与三个对话框视觉检查；格式化后用量归零；缺失 ESP 场景新建 FAT32 ESP 并保存；资料目录树与文件表联动；空白盘自定 2 分区后生成 ESP/MSR/两个 NTFS 卷。浏览器无脚本错误，原有 model 测试继续通过。


## 自由安装与 Dism++ 流程调整（2026-10-11）

- U 盘卷名统一为 Ventoy，EFI 小分区为 VTOYEFI。FirPE 只用于 PE 桌面品牌，不作为装机 U 盘卷标。
- 未展开功能统一提示“前面的区域以后再来探索吧”。
- 快速分区的自定状态独立保存：选择自定后，即使数量是 3/4/5/6，也不会跳回预设单选项。
- 未加载有效镜像时，目标映像下拉为空且禁用，确定按钮禁用。加载有效 ISO/WIM/ESD 后才生成版本列表。安装说明与目标映像选择依据仍为上文作者安装教程。
- 按本轮指定交互实现：释放映像在主窗口底部状态栏显示进度；勾选添加引导时，释放完成后提示“引导将写入 … 分区”，展示实际目标硬盘及 ESP。确认后写入引导；取消确认保留已释放的系统，不执行本次引导写入。缺失 ESP 则提示修复。
- 整盘重分区后完成安装不会因原文件被清除判为失败。原始数据删除的确认仍保留，以复现工具操作本身。
- 本轮浏览器已验证自定数量保持选中、镜像加载前后版本列表状态、状态栏进度、ESP 确认及最终内置盘启动。


## 与原教程合并（2026-10-11）

当前实现覆盖前文“独立、不部署”的开发阶段记录：PE 已嵌入 Windows 教程，Ventoy 的 Windows ISO 与 FirPE ISO 自动分流；左侧可手动切换。PE 成功启动后通过校验来源窗口与本次运行标识的消息，把所选 Windows 版本传给原 OOBE/桌面流程。

ESP 确认按本轮指定更正为释放开始前显示，仅显示“写入ESP分区磁盘N分区N”，按钮为确定/取消，不再展示名称或“是否继续”。进度仍显示于 Dism++ 底部。页面上的预览标签、资料链接与教学模拟小字已删除。
