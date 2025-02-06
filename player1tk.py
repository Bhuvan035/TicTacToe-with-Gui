#Tested using IP-127.0.0.1 and port-8888
from gameboardtk import BoardClass
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import socket

p1=BoardClass('X')
p2=BoardClass('O')
clientTurn=1
counter=0
games_played1=1


master=0
username=''
server_address=''
portnum=0
left_frame=0
top_frame=0
buttons=''






        

master=tk.Tk()
master.title("TIC TAC TOE GAME Client")
master.geometry('600x450')
master.configure(background='grey')
master.resizable(0,0)






username= tk.StringVar()
server_address= tk.StringVar()
portnum= tk.IntVar()
buttons=StringVar()


def display_text():
    global username
    global server_address
    global portnum
    user= username.get()
    serveradd=server_address.get()
    portnumber=portnum.get()
    #print("The username is :",user)
    #print("The Server address is :",serveradd)
    #print("The Port number is :",portnumber)
    return[user,serveradd,portnumber]








#username=input('Enter your username: ')
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connection1():
    global connectionSocket
    try:
        l = display_text()
        u,s,p=l[0],l[1],l[2]
        connectionSocket.connect((s,p))
        #connectionSocket.setblocking(0)
        print("Connection Succesfull!")
        connectionSocket.send(u.encode("ascii"))
        #username_p2=connectionSocket.recv(1024)
    except Exception as e:
        print(e)
        print("Connection Failed!")
        sadtxt.delete(0,'end')
        porttxt.delete(0,'end')
        master.update()
        option=input("Do You want to try again?")
        if option=="y":
            run_connection()







top_frame=tk.Frame(master,bg='bisque2',width=600,height=90)
top_frame.grid(row=0,column=0,sticky=N+S+W+E)
top_frame.grid_propagate(0)

TopTtl=tk.Label(top_frame, font=("arial",10,"bold"), text= "Username:",bg="steelblue3",pady=4,padx=4)
TopTtl.grid(row=0,column=0,sticky=W)
usertxt=tk.Entry(top_frame,font=('arial',10,'bold'),fg="Black",textvariable=username,width=30,justify=LEFT)
usertxt.grid(row=0,column=1)

sadTtl=tk.Label(top_frame, font=("arial",10,"bold"), text= "Server address:",bg="steelblue3",pady=4,padx=4)
sadTtl.grid(row=1,column=0,sticky=W)
sadtxt=tk.Entry(top_frame,font=('arial',10,'bold'),bd=2,fg="Black",textvariable=server_address,width=30,justify=LEFT)
sadtxt.grid(row=1,column=1)

portTtl=tk.Label(top_frame, font=("arial",10,"bold"), text= "Port number:",bg="steelblue3",pady=4,padx=4)
portTtl.grid(row=2,column=0,sticky=W)
porttxt=tk.Entry(top_frame,font=('arial',10,'bold'),bd=2,fg="Black",textvariable=portnum,width=30,justify=LEFT)
porttxt.grid(row=2,column=1)


main_frame=tk.Frame(master,bg='bisque3', width=600, height=250)
main_frame.grid(row=1,column=0,sticky=N+S+W+E)
main_frame.grid_propagate(0)


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


rmatch=tk.Button(top_frame, text='REMATCH', font=('Times 10 bold'),state=DISABLED, bg='steel blue')
rmatch.configure(height=1,width=15)
rmatch.grid(row=1,column=2)

grid = {'A1':' ','B1':' ','C1':' ','A2':' ','B2':' ','C2':' ','A3':' ','B3':' ','C3':' '}

def sendWinner(msg1,g):
    global winner_label,turn_label
    winner_label["text"]=msg1
    turn_label['text']='Game Over'
    tk.messagebox.showinfo('Update','GAME OVER! CLICK "REMATCH" FOR A NEW GAME OR "SHOW STATISTICS" TO DISPLAY THE GAME RESULTS')
    #rematch ()


def drawgame(g):
    global winner_label,turn_label
    winner_label["text"]="The game has tied!"
    turn_label['text']='Game Over'
    tk.messagebox.showinfo("Important Update","GAME OVER! PRESS REMATCH FOR A NEW GAME OR SHOW STATS TO DISPLAY THE GAME RESULTS")

def sendbtn1 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'A1'
        g['A1']['text']='X'
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
             
def sendbtn2 ():
     global clientTurn,g,grid,connectionSocket
     if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'B1'
        g['B1']['text']='X'
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
     
                
def sendbtn3 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'C1'
        g['C1']['text']="X"
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
def sendbtn4 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'A2'
        g['A2']['text']="X"
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
            
def sendbtn5 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'B2'
        g['B2']['text']="X"
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
            
def sendbtn6 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'C2'
        g['C2']['text']="X"
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
            
def sendbtn7 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'A3'
        g['A3']['text']="X"
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
             
def sendbtn8 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'B3'
        g['B3']['text']="X"
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()
             
