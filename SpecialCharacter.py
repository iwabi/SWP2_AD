special_Character = ['<', '>', '+', '-', '/', '%', '=', '*','!']
special_semiclone = ';'
special_Character2 = [':', ',']
special_Character3 = ['[', ']', '(', ')', '{', '}']
special_Character4 = ['import']

def special(line):
    string = ""

    for i in line:
        if i not in special_Character:
            string += i
        else:
            string += '@'

    for i in line:
        if i in special_Character:
            while line.find(i) != -1:
                index = line.find(i)
                string = string[:index].rstrip() + " " + i + " " + string[index+1:].lstrip()
                line = line[:index].rstrip() + " " + '@' + " " + line[index + 1:].lstrip()

    for i in special_Character:
        index2 = string.find(i)
        if string[index2+2] in special_Character:
            string = string[:index2+1] + string[index2+2:]
    return string

def semiclone(line):
    for i in line:
        if i == special_semiclone and line[-2] == special_semiclone:
            line = line[:-2] + '\n'
    return line

def special2(line):
    string = ""
    for i in line:
        if i not in special_Character2:
            string += i
        else:
            string += '@'

    for i in line:
        if i in special_Character2:
            while line.find(i) != -1:
                index = line.find(i)
                string = string[:index].rstrip() + i + " " + string[index + 1:].lstrip()
                line = line[:index].rstrip() + '@' + " " + line[index + 1:].lstrip()

    return string

def special3(line):
    string = ""
    for i in line:
        if i not in special_Character3:
            string += i
        else:
            string += '@'

    for i in line:
        if i in special_Character3:
            while line.find(i) != -1:
                index = line.find(i)
                string = string[:index].rstrip() + i + string[index+1:].lstrip()
                line = line[:index].rstrip() + '@' + line[index + 1:].lstrip()

    return special(special2(string))

def special4(line):
    tmp = line.split()
    tmpline = ""
    if tmp[0] in special_Character4: #import a, b
        for i in range(1, len(tmp)):
            if i == len(tmp) - 1:
                tmpline += tmp[0] + ' ' + tmp[i] + '\n' #마지막 검사면 ,가 없으므로 그냥[i]
            else:
                tmpline += tmp[0] + ' ' + tmp[i][:-1] + '\n' #[:-1]은 ',' 제거

    return tmpline