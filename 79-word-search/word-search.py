class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        w=len(word)
        def backtrack(i,j, index):
            if index==w:
                return True
            if i<0 or i>=m or j<0 or j>=n:
                return False

            if board[i][j]!=word[index]:
                return False
            #mark cell as visited
            done=board[i][j]
            board[i][j] = '#'
            #paths defined
            path=(backtrack(i+1,j,index+1) or backtrack(i-1,j,index+1) or backtrack(i,j+1,index+1) or backtrack(i,j-1,index+1))
            #restore original
            board[i][j]=done
            return path
        #find a path    
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
                
        #path not found
        return False