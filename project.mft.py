from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from random import randint

master1 = Tk()
master1.geometry('350x500')
master1.title('Start')
master1.resizable(0,0)

j=0
r=0

for i in range(100):
    Frame(master1,width=10,height=500,bg='darkorange').place(x=j , y=0)
    j=j+10
    r=r+1
Frame(master1,width=250,height=400,bg='white').place(x=50,y=50)

l1=Label(master1,text='First name',bg='white')
l=('consolas',13)
l1.config(font=1)
l1.place(x=80,y=180)
e1=Entry(master1, width=20,border=0)
e1.config(font=1)
e1.place(x=70,y=210)

l2=Label(master1,text='Last name',bg='white')
l=('consolas',13)
l2.config(font=1)
l2.place(x=80,y=250)
e2=Entry(master1, width=20,border=0)
e2.config(font=1)
e2.place(x=70,y=280)

l3=Label(master1,text='Code',bg='white')
l=('consolas',13)
l3.config(font=1)
l3.place(x=80,y=320)
e3=Entry(master1, width=20,border=0)
e3.config(font=1)
e3.place(x=70,y=350)

Frame(master1,width=180,height=2,bg='darkorange').place(x=80,y=230)
Frame(master1,width=180,height=2,bg='darkorange').place(x=80,y=300)
Frame(master1,width=180,height=2,bg='darkorange').place(x=80,y=370)


from PIL import ImageTk,Image

image1=Image.open("C:\\Users\\Kiana\\Desktop\\k.png")
image2=ImageTk.PhotoImage(image1)

label1=Label(image=image2,border=0,justify=CENTER)
label1.place(x=100,y=50)

