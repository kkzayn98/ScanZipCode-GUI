<p align="right">
  🈶 <a href="#中文">中文</a> | <a href="#english">English</a>
</p>

# 🚀 Code Archive Auditor

> A Python + PyQt5 GUI tool to detect source code in `.zip`, `.rar`, `.7z`, `.tar(.gz/.bz2)` archives.

---

## 🧩{#中文}

### 🔍 压缩包源码审核工具

这是一个基于 Python 和 PyQt5 开发的图形界面工具，用于自动分析 `.zip`、`.rar`、`.7z`、`.tar` 等压缩文件中是否包含源代码文件。适用于代码安全审核、归档检查等场景。

### ✅ 功能特性

- 支持压缩格式：`.zip` / `.rar` / `.7z` / `.tar(.gz/.bz2)`
- 自动识别常见源码和配置文件
- 简单易用的图形界面
- 支持中文路径和中文文件名
- 支持一键打开解压目录
- 最多列出 100 个可疑文件

### 📦 打包说明（PyInstaller）

可使用 PyInstaller 一键打包为 `.exe`，无需安装 Python：

```bash
pyinstaller audit_gui.py ^
  --noconfirm ^
  --onefile ^
  --windowed ^
  --icon=rocket.ico ^
  --add-binary "unrar.exe;." ^
  --add-binary "7z.exe;." ^
  --add-binary "7z.dll;."
```

#### 打包目录结构示例

```
your_project/
├── audit_gui.py
├── rocket.ico
├── unrar.exe
├── 7z.exe
├── 7z.dll
└── ...
```

### 📁 识别规则

**扩展名（示例）**：

```text
.py .c .cpp .h .java .js .ts .go .rs .sh .html .yaml .json ...
```

**文件名（示例）**：

```text
Makefile, CMakeLists.txt, package.json, pom.xml, requirements.txt ...
```

### 🖥️ 环境依赖

- Python 3.6+
- PyQt5
- rarfile
- py7zr

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

### 📸 示例截图

发现源码（支持下拉显示100条数据，完整数据点击“打开解压目录”）：

![image](https://github.com/user-attachments/assets/d0459446-f608-4103-9e0c-5640e0afec7f)

---

## 🧩{#english}

### 🔍 Source Code Archive Auditor

A graphical utility built with Python and PyQt5 that automatically scans `.zip`, `.rar`, `.7z`, and `.tar(.gz/.bz2)` archives to detect whether they contain source code files. Ideal for code audits and archive validation.

### ✅ Features

- Supported formats: `.zip`, `.rar`, `.7z`, `.tar(.gz/.bz2)`
- Auto-detects source code and config files
- Simple and intuitive GUI
- Supports Chinese paths and filenames
- One-click to open extracted folder
- Displays up to 100 suspicious files

### 📦 Packaging with PyInstaller

You can package it into a standalone `.exe` using `PyInstaller`:

```bash
pyinstaller audit_gui.py ^
  --noconfirm ^
  --onefile ^
  --windowed ^
  --icon=rocket.ico ^
  --add-binary "unrar.exe;." ^
  --add-binary "7z.exe;." ^
  --add-binary "7z.dll;."
```

#### Example Project Structure

```
your_project/
├── audit_gui.py
├── rocket.ico
├── unrar.exe
├── 7z.exe
├── 7z.dll
└── ...
```

### 📁 Detection Rules

**Detected extensions (examples):**

```text
.py .c .cpp .h .java .js .ts .go .rs .sh .html .yaml .json ...
```

**Detected filenames (examples):**

```text
Makefile, CMakeLists.txt, package.json, pom.xml, requirements.txt ...
```

### 🖥️ Requirements

- Python 3.6+
- PyQt5
- rarfile
- py7zr

Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
pyqt5
rarfile
py7zr
```

### 📸 Screenshot

Detected source files (max 100 shown; full list available via "Open Extracted Directory"):

![image](https://github.com/user-attachments/assets/d0459446-f608-4103-9e0c-5640e0afec7f)
