from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('한양해서', 'UNI_HSR.TTF'))

def create_pdf(text, image_path):
    c = canvas.Canvas("output.pdf", pagesize=A4)

    c.setFont('한양해서', 12)
    c.drawString(1 * mm, 10 * mm, text)

    # c.drawImage(image_path, 1 * mm, 7.5 * mm, width=6*mm, height=3*mm)

    c.line(1 * mm, 7 * mm, 7 * mm, 7 * mm)

    c.save()

text = input("출력할 텍스트를 입력하세요: ")
image_path = input("출력할 이미지 경로를 입력하세요: ")

create_pdf(text, image_path)

print("PDF 파일이 생성되었습니다.")



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog
# from PyQt5.QtGui import QPixmap
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont

# pdfmetrics.registerFont(TTFont('한양해서', 'UNI_HSR.TTF'))

# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.textbox = QLineEdit(self)
#         self.textbox.move(20, 20)
#         self.textbox.resize(280, 30)

#         self.button1 = QPushButton('이미지 선택', self)
#         self.button1.move(20, 60)
#         self.button1.clicked.connect(self.showDialog)

#         self.label = QLabel(self)
#         self.label.move(20, 100)
#         self.label.resize(280, 200)

#         self.button2 = QPushButton('PDF 생성', self)
#         self.button2.move(20, 320)
#         self.button2.clicked.connect(self.create_pdf)

#         self.setWindowTitle('PDF 생성기')
#         self.setGeometry(300, 300, 320, 360)
#         self.show()

#     def showDialog(self):
#         fname = QFileDialog.getOpenFileName(self, 'Open file', './')
#         pixmap = QPixmap(fname[0])
#         pixmap = pixmap.scaledToWidth(280)
#         self.label.setPixmap(pixmap)

#     def create_pdf(self):
#         text = self.textbox.text()
#         image_path = QFileDialog.getOpenFileName(self, 'Open file', './')[0]

#         c = canvas.Canvas("output.pdf", pagesize=A4)

#         c.setFont('한양해서', 12)
#         c.drawString(1 * mm, 10 * mm, text)

#         c.drawImage(image_path, 1 * mm, 7.5 * mm, width=6*mm, height=3*mm)

#         c.line(1 * mm, 7 * mm, 7 * mm, 7 * mm)

#         c.save()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())