def cmd():
    if e1.get() and e2.get() and e3.get() :
        messagebox.showinfo("LOGIN SUCCESSFULLY","     WELCOME     ")
        #========================================================================
        def game1():
            
            window = Tk()
            window.geometry('350x500')
            window.title('Game 1')
            window.resizable(0,0)

            j=0
            r=0

            for i in range(100):
                Frame(window,width=10,height=500,bg='darkorange').place(x=j , y=0)
                j=j+10
                r=r+1
            Frame(window,width=250,height=400,bg='white').place(x=50,y=50)
            global turn , results, player_point
            turn = "X"
            results=["" , "" , "" , "" , "" , "" , "" , "" , ""]
            player_point = [0 , 0]
            def clicked(btn):
                global turn
                btn=int(btn)
                if results[btn] == "":
                    if turn =="X":
                        results[btn] = "X"
                        buttons[btn]["bg"]="yellow"
                        buttons[btn]["fg"]="black"
                        buttons[btn]["text"]="X"
                        #button[btn]['state']=DISABLED
                        turn = "O"
                    else:
                        results[btn] = "O"
                        buttons[btn]["bg"]="green"
                        buttons[btn]["fg"]="black"
                        buttons[btn]["text"]="O"
                        #button[btn]['state']=DISABLED
                        turn = "X"
                rule()
                print(results)

            def rule():
                if (results[0]==results[1]==results[2] and results[0]!=""
                    or results[3]==results[4]==results[5] and results[3]!=""
                    or results[6]==results[7]==results[8] and results[6]!=""
                    or results[0]==results[3]==results[6] and results[0]!=""
                    or results[1]==results[4]==results[7] and results[1]!=""
                    or results[2]==results[5]==results[8] and results[2]!=""
                    or results[0]==results[4]==results[8] and results[0]!=""
                    or results[2]==results[4]==results[6] and results[2]!=""):
                    show_winner(results[0])
                else:
                    check_draw()
            def show_winner(winner):
                if winner == "X":
                    player_point[0]+=1
                    showinfo("finished" , "user1 won!")
                    print(player_point)
                    reset()
                else:
                    player_point[1]+=1
                    showinfo("finished" , "user2 won!")
                    print(player_point)
                    reset()
            def reset():
                global results, turn
                results = ["" , "" , "" , "" , "" , "" , "" , "" , ""]
                turn = "X"
                point()
                board()

            def check_draw():
                if "" not in results:
                    showinfo("finish","tie!")
                    reset()

            def point():
                global points
                board_frame = Frame(window)
                board_frame.grid(row=0)
                label_user1 = Label(board_frame,text='User 1',font=("arial",10),padx=10)
                label_user2 = Label(board_frame,text='User 2',font=("arial",10),padx=10)
                label_user1.grid(row=3 , column=3)
                label_user2.grid(row=3 , column=4)

                point_frame = Frame(window)
                point_frame.grid(row=1)
                point_user1 = Label(point_frame, text=player_point[0],padx=10,font=("arial",12))
                point_user2 = Label(point_frame, text=player_point[1],padx=10,font=("arial",12))
                point_user1.grid(row=0,column=0)
                point_user2.grid(row=0,column=1)

            def board():
                global buttons
                buttons = []
                counter = 0
                board_frame = Frame(window)
                board_frame.grid(row=2)
                for row in range (1,4):
                    for column in range (1,4):
                        index = counter
                        buttons.append(index)
                        buttons[index]=Button(board_frame, command=lambda x=f"{index}": clicked(x))
                        buttons[index].config(width=14,height=4,font=("arial",10,"bold"))
                        buttons[index].grid(row=row , column=column)
                        counter+=1

            tictactoe=Label(window,
                     text="tic tac toe",
                     font=('Ink Free',30,'bold'),
                     fg='darkorange',
                     bg='white')
            tictactoe.place(x=75,y=350)


            point()
            board()
            window.mainloop()




        def game2():
            win = Tk()

            select ={
                1:"Stone",
                2:"Scissors",
                3:"Paper"
                }

            def stone():
                comp=randint(1,3)
                lb1["text"] = "Computer choice : "+select[comp]
                if comp==2:
                    lblresultuser["text"] = int(lblresultuser["text"])+1
                elif comp==3:
                    lblresultcomputer["text"] = int(lblresultcomputer["text"])+1

            def scissors():
                comp=randint(1,3)
                lb1["text"] = "Computer choice : "+select[comp]
                if comp==3:
                    lblresultuser["text"] = int(lblresultuser["text"])+1
                elif comp==1:
                    lblresultcomputer["text"] = int(lblresultcomputer["text"])+1

            def paper():
                comp=randint(1,3)
                lb1["text"] = "Computer choice : "+select[comp]
                if comp==1:
                    lblresultuser["text"] = int(lblresultuser["text"])+1
                elif comp==2:
                    lblresultcomputer["text"] = int(lblresultcomputer["text"])+1

            def reset():
                 lblresultuser["text"] = 0
                 lblresultcomputer["text"] = 0
                 lb1["text"] = "Choose"

            win.geometry('350x500')
            win.title('Game 2')
            win.resizable(0,0)
            win.rowconfigure([0,1],weight=1)
            win.columnconfigure(0,weight=1)
            j=0
            r=0

            for i in range(100):
                Frame(win,width=10,height=500,bg='darkorange').place(x=j , y=0)
                j=j+10
                r=r+1
            Frame(win,width=250,height=400,bg='darkorange').place(x=50,y=50)

            lb1=Label(master=win,text="Choose",bg ="darkorange",height=2,font=("arial",18,"bold"))
            lb1.grid(row=0,column=0,sticky="nwe")
            frmbtn=Frame(master=win,height=100,bg="orange")

            frmbtn.rowconfigure(0, weight=1)
            frmbtn.columnconfigure([0,1,2], weight=1)

            stonebtn=Button(master=frmbtn,text="Stone",height=4,font=("arial",12,"bold"),command=stone).grid(row=0,column=0,sticky="nwes",padx=2,pady=3)
            paperbtn=Button(master=frmbtn,text="Paper",height=4,font=("arial",12,"bold"),command=paper).grid(row=0,column=1,sticky="nwes",padx=2,pady=3)
            scissorsbtn=Button(master=frmbtn,text="Scissors",height=4,font=("arial",12,"bold"),command=scissors).grid(row=0,column=2,sticky="nwes",padx=2,pady=3)

            frmbtn.grid(row=1,column=0,sticky="wen")

            frmresult=Frame(master=win,height=200,bg="darkorange")
            frmresult.rowconfigure([0,1],weight=1)
            frmresult.columnconfigure([0,1],weight=1)
            lblresultnameuser=Label(master=frmresult,text="    user    ",height=4,relief="ridge",font=("arial",12,"bold")).grid(row=0,column=0,sticky="nswe")
            lblresultnamecomputer=Label(master=frmresult,text="computer",height=4,relief="ridge",font=("arial",12,"bold")).grid(row=0,column=1,sticky="nswe")

            lblresultuser=Label(master=frmresult,text="0",height=6,fg="darkorange",bg="white",font=("arial",20,"bold"))
            lblresultuser.grid(row=1,column=0,sticky="nswe")
            lblresultcomputer=Label(master=frmresult,text="0",height=6,fg="darkorange",bg="white",font=("arial",20,"bold"))
            lblresultcomputer.grid(row=1,column=1,sticky="nswe")

            frmresult.grid(row=2,column=0,sticky="nswe")

            btnreset=Button(master=win,text="Reset",font=("arial",12,"bold"),border=4,relief="ridge",command=reset).grid(row=3,column=0,sticky="nswe")

            win.mainloop()












        q = Tk()
        q.geometry('350x500')
        q.title('Game')
        q.resizable(0,0)
        j=0
        r=0

        for i in range(100):
            Frame(q,width=10,height=500,bg='darkorange').place(x=j , y=0)
            j=j+10
            r=r+1
        Frame(q,width=250,height=400,bg='white').place(x=50,y=50)
        text=Label(q,
                 text="Game",
                 font=('Ink Free',60,'bold'),
                 fg='darkorange',
                 bg='white')
        text.place(x=75,y=70)


        Button(q,width=20,height=2,fg="white",bg="darkorange",border=0,command=game1,text="Game 1").place(x=100,y=300)
        Button(q,width=20,height=2,fg="white",bg="darkorange",border=0,command=game2,text="Game 2").place(x=100,y=350)

        q.mainloop()
        #========================================================================
    else:
        messagebox.showinfo("LOGIN FAILED","     PLEASE TRY AGAIN     ")

Button(master1,width=20,height=2,fg="white",bg="darkorange",border=0,command=cmd,text="S T A R T").place(x=100,y=400)
master1.mainloop()



#--------------------------------------------------------------



