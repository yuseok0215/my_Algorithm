# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().rstrip())))

# row_sum = 0
# for i in range(n):
#     row_num = ''
#     for j in range(m):
#         row_num += str(graph[i][j])
#     row_sum += int(row_num)

# col_sum = 0
# for i in range(m):
#     col_num = ''
#     for j in range(n):
#         col_num += str(graph[j][i])
#     col_sum += int(col_num)

# print(max(col_sum, row_sum))    

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

def bf():
  result = 0
  for i in range(1 << N * M):
      total = 0
      for row in range(N):
          srow = 0
          for col in range(M):
              idx = row * M + col
              if i & (1 << idx) != 0: srow = srow * 10 + arr[row][col]
              else:
                  total += srow
                  srow = 0
          total += srow

      for col in range(M):
          scol = 0
          for row in range(N):
              idx = row * M + col
              if i & (1 << idx) == 0: scol = scol * 10 + arr[row][col]
              else:
                  total += scol
                  scol = 0
          total += scol
      result = max(result, total)
  return result

print(bf())