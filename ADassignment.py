##Adventure Design Assignment
##Software Project2

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class SWP(QWidget):

    def __init__ (self):
        super().__init__()

        self.Userinput = QTextEdit()
        self.Userinput.setFixedSize(500,700)

        self.result = QTextEdit()
        self.result.setFixedSize(500,700)

        self.button = QToolButton()
        self.button.setText("CLICK")
        self.label = QLabel()
        self.label.setText("코딩 규칙 출처 - \t 국민대 소프트웨어 프로젝트 2")

        mainlayout = QGridLayout()
        mainlayout.addWidget(self.Userinput,0,0)
        #mainlayout.addWidget(self.result,0,3)
        mainlayout.addWidget(self.button,0,1)
        mainlayout.addWidget(self.label,1,1)
        self.setLayout(mainlayout)

        subLayout = QGridLayout()
        subLayout.addWidget(self.result)
        self.pushButton = QPushButton("File Open")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()
        mainlayout.addWidget(self.pushButton,1,0)
        #mainlayout.addWidget(self.label,0,0)

    def pushButtonClicked(self):
        faddress = QFileDialog.getOpenFileName(self)
        fname = faddress[0].split('/')[-1]
        f = open(fname, 'r')
        data = f.readline()
        idx = data.find(";")
        f.close()

        fw = open(fname, 'w')
        fw.write(data[:idx])
        fw.close()

        fh = open(fname, 'r')
        input_str = fh.readline()
        self.Userinput.setText(input_str)
        self.label.setText(faddress[0])


    def writedb(self):

        fh = open(fname, 'w')
        for line in fh.readline():
            fh.write(line)
            #for i in range(len(line)):
             #   if line.find(';'):
              #      line = line[:len(line)]
               #     print(line[i])
            #self.Userinput.setText(line)


#        for line in f.readline():


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    game = SWP()
    game.show()
    sys.exit(app.exec_())