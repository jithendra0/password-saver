import tkinter
from tkinter import *
from tkinter import messagebox
import random
import math 
GREEN = "#b3ff99"

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spl_chars = [ '@', '#', '$', '&', '(', ')', '!', '?', '/', '{','}', '[', ']', '<', '¥', 'π', '£', '¢', '€', '^', '¶']

    #-3rd part--password generation #
 

def gen_pass( ):
	no_of_C_letters = random.randint(5,12)
	no_of_S_letters = random.randint(6,10)
	no_of_symbols = random.randint(5,10)
	pass_C_letters = [random. choice(cap_letters) for _ in range(no_of_C_letters)]
	pass_S_letters = [random. choice(lower_letters) for _ in range(no_of_S_letters)]
	pass_symbols = [random.choice(spl_chars) for _ in range(no_of_symbols)]
	Pre_final_pass = pass_C_letters + pass_S_letters + pass_symbols
	random.shuffle(Pre_final_pass)
	Final_pass = ""
	for char in Pre_final_pass:
	   Final_pass += char 
	pass_input.insert(0,Final_pass)       	 
     
# or you can use join method
# arraydata = any data - list- dict-tuple
#   x = ""join(arraydata)
# print(x)
       

   #---2nd part---functon to add data--#

def data( ):
	website    = web_input.get( )
	email        = email_input.get( )
	password = pass_input.get( )
	
	if len(password)==0 or len(email)==0 or len(website) == 0:
		 messagebox.showwarning(title = "warning", message = " dont left empty fields")
	else :
		messagebox.askokcancel(title = website, message = f"these details are entered \n email : {email} \n password : {password} ")
		with open("data.txt","a") as file:
			     file.write(f"{website} | { email } | {password} \n")
			     web_input.delete(0,END)
			     pass_input.delete(0,END)
	
        # -----1 ST PART.------UI ----------#

#window creation

window = tkinter.Tk( )
window.config(padx = 550,pady= 80)

#canvas creation

canvas = tkinter.Canvas(width = 256,height = 256)
   
#insert image
lock = tkinter.PhotoImage(file ="unlock.png")
canvas.create_image(128,128,image = lock)
canvas.grid(column = 1,row = 0,pady = 30,sticky = E)
#sticky E means East, west,north,south etc.

#Label creation
     
     
#website Label 

web_label = tkinter.Label(text= "website :  ",font = ("times",6,"bold"))
web_label.grid(column=0,row = 1,sticky = E)
web_label.config(pady= 20)

#website input box

web_input = tkinter.Entry(width = 35)
web_input.grid(column= 1, row = 1,columnspan = 2)


#email label

email_label = tkinter.Label(text = "Email :  ",font=("times",6,"bold"))
email_label.grid(column = 0, row =2,sticky = E)
email_label.config(pady= 20)


# email input box

email_input = tkinter.Entry(width = 35)
email_input.grid(column = 1, row = 2,columnspan = 2) 
email_input.insert(0,"@gmail.com")


# password label

pass_label = tkinter.Label(text = "Password :  ",font=("times",6,"bold"))
pass_label.grid(column = 0, row = 3,sticky = E)


# password input box

pass_input = tkinter.Entry(width = 16)
pass_input.grid(column = 1, row = 3)


# password generate button

pass_button = tkinter.Button(text = "Generate Password",command = gen_pass)
pass_button.grid(column = 2, row = 3)


# add to file button

Add = tkinter.Button(text = "Add",width = 31,command = data)
Add.grid(column = 1, row = 4,columnspan = 2)


    #----------stay on mode forever-------#
window.mainloop( )