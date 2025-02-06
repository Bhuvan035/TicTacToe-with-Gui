#Tested using IP-127.0.0.1 and port-8888
from gameboardtk import BoardClass
import tkinter as tk 
from tkinter import *
import socket 

p1=BoardClass('X')
p2=BoardClass('O')
clientTurn,counter=1,0
games_played1=1

master=0
username='Player2'
server_address=''
portnum=0
left_frame=0
top_frame=0
buttons=''



master=tk.Tk()
master.title("TIC TAC TOE GAME Server")
master.geometry('600x450')
master.configure(background='grey')
master.resizable(0,0)



username='Player2'
server_address= tk.StringVar()
portnum= tk.IntVar()
buttons=StringVar()


def display_text():
    global username
    global server_address
    global portnum
    #user= username.get()
    serveradd=server_address.get()

    portnumber=portnum.get()
    #print("The username is :",user)
    #print("The Server address is :",serveradd)
    #print("The Port number is :",portnumber)
    return[serveradd,portnumber]



serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connectionSocket=0
def connection1():
    global serverSocket,connectionSocket,name_1
    l=display_text()
    s,p=l[0],l[1]
    serverSocket.bind((s,p))
    serverSocket.listen(5)
    connectionSocket,connectionAddress = serverSocket.accept()
    print("Running")
    #connectionSocket.send(b'Player2')
    name_1=connectionSocket.recv(1024)
    name_1=name_1.decode('ascii')
    print("Player 1's username: "+name_1)
    firstmove()










top_frame=tk.Frame(master,bg='bisque2',width=600,height=90)
top_frame.grid(row=0,column=0,sticky=N+S+W+E)
top_frame.grid_propagate(0)

TopTtl=tk.Label(top_frame, font=("arial",10,"bold"), text= "Username: Player2",bg="steelblue3",pady=4,padx=4)
TopTtl.grid(row=0,column=0,sticky=W)
#usertxt=tk.Entry(top_frame,font=('arial',10,'bold'),fg="Black",textvariable=username,width=30,justify=LEFT).grid(row=0,column=1)

sadTtl=tk.Label(top_frame, font=("arial",10,"bold"), text= "Server address:",bg="steelblue3",pady=4,padx=4)
sadTtl.grid(row=1,column=0,sticky=W)
sadtxt=tk.Entry(top_frame,font=('arial',10,'bold'),bd=2,fg="Black",textvariable=server_address,width=30,justify=LEFT).grid(row=1,column=1)

portTtl=tk.Label(top_frame, font=("arial",10,"bold"), text= "Port number:",bg="steelblue3",pady=4,padx=4)
portTtl.grid(row=2,column=0,sticky=W)
porttxt=tk.Entry(top_frame,font=('arial',10,'bold'),bd=2,fg="Black",textvariable=portnum,width=30,justify=LEFT).grid(row=2,column=1)


main_frame=tk.Frame(master,bg='bisque3', width=600, height=250)
main_frame.grid(row=1,column=0,sticky=N+S+W+E)
main_frame.grid_propagate(0)

submitbutton1=Button(top_frame, text='Submit', font=('Times 15 bold'), bg='steel blue',command=connection1)
submitbutton1.configure(height=1, width=9)
submitbutton1.grid(row=1,column=2,rowspan=2,columnspan=4)


left_frame=tk.Frame(main_frame,bg='red',width=300, height=250)
left_frame.pack(side=LEFT,fill=BOTH)



right_frame=tk.Frame(main_frame,bg='antiquewhite1',width=300, height=250)
right_frame.pack(side=RIGHT,fill=BOTH)



bottom_frame=tk.Frame(master,bg='bisque4', width=600, height=100)
bottom_frame.grid(row=2,column=0,sticky=N+S+W+E)
bottom_frame.grid_propagate(0)

winner_label=tk.Label(bottom_frame,bg='white',text='Game In Progress',font=('arial',15,'bold'))
winner_label.grid(row=0,column=0,sticky=W)

turn_label=tk.Label(bottom_frame,bg='white',text='Your Turn',font=('arial',15,'bold'))
turn_label.grid(column=3,row=0,padx=20)





grid = {'A1':' ','B1':' ','C1':' ','A2':' ','B2':' ','C2':' ','A3':' ','B3':' ','C3':' '}


