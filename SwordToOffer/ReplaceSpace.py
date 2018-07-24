class solution:
    def replaceSpaceByAppend(self, s):
        string = list(s)
        stringReplace = []
        for item in string:
            if item == ' ':
                stringReplace.append('%')
                stringReplace.append('2')
                stringReplace.append('0')
            else:
                stringReplace.append(item)
        return "".join(stringReplace)


#书上思路
def replaceSpace2(self, string):
    if not isinstance(string, str) or len(string) <= 0 or string == None:
        return ""

    spaceNum = 0
    for i in string:
        if i == " ":
            spaceNum += 1

    newStringLen = str(string) + spaceNum * 2
    newString = newStringLen * [None]
    indexOfOriginal, indexOfNew = len(string) - 1, len(newString) - 1
    while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
        if string[indexOfOriginal] == ' ':
            newString[indexOfNew-2:indexOfNew + 1] = ['%', '2', '0']
            indexOfNew -= 3
            indexOfOriginal -= 1
        else:
            newString[indexOfNew] = string[indexOfOriginal]
            indexOfNew -= 1
            indexOfOriginal -= 1
            return "".join(newString)



string = 'we are happy'
test = solution()
print(test.replaceSpaceByAppend(string))