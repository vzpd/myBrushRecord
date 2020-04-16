# Bit Manipulation,DFS,python solution
from exercise.myUtils import count_time


class Solution(object):
    @count_time
    def solveSudoku(self, board):
        pos, H, V, G = [], [0] * 9, [0] * 9, [0] * 9  # Empty cells'position,horizontal,vertical,grid
        # print('pos:', pos)
        # print('H:', H)
        # print('V:', V)
        # print('G', G)
        ctoV = {str(i): 1 << (i - 1) for i in range(1, 10)}  # eg:'4'=>1000
        # print('ctoV:', ctoV)
        self.vtoC = {1 << (i - 1): str(i) for i in range(1, 10)}  # eg:100=>'3'
        # print('vtoC:', self.vtoC)
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    v = ctoV[c]
                    H[i], V[j], G[i // 3 * 3 + j // 3] = H[i] | v, V[j] | v, G[i // 3 * 3 + j // 3] | v
                else:
                    pos += (i, j),
        # dict {(i,j):[possible vals(bit-identify),count]}
        posDict = {(i, j): [x, self.countOnes(x)] for i, j in pos \
                   for x in [0x1ff & ~(H[i] | V[j] | G[i // 3 * 3 + j // 3])]}
        self.slove(board, posDict)

    def countOnes(self, n):
        count = 0
        while n:
            count, n = count + 1, n & ~(n & (~n + 1))
        return count

    def slove(self, board, posDict):
        if len(posDict) == 0:
            return True
        p = min(posDict.keys(), key=lambda x: posDict[x][1])  #
        candidate = posDict[p][0]
        while candidate:
            v = candidate & (~candidate + 1)  # get last '1'
            candidate &= ~v
            tmp = self.updata(board, posDict, p, v)  # updata board and posDict
            if self.slove(board, posDict):  # slove next position
                return True
            self.recovery(board, posDict, p, v, tmp)  # backtrack-->recovery
        return False

    def updata(self, board, posDict, p, v):
        i, j = p[0], p[1]
        board[i][j] = self.vtoC[v]
        tmp = [posDict[p]]
        del posDict[p]
        for key in posDict.keys():
            if i == key[0] or j == key[1] or (i // 3, j // 3) == (key[0] // 3, key[1] // 3):  # relevant points
                if posDict[key][0] & v:  # need modify
                    posDict[key][0] &= ~v
                    posDict[key][1] -= 1
                    tmp += key,  # Record these points.
        return tmp

    def recovery(self, board, posDict, p, v, tmp):
        board[p[0]][p[1]] = '.'
        posDict[p] = tmp[0]
        for key in tmp[1:]:
            posDict[key][0] |= v
            posDict[key][1] += 1


@count_time
def countSolution():
    s = Solution()
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    # print('///////////////////////////////////////////////////////////////////')
    s.solveSudoku(board)
    # printBoard(board)
    board = [['.', '.', '9', '7', '4', '8', '.', '.', '.'],
             ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '2', '.', '1', '.', '9', '.', '.', '.'],
             ['.', '.', '7', '.', '.', '.', '2', '4', '.'],
             ['.', '6', '4', '.', '1', '.', '5', '9', '.'],
             ['.', '9', '8', '.', '.', '.', '3', '.', '.'],
             ['.', '.', '.', '8', '.', '3', '.', '2', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '6'],
             ['.', '.', '.', '2', '7', '5', '9', '.', '.']]
    # print('///////////////////////////////////////////////////////////////////')
    s.solveSudoku(board)
    # printBoard(board)
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."],
             [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."],
             [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    # print('///////////////////////////////////////////////////////////////////')
    s.solveSudoku(board)
    # printBoard(board)
    board = [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
             ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
             [".", ".", "1", ".", ".", "3", "9", "8", "."],
             [".", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "3", "8", ".", ".", "."],
             [".", "3", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", "6", "3", ".", ".", "5", ".", "."],
             ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
             ["4", "7", ".", ".", ".", "1", ".", ".", "."]]
    # print('///////////////////////////////////////////////////////////////////')
    s.solveSudoku(board)
    # printBoard(board)


countSolution()
