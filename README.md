````markdown
# 🔍 压缩包源码审核工具

这是一个基于 Python 和 PyQt5 开发的图形界面工具，用于自动分析 `.zip`、`.rar`、`.7z`、`.tar` 等压缩文件中是否包含源代码文件。适用于代码安全审核、归档检查等场景。

## 🧩 功能特性

- 支持压缩格式：`.zip` / `.rar` / `.7z` / `.tar(.gz/.bz2)`
- 自动识别各类源代码及配置文件
- 图形界面操作，简单易用
- 支持中文路径、中文文件名
- 支持“打开解压目录”一键定位
- 自动列出最多 100 个可疑文件

## 📦 打包说明（使用 PyInstaller）

项目可使用 `PyInstaller` 一键打包为 `.exe`，无需依赖 Python 环境：

```bash
pyinstaller audit_gui.py ^
  --noconfirm ^
  --onefile ^
  --windowed ^
  --icon=rocket.ico ^
  --add-binary "unrar.exe;." ^
  --add-binary "7z.exe;." ^
  --add-binary "7z.dll;."
````

### 打包文件结构示例：

```
your_project/
├── audit_gui.py
├── rocket.ico
├── unrar.exe
├── 7z.exe
├── 7z.dll
└── ...
```

## 📁 源码文件识别规则

识别扩展名包括（部分示例）：

```text
.py .c .cpp .h .java .js .ts .go .rs .sh .html .yaml .json ...
```

识别文件名包括（部分示例）：

```text
Makefile, CMakeLists.txt, package.json, pom.xml, requirements.txt ...
```

## 🖥️ 环境依赖

* Python 3.6+
* PyQt5
* rarfile
* py7zr

安装依赖：

```bash
pip install -r requirements.txt
```

`requirements.txt` 示例：

```
pyqt5
rarfile
py7zr
```

## 📸 截图示例
发现源码：（支持下拉显示100条数据，完整数据点击“打开解压目录”）
![image](https://github.com/user-attachments/assets/d0459446-f608-4103-9e0c-5640e0afec7f)

