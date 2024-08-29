n = int(input())
a = list(map(int, input().split()))

index_ratings = [(a[i], i) for i in range(n)]
index_ratings.sort(reverse = True, key = lambda x: x[0])

j = 1
positions = [0] * n

for i in range(n):
    if i > 0 and index_ratings[i][0] == index_ratings[i - 1][0]:
        positions[index_ratings[i][1]] = j 
    else:
        positions[index_ratings[i][1]] = i + 1
        j = i + 1

print(" ".join(map(str, positions)))


