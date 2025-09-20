class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        res=0
        for i in s:
            if i =="(":
                st.append(i)
            elif i == ')':
                res=max(res,len(st))
                st.pop()
        return res