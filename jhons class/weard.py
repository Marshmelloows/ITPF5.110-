
grades = 0
grades[0] =0
grades[1] =0
grades[2] =0
#----------------------20 percent of grade-------------------#
def your_number1():
    grades[0]=int(input("this is 20 percent of your grade!.please out in your number out of 100:"))
    if grades[0] >0 or grades[0] <101:
        print("well done")
        grades[0] = grades[0]*0.2
        print(grades[0])
    else:
        print("that did not work!!")
#----------------------30 percent of your grade----------------#
def your_number2():
    grades[1]=int(input("this is 20 percent of your grade!.please out in your number out of 100:"))
    if grades[1] >0 or grades[1] <101:
        print("well done")
        grades[1] = grades[1]*0.2
        print(grades[1])
    else:
        print("that did not work!!")
#---------------------50 percent of your grade----------------------#
def your_number3():
    grades[2]=int(input("this is 20 percent of your grade!.please out in your number out of 100:"))
    if grades[2] >0 or grades[2] <101:
        print("well done")
        grades[2] = grades[2]*0.2
        print(grades[2])
    else:
        print("that did not work!!")
#---------------------addup------------------------#
def finalised():
    grade4 = grades[0] + grades[1] + grades[2]
    print(grade4)
#----------------------runing the code---------------------#
your_number1()
your_number2()
your_number3()
finalised()