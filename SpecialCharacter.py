class specialcharacter(object):

    def __init__(self):
        self.special_Character = ['<', '>', '+', '-', '/', '%', '=', '*', '!']
        self.special_Character2 = [':', ',']
        self.special_Character3 = ['[', ']', '(', ')', '{', '}']
        self.special_Character4 = ['from', 'import']

    def semiclone(self, line):
        if line[-1] == ';' or line[-2] == ';':  # 세미콜론제거
            line = line[:-1]
        elif line[line.find(';')+1].isalpha():
            line = line[:line.find(';')] + '\n' + line[line.find(';') + 1:] + '\n'
        return line

    def special(self,line):
        string = ""
        for i in line:
            if i not in self.special_Character:
                string += i
            else:
                string += '@'

        for i in line:
            if i in self.special_Character:
                while line.find(i) != -1:
                    index = line.find(i)
                    string = string[:index].rstrip() + " " + i + " " + string[index+1:].lstrip()
                    line = line[:index].rstrip() + " " + '@' + " " + line[index + 1:].lstrip()

        for i in self.special_Character:
            index2 = string.find(i)
            if string[index2+2] in self.special_Character:
                string = string[:index2+1] + string[index2+2:]
        return string

    def special2(self,line):
        string = ""
        for i in line:
            if i not in self.special_Character2:
                string += i
            else:
                string += '@'

        for i in line:
            if i in self.special_Character2:
                while line.find(i) != -1:
                    index = line.find(i)
                    string = string[:index].rstrip() + i + " " + string[index + 1:].lstrip()
                    line = line[:index].rstrip() + '@' + " " + line[index + 1:].lstrip()

        return string

    def special3(self,line):
        string = ""
        for i in line:
            if i not in self.special_Character3:
                string += i
            else:
                string += '@'

        for i in line:
            if i in self.special_Character3:
                while line.find(i) != -1:
                    index = line.find(i)
                    string = string[:index].rstrip() + i + string[index+1:].lstrip()
                    line = line[:index].rstrip() + '@' + line[index + 1:].lstrip()

        return self.special(self.special2(string))

    def special4(self,line):
        line = self.special2(line)
        tmp = line.split()
        string = ""
        string1 = ""
        if tmp[0] == self.special_Character4[0]:
            index = tmp.index(self.special_Character4[1])
            for i in range(index + 1):
                string = string + tmp[i] + ' '
            for i in range(index + 1, len(tmp)):
                string1 += string + tmp[i] + '\n'
                string1 = string1.replace(',', '')

        elif tmp[0] == self.special_Character4[1]:
            index = tmp.index(self.special_Character4[1])
            for i in range(index + 1):
                string = string + tmp[i] + ' '
            for i in range(index + 1, len(tmp)):
                string1 += string + tmp[i] + '\n'
                string1 = string1.replace(',', '')

        return string1
