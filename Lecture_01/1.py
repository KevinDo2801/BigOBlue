n = int(input())
a = list(map(int, input().split()))

if n == 1:
    if a[0] == 1:
        print("YES")
    else:
        print("NO")
else:
    count = 0
    for bu in a:
        if bu == 0:
            count += 1
    if count == 1:
      print("YES")
    else:
    	print("NO")  
    
