def reverseVowels(self, s: str) -> str:
        stk=[]#Create a stack
        for i in s:
            if i.lower() in "aeiou":
                stk.append(i)
        rev=""
        for i in s:
            if i.lower() in "aeiou":
                rev+=stk.pop(-1)
            else:
                rev+=i
        
        return rev
