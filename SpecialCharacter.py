special_Character = ['<', '>', '+', '-', '/', '%', '=', '*','!']
special_semiclone = ';'
special_Character2 = [':', ',']
special_Character3 = ['[', ']', '(', ')', '{', '}']

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