def sendWinner(msg1,g):
    global winner_label,connectionSocket
    #client.send(msg.encode('ascii'))
    #lbl4 = tk.Label(right_frame,text=msg1,bg='white',font=('arial',15,'bold'))
    winner_label["text"]=msg1
    replaymsg=connectionSocket.recv(1024)
    replaymsg1=replaymsg.decode('ascii')
    if replaymsg1=='Play Again':
        tkinter.messagebox.showinfo('Update','Player 1 wants to Play Again!')
        rematch ()

def drawgame(g):
    global winner_label
    winner_label["text"]="The game has tied!"
    replaymsg=connectionSocket.recv(1024)
    replaymsg1=replaymsg.decode('ascii')
    if replaymsg1=="Play Again":
        tkinter.messagebox.showinfo("Important Update","Player 1 wants to Play Again!")
        rematch()
    else:
        showstats()



def sendbtn1 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'A1'
        g['A1']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        
def sendbtn2 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'B1'
        g['B1']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        
             
def sendbtn3 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'C1'
        g['C1']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        
             
def sendbtn4 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'A2'
        g['A2']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        
             
def sendbtn5 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'B2'
        g['B2']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        
def sendbtn6 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'C2'
        g['C2']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        
             
def sendbtn7 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'A3'
        g['A3']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()

def sendbtn8 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'B3'
        g['B3']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        
             
def sendbtn9 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']=name_1+"'s Turn"
        clientTurn = 0
        msg = 'C3'
        g['C3']['text']='O'
        grid[msg]='O'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='O'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p2.isWinner(list(grid.values()))
        f2=p2.boardIsFull(list(grid.values()))
        if p==True:
            p2.wins+=1
            sendWinner('O-Winner',g)
        if f2==True:
            print("It's a tie!")
            p2.ties+=1
            drawgame(g)
            #rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
        


def firstmove():
    global connectionSocket,g,grid
    frststring=connectionSocket.recv(1024)
    f=frststring.decode('ascii')
    g[f]["text"]="X"
    g[f]["state"]=DISABLED
    grid[f]="X"
             















button1=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn1)
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn2)
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn3)
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn4)
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn5)
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn6)
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn7)
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn8)
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9=Button(left_frame, text='', font=('Times 23 bold'),height=2, width=5, bg='steel blue',command=sendbtn9)
button9.grid(row=3, column=2, sticky=S+N+E+W)



#submitbutton2=Button(top_frame, text='Submit', font=('Times 26 bold'), bg='azure2')
#submitbutton2.grid(row=1, column=2)

#submitbutton3=Button(top_frame, text='Submit', font=('Times 26 bold'), bg='azure2')
#submitbutton3.grid(row=2, column=2)

g = {'A1':button1,'B1':button2,'C1':button3,'A2':button4,'B2':button5,'C2':button6,'A3':button7,'B3':button8,'C3':button9}


def opponent_turn():
    global clientTurn,g,grid,connectionSocket
    if clientTurn==0:
        clientTurn=1
        master.update()
        turn_label['text']='Your Turn'
        string2=connectionSocket.recv(1024)
        string2=string2.decode('utf-8')
        k=g[string2]
        k['text']='X'
        k['state']=DISABLED
        grid[string2]='X'
        if p1.isWinner(list(grid.values())) :
            p2.losses+=1
            sendWinner('X-Winner',g)
        if p2.boardIsFull(list(grid.values())):
            p2.ties+=1
            drawgame(g)

def rematch():
    #pop-up window
    global g,grid,turn_label,games_played1,winner_label
    p2.resetGameBoard(g)
    games_played1+=1
    winner_label['text']='Game In Progress'
    turn_label['text']="Opponent's Turn"
    button1['state']= tk.NORMAL
    button2['state']= tk.NORMAL
    button3['state']= tk.NORMAL
    button4['state']= tk.NORMAL
    button5['state']= tk.NORMAL
    button6['state']= tk.NORMAL
    button7['state']= tk.NORMAL
    button8['state']= tk.NORMAL
    button9['state']= tk.NORMAL
    button1['text']= ''
    button2['text']= ''
    button3['text']= ''
    button4['text']= ''
    button5['text']= ''
    button6['text']= ''
    button7['text']= ''
    button8['text']= ''
    button9['text']= '' 
    global clientTurn
    clientTurn = 0
    global counter
    counter = 0
    grid = {'A1':' ','B1':' ','C1':' ','A2':' ','B2':' ','C2':' ','A3':' ','B3':' ','C3':' '}
    g = {'A1':button1,'B1':button2,'C1':button3,'A2':button4,'B2':button5,'C2':button6,'A3':button7,'B3':button8,'C3':button9}
    opponent_turn()


