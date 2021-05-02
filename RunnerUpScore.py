# Hacker Rank RunnerUp Score Problem



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    for i in range(n,-1,-1):
        if arr[i-1] == arr[i-2]:
            arr.pop()
        else:
            print(arr[i-2])
            break
