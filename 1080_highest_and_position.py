result = {}

for i in range(100):    # 100 ti input dile then output ashbe.    
    n = int(input())
    result[i] = n

h_result_key = max(result,key = result.get)
print(result[h_result_key])
print(h_result_key+1)