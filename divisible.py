num = int(input("ENTER YOUR NUMBER :"))
div = int(input("ENTER YOUR DIVISIBLE NUMBER :"))
if num%7==0:
    print("THE NUMBER IS DIVISIBLE BY 7")
    print(7,"times",num//7,"is" ,num)
elif num%7!=0:
    print("THE NUMBER IS NOT DIVISIBLE by 7")

if num%5==0:
    print("THE NUMBER IS DIVISIBLE by 5")
    print(5,"times",num//5,"is" ,num)
elif num%5!=0:
    print("THE NUMBER IS NOT DIVISIBLE by 5")
else:
    print("invalid statement")
