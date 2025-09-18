#-------------------importing guizero-------------------------#
import guizero as gz




#----------------Widgit events


#----------------------20 percent of grade-------------------#
def your_number1():
    total1 = []
    total2 = []
    total3 = []
    print("test")
    try:
        total1.append(int(Mark1.value))
        total1.append(int(outof1.value))
        total1.append(int(weight1.value))
        result1 = (total1[0] + total1[1] + total1[2])
        print(result1)

    except:
        return []
    return
    




#---------------------addup------------------------#
def finalised():
    grade4 = int, Mark1 + Mark2 + Mark3
    print(grade4)
#----------------------runing the code---------------------#


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
grade = gz.Text(box, text="---", grid=[2, 5], size=20)
passing = gz.Text(box, text="-------", grid=[3, 5], size=20)

#----------------start of comand structure------------------#
submitPushButton = gz.PushButton(   
    app, text="Submit", grid=[0, 2], align='left', padx=5, pady=5, command=your_number1)
    
exitPushButton = gz.PushButton(
    app, text="Leave", grid=[0, 2], align='right', padx=5, pady=5)

#---------Render the layout and start the event-loop--------#



app.display()