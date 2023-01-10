def get_factorial(arr, n):
    arr[0] = 1
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = i * arr[i - 1]

def get_answer(answer, factorial, k):
    
    N = len(answer)
    numbers = [j for j in range(1, N + 1)]
    for i in range(N):
        #print(numbers )
        answer[i] = numbers[k // factorial[N - 1 - i]]
        print(numbers, answer[i], k, factorial[N - 1 - i])
        numbers.remove(answer[i])
        k = k % factorial[N - 1 - i] 
        

def solution(n, k):
    factorial = [0] * (n + 1)
    answer = [0] * n
    get_factorial(factorial, n)
    get_answer(answer, factorial, k - 1)
    return answer
table = solution(4,12)
print(table)
# table2 = solution(4,7)
# print(table2)