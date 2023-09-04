from tkinter import *



window = Tk()
window.geometry("350x500") #diemnsion of the calci
window.title("Calculator") #title
window.configure(bg="#82aef5") #setting the background color
#window.iconbitmap("calculator_icon.ico")

expression = ''#empty string to store input value

#function definition for adding functionality to the buttons

def press(n):
	global expression
	expression +=str(n)
	equation.set(expression)
#function definition for addinf functionality to equal button
def equal():
	#expection handling for division by zero
	try:
		global expression
		total= str(eval(expression))
		equation.set(total)
		expression=''
	except:
		equation.set('undefined')
		expression=''

#function definition for adding functionality to clear button
def clear():
	global expression
	expression=''
	equation.set('0')

#function definition for adding functionality to backspace button
def backspace():
	global expression
	expression = expression.rstrip(expression[-1]) #rstrip function help us to retrieve the last element and delete it
	equation.set(expression)

expression_frame = Frame(window,bg="#82aef5")#creates the button
buttons_frame = Frame(window,bg="#82aef5")#creates the button
expression_frame.pack()#insert the button
buttons_frame.pack()#insert the button


font_entry = ('ariel',20,'bold')#styles for the input
font_button = ('times new roman',12)#styles for the input button
equation = StringVar()
equation.set('0')#to set a default value as 0

equation_field = Entry(expression_frame,textvariable=equation,font=font_entry,justify='right')#alignment for input
equation_field.pack(ipadx=10,ipady=10,pady=20)#ipadx-> increases horizontal size
#ipady-> increases vertical size
#pady increases the space between buttons

#creating buttons for input

button1 = Button(buttons_frame,text='1',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(1))
button2 = Button(buttons_frame,text='2',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(2))
button3 = Button(buttons_frame,text='3',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(3))
plus = Button(buttons_frame,text='+',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press('+'))
button4 = Button(buttons_frame,text='4',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(4))
button5 = Button(buttons_frame,text='5',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(5))
button6 = Button(buttons_frame,text='6',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(6))
minus = Button(buttons_frame,text='-',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press('-'))
button7 = Button(buttons_frame,text='7',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(7))
button8 = Button(buttons_frame,text='8',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(8))
button9 = Button(buttons_frame,text='9',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(9))
multiply = Button(buttons_frame,text='*',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press('*'))
button0 = Button(buttons_frame,text='0',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press(0))
decimal = Button(buttons_frame,text='.',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press('.'))
clear = Button(buttons_frame,text='C',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=clear)
divide = Button(buttons_frame,text='/',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=lambda:press('/'))
equal = Button(buttons_frame,text='=',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=equal)
backspace = Button(buttons_frame,text='<<',font=font_button,relief='raised',bg='#80bfff',borderwidth=1,
	width=8,height=3,command=backspace)

#**********rows and column should start with 0************

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
plus.grid(row=0,column=3)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
minus.grid(row=1,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
multiply.grid(row=2,column=3)

button0.grid(row=3,column=0)
decimal.grid(row=3,column=1)
clear.grid(row=3,column=2)
divide.grid(row=3,column=3)

equal.grid(row=4,column=0,columnspan=3,sticky='nsew')#columnspan=3 implies that equal button occupies space that is equal to three button space
backspace.grid(row=4,column=3)#note here we set column as 3






window.mainloop()