games_won=tk.IntVar()
games_lost=tk.IntVar()
games_tie=tk.IntVar()



def showstats():
    global right_frame
    stats=p2.printStats()
    print(stats)
    games_played="Games Played:"+str(games_played1)
    games_won1=stats[2]
    games_won="Games Won:"+str(games_won1)
    games_lost1=stats[3]
    games_lost="Games Lost:"+str(games_lost1)
    games_tie1=stats[4]
    games_tie="Games Tied:"+str(games_tie1)
    #stat="Games Played : ",games_played,"\n"+"Games Won: ",games_won
    stlbl1 = tk.Label(right_frame,bg='white',text=games_played,font=('arial',15,'bold'))
    stlbl1.grid(column=0,row=0,sticky=N+S+W+E)
    #stlbl2 = tk.Label(right_frame,bg='white',text=last_player,font=('arial',15,'bold'))
    #stlbl2.grid(column=0,row=1,sticky=N+S+W+E)
    stlbl3 = tk.Label(right_frame,bg='white',text=games_won,font=('arial',15,'bold'))
    stlbl3.grid(column=0,row=2,sticky=N+S+E+W)
    stlbl4 = tk.Label(right_frame,bg='white',text=games_lost,font=('arial',15,'bold'))
    stlbl4.grid(column=0,row=3,sticky=W+S+E+N)
    stlbl5 = tk.Label(right_frame,bg='white',text=games_tie,font=('arial',15,'bold'))
    stlbl5.grid(column=0,row=4,sticky=W+N+S+E)
    
    over=tk.Button(right_frame, text="QUIT GAME", font=('Times 20 bold'), bg='azure2',command=master.destroy)
    over.configure(height=2,width=15)
    over.grid(row=8,column=0,columnspan=4)


master.mainloop()










#serverAddress=input('Enter the IP address')
#port=int(input('Enter the port'))
#serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serverSocket.bind((serverAddress,port))
#serverSocket.listen(5)
'''clientSocket,clientAddress = serverSocket.accept()
clientSocket.send(b'Player2')
name_1=clientSocket.recv(1024)
name_1=name_1.decode('ascii')
print("Player 1's username: "+name_1)'''


'''p2=BoardClass('O')
rematch=True

while rematch==True:
    p2.updateGamesPlayed()
    while p2.isWinner('O')==False and p2.isWinner('X')==False and p2.boardIsFull()==False:
        p2.draw_gameboard()
        print('Waiting for',name_1,"'s turn")
        string=clientSocket.recv(1024)
        grid_value=string.decode('ascii')
        p2.updateGameBoard(grid_value,'X')
        p2.draw_gameboard()
        p2.set_lastplayer(name_1)
        if p2.isWinner('X')==False and p2.boardIsFull()==False:
            while True:
                position2=input('Enter the position to place the pawn in: ') 
                if  p2.updateGameBoard(position2,'O')==True:
                    break
            string2=position2.encode('ascii')
            clientSocket.send(string2)
            p2.set_lastplayer('Player 2')
    #End game messages
    if p2.isWinner('O')==True:
        print('Congratulations you have won the game')
        p2.wins+=1
    elif p2.boardIsFull()==True:
        print('The game was a draw')
        p2.ties+=1
    elif p2.isWinner('X')==True: 
        print('Sorry',name_1,'won')
        p2.losses+=1
    response_host=clientSocket.recv(1024)
    r=response_host.decode('ascii')
    print(response_host)
    if r=='Fun times':
        rematch=False
        break
    else:
        p2.resetGameBoard()
        
#Printing Statistics for Player 2
print('Thank you for playing!')
print('Here are your stats')
print('Your username: Player2')
print("Opponent's username: ",name_1)
p2.printStats()
serverSocket.close()'''


