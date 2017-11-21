from tkinter import *
from tkinter.colorchooser import *
from tkinter import messagebox


class GetPointsDialog:
    #This is the constructor, and it initializes all the values, once the class is instantiated.
    #window is called based on the window type, which is selected by the user.
    def __init__(self,master, wid_typ):
        Options = ["Dashed","Undashed"]
        choice =IntVar()
        self.master = master
        self.xcord = IntVar()
        #If the window type is 1, then the a toplevel window is created, which gets the coordinates for creating the circle.
        if(wid_typ == 1):
            top1 = Toplevel()
            top1.grab_set()
            #top1.transient(master)
            #master.wait_window(top1)
            top1.geometry("600x400")
            top1.title("Enter the Co-ordinate points")
            #The labels for the all the required cordinates are created and placed in the window.
            L1 = Label(top1, text="X1").place(x=20,y=50)
            self.x1 = StringVar()
            self.L2 = Entry(top1,textvariable=self.x1).place(x=80, y=50)

            L3 = Label(top1, text="Y1").place(x=250,y=50)
            self.y1 = StringVar()
            L4 = Entry(top1,textvariable=self.y1).place(x=280, y=50)

            L5 = Label(top1, text="Enter Radius").place(x=8,y=70)
            self.x3 = StringVar()
            L6 = Entry(top1,textvariable=self.x3).place(x=80, y=70)
            #Buttons are created, and placed in the window. Each button when clicked, calls a particular function.
            COLOR = Button(top1, text="Color", state=NORMAL, command=self.choose_color).place(x=210,y=90)
            SUBMIT = Button(top1, text="Submit", state=NORMAL,command=lambda:self.submit(12)).place(x=120,y=120)
            RESET = Button(top1, text="Reset", state=NORMAL).place(x=340,y=120)

            radiogroup = Frame(top1)
            #This holds the value of the radiobutton.
            self.radiovalue = IntVar()
            #This is the radiobutton for the creating the dashed circle.
            rb1= Radiobutton(top1, text= Options[0], variable=self.radiovalue, value=1, command=self.submit)
            rb1.pack(side=LEFT, anchor=W)

            #This is the radiobutton for the creating the undashed circle.
            rb2= Radiobutton(top1, text= Options[1], variable=self.radiovalue, value=2, command=self.submit)
            rb2.pack(side=LEFT, anchor=W)


        #If the window type is 2, then the a toplevel window is created, which gets the coordinates for creating the Rectangle.
        elif(wid_typ == 2):
            top2 = Toplevel(width= 300, height=200)
            top2.grab_set()
            top2.geometry("600x400")
            top2.title("Enter the Co-ordinate points")
            rL1 = Label(top2, text="X1").place(x=20,y=50)
            self.x5 = StringVar()
            self.rL2 = Entry(top2,textvariable=self.x5).place(x=80, y=50)

            rL3 = Label(top2, text="Y1").place(x=250,y=50)
            self.ry1 = StringVar()
            rL4 = Entry(top2,textvariable=self.ry1).place(x=280, y=50)

            rL7 = Label(top2, text="X2").place(x=20,y=80)
            self.x6 = StringVar()
            rL8 = Entry(top2,textvariable=self.x6).place(x=80, y=80)
            rL9 = Label(top2, text="Y2").place(x=250,y=80)
            self.y2 = StringVar()
            rL10 = Entry(top2,textvariable=self.y2).place(x=280, y=80)

            COLOR = Button(top2, text="Color", state=NORMAL, command=self.choose_color).place(x=210,y=105)
            SUBMIT = Button(top2, text="Submit", state=NORMAL, command=lambda:self.submit(13)).place(x=120,y=120)
            RESET = Button(top2, text="Reset", state=NORMAL, command = self.reset).place(x=340,y=120)

            radiogroup = Frame(top2)

            self.rect_radio = IntVar()

            #This is the radiobutton for the creating the dashed rectangle.
            rb1= Radiobutton(top2, text= "Dashed", variable=self.rect_radio, value=3, command=self.submit)
            rb1.pack(side=LEFT, anchor=W)

            #This is the radiobutton for the creating the unddashed rectangle.
            rb2= Radiobutton(top2, text= Options[1], variable=self.rect_radio, value=4, command=self.submit)
            rb2.pack(side=LEFT, anchor=W)


        elif(wid_typ==3):
            top3 = Toplevel()
            top3.geometry("600x400")
            top3.grab_set()
            top3.title("Enter the Co-ordinate points")
            line1 = Label(top3, text="X1").place(x=20,y=50)
            self.line_x =StringVar()
            rL2 = Entry(top3,textvariable=self.line_x).place(x=80, y=50)

            rL3 = Label(top3, text="Y1").place(x=250,y=50)
            self.line_y = StringVar()
            rL4 = Entry(top3,textvariable=self.line_y).place(x=280, y=50)

            rL7 = Label(top3, text="X2").place(x=20,y=80)
            self.line_x2 = StringVar()
            rL8 = Entry(top3,textvariable=self.line_x2).place(x=80, y=80)
            rL9 = Label(top3, text="Y2").place(x=250,y=80)
            self.line_y2 = StringVar()
            rL10 = Entry(top3,textvariable=self.line_y2).place(x=280, y=80)

            COLOR = Button(top3, text="Color", state=NORMAL, command=self.choose_color).place(x=210,y=105)
            SUBMIT = Button(top3, text="Submit", state=NORMAL, command=lambda:self.submit(14)).place(x=120,y=120)
            RESET = Button(top3, text="Reset", state=NORMAL).place(x=340,y=120)

            radiogroup = Frame(top3)

            self.line_radio = IntVar()

            #This is the radiobutton for the creating the dashed rectangle.
            rb1= Radiobutton(top3, text= "Dashed", variable=self.line_radio, value=5, command=self.submit)
            rb1.pack(side=LEFT, anchor=W)

            #This is the radiobutton for the creating the unddashed rectangle.
            rb2= Radiobutton(top3, text= Options[1], variable=self.line_radio, value=6, command=self.submit)
            rb2.pack(side=LEFT, anchor=W)


    #This method is called, when the user clicks "color" button.
    def choose_color(self):
         self.get_color = askcolor()
         self.color = self.get_color[1]
         #print(self.get_color)

    #After entering all the values, this will get the required values and is submitted to the get_coordinate method.
    def submit(self, value):
        p = Painter(self)

        if(value == 12):
            radio_val = self.radiovalue.get()
            x_one = str(self.x1.get())
            y_one = str(self.y1.get())
            radius = str(self.x3.get())
            color = self.get_color

            '''if(askcolor() == 0):
                #color = '#80acc1'
                self.get_color = askcolor()
                self.color = self.get_color[1]
                messagebox.showinfo("Error","Color has to be selected")
                color = self.get_color'''
            if (len(self.x1.get())==0 or len(self.y1.get())==0 or len(self.x3.get())==0):
                messagebox.showinfo("Error","Values can't be null")
            else:
                p.Create_Circle(x_one, y_one, radius, radio_val, color)
        elif(value == 13):
            rectangle_radio = self.rect_radio.get()
            x1 = str(self.x5.get())
            y1 = str(self.ry1.get())
            x2 = str(self.x6.get())
            y2 = str(self.y2.get())
            rect_color = self.get_color
            if (len(self.x5.get())==0 or len(self.ry1.get())==0 or len(self.x6.get())==0 or len(self.y2.get())==0):
                messagebox.showinfo("Error","Coefficient's cannot be null")
            elif(int(x1) < 50 or int(x2) <50 or int(x1)<int(x2) or int(y1)<int(y2) ):
                messagebox.showinfo("Error","Coefficient's of X1 or X2 can't be less than 50 or X1<X2 or Y1<Y2")
            else:
                p.Create_Rect(x1, y1, x2, y2, rectangle_radio, rect_color)
        elif(value==14):
            line_radiovalue = self.line_radio.get()
            xx = str(self.line_x.get())
            yy = str(self.line_y.get())
            xl = str(self.line_x2.get())
            yl = str(self.line_y2.get())
            line_color = self.get_color
            if(len(self.line_x.get())==0 or len(self.line_y.get())==0 or len(self.line_x2.get())==0 or len(self.line_y2.get())==0):
                messagebox.showinfo("Value Error","Coefficient's cannot be Null")
            elif(int(xx) < 50 or int(yy) <50 or int(xx)<int(xl) or int(yy)<int(yl) ):
                messagebox.showinfo("Error","Coefficient's of X1 or X2 can't be less than 50 or X1<X2 or Y1<Y2")
            else:
                p.Create_line(xx, yy, xl, yl, line_radiovalue, line_color)

        #print(x_one)
        #self.master.x1 = self.x1.get()
    def reset(self):
        print(type(self.rL2))
        self.rL2.delete(0, 'end')


