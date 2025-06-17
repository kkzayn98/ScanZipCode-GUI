import sys
import os
import zipfile
import rarfile
import py7zr
import tarfile
import tempfile
import shutil
import subprocess

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QMessageBox, QScrollArea, QHBoxLayout
)
from PyQt5.QtCore import Qt

# 指定unrar路径（适用于PyInstaller打包的exe）
rarfile.UNRAR_TOOL = os.path.join(os.path.dirname(sys.executable), r"C:\Users\pcuser10\UnRAR.exe")
py7zr.helpers._7Z_BIN = os.path.join(os.path.dirname(sys.executable), r"C:\7-Zip\7z.exe")

SOURCE_EXTS = {
    ".c", ".cpp", ".h", ".hpp", ".py", ".java", ".js", ".ts", ".go", ".cs", ".rs", ".php", ".swift",
    ".html", ".css", ".scss", ".vue", ".jsx", ".tsx",
    ".sh", ".bash", ".bat", ".cmd", ".ps1",
    ".conf", ".ini", ".yaml", ".yml", ".json", ".xml", ".toml", ".cfg", ".properties",
    ".tpl", ".jinja", ".erb", ".ejs"
}

SOURCE_FILENAMES = {
    "Makefile", "CMakeLists.txt", "Dockerfile", "Vagrantfile",
    "build.gradle", "pom.xml", "package.json", "tsconfig.json",
    "requirements.txt", "setup.py", "setup.cfg", "pyproject.toml",
    "Gemfile", "Procfile"
}

class ArchiveAuditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("压缩包源码审核工具")
        self.setFixedSize(600, 400)

        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        icon_path = os.path.join(base_path, "rocket.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.label = QLabel("请选择一个压缩文件 (*.zip *.rar *.7z *.tar *.tar.gz *.tgz *.tar.bz2 *.tbz)：", self)
        self.button = QPushButton("选择文件", self)
        self.button.clicked.connect(self.select_file)

        self.open_dir_button = QPushButton("打开解压目录", self)
        self.open_dir_button.clicked.connect(self.open_extract_dir)
        self.open_dir_button.setEnabled(False)

        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)
        self.result_area.setLineWrapMode(QTextEdit.NoWrap)
        self.result_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button)
        button_layout.addWidget(self.open_dir_button)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addLayout(button_layout)
        self.layout.addWidget(self.result_area)
        self.setLayout(self.layout)

        self.last_extract_dir = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择压缩文件", "", "压缩文件 (*.zip *.rar *.7z *.tar *.tar.gz *.tgz *.tar.bz2 *.tbz)"
        )
        if file_path:
            self.result_area.clear()
            self.result_area.append(f"正在分析: {file_path}")
            result, temp_dir = self.audit_archive(file_path)
            self.result_area.setPlainText(result)
            QMessageBox.information(self, "分析结果", result.splitlines()[0])
            if temp_dir:
                self.last_extract_dir = temp_dir
                self.open_dir_button.setEnabled(True)

    def open_extract_dir(self):
        if self.last_extract_dir and os.path.exists(self.last_extract_dir):
            subprocess.Popen(f'explorer "{self.last_extract_dir}"', shell=True)

    def extract_archive(self, file_path, extract_to):
        file_path_lower = file_path.lower()
        try:
            if file_path_lower.endswith(".zip"):
                with zipfile.ZipFile(file_path, 'r') as zf:
                    for info in zf.infolist():
                        try:
                            info.filename = info.filename.encode('cp437').decode('gbk')
                        except:
                            pass
                        zf.extract(info, extract_to)
            elif file_path_lower.endswith(".rar"):
                with rarfile.RarFile(file_path) as rf:
                    rf.extractall(extract_to)
            elif file_path_lower.endswith(".7z"):
                with py7zr.SevenZipFile(file_path, mode='r') as szf:
                    szf.extractall(path=extract_to)
            elif file_path_lower.endswith((".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz")):
                with tarfile.open(file_path, 'r:*') as tf:
                    tf.extractall(path=extract_to)
            else:
                return False, "不支持的文件类型"
            return True, ""
        except Exception as e:
            return False, f" {e}"

    def contains_source_code(self, path):
        found_files = []
        for root, _, files in os.walk(path):
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in SOURCE_EXTS or f in SOURCE_FILENAMES:
                    found_files.append(os.path.join(root, f))
        return found_files

    def audit_archive(self, file_path):
        temp_dir = tempfile.mkdtemp()
        try:
            success, err = self.extract_archive(file_path, temp_dir)
            if not success:
                shutil.rmtree(temp_dir)
                return f"❌ 解压失败: {err}", None

            source_files = self.contains_source_code(temp_dir)
            if source_files:
                max_display = 100
                display_files = source_files[:max_display]
                file_list = "\n".join(f"- {f}" for f in display_files)
                more_msg = "\n...（仅显示前 100 项）" if len(source_files) > max_display else ""
                return f"⚠️ 发现源代码文件，共 {len(source_files)} 个：\n{file_list}{more_msg}", temp_dir
            else:
                return "✅ 未发现源代码文件。", temp_dir
        except Exception as e:
            shutil.rmtree(temp_dir)
            return f"❌ 出错: {e}", None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArchiveAuditor()
    window.show()
    sys.exit(app.exec_())
