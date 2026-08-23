# Exercises: 
# 1) تابعی بنویسید که مغلوب عدد را حساب کند
def reverse(reverseNum):
    reverse=0
    while reverseNum>0:
      remain = reverseNum%10
      reverse = reverse*10 + remain
      reverseNum = reverseNum//10
    return reverse
reverseNum= int(input("please enter a number : "))
print(reverse(reverseNum))


# 2) تابعی بنویسید که دو عدد به عنوان پارامتر گرفته و اعداد اول مابین را یافته و در قالب لیست برگرداند
def prime(a,b):
    primes=[]
    if a>b:
        a,b=b,a
    for num in range(a , b+1):
        if num<2:
            continue
        is_prime=True
        for i in range (2,num):
            if num%i == 0 :
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes

print (prime(2,12))


# 3) تابع سرچ بنویسید
# یک لیست دلخواه و یک آیتم دلخواه بگیرد و اگر آیتم در لیست بود Trueبرگرداند

def search(my_list , item):
    for i in my_list:
        if i ==item:
            return True
        else :
            return False
my_list=[1,2,3,5,7,12,13]
print(search(my_list,20))


# ۰۱۲۳۴۵۶۷۸۹
def persian(a):
    numbers={
        "0":"۰",
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹"
    }
    result=""
    for i in a:
        result +=numbers[i]
    return result

print(persian(" "))