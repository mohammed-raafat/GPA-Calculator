from tkinter import *
import tkinter.messagebox

check = "L"
def Choice():
    global check
    if Course_Score.get() == 1 :
        Literal_Options.grid_forget()
        Percentage_Entry.configure(state = NORMAL)
        check = "P"

    elif Course_Score.get() == 0 :
        Percentage_Entry.delete(0,END)
        Percentage_Entry.configure(state = DISABLED)
        Literal_Options.grid(row = 0 ,column = 1)
        check = "L"

Courses_Number = 0
def Add_Course():
    global Courses_Number ,check ,point
    score = DoubleVar()
    point = DoubleVar()
    if check == "P" :
        try :
            Percentage = float(Percentage_Entry.get())
            if Percentage >= 0.0 and Percentage <= 100.0 :
                if Percentage >= 90.0 and Percentage <= 100.0 :
                    point = 4.0
                elif Percentage >= 85.0 and Percentage < 90.0 :
                    point = 3.75
                elif Percentage >= 80.0 and Percentage < 85.0 :
                    point = 3.4
                elif Percentage >= 75.0 and Percentage < 80.0 :
                    point = 3.1
                elif Percentage >= 70.0 and Percentage < 75.0 :
                    point = 2.75
                elif Percentage >= 65.0 and Percentage < 70.0 :
                    point = 2.5
                elif Percentage >= 60.0 and Percentage < 65.0 :
                    point = 2.2
                elif Percentage >= 50.0 and Percentage < 60.0 :
                    point = 2.0
                elif Percentage >= 0.0 and Percentage < 50.0 :
                    point = 1.0

                Courses_Number += 1
                Courses_Number_Display.configure(text = Courses_Number)
                HoursList.append(hours.get())
                Hours_Number_Display.configure(text = sum(HoursList))
                ScoreList.append(point)
                score = point
                TotalList.append( float(score * hours.get()) )

            else :
                Percentage_Entry.delete(0 ,END)
                tkinter.messagebox.showerror("ERROR !" ,"You must enter a value between 0 and 100")

        except ValueError :
            Percentage_Entry.delete(0 ,END)
            tkinter.messagebox.showerror("ERROR !" ,"You must enter a value between 0 and 100")

    elif check == "L" :
        Courses_Number += 1
        Courses_Number_Display.configure(text = Courses_Number)
        HoursList.append(hours.get())
        Hours_Number_Display.configure(text = sum(HoursList))
        ScoreList.append(Literal_Points.get(letter.get()))
        score = Literal_Points.get(letter.get())
        TotalList.append( float(score * hours.get()) )

def Undo() :
    global Courses_Number
    if len(TotalList) != 0 :
        HoursList.pop()
        ScoreList.pop()
        TotalList.pop()
        Courses_Number -= 1
        if Courses_Number == 0 and sum(HoursList) == 0 :
            Courses_Number_Display.configure(text = "")
            Hours_Number_Display.configure(text = "")
            Letter.configure(text = "")
        else :
            Courses_Number_Display.configure(text = Courses_Number)
            Hours_Number_Display.configure(text = sum(HoursList))

        Percentage_Entry.delete(0 ,END)
        GPA_Display.configure(text = "")
        Grade_Display.configure(text = "")

    else: tkinter.messagebox.showwarning("Warning !" ,"You didn't add any course to undo addition")

def Caculate_GPA() :
    if sum(HoursList) != 0 :
        gpa = float(sum(TotalList)/sum(HoursList))
        print ("Course Points * Hours = ")#227.29999999999995
        print (sum(TotalList))
        print ("Hours = ")#93
        print (sum(HoursList))
        grade = StringVar()
        f_color = StringVar()
        let = StringVar()
        
        if gpa >= 3.4 and gpa <= 4.0 :
            grade = "Excellent"
            f_color = "green"
            let = "A"
        elif gpa >= 2.8 and gpa < 3.4 :
            grade = "Very Good"
            f_color = "#000fff000"
            let = "B"
        elif gpa >= 2.4 and gpa < 2.8 :
            grade = "Good"
            f_color = "orange"
            let = "C"
        elif gpa >= 2.0 and gpa < 2.4 :
            grade = "Pass"
            f_color = "red"
            let = "D"
        elif gpa >= 1.4 and gpa < 2.0 :
            grade = "Weak"
            f_color = "magenta"
            let = "F"
        elif gpa < 1.4 :
            grade = "Very Weak"
            f_color = "purple"
            let = "F"
        else :
            grade = "asd"
            let = "asd"



        GPA_Display.configure(text = round(gpa ,3))
        Grade_Display.configure(text = grade ,fg = f_color)
        Letter.configure(text = let)

    else :tkinter.messagebox.showwarning("Warning !" ,"You must add a course to be calculated")

def New():
    global check ,Courses_Number
    CheckBtn.deselect()
    Courses_Number = 0
    Percentage_Entry.delete(0,END)
    Percentage_Entry.configure(state = DISABLED)
    Literal_Options.grid(row = 0 ,column = 1)
    check = "L"
    Courses_Number_Display.configure(text = "")
    Hours_Number_Display.configure(text = "")
    GPA_Display.configure(text = "")
    Grade_Display.configure(text = "")
    Letter.configure(text = "")
    
    ScoreList.clear()
    HoursList.clear()
    TotalList.clear()

def About():
    root.maxsize(width = 280 ,height = 400)
    Photo_lbl.pack(side = BOTTOM)
    tkinter.messagebox.showinfo("" ,"Created by :\nMohammed Raafat Ibrahim\n\nWe don't forget our classmate Amr Hendy")
    Photo_lbl.pack_forget()
    root.maxsize(width = 280 ,height = 270)

