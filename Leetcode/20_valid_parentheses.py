class Solution:
    def isValid(self, str):
        map = {}
        OPEN = ['(', '{', '[']
        CLOSE = [')', '}', ']']
        for index, each in enumerate(OPEN):
            map[each] = CLOSE[index]

        stack = []
        isValid = True
        if str == "": return isValid

        for index, each in enumerate(str):
            if each in OPEN:
                stack.append(each)
            if each in CLOSE:
                if stack == []:
                    isValid = False
                if stack != [] and each != map.get(stack.pop()):
                    isValid = False

        if stack != []:
            isValid = False
        return isValid
