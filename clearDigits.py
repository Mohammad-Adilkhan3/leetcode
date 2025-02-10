class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for i in s:
            if i.isdigit():
                if st:
                    st.pop()
            else:
                st.append(i)
        return "".join(st)
        
