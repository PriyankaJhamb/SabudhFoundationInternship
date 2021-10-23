
str1=input("Enter the String: ");

#Check string is Palindrome or not
print(str1==str1[::-1]);

#remove starting 2 characters and add starting 2 characters to last of the string
print(str1[2:len(str1)] +str1[0:2])


a="Data Science"
print(a)
print("studies {}".format(a))
print("%s"%a)
