# 1) دو عدد از کاربر گرفته و از عدد کوچکتر تا بزرگتر اعداد اول مابین دو عدد را یافته و در لیستی ذخیره کنید
num1 = int(input("please enter a number : "))
num2 = int(input("please enter a number : "))
prime=[]
if num1>num2:
    num1 , num2 = num2 , num1
for num in range(num1 , num2+1):
    flag=True
    for i in range (2 , num):
        if num%2 == 0:
          flag= False
          break
    if flag :
        prime.append(num)
print(prime)

# 2) کار بالا برای اعداد کامل
a = int(input("please enter a number : "))
b = int(input("please enter a number : "))
perfect=[]
if a>b :
    a,b = b,a
for perfect_num in range(a,b+1):
    summ=0
    for i in range(1,perfect_num):
        if perfect_num % i ==0 :
            summ+= i
    if summ == perfect_num:
        perfect.append(perfect_num)
print(perfect)

# 3) 
# colors = ["crimson", "red", "blue", "green", "yellow", "gray", "white", "pink"]
# [["crimson", "pink"], ["red", "white"], ["blue", "gray"], ["green", "yellow"]]
colors = ["crimson", "red", "blue", "green", "yellow", "gray", "white", "pink"]
res=[]
for i in  range (0 , len(colors)//2):
    res.append([colors[i] , colors[-i-1]])
print(res)


# 4) سری فیبوناچی با استفاده از لیست
tedad = int(input("please enter a number... "))
if tedad == 0:
    fib=[]
elif tedad == 1:
    fib=[0]
elif tedad == 2 :
    fib = [0,1]
else :
    fib = [0,1]
    for i in range(2 , tedad) : 
      fib.append(fib[i-1] + fib[i-2])
print(fib)