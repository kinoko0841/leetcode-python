class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        def dfs(x, y, word):
            if len(word)==0: return True
            #up
            if x>0 and board[x-1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x-1,y,word[1:]):
                    board[x][y]=tmp
                    return True
                board[x][y]=tmp
            #down
            if x<len(board)-1 and board[x+1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x+1,y,word[1:]):
                    board[x][y]=tmp
                    return True
                board[x][y]=tmp
            #left
            if y>0 and board[x][y-1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y-1,word[1:]):
                    board[x][y]=tmp
                    return True
                board[x][y]=tmp
            #right
            if y<len(board[0])-1 and board[x][y+1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y+1,word[1:]):
                    board[x][y]=tmp
                    return True
                board[x][y]=tmp
            return False
                
        res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                for k in range(len(words)):
                    if board[i][j]==words[k][0]:
                        if(dfs(i,j,words[k][1:])) and words[k] not in res:
                            res.append(words[k])
        return res

a=[['a','b'],['c','d']]
b=["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
sol=Solution()
print sol.findWords(a,b)