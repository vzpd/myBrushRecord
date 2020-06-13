from functools import lru_cache
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def solveSudoku(self, board: List[List[str]]) -> bool:

        @lru_cache()
        def getRelateIndex(i, j):
            partH = [(i, k) for k in range(9)]
            partV = [(k, j) for k in range(9)]
            indexH, indexV = i % 3, j % 3
            indexNearHs = sorted([k for k in range(i - indexH, i - indexH + 3)] * 3)
            indexNearVs = [k for k in range(j - indexV, j - indexV + 3)] * 3
            partN = zip(indexNearHs, indexNearVs)
            partNear = [(m, n) for m, n in partN]
            return set(partH + partV + partNear)

        def reduceLeftDict(dict, i, j, sefValFlag: bool):
            if len(dict.get((i, j))) == 1:
                if sefValFlag:
                    board[i][j] = dict.get((i, j))[0]
                val = dict.get((i, j))[0]
                for m, n in getRelateIndex(i, j):
                    if m != i or n != j:
                        res = dict.get((m, n))
                        if res and val in res:
                            dict.get((m, n)).remove(val)
                            reduceLeftDict(dict, m, n, sefValFlag)

        def copyDict(mainDict):
            tempDict = {}
            for key in mainDict.keys():
                vals = mainDict.get(key)
                if len(vals) > 0:
                    tempDict[key] = mainDict.get(key)[:]
            return tempDict

        def gussIndex(gussDict, count):
            lenList = [len(gussDict.get(x)) for x in gussDict.keys()]
            if 0 in lenList:
                return False
            elif max(lenList) > 1:
                tempDict = copyDict(gussDict)
                for key in gussDict.keys():
                    if 1 < len(gussDict.get(key)) < 3:
                        for val in gussDict.get(key):
                            tempDict[key] = [val]
                            # print('    ' * count, 'try set ', key, '->', val)
                            reduceLeftDict(tempDict, key[0], key[1], False)
                            if gussIndex(tempDict, count + 1):
                                # print('    ' * count, 'try set ', key, '->', val, ' success')
                                return True
                            else:
                                # print('    ' * count, 'try set ', key, '->', val, ' fail')
                                tempDict = copyDict(gussDict)
                        return False
            else:
                for key in gussDict.keys():
                    board[key[0]][key[1]] = gussDict.get(key)[0]
                return True

        leftDict = {}

        all = [str(x) for x in range(1, 10)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':

                    rIndex = getRelateIndex(i, j)
                    leftDict[(i, j)] = [z for z in all if z not in [board[x][y] for x, y in rIndex]]

                    if len(leftDict[i, j]) == 1:
                        board[i][j] = leftDict[i, j][0]
                        reduceLeftDict(leftDict, i, j, True)

        gussDict = copyDict(leftDict)

        gussIndex(gussDict, 0)

        for i, j in zip([x for x in range(9)] * 9, sorted([x for x in range(9)] * 9)):
            val = board[i][j]
            if val == '.':
                print('FAIL!!!')
            for m, n in getRelateIndex(i, j):
                if i != m and j != n and board[m][n] == val:
                    print('FAIL!!!')


def printBoard(board):
    for i in range(len(board)):
        print(board[i])


@timer
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


print('///////////////////////////////////////////////////////////////////')
countSolution()
