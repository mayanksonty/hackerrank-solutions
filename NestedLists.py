if __name__ == '__main__':
  
    dic = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li = list()
        
        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]
        
    for key in dic:
        li.append(key)
    

    a = min(li)
    li.remove(a)

    b = min(li)

    value = dic[b]
    value.sort()

    for item in value:
        print(item)


            

   
    