# tkinter module
# import tkinter

from tkinter import *
# call the object
window = Tk()
# bring the title
window.title("myfirst_gui")

# make the function for submit button.
def click():
    enter_text = str(textbox.get())
    output.delete(0.0,END)

    #exception handling
    try:
        define = my_dict[enter_text]
    except:
        define = 'not available'
    output.insert(END,define)






# creating the label
Label(window,text="Hello I am from python",bg='red',fg='white').grid(row=0,column=0,sticky=W)

# text box
textbox = Entry(window,width=50,bg='white',).grid(row=1,column=0,sticky=W)

# submit button
Button(window,text = 'SUBMIT',width=10,command = click,bg='red',fg='black').grid(row=2,column=0,sticky=W)

# label
Label(window,text = 'Defination',bg='red',fg='black',font='none 12 bold').grid(row=3,column=0,sticky=W)

# create a text box
output = Text(window,width=30,height=10,bg='white',wrap=WORD,)
output.grid(row=4,column=0,sticky=W)

# create a dict
my_dict = {
    'animal':['dog','cat'],
    'bug':'error in code'
}

window.mainloop()
