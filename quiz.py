import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time

def create_exit_button(window):
    """Create a consistent exit button for any window"""
    exit_button = Button(window, 
                        text="X", 
                        command=lambda: window.destroy(),
                        bg="red", 
                        fg="white",
                        font=("Arial", "12", "bold"),
                        width=3,
                        height=1)
    exit_button.place(relx=0.95, rely=0.02, anchor=NE)

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')
    create_exit_button(login)
    
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
        global current_user
        for a, b, c, d in logdata:
            if b == uname.get() and c == pas.get():
                current_user = b
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
    create_exit_button(sup)
    
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

def menu(user):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Quiz App Menu')
    create_exit_button(menu)
    
    
    menu_canvas = Canvas(menu_window,width=720,height=440,bg="orange")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#7FFFD4")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="orange") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    abcdefgh='Welcome '+ user
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
            menu_window.destroy()
            easy()
        elif x == 2:
            menu_window.destroy()
            medium()
        
        elif x == 3:
            menu_window.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="black",fg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu_window.mainloop()
def easy():
    
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')
    create_exit_button(e)
    
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
    
    # Question label with better visibility
    ques = Label(easy_frame,
                 text=easyQ[x][0],
                 font=("calibri", 16, "bold"),  # Larger, bold font
                 bg="orange",                   # Distinctive background
                 wraplength=500,                # Wrap text if too long
                 justify=LEFT,                  # Left-align text
                 padx=20,                       # Horizontal padding
                 pady=10)                       # Vertical padding
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()
    
    # Make radio buttons bigger and square-shaped
    style_config = {
        'font': "calibri 16",      # Large font
        'width': 50,               # Much wider
        'height': 3,               # Taller
        'selectcolor': '#333333',  # Dark grey when selected
        'indicatoron': 0,          # Remove circular indicator
        'relief': 'raised',        # 3D effect
        'bd': 3,                   # Border width
        'activebackground': '#555555',  # Color when hovering
        'activeforeground': 'white'     # Text color when hovering
    }
    
    # Center the text and add padding
    a = Radiobutton(easy_frame, text=easyQ[x][1], value=easyQ[x][1], 
                    variable=var, bg="#BADA55", **style_config,
                    padx=20, pady=10, anchor='center')
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(easy_frame, text=easyQ[x][2], value=easyQ[x][2], 
                    variable=var, bg="#BADA55", **style_config,
                    padx=20, pady=10, anchor='center')
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(easy_frame, text=easyQ[x][3], value=easyQ[x][3], 
                    variable=var, bg="#BADA55", **style_config,
                    padx=20, pady=10, anchor='center')
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(easy_frame, text=easyQ[x][4], value=easyQ[x][4], 
                    variable=var, bg="#BADA55", **style_config,
                    padx=20, pady=10, anchor='center')
    d.place(relx=0.5, rely=0.72, anchor=CENTER)
    
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
        showMark(score)
    
    # Exit button (placed at top of page)
    exit_button = Button(easy_frame, 
                        text="Exit", 
                        command=lambda: e.destroy(),
                        bg="red", 
                        fg="white",
                        font=("Arial", "12", "bold"),
                        width=15,
                        height=1)
    exit_button.place(relx=0.87, rely=0.1, anchor=CENTER)  # Moved to top
    
    # Submit and Next buttons
    nextQuestion = Button(easy_frame, command=display, text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.5, rely=0.82, anchor=CENTER)
    
    submit = Button(easy_frame, command=calc, text="Submit", fg="white", bg="black")
    submit.place(relx=0.87, rely=0.82, anchor=CENTER)
    
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
    create_exit_button(m)
    
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
    
    # Question label with better visibility
    ques = Label(med_frame,
                 text=mediumQ[x][0],
                 font=("calibri", 16, "bold"),  # Larger, bold font
                 bg="#B26500",                   # Distinctive background
                 wraplength=500,                # Wrap text if too long
                 justify=LEFT,                  # Left-align text
                 padx=20,                       # Horizontal padding
                 pady=10)                       # Vertical padding
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame, text=mediumQ[x][1], font="calibri 14", value=mediumQ[x][1], 
                    variable=var, bg="#A1A100", width=30, height=2)
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med_frame, text=mediumQ[x][2], font="calibri 14", value=mediumQ[x][2], 
                    variable=var, bg="#A1A100", width=30, height=2)
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med_frame, text=mediumQ[x][3], font="calibri 14", value=mediumQ[x][3], 
                    variable=var, bg="#A1A100", width=30, height=2)
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med_frame, text=mediumQ[x][4], font="calibri 14", value=mediumQ[x][4], 
                    variable=var, bg="#A1A100", width=30, height=2)
    d.place(relx=0.5, rely=0.72, anchor=CENTER)
    
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
        showMark(score)
    
    # Exit button (placed at top of page)
    exit_button = Button(med_frame, 
                        text="Exit", 
                        command=lambda: m.destroy(),
                        bg="red", 
                        fg="white",
                        font=("Arial", "12", "bold"),
                        width=15,
                        height=1)
    exit_button.place(relx=0.87, rely=0.1, anchor=CENTER)  # Moved to top
    
    # Submit and Next buttons
    nextQuestion = Button(med_frame, command=display, text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.5, rely=0.82, anchor=CENTER)
    
    submit = Button(med_frame, command=calc, text="Submit", fg="white", bg="black")
    submit.place(relx=0.87, rely=0.82, anchor=CENTER)
    
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
    create_exit_button(h)
    
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
    
    # Question label with better visibility
    ques = Label(hard_frame,
                 text=hardQ[x][0],
                 font=("calibri", 16, "bold"),  # Larger, bold font
                 bg="#A0DB8E",                   # Distinctive background
                 wraplength=500,                # Wrap text if too long
                 justify=LEFT,                  # Left-align text
                 padx=20,                       # Horizontal padding
                 pady=10)                       # Vertical padding
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame, text=hardQ[x][1], font="calibri 14", value=hardQ[x][1], 
                    variable=var, bg="#008080", fg="white", width=30, height=2)
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(hard_frame, text=hardQ[x][2], font="calibri 14", value=hardQ[x][2], 
                    variable=var, bg="#008080", fg="white", width=30, height=2)
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(hard_frame, text=hardQ[x][3], font="calibri 14", value=hardQ[x][3], 
                    variable=var, bg="#008080", fg="white", width=30, height=2)
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(hard_frame, text=hardQ[x][4], font="calibri 14", value=hardQ[x][4], 
                    variable=var, bg="#008080", fg="white", width=30, height=2)
    d.place(relx=0.5, rely=0.72, anchor=CENTER)
    
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
        showMark(score)
    
   # def lastPage():
    #    h.destroy()
     #   showMark()
    
    # Exit button (placed at top of page)
    exit_button = Button(hard_frame, 
                        text="Exit", 
                        command=lambda: h.destroy(),
                        bg="red", 
                        fg="white",
                        font=("Arial", "12", "bold"),
                        width=15,
                        height=1)
    exit_button.place(relx=0.87, rely=0.1, anchor=CENTER)  # Moved to top
    
    # Submit and Next buttons
    nextQuestion = Button(hard_frame, command=display, text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.5, rely=0.82, anchor=CENTER)
    
    submit = Button(hard_frame, command=calc, text="Submit", fg="white", bg="black")
    submit.place(relx=0.87, rely=0.82, anchor=CENTER)
    
    #pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    #pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
   # end=Button(hard_frame,command=showMark(m), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    # Store the score in the database
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (username, score) VALUES (?, ?)", (current_user, mark))
    conn.commit()

    # Retrieve top scores
    cursor.execute("SELECT username, score FROM scores ORDER BY score DESC LIMIT 5")
    top_scores = cursor.fetchall()
    conn.close()

    sh = Tk()
    sh.title('Quiz Results')
    create_exit_button(sh)
    sh.geometry('800x600')  # Increased from default size
    
    result_canvas = Canvas(sh, width=800, height=600, bg="#1a1a1a")
    result_canvas.pack(fill="both", expand=True)
    
    result_frame = Frame(result_canvas, bg="#2d2d2d")
    result_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    
    congrats = "Quiz Completed!"
    clabel = Label(result_frame, text=congrats, font=("Helvetica", 24, "bold"), fg="#FFD700", bg="#2d2d2d")
    clabel.pack(pady=20)
    
    percentage = (mark/5) * 100
    score_text = f"Your Score: {mark}/5 ({percentage:.1f}%)"
    score_label = Label(result_frame, text=score_text, font=("Helvetica", 20), fg="white", bg="#2d2d2d")
    score_label.pack(pady=10)
    
    if percentage >= 80:
        message = "Excellent! Outstanding performance! 🏆"
        color = "#00ff00"
    elif percentage >= 60:
        message = "Good job! Keep it up! 👍"
        color = "#ffff00"
    else:
        message = "Keep practicing! You can do better! 💪"
        color = "#ff9900"
        
    msg_label = Label(result_frame, text=message, font=("Helvetica", 16), fg=color, bg="#2d2d2d")
    msg_label.pack(pady=10)
    
    # Display top scores
    ranking_label = Label(result_frame, text="Top Scores", font=("Helvetica", 18, "bold"), fg="white", bg="#2d2d2d")
    ranking_label.pack(pady=10)

    for i, (username, score) in enumerate(top_scores, start=1):
        score_text = f"{i}. {username}: {score}"
        score_label = Label(result_frame, text=score_text, font=("Helvetica", 14), fg="white", bg="#2d2d2d")
        score_label.pack()

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

def initialize_database():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()
