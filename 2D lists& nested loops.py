number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

#nested for loop is whereby you have a for loop within another for loop

for row in number_grid:
    for column in row:
        print(column)