def sendbtn9 ():
    global clientTurn,g,grid,connectionSocket
    if clientTurn == 1:
        turn_label['text']="Player 2's Turn"
        clientTurn = 0
        msg = 'C3'
        g['C3']['text']="X"
        grid[msg]='X'
        connectionSocket.send(msg.encode('ascii'))
        button1['text']='X'
        button1['state']= tk.DISABLED
        global counter
        counter += 1
        p=p1.isWinner(list(grid.values()))
        f2=p1.boardIsFull(list(grid.values()))
        if p==True:
            print("We have a winner")
            p1.wins+=1
            sendWinner('X-Winner',g)
            rmatch['state']=tk.NORMAL
        if f2==True:
            print("It's a tie!")
            p1.ties+=1
            drawgame(g)
            rmatch['state']=tk.NORMAL
        if p==False and f2==False:
            opponent_turn()



















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

submitbutton1=Button(top_frame, text='Submit', font=('Times 10 bold'), bg='steel blue',command=connection1)
submitbutton1.configure(height=1, width=9)
submitbutton1.grid(row=0,column=2,rowspan=1) 


        

#submitbutton2=Button(top_frame, text='Submit', font=('Times 26 bold'), bg='azure2',command=display_text)
#submitbutton2.grid(row=1, column=2)

#submitbutton3=Button(top_frame, text='Submit', font=('Times 26 bold'), bg='azure2',command=display_text)
#submitbutton3.grid(row=2, column=2)


g = {'A1':button1,'B1':button2,'C1':button3,'A2':button4,'B2':button5,'C2':button6,'A3':button7,'B3':button8,'C3':button9}


def opponent_turn():
    global clientTurn,g,grid
    if clientTurn==0:
        clientTurn=1
        print("Hey")
        master.update()
        turn_label['text']="Your Turn"
        string2=connectionSocket.recv(1024)
        string2=string2.decode('utf-8')
        k=g[string2]
        k["text"]="O"
        k['state']= tk.DISABLED
                #p1.updateGameBoard(string2,"O")
                #y=p1.set_lastplayer("player 2")
        grid[string2]="O"
        #p=p1.isWinner(list(grid.values()))
        if p2.isWinner(list(grid.values())) :
            p1.losses+=1
            sendWinner('O-Winner',g)
            rmatch['state']=tk.NORMAL




def rematch():
    global g,grid,games_played1
    p1.resetGameBoard(g)
    games_played1+=1
    winner_label['text']='Game In Progress'
    turn_label['text']='Your Turn'
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
    msg='Play Again'
    connectionSocket.send(msg.encode('ascii'))
    global clientTurn
    clientTurn = 1
    global counter
    counter = 0
    rmatch['state']=DISABLED
    grid = {'A1':' ','B1':' ','C1':' ','A2':' ','B2':' ','C2':' ','A3':' ','B3':' ','C3':' '}
    g = {'A1':button1,'B1':button2,'C1':button3,'A2':button4,'B2':button5,'C2':button6,'A3':button7,'B3':button8,'C3':button9}


games_won=tk.IntVar()
games_lost=tk.IntVar()
games_tie=tk.IntVar()




def showstats():
    global right_frame,connectionSocket
    msg="Game Over"
    connectionSocket.send(msg.encode('ascii'))
    stats=p1.printStats()
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
    
quitbtn=tk.Button(top_frame, text="SHOW STATISTICS", font=('Times 10 bold'), bg='steel blue',command=showstats)
quitbtn.configure(height=1,width=20)
quitbtn.grid(row=2,column=2)
                     










#Taking the IP address and the port number from the user for connection
'''def connection_credentials():
    serverAddress = input('Enter the server IP address: ')
    serverPort = int(input('Enter the port number: '))
    return serverAddress,serverPort'''

master.mainloop()


'''
p1=BoardClass('X')
rematch=True
while rematch == True:
    p1.updateGamesPlayed()
    print('TIC TAC TOE GAME')
    while p1.isWinner('X')==False and p1.boardIsFull()==False and p1.isWinner('O')==False:
        p1.draw_gameboard()
        while True:
            position=input('Enter the position to place the pawn in: ')
            if p1.updateGameBoard(position,'X')==True:
                break
        p1.draw_gameboard()
        grid_value=position.encode('ascii')
        connectionSocket.send(grid_value)
        p1.set_lastplayer(username)
        if p1.isWinner("X")==False and p1.boardIsFull()==False:
            print('Waiting for Player2') 
            string2=connectionSocket.recv(1024)
            string2=string2.decode('ascii')
            p1.updateGameBoard(string2,'O')
            p1.set_lastplayer("Player 2")
    #End game messages
    if p1.isWinner("X") == True:
        print(f'Congratulations, you won!')
        p1.wins+=1
    elif p1.isWinner('O')==True:
        print(f'Sorry, Player2 won.')
        p1.losses+=1
    elif p1.boardIsFull() == True:
        print(f"It's a draw!")
        p1.ties+=1

    # Asking for a rematch 
    host_response = input(f'Do you want to have a rematch? (Y for yes/N for no): ')
    if host_response == 'N' or host_response =='n':
        connectionSocket.send(b'Fun times')
        rematch = False
    elif host_response == 'Y' or host_response =='y':
        connectionSocket.send(b'Play Again')
        p1.resetGameBoard()
        
#Printing Statistics for Player 1
print('Thank you for playing!')
print('Here are your stats')
print('Username: ',username)
print("Opponent's Username: Player2")
p1.printStats()
connectionSocket.close()'''


