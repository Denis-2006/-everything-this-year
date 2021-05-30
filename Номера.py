a = input()
flag = False
ABC = ["A", "B", "C", "E"]
nom = ['1', '0', '2', '3', '4', '5', '6', '7', '8', '9']
if len(a) == 6:
    for i in range (6):
        if 0 < i < 4:
            if a[i] not in nom:
                flag = True
                break
        else:
            if a[i] not in ABC:
                flag = True
                break
else:
    flag = True
if flag == False:
    print('Yes')
else:
    print('No')
                
                
            
            