class Painter:

    def __init__(self, master):
        self.init_widgets()
        self.master = master
        #self.x1 = IntVar()

    #The parent window is created here, initialising all the values and placed those in the window.
    def init_widgets(self):
        #Menu bar is created and all the menu options are added, along with the function.
        menu_bar = Menu(root)
        file_menu = Menu(root)
        Options_menu = Menu(root)
        file_menu.add_command(label="New",command=self.create_New_Canvas) #command=GetPointsDialog.__init__(self,root))

        file_menu.add_command(label="Save", command=self.save_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.exit)
        menu_bar.add_cascade(label="File", menu= file_menu )
        menu_bar.add_cascade(label="Options", menu= Options_menu)
        Options_menu.add_command(label="Circle", command=lambda:self.Get_Cordinate_Points(1))
        Options_menu.add_command(label="Line", command=lambda:self.Get_Cordinate_Points(3))
        Options_menu.add_command(label="Rectangle", command=lambda:self.Get_Cordinate_Points(2))
        Options_menu.add_command(label="Clear All", command=self.clear_canvas)
        root.config(menu=menu_bar)
        menu_bar.add_command(label="Help", command=self.show_help_about)
        #A frame is created, with buttons packed in it, and all are disabled by default.
        menuframe = Frame(root)
        menuframe.pack()

        PENBUTTON= Button(root, text="PEN", state=DISABLED, command =lambda:self.activate_button("PEN")).place(x=2,y=10)
        LINEBUTTON = Button(root, text="LINE", state=DISABLED, command =lambda:self.activate_button("LINE")).place(x=35,y=10)
        CIRCLEBUTTON = Button(root, text="CIRCLE",state=DISABLED, command =lambda:self.activate_button("CIRCLE")).place(x=70,y=10)


    #When the user clicks the "new" button, this method is called, and it creates a new canvas.
    def create_New_Canvas(self):
        #wind = Tk()
        self.canvs = Canvas(root, width=700, height=600, bg='white')
        self.canvs.place(x=35, y=135)
        self.enable_menu()
        #root.geometry("400x400")
        #Enable_menu() method is called from here


    #This method enables all th buttons in the frame.
    def enable_menu(self):
        PENBUTTON = Button(root, text="PEN", state=NORMAL,command =lambda:self.activate_button("PEN")).place(x=2,y=10)
        LINEBUTTON = Button(root, text="LINE", state=NORMAL,command =lambda:self.activate_button("LINE")).place(x=35,y=10)
        CIRCLEBUTTON = Button(root, text="CIRCLE",state=NORMAL,command =lambda:self.activate_button("CIRCLE")).place(x=70,y=10)


    def Get_Cordinate_Points(self, wid_typ):
        A = GetPointsDialog(self, wid_typ)
        #self.master.wait_window(A)
        #print('Inside painter: ' + str(self.x1))

    def Create_Circle(self, x, y, r, radio, colo):
        #b = GetPointsDialog()
        self.cx = int(x)
        self.cy = int(y)
        self.cr = int(r)
        self.radio = radio
        self.color = colo
        #print("radio val is" + str(self.radio))
        dash_val =IntVar()
        dash_val = str(self.radio)


        if(dash_val=="1"):
            self.create_New_Canvas()
            self.circ = self.canvs.create_oval(self.cx-self.cr, self.cy-self.cr, self.cx+self.cr, self.cy+self.cr, fill=self.color[1], dash=(dash_val))
        elif(dash_val=="2"):
            self.create_New_Canvas()
            self.circ = self.canvs.create_oval(self.cx-self.cr, self.cy-self.cr, self.cx+self.cr, self.cy+self.cr, fill=self.color[1])
        else:
           messagebox.showerror("Error", "You have to select either: Dashed or UnDashed !")



    def Create_line(self,lx,ly,lx1,ly1,line_r, color_l):
        #b = GetPointsDialog()
        self.xl = lx
        self.yl= ly
        self.x1l = lx1
        self.y1l = ly1
        self.line_r = line_r
        self.color_l = color_l
        #print("radio val is" + str(self.radio))
        line_dash_val =IntVar()
        line_dash_val = str(self.line_r)
        #print(dash_val)

        if(line_dash_val=="5"):
            self.create_New_Canvas()
            self.line = self.canvs.create_line(self.xl, self.yl, self.x1l, self.y1l,  fill=self.color_l[1], dash=(line_dash_val))
        elif(line_dash_val=="6"):
            self.create_New_Canvas()
            self.line = self.canvs.create_line(self.xl, self.yl, self.x1l, self.y1l, fill=self.color_l[1])
        else:
            messagebox.showerror("Error", "You have to select either: Dashed or UnDashed !")


    def Create_Rect(self, x1, x2, y1, y2, r_radio, r_color):
        self.rx1 = x1
        self.rx2 = x2
        self.ry1 = y1
        self.ry2 = y2
        self.r_radio = r_radio
        self.r_color = r_color
        dash_val =IntVar()
        rdash_val = str(self.r_radio)

        if(rdash_val=="3"):
            self.create_New_Canvas()
            self.rect = self.canvs.create_rectangle( self.rx1, self.ry1, self.rx2, self.ry2, fill=self.r_color[1], dash=(rdash_val))
        elif(rdash_val=="4"):
            self.create_New_Canvas()
            self.rect = self.canvs.create_rectangle( self.rx1, self.ry1, self.rx2, self.ry2, fill=self.r_color[1])
        else:
             messagebox.showerror("Error", "You have to select either: Dashed or UnDashed !")


    #When any of the  free hand drawing button, is clicked, then the corresponding method is called based on the button type.
    def activate_button(self, Btn_Typ):
        self.old_x = 0
        self.old_y = 0

        if Btn_Typ == "LINE":
            #self.canvs.bind("<ButtonPress-1>", self.on_button_press)
            self.canvs.bind('<B1-Motion>', self.line_click)
            self.canvs.bind('<ButtonRelease-1>', self.button_released)
        elif Btn_Typ == "CIRCLE":
             self.canvs.bind('<B1-Motion>', self.Circle_click)
             self.canvs.bind('<ButtonRelease-1>', self.button_released)
        elif Btn_Typ == "PEN":
             self.canvs.bind('<B1-Motion>', self.Brush)
             self.canvs.bind('<ButtonRelease-1>', self.button_released)

    #When the mouse button is released, then the coordinates are reset.
    def button_released(self, event):
         event.x = self.old_x
         event.y = self.old_y

    def Brush(self,event):
         self.canvs.create_oval(event.x -2,event.y - 2,event.x + 2,event.y + 2, fill='black')

    #This method is called, when the "line" button type is selected.
    def line_click(self, event):
         self.line = self.canvs.create_line(self.old_x, self.old_y, event.x, event.y, fill="black")
         self.old_x = event.x
         self.old_y = event.y

    #This method is called, when the "Circle" button type is selected.
    def Circle_click(self,event):
        self.circle = self.canvs.create_oval(self.old_x, self.old_y, event.x, event.y, fill="black")

    '''def test(self, wid_typ):
        A = GetPointsDialog(self, wid_typ)'''

    #This method is called, when the clear all ooption is selected. This clears the whole canvas, and empties it.
    def clear_canvas(self):
         self.old_x = 0
         self.old_y = 0
         self.canvs.delete("all")


    def save_canvas(self):
        self.canvs.postscript(file="1014265.ps",colormode="color")
        self.save_canvas = Toplevel()
        self.save_canvas.title("Save Successful")
        help_message = Label(self.save_canvas, text="Success").place(x=60, y=60)

    #This method is called, whne the help menu item is clicked in the main window.
    def show_help_about(self):
        messagebox.showinfo("Info","Created by: Manoj \n ID: 1014265")


    #When we click the exit item in menu, then this method is called, and closed based upon the request by the user.
    def exit(self):
        result = messagebox.askyesno("Exit","Are you sure ?")
        if result == True:
            self.quit()
        else:
            pass

    def quit(self):
        root.destroy()

root = Tk()
my_gui = Painter(root)
root.geometry("800x800")
root.title("Python Paint application")
root.mainloop()


