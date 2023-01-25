num=int(input("Enter Number:"))
step=0
while num > 0:
    if ( num % 2 ) == 0:
        step=step + 1
        num = num // 2
        print(num)
    elif num == 1 :
        break
        
    else:
        
        num = 3 * num + 1
        step=step + 1
        print(num)
        
print("Steps:",step)
