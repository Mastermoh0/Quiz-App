import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#B64D4D")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="orange")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Quiz App Login",fg="white",bg="orange")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                
                menu(a)
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Quiz App')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#BADA55")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Quiz App SignUp",fg="#FFA500",bg="#BADA55")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='white',bg='black')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='white',bg='black')
    clabel.place(relx=0.217,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Username and password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Username can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="#BADA55", fg="black")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Quiz App Menu')
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="orange")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#7FFFD4")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="orange") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    abcdefgh='Welcome '+ abcdefgh
    level34 = Label(menu_frame,text=abcdefgh,bg="black",font="calibri 18",fg="white")
    level34.place(relx=0.17,rely=0.15)
    
    level = Label(menu_frame,text='Select your Difficulty Level !!',bg="orange",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='Easy',bg="#7FFFD4",font="calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR = Radiobutton(menu_frame,text='Medium',bg="#7FFFD4",font="calibri 16",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR = Radiobutton(menu_frame,text='Hard',bg="#7FFFD4",font="calibri 16",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="black",fg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def easy():
    
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')
    
    easy_canvas = Canvas(e,width=720,height=440,bg="orange")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="#BADA55")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(15, 0, -1):
            
            if k == 1:
                check=-1
            
            if k >= 10:
                timer_color = "#00FF00"
            elif k >= 5:
                timer_color = "#FFD700"
            else:
                timer_color = "#FF0000"
                
            timer.configure(
                text=str(k),
                font=("Helvetica", 24, "bold"),
                fg=timer_color,
                bg=easy_frame['bg']
            )
            
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(
            text="Times up!",
            font=("Helvetica", 24, "bold"),
            fg="#FF0000"
        )
        
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    easyQ = [
                 [
                     "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
                     "[1, 0, 2, ‘hello’, '', []]",
                     "Error",
                     "[1, 2, ‘hello’]",
                     "[1, 0, 2, 0, ‘hello’, '', []]" 
                 ] ,
                 [
                     "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)" ,
                    "34.00",
                    "34.000000",
                    "34.0000",
                    "34.00000000"
                     
                 ],
                [
                    "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10" ,
                    "30.8",
                    "27.2",
                    "28.4",
                    "30.0"
                ],
                [
                    "Which of these in not a core data type?" ,
                    "Tuples",
                    "Dictionary",
                    "Lists",
                    "Class"
                ],
                [
                    "Which of the following represents the bitwise XOR operator?" ,
                    "&",
                    "!",
                    "^",
                    "|"
                ],
                [
                    "What is the output of 'hello'[1]?",
                    "h",
                    "e",
                    "l", 
                    "o"
                ],
                [
                    "Which of the following is correct about Python?",
                    "It supports automatic garbage collection",
                    "It can be easily integrated with C, C++, COM, ActiveX etc",
                    "Both A and B",
                    "None of the above"
                ],
                [
                    "Which of the following is the truncation division operator in Python?",
                    "/",
                    "//",
                    "%",
                    "None of the above"
                ]
            ]
    answer = [
                "[1, 2, ‘hello’]",
                "34.000000",
                "27.2",
                "Class",
                "^",
                "e",
                "Both A and B",
                "//"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="orange")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="#BADA55")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="#BADA55")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="#BADA55")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="#BADA55")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(easy_frame, bg="#BADA55")
    timer.place(relx=0.8, rely=0.3, anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium():
    
    global m
    m = Tk()
    m.title('Quiz App - Medium Level')
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="#A1A100")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(15, 0, -1):
            
            if k == 1:
                check=-1
            
            if k >= 10:
                timer_color = "#00FF00"
            elif k >= 5:
                timer_color = "#FFD700"
            else:
                timer_color = "#FF0000"
                
            timer.configure(
                text=str(k),
                font=("Helvetica", 24, "bold"),
                fg=timer_color,
                bg=med_frame['bg']
            )
            
            med_frame.update()
            time.sleep(1)
            
        timer.configure(
            text="Times up!",
            font=("Helvetica", 24, "bold"),
            fg="#FF0000"
        )
        
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    mediumQ = [
                [
                    "Which of the following is not an exception handling keyword in Python?",
                     "accept",
                     "finally",
                     "except",
                     "try"
                ],
                [
                    "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
                    "3",
                    "5",
                    "25",
                    "1"
                ],
                [
                    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
                    "Error",
                    "None",
                    "25",
                    "2"
                ],
                [
                    "print(0xA + 0xB + 0xC):",
                    "0xA0xB0xC",
                    "Error",
                    "0x22",
                    "33"
                ],
                [
                    "Which of the following is invalid?",
                    "_a = 1",
                    "__a = 1",
                    "__str__ = 1",
                    "none of the mentioned"
                ], 
                [
                    "What is the output of print(2**3**2)?",
                    "64",
                    "512",
                    "None",
                    "Error"
                ],
                [
                    "Which of the following is not a valid set operation in Python?",
                    "union()",
                    "intersection()",
                    "difference()",
                    "addition()"
                ],
                [
                    "What will be the output of print(0.1 + 0.2 == 0.3)?",
                    "True",
                    "False",
                    "None",
                    "Error"
                ]
            ]
    answer = [
            "accept",
            "1",
            "25",
            "33",
            "none of the mentioned",
            "512",
            "addition()",
            "False"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =mediumQ[x][0],font="calibri 12",bg="#B26500")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="#A1A100")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="#A1A100")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="#A1A100")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="#A1A100")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(med_frame, bg="#A1A100")
    timer.place(relx=0.8, rely=0.3, anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
       
    global h
    #count=0
    h = Tk()
    h.title('Quiz App - Hard Level')
    
    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="#008080")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(15, 0, -1):
            
            if k == 1:
                check=-1
            
            if k >= 10:
                timer_color = "#00FF00"
            elif k >= 5:
                timer_color = "#FFD700"
            else:
                timer_color = "#FF0000"
                
            timer.configure(
                text=str(k),
                font=("Helvetica", 24, "bold"),
                fg=timer_color,
                bg=hard_frame['bg']
            )
            
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(
            text="Times up!",
            font=("Helvetica", 24, "bold"),
            fg="#FF0000"
        )
        
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    hardQ = [
                [
       "All keywords in Python are in _________",
        "lower case",
        "UPPER CASE",
        "Capitalized",
        "None of the mentioned"
    ],
    [
        "Which of the following cannot be a variable?",
        "__init__",
        "in",
        "it",
        "on"
    ],
    [
     "Which of the following is a Python tuple?",
        "[1, 2, 3]",
        "(1, 2, 3)",
        "{1, 2, 3}",
        "{}"   
    ],
    [
        "What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],
    [
        "What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ],
    [
        "What is the output of print(type(1/2))?",
        "<class 'int'>",
        "<class 'float'>",
        "<class 'double'>",
        "<class 'number'>"
    ],
    [
        "Which of the following is correct about Python memory management?",
        "Memory is managed by Python private heap space",
        "Memory is managed by operating system",
        "Memory is managed by user",
        "None of the above"
    ],
    [
        "What will be the output of print(2 * 3 ** 3 * 4)?",
        "216",
        "108",
        "72",
        "144"
    ] 
            
]
    answer = [
            "None of the mentioned",
            "in",
            "(1,2,3)",
            "4",
            "error",
            "<class 'float'>",
            "Memory is managed by Python private heap space",
            "216"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(hard_frame,text =hardQ[x][0],font="calibri 12",bg="#A0DB8E")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="#008080",fg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="#008080",fg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="#008080",fg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="#008080",fg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(hard_frame, bg="#008080")
    timer.place(relx=0.8, rely=0.3, anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        #count=count+1
        if (var.get() in answer):
            score+=1
        display()
    
   # def lastPage():
    #    h.destroy()
     #   showMark()
    
    submit = Button(hard_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    #pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    #pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
   # end=Button(hard_frame,command=showMark(m), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    # IMPROVEMENT 1: Larger window with custom size
    sh = Tk()
    sh.title('Quiz Results')
    sh.geometry('800x600')  # Increased from default size
    
    # IMPROVEMENT 2: Added gradient-like effect with nested frames
    result_canvas = Canvas(sh, width=800, height=600, bg="#1a1a1a")  # Dark outer background
    result_canvas.pack(fill="both", expand=True)
    
    result_frame = Frame(result_canvas, bg="#2d2d2d")  # Slightly lighter inner background
    result_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    
    # IMPROVEMENT 3: Added congratulations header with custom styling
    congrats = "Quiz Completed!"
    clabel = Label(result_frame, text=congrats, 
                  font=("Helvetica", 24, "bold"),  # Larger, bold font
                  fg="#FFD700",  # Gold color for emphasis
                  bg="#2d2d2d")
    clabel.pack(pady=20)
    
    # IMPROVEMENT 4: Enhanced score display with percentage
    percentage = (mark/5) * 100
    score_text = f"Your Score: {mark}/5 ({percentage:.1f}%)"
    score_label = Label(result_frame, text=score_text, 
                       font=("Helvetica", 20),
                       fg="white", bg="#2d2d2d")
    score_label.pack(pady=10)
    
    # IMPROVEMENT 5: Added dynamic performance message with emojis
    if percentage >= 80:
        message = "Excellent! Outstanding performance! 🏆"
        color = "#00ff00"  # Green for excellent
    elif percentage >= 60:
        message = "Good job! Keep it up! 👍"
        color = "#ffff00"  # Yellow for good
    else:
        message = "Keep practicing! You can do better! 💪"
        color = "#ff9900"  # Orange for needs improvement
        
    msg_label = Label(result_frame, text=message, 
                     font=("Helvetica", 16),
                     fg=color, bg="#2d2d2d")
    msg_label.pack(pady=10)
    
    # IMPROVEMENT 6: Enhanced pie chart with better styling
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    
    fig = Figure(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor('#2d2d2d')  # Match background color
    
    plot = fig.add_subplot(111)
    plot.set_facecolor('#2d2d2d')
    
    # IMPROVEMENT 7: Better color scheme for pie chart
    labels = ['Correct', 'Incorrect']
    sizes = [int(mark), 5-int(mark)]
    colors = ['#00ff00', '#ff4444']  # Green for correct, red for incorrect
    explode = (0.1, 0)  # Emphasize correct answers
    
    plot.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    
    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)
    
    # IMPROVEMENT 8: Added hover effects for buttons
    def on_enter(e, button):
        button['background'] = '#404040'  # Lighter shade on hover
        
    def on_leave(e, button):
        button['background'] = '#333333'  # Original color
    
    # IMPROVEMENT 9: Better button organization with frame
    button_frame = Frame(result_frame, bg="#2d2d2d")
    button_frame.pack(pady=20)
    
    # IMPROVEMENT 10: Styled buttons with modern flat design
    retry_btn = Button(button_frame, text="Try Again", 
                      command=lambda: [sh.destroy(), easy()],
                      font=("Helvetica", 12), 
                      width=15, height=2,
                      bg="#333333", fg="white", 
                      relief=FLAT)  # Flat design for modern look
    retry_btn.pack(side=LEFT, padx=10)
    # Add hover effect
    retry_btn.bind("<Enter>", lambda e: on_enter(e, retry_btn))
    retry_btn.bind("<Leave>", lambda e: on_leave(e, retry_btn))
    
    signout_btn = Button(button_frame, text="Sign Out", 
                        command=lambda: [sh.destroy(), start()],
                        font=("Helvetica", 12), 
                        width=15, height=2,
                        bg="#333333", fg="white", 
                        relief=FLAT)
    signout_btn.pack(side=LEFT, padx=10)
    # Add hover effect
    signout_btn.bind("<Enter>", lambda e: on_enter(e, signout_btn))
    signout_btn.bind("<Leave>", lambda e: on_leave(e, signout_btn))
    
    sh.mainloop()

def start():
    global root 
    root = Tk()
    root.title('Welcome To Quiz App')
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="output-onlinepngtools.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage,bg="red",fg="yellow") 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
