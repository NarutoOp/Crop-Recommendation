import tkinter as tk
from tkinter import font
from b import *

def test_function():
	
	a = OptionList[variable.get()]
	b = OptionList1[variable1.get()]

	z = variable.get()

	
	label['text'] = pre(a,b,z) 


root = tk.Tk()

canvas = tk.Canvas(root,height='500',width='600')
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

label1 = tk.Label(root,text="Crop Recommendation System",bg = '#99ffcc', font=('Helvetica',15), fg='red',bd=5)
label1.place(relx=0.15,rely=0.02,relwidth=0.7,relheight=0.06)



frame = tk.Frame(root, bg = '#80c1ff',bd=5)
frame.place(relx=0.5, rely=0.1,relwidth=0.75,relheight=0.1, anchor='n')

#dropdown
OptionList = {
'Aandhra Pradesh': '0',
 'Arunachal Pradesh' : '1',
 'Assam' : '2',
 'Bihar' : '3',
 'Chattisgarh' : '4',
 'Goa' : '5',
 'Gujarat' : '6',
 'Haryana' : '7',
 'Himachal Pradesh' : '8',
 'Jammu and Kashmir' : '9',
 'Himachal Pradesh' : '10',
 'Jharkhand' : '11',
 'Karnataka' : '12',
 'Kerala' : '13',
 'Madhaya Pradesh' : '14',
 'Maharashtra' : '15',
 'Manipur' : '16',
 'Mizoram' : '17',
 'Meghalaya' : '18',
 'Nagaland' : '19',
 'Odisha' : '20',
 'Punjab' : '21',
 'Rajasthan' : '22',
 'Sikkim' : '23',
 'Tamil Nadu' : '24',
 'Telangana' : '25',
 'Tripura' : '26',
 'Uttar Pradesh' : '27',
 'Uttarakhand' : '28',
 'West Bengal':'29'
}

variable = tk.StringVar(frame)
variable.set("Location")

opt = tk.OptionMenu(frame, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))
    # return variable.get()

variable.trace("w", callback)

frame1 = tk.Frame(root, bg = '#80c1ff',bd=5)
frame1.place(relx=0.5, rely=0.25,relwidth=0.75,relheight=0.1, anchor='n')

OptionList1 = {
'Alluvial' : '0',
'Black': '1',
'Desert': '2',
'Laterite':'3',
'Mountain':'4',
'Red':'5'
}

variable1 = tk.StringVar(frame1)
variable1.set('Soil')

opt1 = tk.OptionMenu(frame1, variable1, *OptionList1)
opt1.config(width=90, font=('Helvetica', 12))
opt1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

labelTest1 = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest1.pack(side="top")

button = tk.Button(root,text="Submit",font=40,command=lambda: test_function())
button.place(relx=0.36,rely=0.4,relheight=0.07,relwidth=0.3)

lower_frame =tk.Frame(root,bg='#80c1ff',bd =10)
lower_frame.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.4,anchor='n')

label = tk.Label(lower_frame,font=('Courier','14'),anchor = 'nw',justify = 'left',bd=4)
label.place(relwidth=1,relheight=1)
# start the GUI 
root.mainloop() 
