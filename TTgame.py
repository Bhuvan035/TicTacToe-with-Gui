import tkinter as tk
from tkinter import Frame, ttk
from tkinter import *

class TTUI():
    master=0
    username=''
    server_address=''
    portnum=0
    left_frame=0
    top_frame=0
    buttons=''
    
    
    
    click=True

    
    def __init__(self):
        self.canvasSetup()
        self.initTKVariables()
        self.frameSetup()
        self.buttonSetup()
        self.checker()
        self.loop_main()
        

    def initTKVariables(self):
      self.username= tk.StringVar()
      self.server_address= tk.StringVar()
      self.portnum= tk.IntVar()
      self.buttons=StringVar()
      
        


    def canvasSetup(self):
        self.master=tk.Tk()
        self.master.title("TIC TAC TOE GAME")
        self.master.geometry('1200x750')
        self.master.configure(background='Blue')
        self.master.resizable(0,0)

    def frameSetup(self):
        self.top_frame=tk.Frame(self.master,bg='Cadet Blue',pady=2, width=1200, height=130)
        self.top_frame.grid(row=0,column=0)

        TopTtl=tk.Label(self.top_frame, font=("arial",15,"bold"), text= "Username:",bg="pink", pady=2)
        TopTtl.grid(row=0,column=0,sticky=W)
        usertxt=tk.Entry(self.top_frame,font=('arial',15,'bold'),bd=2,fg="Black",textvariable=self.username,width=60,justify=LEFT).grid(row=0,column=1)

        sadTtl=tk.Label(self.top_frame, font=("arial",15,"bold"), text= "Server address:",bg="pink", pady=2)
        sadTtl.grid(row=1,column=0,sticky=W)
        sadtxt=tk.Entry(self.top_frame,font=('arial',15,'bold'),bd=2,fg="Black",textvariable=self.server_address,width=60,justify=LEFT).grid(row=1,column=1)

        portTtl=tk.Label(self.top_frame, font=("arial",15,"bold"), text= "Port number:",bg="pink", pady=2)
        portTtl.grid(row=2,column=0,sticky=W)
        porttxt=tk.Entry(self.top_frame,font=('arial',15,'bold'),bd=2,fg="Black",textvariable=self.portnum,width=60,justify=LEFT).grid(row=2,column=1)


        main_frame=tk.Frame(self.master,bg='Orange', width=1200, height=500)
        main_frame.grid(row=1,column=0)
        
        
        right_frame=tk.Frame(main_frame,bd=10, width=600, height=500,bg='yellow')
        right_frame.pack(side=RIGHT)

        self.left_frame=tk.Frame(main_frame,bd=10, width=751, height=500,bg='Red')
        self.left_frame.pack(side=LEFT)

        
        bottom_frame=tk.Frame(self.master,bg='Pink', width=1350, height=150)
        bottom_frame.grid(row=2,column=0)


    def buttonSetup(self):
        button1=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2',command=lambda:checker(button1))
        button1.grid(row=1, column=0, sticky=S+N+E+W)

        button2=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button2.grid(row=1, column=1, sticky=S+N+E+W)

        button3=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button3.grid(row=1, column=2, sticky=S+N+E+W)

        button4=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button4.grid(row=2, column=0, sticky=S+N+E+W)

        button5=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button5.grid(row=2, column=1, sticky=S+N+E+W)

        button6=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button6.grid(row=2, column=2, sticky=S+N+E+W)

        button7=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button7.grid(row=3, column=0, sticky=S+N+E+W)

        button8=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button8.grid(row=3, column=1, sticky=S+N+E+W)

        button9=Button(self.left_frame, text='', font=('Times 26 bold'),height=3, width=8, bg='azure2')
        button9.grid(row=3, column=2, sticky=S+N+E+W)

        '''submitbutton1=Button(self.top_frame, text='Submit', font=('Times 26 bold'), bg='azure2')
        submitbutton1.configure(height=0, width=0)
        submitbutton1.grid(row=0, column=2)

        submitbutton2=Button(self.top_frame, text='Submit', font=('Times 26 bold'), bg='azure2')
        submitbutton2.grid(row=1, column=2)

        submitbutton3=Button(self.top_frame, text='Submit', font=('Times 26 bold'), bg='azure2')
        submitbutton3.grid(row=2, column=2)'''

    def checker(buttons):
        global click
        if buttons['text']==' ' and click=='True':
            buttons['text']='X'
            click=False
        elif buttons['text']=='' and click=='False':
            buttons['text']='o'
            click=True
            
    def loop_main(self):
        master.mainloop()
        



        
        
        

    

if __name__=='__main__':
    basicui=TTUI()




