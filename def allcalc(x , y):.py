def allcalc(x , y):
    return x+y , x-y , x*y , x/y , x%y

#_main_

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
add , sub , mult , div , mod = allcalc(num1 , num2)
list(print('sum of given number :',add))
print('subtraction of given number :',sub )
print('product of given number :' ,mult )
print('Division of given number :',div )
print('Modulo of given number : ',mod )
