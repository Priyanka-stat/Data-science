num =int(input("enter the number:"))

if num>1:
    for i in range(2,num):
        if num % i==0:
            print('number is not prime')
            break
    else:
        print("The number is Prime")
else:
    print("The number is not Prime")       
         
