__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You are given a placement of queens on a nxn board in which there is exactly one queen in each row and column.

Input representation (board) is a list of queen column positions (ie) if board[i] = j. It means queen in
ith column is placed in jth row. For nxn chessboard, you have rows 0..n-1 and cols 0..n-1.

Given a board, we define equivalent boards as placements obtained by:

1. Rotating the original by 90, 180 or 270 degrees clockwise.
2. Taking a mirror reflection of each of those rotations (including the original) assuming mirror
   is to the right

So you can get 8 equivalent boards (including original). Some of these can be duplicates as shown below.

E.x. if board = [0, 1, 2] it is equivalent to following chessboard - left bottom is (0, 0):

_ _ Q    |
_ Q _    |
Q _ _    |

90 degree clockwise rotation of above board is

Q _ _
_ Q _
_ _ Q

Right Mirror reflection is:

Q _ _
_ Q _
_ _ Q

In the above case mirror reflection is same as 90 degree rotation, but that is not always the case.

Your job is to get unique equivalents for a given board position (filter out duplicates).

Additional notes:
1. Assume inputs are of valid type and content (ie) positions are valid too (one queen in every column and row).
2. Return a list of unique equivalent boards without repetitions. You could end up anywhere from 1 to 8 boards.
3. Hint: 180 deg rotation is 2 90 degree rotations, 270 is 3 90 deg rotations.
'''
def rotate_90(board):
    row = len(board)
    col = row
    matrix = []
    for i in range(row):
        mat = []
        for j in range(col-1,-1,-1):
            mat.append(board[i][j])
        matrix.append(mat)
    return matrix

def board_gen(board):
    board.reverse()
    li = []
    for i in range(len(board)):
        li.append((board[i],i))
    col = len(board)
    row = col
    matrix = []
    for i in range(row):
         mat = []
         for j in range(col):
            if (i,j) in li:
                mat.append('Q')
            else:
                mat.append('_')
         matrix.append(mat)
    return matrix

def equi(matrix):
    new_mat = rotate_90(matrix)
    mat = []
    for i in range(len(new_mat)):
        for j in range(len(new_mat[i])):
            if new_mat[i][j] == 'Q':
                mat.append([len(new_mat) - 1 - i, len(new_mat) - 1 - j])
    print(mat)
    return mat
def right_ref(matrix):
    right_reflect = []
    for i in matrix:
        right_reflect.append(i[::-1])
    return right_reflect

def get_equivalents(board):
    matrix = board_gen(board)
    righ_r = equi(right_ref(matrix))
    a = equi(matrix)
    li=[]
    li.append(a)
    li.append(righ_r)
    count = 0
    while count<3:
        a = equi(rotate_90(matrix))
        li.append(a)
        righ_r = right_ref(a)
        li.append(righ_r)
        matrix = a[::-1]
        count+=1

#write your own tests
def test_equivalents():
    assert [[0,1], [1,0]] == get_equivalents([0,1])
    print(get_equivalents([0,1,2]))


