x = [[12, 7, 3, 1],
     [4, 5, 6, 2],
     [7, 8, 9, 3]]

y = [[5, 8, 1, 5],
     [6, 7, 3, 0],
     [4, 5, 9, 7]]

# result = [[0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0]]
#
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j]+y[i][j]
#
# for r in result:
#     print(r)

result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
print(result)