#Sample Input
#3
#sam 99912222
#tom 11122222
#harry 12299933
#sam
#edward
#harry
#Sample Output

sam=99912222
Not found
harry=12299933
n = int(input())
phnbook = {}

for i in range(n):
    a,num = input().split()
    phnbook[a] = num
    
for j in range(n):
    try:
        
        nam = str(input())
    
        if nam in phnbook:
            print (str(nam) + "=" + str(phnbook[nam]))
        
        else:
            print("Not found")    
    except:
        break
                
