# 1) حدس کولاتز
number=int(input("please enter a number : "))
while number != 1 :
    if number %2 ==0:
        number = number//2
    else :
        number = number*3 +1
    print(number , end="  -  ")

print()


# 2) برنامه ای برای تشخیص کامل بودن عدد بنویسید با استفاده از while

num=int(input("please enter a number : "))
perfect=0
i=1
while i < num:
    if num%i== 0:
        perfect+=i
    i+=1
if perfect == num:
    print(f"{num} is perfect")
else:
    print(f"{num} is not perfect")
    
print()
    
# 3) لوزی با while
row =1
while row<4:
    j=0
    while j<= -row+3:
        print(" ",end=" ")
        j+=1
    col=1
    while col<= 2*row - 1:
        print("*" ,end=" ")
        col+=1
    print()
    row+=1
row =2
while row>=1:
    j=0
    while j<=-row +3:
        print(" " , end=" ")
        j+=1
    col=0
    while col<=2*row-2:
        print("*" , end=" ")
        col+=1
    print()
    row-=1
    
print()
    
    
# 4) reveresd number
reverseNum= int(input("please enter a number : "))
reverse=0
while reverseNum>0:
    remain = reverseNum%10
    reverse = reverse*10 + remain
    reverseNum = reverseNum//10
print(reverse)
    
