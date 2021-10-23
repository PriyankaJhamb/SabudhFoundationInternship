#-- Special Operators--

a=1000
b=1000
print(id(a))
print(id(b))
print('aa'*20)
print('a'*40)

#--Identity Operators--
print('aa'*20 is 'a'*40)
print(a is b)#it will compare the ids
print(a is not b )
#-- MemberShip Operators--
# print(1 in a)
a="Priyanka"
print('i' in a)