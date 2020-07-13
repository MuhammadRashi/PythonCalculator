from tkinter import *
from tkinter import font as tkFont

mainFrame=Tk()
# boldStyle=mainFrame.style()
mainFrame.title("My Calculator")
mainFrame.geometry("250x400")
mainFrame.config(bg="dark gray")
textStyle = tkFont.Font(family='Malgun Gothic', size=15, weight=tkFont.BOLD)
entryBox=Entry(mainFrame,width=17,borderwidth=5,font=textStyle)
# entryBox=Text(mainFrame,width=26,height=2,borderwidth=5,font=textStyle)
entryBox.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#entryBox.insert(0,"Your result here")
val=""
fnumber=0
def numButtonClick(number):
    temp=entryBox.get()
    if temp=="+" or temp=="-":
        print("temp"+temp)
        entryBox.delete(0,END)
    val=entryBox.get()  #get data from Entry box
    val=str(val)+str(number) # congantinate tentry box and new entered value
    entryBox.delete(0,END)  # delete data from Entry Box

    entryBox.insert(0,val) #insert data from val to entryBox
def oppButtonClick(operator):
    global fnumber
    global oprt
    global result

    if operator =="+":
        fnumber = entryBox.get()
        oprt=operator
        entryBox.delete(0,END)
        entryBox.insert(0,oprt)
        print("fnumber"+fnumber)
        print("Oprt"+oprt)
    elif operator=="=":
        if oprt=="+":

            result=int(fnumber)+int(entryBox.get()) #+int(entryBox.get())
            entryBox.delete(0,END)
            entryBox.insert(0,result)



    # if operator == "=":         #-----call operator overloading
    #     if oprt=="+":
    #         result = int(fnumber) + int(entryBox.get())
    #         entryBox.delete(0, END)
    #         entryBox.insert(0, result)
    #     elif oprt=="-":
    #         result = int(fnumber) - int(entryBox.get())
    #         entryBox.delete(0, END)
    #         entryBox.insert(0, result)
    # else:
    #     fnumber = entryBox.get()
    #     print("fnumber"+fnumber)
    #     oprt = operator
    #     entryBox.delete(0, END)
    #     entryBox.insert(0,oprt)

        # entryBox.insert(0,result)
    # fnumber = entryBox.get()
    # if operator != "=":
    #     oprt=operator
    # if operator=="=":
    #     if oprt== "+":
    #         result=fnumber+entryBox.get()
    #
    #
    # # val = str(fnumber) + str(operator)
    # entryBox.delete(0, END)
    # entryBox.insert(0, result)

# button style

buttonStyle = tkFont.Font(family='Arial Narrow', size=12, weight=tkFont.BOLD)

#Define number buttons  -- lambda used for pass argument to function
button_1=Button(mainFrame,text="1",padx=30,pady=11, command=lambda: numButtonClick(1),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_2=Button(mainFrame,text="2",padx=30,pady=11, command=lambda: numButtonClick(2),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_3=Button(mainFrame,text="3",padx=30,pady=11, command=lambda: numButtonClick(3),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_4=Button(mainFrame,text="4",padx=30,pady=11, command=lambda: numButtonClick(4),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_5=Button(mainFrame,text="5",padx=30,pady=11, command=lambda: numButtonClick(5),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_6=Button(mainFrame,text="6",padx=30,pady=11, command=lambda: numButtonClick(6),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_7=Button(mainFrame,text="7",padx=30,pady=11, command=lambda: numButtonClick(7),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_8=Button(mainFrame,text="8",padx=30,pady=11, command=lambda: numButtonClick(8),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_9=Button(mainFrame,text="9",padx=30,pady=11, command=lambda: numButtonClick(9),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_0=Button(mainFrame,text="0",padx=30,pady=11, command=lambda: numButtonClick(0),borderwidth="2",bg="gray",fg="white",font=buttonStyle)


# Display numbers button to screen

button_1.grid(row=3,column=0,pady=5,padx=3)
button_2.grid(row=3,column=1,pady=5,padx=3)
button_3.grid(row=3,column=2,pady=5,padx=3)

button_4.grid(row=2,column=0,pady=5,padx=3)
button_5.grid(row=2,column=1,pady=5,padx=3)
button_6.grid(row=2,column=2,pady=5,padx=3)

button_7.grid(row=1,column=0,pady=5,padx=3)
button_8.grid(row=1,column=1,pady=5,padx=3)
button_9.grid(row=1,column=2,pady=5,padx=3)
button_0.grid(row=4,column=0,pady=5,padx=3)


# Define Operator Buttons
button_A=Button(mainFrame,text="+",padx=30,pady=11, command=lambda: oppButtonClick("+"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_S=Button(mainFrame,text="-",padx=30,pady=11, command=lambda: oppButtonClick("-"),borderwidth="2",bg="gray",fg="white",font=buttonStyle)
button_E=Button(mainFrame,text="=",padx=30,pady=11, command=lambda: oppButtonClick("="),borderwidth="2",bg="gray",fg="white",font=buttonStyle)

#Display Operators to screen
button_A.grid(row=4,column=1,pady=5,padx=3)
button_S.grid(row=4,column=2,pady=5,padx=3)
button_E.grid(row=5,column=0,pady=5,padx=3)

mainFrame.mainloop()