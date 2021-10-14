#cuberoot, integrals, matrix, square, cube

from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="Powder blue")
root.resizable(W=False, H=False)
root.geometry("480x624+20+20")

"""roott=TK()
roott.title("Conversion")
roott.configure(background="Gray")
roott.resizable(W=False, H=False)
roott.geometry("944x624+20+20")
"""
calc = Frame(root)
calc.grid()


#=============Functions==================================================================================================
#to be added

#================Display================================================================================================


text = Entry(calc, relief=SUNKEN, font=('arial', 20, 'bold'), bg="powder blue", bd=30, W=28, justify=RIGHT)
text.grid(row=0, column=0, columnspan=4, pady=1)
text.insert(0, "0")

#==================Numbers==============================================================================================

numberpad = "789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, W=6, H=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: added_value.numberEnter(x)
        i+=1

#========================Standard Function==============================================================================================================================================

btnSq=Button(calc, text="√", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=added_value.Square).grid(row=1, column=2, pady=1)
btnAdd=Button(calc, text="+", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=lambda:added_value.operation("add")).grid(row=1, column=3, pady=1)

btnClear=Button(calc, text=chr(67), W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)
btnAllClear=Button(calc, text=chr(67)+chr(69), W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)

btnSub=Button(calc, text="-", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=lambda:added_value.operation("sub")).grid(row=2, column=3, pady=1)
btnMult=Button(calc, text="×", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=lambda:added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv=Button(calc, text=chr(247), W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=lambda:added_value.operation("divide")).grid(row=4, column=3, pady=1)
btnZero=Button(calc, text="0", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=lambda:added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

btnEquals=Button(calc, text="=", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=added_value.Sum_of_total).grid(row=5, column=3, pady=1)

btnDot=Button(calc, text=".", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=lambda:added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
btnPM=Button(calc, text=chr(177), W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=added_value.mathsPM).grid(row=5, column=2, pady=1)

#===================Scientific Calculator====================================================================================================================================================

btnTan=Button(calc, text="Tan", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.Tan).grid(row=1, column=6, pady=1)
btnSin=Button(calc, text="Sin", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.Sin).grid(row=1, column=7, pady=1)

btnPi=Button(calc, text='π', W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.PI).grid(row=1, column=4, pady=1)
btnCos=Button(calc, text="Cos", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.Cos).grid(row=1, column=5, pady=1)

btnTanh=Button(calc, text="Tanh", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.Tanh).grid(row=2, column=6, pady=1)
btnSinh=Button(calc, text="Sinh", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.Sinh).grid(row=2, column=7, pady=1)

btnLog=Button(calc, text='log', W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log).grid(row=3, column=4, pady=1)
btninv=Button(calc, text="Inv", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=lambda:added_value.operation("inv")).grid(row=3, column=5, pady=1)

btnMod=Button(calc, text="Mod", W=6, H=2, font=('arial', 20, 'bold'), bd=4, command=lambda:added_value.operation("mod")).grid(row=3, column=6, pady=1)
btnE=Button(calc, text="e", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.e).grid(row=3, column=7, pady=1)

btnLog2=Button(calc, text='log2', W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log2).grid(row=4, column=4, pady=1)
btnDeg=Button(calc, text="deg", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.deg).grid(row=4, column=5, pady=1)

btnACosh=Button(calc, text="aCosh", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.aCosh).grid(row=4, column=6, pady=1)
btnASinh=Button(calc, text="aSinh", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.aSinh).grid(row=4, column=7, pady=1)

btn2Pi=Button(calc, text='2π', W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.Tau).grid(row=2, column=4, pady=1)
btnCosh=Button(calc, text="Cosh", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.Cosh).grid(row=2, column=5, pady=1)

btnLog10=Button(calc, text='log10', W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log10).grid(row=5, column=4, pady=1)
btnLog1p=Button(calc, text="log1p", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log1p).grid(row=5, column=5, pady=1)

btnExpm1=Button(calc, text="expm1", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.expm1).grid(row=5, column=6, pady=1)
btnLgamma=Button(calc, text="lgamma", W=6, H=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.lgamma).grid(row=5, column=7, pady=1)

#===============================Display Text======================================================================================================================================

lblDisplay=Label(calc, text="Scientific Calculator", font=('arial', 30, 'bold'), justify =CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)

lblDisplay=Label(calc, text="Program Warehouse", font=('arial', 30, 'bold'), justify =CENTER)
lblDisplay.grid(row=6, column=0, columnspan=4)


                   
#=======================Menu and function===========================================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit>0:
        root.destroy()
        return

def Scientific():
    root.resizable(W=False, H=False)
    root.geometry("944x624+20+20")

def Standard():
    root.resizable(W=False, H=False)
    root.geometry("480x624+20+20")
"""
def Volume():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Length():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")
    
def W_M():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Temp():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Energy():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Area():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Speed():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Time():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Power():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Data():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Pressure():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")

def Angle():
    roott.resizable(W=False, H=False)
    roott.geometry("944x624+20+20")
"""


menubar = Menu(calc)


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standadrd", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

"""
conversionmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Converter", menu=conversionmenu)
conversionmenu.add_command(label = "Volume", command=Volume)
conversionmenu.add_command(label = "Length", command=Length)
conversionmenu.add_command(label = "Weight and Mass", command=W_M)
conversionmenu.add_command(label = "Temperature", command=Temp)
conversionmenu.add_command(label = "Energy", command=Energy)
conversionmenu.add_command(label = "Area", command=Area)
conversionmenu.add_command(label = "Speed", command=Speed)
conversionmenu.add_command(label = "Time", command=Time)
conversionmenu.add_command(label = "Power", command=Power)
conversionmenu.add_command(label = "Data", command=Data)
conversionmenu.add_command(label = "Pressure", command=Pressure)
conversionmenu.add_command(label = "Angle", command=Angle)

"""

"""editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label = "View Help")
"""

#====================Main Loop=============================================================================

root.config(menu=menubar)
root.mainloop()
