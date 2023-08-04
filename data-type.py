
# DATATYPE
age = 28

print(type(age)==int)

 # isinstance

#isinstance ka use ya dekhna k liya k liya hy jo object hy wo is ki class sa belong krta hy k nhi
print(isinstance(age,int))


age = float(28)
print(isinstance(age,int))


age = "45"
number=int(age)
print(isinstance(number,int))

                        #  ternary operator
age = int(18)

def fun(age):

    return True if age>18 else False

