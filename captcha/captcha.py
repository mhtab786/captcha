import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C',
          'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
special=['!','@','#','$','%','^','&','*','(',')','_','+','-','=','/','|','{',';','"',':','/',',','?',
                                                             '>','<','`','~','}',"'",']','[']
# print(type(number))
# x=(random.choice(alphabet))
# y=(random.choice(number))
# z=(random.choice(special))

# print(x,z,y)

l=random.randint(1,4)
n=random.randint(1,3)
m=random.randint(0,3)

# print(random.choices(number))
# p=(random.choice(number),end="\n")
num=[]
# char=""
# spl=""
# print("number= ",n)
# print("letter= ",l)
# print("symbol= ",m)

for digit in range(0,n):
    x=(random.choice(number))
    num+=x
# print(num)
#     B=digit
for letter in range(0,l):
    y=(random.choice(alphabet))
    num+=y
for case in range(0,m):
    z=(random.choice(special))
    num+=z

random.shuffle(num)
# print(*num)

sys=""
for code in num:
    sys+=code
print("Captcha is ",sys)

enter=input("enter the above captcha: ")
if enter==sys:
    print("Accepted 👍")
else:
    print("Failed ❌")
