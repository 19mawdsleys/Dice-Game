import random
##################
#AUTHENTIFICATION#
##################
u1=input("username")
p1=input("password")
if u1 != "Salem" and p1 != "2007":
    for x in range(2):
        u1=input("username")
        p1=input("password")
    print("bye, bye")
    exit()
else:
    print("Autherised")
u2=input("username")
p2=input("password")
if u1 != "Tay" and p1 != "2008":
    for x in range(2):
        u1=input("username")
        p1=input("password")
    print("bye, bye")
    exit()
else:
    print("Autherised")
#########
#ROUND 1#
#########

r1=0
us1=0
odds=td1/2

d1=random.randint(1,6)
d2=random.randint(1,6)
td1=d1+d2
print(d1)
print(d2)
if d1 == d2:
    print("double")
    d3=random.randint(1,6)
    print(d3)
    td1=d1+d2+d3
elif odds == 1:
    us1=us1-4
