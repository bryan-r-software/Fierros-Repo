ans_num = int(input())
result = []

for i in range(ans_num):
    start, increment, cicles = map(int, input().split())
    mini_result = start
    
    for j in range(1,cicles):
        start += increment
        mini_result += start
        
    result.append(mini_result)

print(" ".join(map(str, result)))