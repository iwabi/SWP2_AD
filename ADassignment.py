##Adventure Design Assignment
##Software Project2

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class SWP(QWidget):

    def __init__ (self):
        super().__init__()
        self.initUI()


    def initUI(self):

        # 1 line UI
        self.fileLineEdit = QTextEdit()
        self.fileLineEdit.setReadOnly(True)
        self.fileLineEdit.setFixedSize(500, 700)
        self.resultLineEdit = QTextEdit()
        self.resultLineEdit.setReadOnly(True)
        self.resultLineEdit.setFixedSize(500, 700)
        hbox = QHBoxLayout()
        hbox.addWidget(self.fileLineEdit)
        hbox.addWidget(self.resultLineEdit)

        # 2 line UI
        self.openbutton = QPushButton("File Open")
        self.clickbutton = QPushButton("CLICK")
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.openbutton)
        hbox1.addWidget(self.clickbutton)

        # 3 line UI
        self.taglabel = QLabel("코드 규칙 출처 - \t  국민대 소프트웨어 프로젝트 2")
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.taglabel)

        # 세로 배치
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)


        # 이벤트 핸들러
        self.openbutton.clicked.connect(self.openbuttonClicked)
        self.clickbutton.clicked.connect(self.clickbuttonClicked)

    def openbuttonClicked(self):
        try:
            faddress = QFileDialog.getOpenFileName(self)
            self.fname = faddress[0].split('/')[-1]
            f = open(self.fname, 'r')
            data = f.read()
            self.fileLineEdit.setText(data)
            self.taglabel.setText(faddress[0])
        except:
            self.taglabel.setText("파일이 없습니다.")



    def clickbuttonClicked(self):
        special_Character = ['+', '-', '/', '%', '=', '!', '*', '-', '/', '%', '<', '>']

        #괄호, 대괄호 (brackets; [] ), 중괄호 (braces; {} ) 의 안쪽에 불필요한 공백을 두지 않는다. ex) [ ]
        special_Character2 = ['(', '{','[']
        string = []

        f = open(self.fname, 'r')

        for line in f:
            line = line[:line.find(';')] + '\n' #세미콜론 제거
            for i in range(len(line)): #line글자 수 만큼 반복해서 검사하고 고침
                for idx in range(len(line)):
                    enter = line.find('\n')
                    if line[idx] in special_Character and line[idx+1] in special_Character2: # a!=b
                        if line[idx-1] != " " and line[idx+2] != " ":
                            line = line[:idx] + " " + line[idx] + line[idx+1] + " " + line[idx+2:]
                        elif line[idx-1] != " ":
                            line = line[:idx] + " " + line[idx] + line[idx+1:]
                        elif line[idx+2] != " ":
                            line = line[:idx] + line[idx] + line[idx+1]+ " " + line[idx+2:]

                    #elif line[enter-1] == ';': #세미 콜론 제거
                     #   line = line[:-2] + '\n'

                    #elif line[idx] == ':':
                     #   if line[idx-1] == " " and line[idx+1] != " ":
                      #      line = line[:idx-1] + line[idx] + " " + line[idx+1:]
                       # elif line[idx-1] == " ":
                        #    line = line[:idx-1] + line[idx:]
                        #elif line[idx+1] != " ":
                         #   line = line[:idx] + line[idx] + " " + line[idx+1:]

                    elif line[idx] == ',':
                        if line[idx-1] == " ":
                            if line[idx+1] != " ": #a ,b
                                line = line[:idx - 1] + line[idx] + " " + line[idx + 1:]
                            else: #a , b
                                line = line[:idx - 1] + line[idx] + line[idx + 1:]
                        elif line[idx+1] != " ": #a,b
                            line = line[:idx] + line[idx] + " " + line[idx+1:]

                    elif line[idx] in special_Character2:
                        if line[idx + 1] == " ":
                            line = line[:idx] + line[idx] + line[idx+2:]
                            break # 안멈추면 인덱스 에러

            string.append(line)

        f.close()
        self.writefile(string)
        self.showfile()

    #파일 읽기
    def writefile(self, string):
        f = open(self.fname, 'w')
        for i in string:
            f.write(i)
        f.close()
    #파일 resultlineEdit에 보이기
    def showfile(self):
        f = open(self.fname, 'r')
        output = f.read()
        self.resultLineEdit.setText(output)
        f.close()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    game = SWP()
    game.show()
    sys.exit(app.exec_())