#*********************************************************************************************************************************************************************************
#***************ROOT***************************ROOT*************************ROOT*************************** ROOT ************************************************************ ROOT
#*********************************************************************************************************************************************************************************
root = Tk()
root.title("GPA Calculator")

letter = StringVar()
letter.set("A+")
hours = IntVar()
Course_Score = IntVar()
ScoreList = []
HoursList = []
TotalList = []
Literal_Points = {'A+':4.0,'A':3.75,'B+':3.4,'B':3.1,'C+':2.75,'C':2.5,'D+':2.2,'D':2.0,'F':1.0}

#*********************************************************************************************************************************************************************************
#***************Top Frame***************************Top Frame**********************Top Frame***************************** Top Frame ************************************ Top Frame
#*********************************************************************************************************************************************************************************
Top_Frame = Frame(root)
Top_Frame.pack(side = TOP)

Course_Score_Hours = LabelFrame(Top_Frame ,relief = FLAT)
Course_Score_Hours.pack(side = TOP )

Course_Score_LabelFrame = LabelFrame(Course_Score_Hours ,text = "Course Score")
Course_Score_LabelFrame.pack(side = LEFT ,padx = 5)

Hours_lblFrame = LabelFrame(Course_Score_Hours ,text = "Course Hours")
Hours_lblFrame.pack(side = RIGHT ,padx = 5)

Label(Course_Score_LabelFrame ,text = "Literal Grade").grid(row =0)

CheckBtn = Checkbutton(Course_Score_LabelFrame ,text = "Percentage   " ,variable = Course_Score ,onvalue = 1 ,offvalue = 0 ,command = Choice)#Check Button
CheckBtn.grid(row = 1)

Percentage_Entry = Entry(Course_Score_LabelFrame ,width = 5 ,state = DISABLED) #Percentage Entry ***************************************** Percentage Entry
Percentage_Entry.grid(row = 1 ,column = 1)

Label(Course_Score_LabelFrame ,text = "%").grid(row = 1 ,column = 3)

Literal_Options = OptionMenu(Course_Score_LabelFrame ,letter ,"A+" ,"A" ,"B+" ,"B" ,"C+" ,"C" ,"D+" ,"D" ,"F" )#Opthin Menu ************** Opthin Menu
Literal_Options.grid(row = 0 ,column = 1)

Radiobutton(Hours_lblFrame ,text = "2" ,variable = hours ,value = 2).pack(side = LEFT) #Radio Button for hour 2 ************************** Radio Button for hour 2
Hours_RadioBtn = Radiobutton(Hours_lblFrame ,text = "3" ,variable = hours ,value = 3) #Radio Button for hour 2 *************************** Radio Button for hour 2
Hours_RadioBtn.pack(side = RIGHT)
Hours_RadioBtn.select()

GPA_Grade_Frame = Frame(Top_Frame ,relief = FLAT)
GPA_Grade_Frame.pack(side = BOTTOM ,pady = 5)

Button(GPA_Grade_Frame ,text = "Add Course" ,command = Add_Course ,bg = "#e6e6e6").grid(row = 0 ,pady = 5) #******************************* Add Course Button

Button(GPA_Grade_Frame ,text = "Undo" ,command = Undo).grid(row = 1) #Undo Button ********************************************************* Undo Button

Label(GPA_Grade_Frame ,text = "Courses No. :").grid(row = 0 ,column = 1 ,pady = 2)
Courses_Number_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 2) #Courses No. Display ******************************************* Courses No. Display
Courses_Number_Display.grid(row = 0, column = 2 ,pady = 2)

Label(GPA_Grade_Frame ,text = "Hours No.    :").grid(row = 1 ,column = 1 ,pady = 2)
Hours_Number_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 2) #Hours No. Display *********************************************** Hours No. Display
Hours_Number_Display.grid(row = 1 ,column = 2 ,pady = 2)

Button(GPA_Grade_Frame ,text = "Calculate GPA" ,width = 15 ,command = Caculate_GPA ,bg = "#d2d2d2").grid(row = 2 ,columnspan = 3 ,pady = 5) #Calculate GPA Button

Label(GPA_Grade_Frame ,text = "GPA    :").grid(row = 3)

GPA_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 15) #GPA Display ************************************************************** GPA Display
GPA_Display.grid(row = 3 ,column = 1)

Label(GPA_Grade_Frame ,text = "Grade :").grid(row = 4)
Grade_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 15) #Grade Display ********************************************************** Grade Display
Grade_Display.grid(row = 4 ,column = 1)

Letter = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 2) #Letter Display ***************************************************************** Letter Display
Letter.grid(row = 3 ,rowspan = 2 ,column = 3)

#*********************************************************************************************************************************************************************************
#***************Bottom Frame***************************Bottom Frame**********************Bottom Frame*************************** Bottom Frame *********************** Bottom Frame
#*********************************************************************************************************************************************************************************

Bottom_Frame = Frame(root)
Bottom_Frame.pack(side = BOTTOM)

Buttons_LabelFrame = LabelFrame(Bottom_Frame ,relief = FLAT)
Buttons_LabelFrame.pack(side = TOP ,pady = 5)

Button(Buttons_LabelFrame ,text = " New  " ,command = New ,bg = "#e6e6e6").pack(side =LEFT ,padx = 15) #New Button ************************* New Button

Button(Buttons_LabelFrame ,text = "About" ,command = About ,bg = "#e6e6e6").pack(side = RIGHT ,padx = 15) #About Button ******************** About Button

Photo = PhotoImage(file = "Amr.png") #Photo ************************************************************************************************* Photo
Photo_lbl = Label(Bottom_Frame ,image = Photo)

#root.maxsize(width= 280 ,height = 270)
root.minsize(width= 280 ,height = 270)

root.mainloop()
