# Windows 安装 Tutorial

通过浏览器练习 BIOS、Ventoy、Windows 安装程序或 PE 安装、OOBE、驱动安装和激活操作。支持键盘操作；所有磁盘、安装和账户操作都是页面内模拟。

在线访问：https://hzwzwzw.github.io/windows-installation-tutorial/

## 目录

- `docs/windows/`：可直接部署的完整网站，Windows 主页面为 `windows.html`。
- `src/pe/`：PE、DiskGenius 和 Dism++ 模拟器的可编辑源文件及参考资料。
- `scripts/build-pe.py`：将 PE 源文件打包到网站，同时同步 Windows 入口页面。

## 本地运行

```sh
python3 scripts/build-pe.py
python3 -m http.server 8000 --directory docs
```

访问 http://localhost:8000/windows/。

## GitHub Pages

发布源为 `main` 分支的 `/docs` 目录。修改后提交并推送到 `main`，GitHub Pages 会自动更新。

修改 PE 后先运行 `python3 scripts/build-pe.py`。修改 Windows 页面时编辑 `docs/windows/windows.html`，再运行同一脚本同步入口；其他 JS/CSS 可直接编辑。

第三方界面名称、图标与素材属于各自权利人。Ventoy 相关许可见 `docs/windows/assets/VENTOY-LICENSE.txt`；PE 界面参考资料见 `src/pe/RESEARCH.md`。
