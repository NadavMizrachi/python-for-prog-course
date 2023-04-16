max_int = 11
f = open('mult_board.txt', 'w+')
nums = [
    f.write(str(j * i) + "\n") if j == max_int - 1
    else f.write(str(j * i) + "\t")
    for i in range(1, max_int) for j in range(1, max_int)
]


