#-------------------importing guizero-------------------------#
import guizero as gz
from guizero import warn



#----------------Widgit events
#----------------------what leatter grade---------------------#

def your_grade(finalres):
    your_grade = "E"
    if finalres >=90:
        your_grade ="A+"
    elif finalres >=85:
        your_grade ="A"#--------- DOWN TO D !!!!

    return your_grade

#----------------------20 percent of grade-------------------#
def MARKS():
    total1 = []
    weightres = []
    outofres = []
    print("test")
    
   

#-----------------------------------------------------#
    try:
        total1.append(int(Mark1.value)) 
        total1.append(int(Mark2.value))
        total1.append(int(Mark3.value))
        if total1[0] <=100 and total1[0] >=0:
            print("die")#----------- NEED TO CHANGE 
        else:
            evtError()
    except ValueError:
        warn("invalid input", "enter numebers only")
        return
#--------------------out of list----------------------#
    try:
        outofres.append(int(outof1.value))
        outofres.append(int(outof2.value))
        outofres.append(int(outof3.value))
        if outofres[0] <=100 and outofres[0] >=0:
                print("die")#----------- NEED TO CHANGE 
        else:
            evtError()
    except ValueError:
        warn("invalid input", "enter numebers only")
        return
#---------------------Weight list---------------------#
    try:
        weightres.append(int(weight1.value))
        weightres.append(int(weight2.value))
        weightres.append(int(weight3.value))
        if weightres[0] <=100 and weightres[0] >=0:
                print("die")#----------- NEED TO CHANGE 
        else:
            evtError()
    except ValueError:
        warn("invalid input", "enter numebers only")
        return
#---------adding evreything to get percentage---------#
    result1 = ((total1[0] / outofres[0])* weightres[0])
    result2 = ((total1[1] / outofres[1])* weightres[1])
    result3 = ((total1[2] / outofres[2])* weightres[2])
    print(result1)



#-----------------------your grade--------------------#
    finalres = result1 + result2 + result3
    letter_grade.value = your_grade(finalres)
    passing.value = "passing" if finalres >=50 else "not passing"
#-----------------------peramiters-----------------------#
    try:
        if finalres <=100 and finalres >=0:
            print("test")
        else:
            evtError()
    except ValueError:
        evtError()
    final.value = finalres
    
#------------------error event----------------#
def evtError():
    gz.error('Error','This is an error')




#---------------------addup------------------------#




    
#--------------grid layout and name of window------------------#
app = gz.App("an assesment grade calulator", 500, 400, layout="grid")

#---------------------tile of app-----------------------------#
titlebox = gz.Box(app, border=True, grid=[0, 0], width="fill")
gz.Text(titlebox, text="Grading System", size=20, align="left")

#------definig the criterea of what this text box is for------#
box = gz.TitleBox(app, text="Results", layout="grid", grid=[0, 1], width="fill")
gz.Text(box, text="Marks", grid=[1, 0], align="left", size=10)
gz.Text(box, text="Out of", grid=[2, 0], align="left", size=10)
gz.Text(box, text="Weight%", grid=[3, 0], align="left", size=10)

#------------------labels for the courses---------------------#
gz.Text(box, text="Assesment1", grid=[0, 1], align="left", size=10)
gz.Text(box, text="Assesment2", grid=[0, 2], align="left", size=10)
gz.Text(box, text="Assesment3", grid=[0, 3], align="left", size=10)

#-----------------the mark input box------------------------#
Mark1 = gz.TextBox(box, width=5, grid=[1, 1], text='0')
Mark1.text_size = 10
Mark2 = gz.TextBox(box, width=5, grid=[1, 2], text='0')
Mark2.text_size = 10
Mark3 = gz.TextBox(box, width=5, grid=[1, 3], text='0')
Mark3.text_size = 10

#-----------------------out of------------------------------#
outof1= gz.TextBox(box, width=5, grid=[2, 1], text='100')
outof1.text_size =10
outof2= gz.TextBox(box, width=5, grid=[2, 2], text='100')
outof2.text_size =10
outof3= gz.TextBox(box, width=5, grid=[2, 3], text='100')
outof3.text_size =10

#-----------------------weight------------------------------#
weight1= gz.TextBox(box, width=5, grid=[3, 1], text='20')
weight1.text_size =10
weight2= gz.TextBox(box, width=5, grid=[3, 2], text='30')
weight2.text_size =10
weight3= gz.TextBox(box, width=5, grid=[3, 3], text='50')
weight3.text_size =10

#----------where the resultes are printed out---------------#
gz.Text(box, text="Total mark", grid=[0, 5], align="right", size=20)
final = gz.Text(box, text='---', grid=[1, 5], align="right", size=20)
letter_grade = gz.Text(box, text="---", grid=[2, 5], size=20)
passing = gz.Text(box, text="-------", grid=[3, 5], size=20)

#----------------start of comand structure------------------#
submitPushButton = gz.PushButton(   
    app, text="Submit", grid=[0, 2], align='left', padx=5, pady=5, command=MARKS)



exitPushButton = gz.PushButton(
    app, text="Leave", grid=[0, 2], align='right', padx=5, pady=5)

#---------Render the layout and start the event-loop--------#



app.display()