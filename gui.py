import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QSizePolicy, QMessageBox, QComboBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from detect import detect  # Assuming detect and opt are defined in detect.py
import argparse
import os

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Image Detection GUI'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        
        # Layouts
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # Buttons
        self.open_button = QPushButton('Open Image')
        self.open_button.clicked.connect(self.open_image)
        self.layout.addWidget(self.open_button)

        # Buttons
        self.detect_button = QPushButton('Detect Image')
        self.detect_button.clicked.connect(self.detect_image)
        self.layout.addWidget(self.detect_button)

        # Algorithm selection
        self.algorithm_combo = QComboBox(self)
        self.algorithm_combo.addItem("Algorithm 1")
        self.algorithm_combo.addItem("Algorithm 2")
        self.algorithm_combo.addItem("Algorithm 3")
        self.layout.addWidget(self.algorithm_combo)
        
        # Image display
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)
        
        # Status display
        self.status_label1 = QLabel(self)
        self.layout.addWidget(self.status_label1)
        self.status_label2 = QLabel(self)
        self.layout.addWidget(self.status_label2)
        self.status_label3 = QLabel(self)
        self.layout.addWidget(self.status_label3)
    
        
        # Set size policy
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        # Result display
        self.result_label = QLabel(self)
        self.layout.addWidget(self.result_label)
        
        self.setGeometry(100, 100, 800, 600)
        self.show()
    
    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)", options=options)
        if self.file_name:
            self.display_image(self.file_name)
    
    def detect_image(self):
        if self.file_name:
            self.run_detection(self.file_name)
        else:
            QMessageBox.warning(self, 'Warning', 'Please open an image first.')
    
    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(False)
        
    def run_detection(self, file_path):
        # Update opt.source to the selected image file path
        opt.source = file_path
        
        # Run detection
        result_image_dir = detect(opt)
        # Display the result
        print("result_image_dir", result_image_dir)
        # Display all the results in the result_image_dir
        
        if os.path.exists(result_image_dir):
            image_files = os.listdir(result_image_dir)

            for image_file in image_files:
                result_image_path = os.path.join(result_image_dir, image_file)
                result_pixmap = QPixmap(result_image_path)
                self.image_label.setPixmap(result_pixmap)
                self.image_label.setScaledContents(False)
                self.result_label.setText('Detection successful. Result image saved at: ' + result_image_path)
                self.status_label1.setText('status_label1')
                self.status_label2.setText('status_label2')
                self.status_label3.setText('status_label3')
        else:
            self.result_label.setText('Detection failed, no result image found.')
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='weights/v5lite-s.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='sample', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.45, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    opt = parser.parse_args()
    print(opt)
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
