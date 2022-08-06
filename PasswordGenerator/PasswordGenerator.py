import random
numbers="0123456789"
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMOPQRSTUVWXYZ"
special="~!@#$%^&*()<>,"
password=numbers+lower+upper+special
n=int(input("\nEnter the legth of password:"))
print("Generating Password.......")
print("Your password is >>>>>>>>>> "+"".join(random.sample(password,n)))
