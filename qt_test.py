import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 创建一个标签
        self.label = QLabel('Hello, PyQt5!', self)
        
        # 创建一个按钮
        self.btn = QPushButton('Click me', self)
        self.btn.clicked.connect(self.changeText)
        
        # 创建一个垂直布局，并将标签和按钮添加到布局中
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn)
        
        # 设置窗口的主布局
        self.setLayout(vbox)
        
        # 设置窗口属性
        self.setWindowTitle('PyQt5 Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    
    def changeText(self):
        self.label.setText('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
