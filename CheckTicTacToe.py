# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

win_1 = "1 is the winner!"
win_2 = "2 is the winner!"

matrix = [
    [0, 0, 1],
    [2, 1, 2],
    [1, 2, 1]
]

for i, mat in enumerate(matrix):
    if len(set(mat)) == 1:
        if mat[0] == 1:
            print(win_1)
            break
        elif mat[0] == 1:
            print(win_2)
            break
    vr_mat = [mat[i] for mat in matrix]
    if len(set(vr_mat)) == 1:
        if vr_mat[i] == 1:
            print(win_1)
            break
        elif vr_mat[i] == 2:
            print(win_2)
            break

cross_ax_1 = set([mat[ind] for ind, mat in enumerate(matrix)])
cross_ax_2 = set([mat[2-ind] for ind, mat in enumerate(matrix)])
for cross_ax in (cross_ax_1, cross_ax_2):
    if len(cross_ax) == 1 and cross_ax.pop() == 1:
        print(win_1)
        break
    elif len(cross_ax) == 1 and cross_ax.pop() == 2:
        print(win_2)
        break
