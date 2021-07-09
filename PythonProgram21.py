# Inner if statement ; also called nested
num1 = 30
num2 = -40
num3 = 20
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
        if num2 > num1:
            if num2 > num3:
                print(num2)
            else:
                print(num3)
