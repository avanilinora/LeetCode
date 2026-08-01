class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open=0
        close=0
        
        res=[]

        def par(s,open,close):
            if open==n and close==n:
                res.append(s)
                return
            if open<n:
                
                par(s+'(',open+1,close)

            if close<open:
                
                par(s+')',open,close+1)

        par('',open,close)

        return res

