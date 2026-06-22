import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class HotspotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("تكة Hotspot - برنامج سطح المكتب")
        self.resize(1200, 800)

        # إنشاء عرض الويب
        self.browser = QWebEngineView()
        
        # تحميل ملف HTML
        html_path = os.path.abspath("index.html")
        self.browser.load(QUrl.fromLocalFile(html_path))

        # إعداد الواجهة
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HotspotApp()
    window.show()
    sys.exit(app.exec())
