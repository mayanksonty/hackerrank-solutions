
if __name__ == '__main__':
    N = int(input())

    lis = []

    for i in range(N):
        user_input = input().split(" ")
        if 'append' in user_input:
            lis.append(int(user_input[1]))
        
        elif 'remove' in user_input:
            lis.remove(int(user_input[1]))

        elif 'pop' in user_input:
            lis.pop()
        
        elif 'insert' in user_input:
            lis.insert(int(user_input[1]),int(user_input[2]))
        
        elif 'sort' in user_input:
            lis.sort()
        
        elif 'reverse' in user_input:
            lis.reverse()
        
        elif 'print' in user_input:
            print(lis)
    


        



