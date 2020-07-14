from tkinter import *
from tkinter import font as tkFont

mainFrame=Tk()

mainFrame.title("My Calculator")
mainFrame.geometry("390x340")
mainFrame.config(bg="gray18")
# Heading----
# Style define
textStyle = tkFont.Font(family='Malgun Gothic', size=15, weight=tkFont.BOLD)
nameStyle = tkFont.Font(family='Agency FB', size=12, weight=tkFont.BOLD)
buttonStyle = tkFont.Font(family='Arial Narrow', size=12, weight=tkFont.BOLD)
# Define and display Heading part
entryBox=Entry(mainFrame,width=30,borderwidth=5,font=textStyle,bg="gray60",justify='right')
caName=Label(mainFrame,width=6,border=1,text="CASIO",bg="gray18",fg="white",font=nameStyle)
caSolar=Label(mainFrame,width=15,border=4,bg="brown4")
caModel=Label(mainFrame,width=10,border=1,text="MJ-12Da",bg="gray18",fg="white")
caName.grid(row=2,column=0,pady=8)
caSolar.grid(row=2,columnspan=6,pady=4)
caModel.grid(row=2,column=4,pady=4)
entryBox.grid(row=3,column=0,columnspan=8,padx=10,pady=2)


val=""
fnumber=0
# Number button click function
def numButtonClick(number):
    temp=entryBox.get()
    if temp=="+" or temp=="-" or temp=="x" or temp=="*" or temp=="/":
        entryBox.delete(0,END)
    val=entryBox.get()  #get data from Entry box
    val=str(val)+str(number)
    entryBox.delete(0,END)  # delete data from Entry Box
    entryBox.insert(0,val) #insert data from val to entryBox

# Operator button click
def oppButtonClick(operator):
    global fnumber
    global oprt
    global result

    if operator=="=":
        if oprt=="+":
            result=int(fnumber)+int(entryBox.get())
            entryBox.delete(0,END)
            entryBox.insert(0,result)
        elif oprt=="-":
            result = int(fnumber) - int(entryBox.get())
            entryBox.delete(0, END)
            entryBox.insert(0, result)
        elif oprt=="x":
            result = int(fnumber) * int(entryBox.get())
            entryBox.delete(0, END)
            entryBox.insert(0, result)
        elif oprt=="/":
            result = int(fnumber)/int(entryBox.get())
            result=int(result)
            entryBox.delete(0, END)
            entryBox.insert(0, result)
    elif operator=="C":
        entryBox.delete(0,END)
        result=0
    else:
        fnumber = entryBox.get()
        oprt=operator
        entryBox.delete(0,END)
        entryBox.insert(0,oprt)

#Define number buttons  -- lambda used for pass argument to function
button_1=Button(mainFrame,text="1",padx=22,pady=10, command=lambda: numButtonClick(11),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_2=Button(mainFrame,text="2",padx=22,pady=10, command=lambda: numButtonClick(2),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_3=Button(mainFrame,text="3",padx=22,pady=10, command=lambda: numButtonClick(3),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_4=Button(mainFrame,text="4",padx=22,pady=10, command=lambda: numButtonClick(4),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_5=Button(mainFrame,text="5",padx=22,pady=10, command=lambda: numButtonClick(5),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_6=Button(mainFrame,text="6",padx=22,pady=10, command=lambda: numButtonClick(6),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_7=Button(mainFrame,text="7",padx=22,pady=10, command=lambda: numButtonClick(7),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_8=Button(mainFrame,text="8",padx=22,pady=10, command=lambda: numButtonClick(8),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_9=Button(mainFrame,text="9",padx=22,pady=10, command=lambda: numButtonClick(9),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_0=Button(mainFrame,text="0",padx=22,pady=10, command=lambda: numButtonClick(0),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_00=Button(mainFrame,text="00",padx=20,pady=10, command=lambda: numButtonClick("00"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_000=Button(mainFrame,text="000",padx=16,pady=10, command=lambda: numButtonClick("000"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)

# Display numbers button to screen
button_1.grid(row=6,column=0,pady=5,padx=3)
button_2.grid(row=6,column=1,pady=5,padx=3)
button_3.grid(row=6,column=2,pady=5,padx=3)

button_4.grid(row=5,column=0,pady=5,padx=3)
button_5.grid(row=5,column=1,pady=5,padx=3)
button_6.grid(row=5,column=2,pady=5,padx=3)

button_7.grid(row=4,column=0,pady=5,padx=12)
button_8.grid(row=4,column=1,pady=5,padx=5)
button_9.grid(row=4,column=2,pady=5,padx=5)

button_0.grid(row=7,column=0,pady=5,padx=3)
button_00.grid(row=7,column=1,pady=5,padx=3)
button_000.grid(row=7,column=2,pady=5,padx=3)

# Define Operator Buttons
button_A=Button(mainFrame,text="+",padx=22,pady=42, command=lambda: oppButtonClick("+"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_S=Button(mainFrame,text="-",padx=22,pady=10, command=lambda: oppButtonClick("-"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_E=Button(mainFrame,text="=",padx=22,pady=42, command=lambda: oppButtonClick("="),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_M=Button(mainFrame,text="x",padx=22,pady=10, command=lambda: oppButtonClick("x"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_D=Button(mainFrame,text="/",padx=22,pady=10, command=lambda: oppButtonClick("/"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_C=Button(mainFrame,text="C",padx=20,pady=10, command=lambda: oppButtonClick("C"),borderwidth="2",bg="red",fg="white",font=buttonStyle)

#Display Operators to screen
button_A.grid(row=6,column=3,rowspan=2,pady=5,padx=3)
button_S.grid(row=5,column=4,pady=5,padx=3)
button_E.grid(row=6,column=4,rowspan=2,pady=5,padx=3)
button_M.grid(row=5,column=3,pady=5,padx=3)
button_D.grid(row=4,column=3,pady=5,padx=3)
button_C.grid(row=4,column=4,pady=5,padx=3)
mainFrame.mainloop()