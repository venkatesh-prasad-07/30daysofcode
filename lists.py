if __name__ == '__main__':
    N = int(input())


    list1 = []

    

    for i in range(0,N):
        inp = input().split()
        if inp[0] == "insert":
            list1.insert[int(inp[1]),int(inp[2])]
    
        elif inp[0] == "remove":
            list1.remove[int(inp[1])]
         
        elif inp[0] == "append":
            list1.append[int(inp[1])]
        
        elif inp[0] == "pop":
            list1.pop()
    
        elif inp[0] == "sort":
            list1.sort()
        
        elif inp[0] == "reverse":
            list1.reverse()
        
        elif inp[0] == "print":
            list1.print()
        
        else:
            print("Wrong spellings")    
        
        
        
