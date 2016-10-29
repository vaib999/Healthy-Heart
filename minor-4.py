"""# -*- coding: utf-8 -*-

Created on Mon Nov  2 23:53:30 2015

@author: Vaibhav
"""

import Tkinter
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
import tkMessageBox
import warnings
from sklearn.cross_validation import train_test_split
import ttk
from mpl_toolkits.mplot3d import axes3d,Axes3D
import matplotlib.pyplot as ppt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from matplotlib.backend_bases import key_press_handler

global a1,a2,a3,a4,a5,a6

Title="Heart Risk Calculator"
root=Tkinter.Tk()
root.title(Title)
root.geometry("300x400")
#root.configure(background="#030303")
root.resizable(width=False,height=False)

def select():
    val=var.get()
    return val
    
def risage(a1,b):
    roota=Tkinter.Tk()
    
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(5,4),dpi=100)
    a=f.add_subplot(111)
    
    small=data[:200]
    if a1==1 and b==0:
        
        dil=small["age"]
        fil=small["TenYearCHD"]
        a.set_xlabel("Age")
        roota.wm_title("Age vs. TenYearCHD")
    elif a1==2 and b==0:
        dil=small["cigsPerDay"]
        fil=small["TenYearCHD"]
        a.set_xlabel("Ciggaretes per Day")
        roota.wm_title("Cigarettes Per Day vs. TenYearCHD")
    elif a1==3 and b==0:
        dil=small["totChol"]
        fil=small["TenYearCHD"]
        a.set_xlabel("Total Cholesterol")
        roota.wm_title("Total Cholesterol vs. TenYearCHD")
    elif a1==4 and b==0:
        dil=small["sysBP"]
        fil=small["TenYearCHD"]
        a.set_xlabel("systolic blood pressure")
        roota.wm_title("SysBP vs. TenYearCHD")
    else:
        dil=small["glucose"]
        fil=small["TenYearCHD"]
        a.set_xlabel("Glucose")
        roota.wm_title("Glucose vs. TenYearCHD")
    a.scatter(dil,fil,color='blue',s=5,edgecolor='none')
    a.set_ylabel("Ten Year CHD")
    
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    
    roota.mainloop()
class Fun(Tkinter.Frame):
    def __init__(self,gen,f1,f2,f3,f4,f5,master=None):
        Tkinter.Frame.__init__(self,master)
        self.pack()
        self.lab1=Tkinter.Label(master=self,text="Age :")#.grid(row=0,column=0)
        self.lab1.pack()
        self.wage=Tkinter.Scale(master=self,orient=Tkinter.HORIZONTAL,from_=20,to=100,command=self.getValue)#.grid(row=0,column=1)
        self.wage.pack()
        self.wage.set(f1)
        self.lab2=Tkinter.Label(master=self,text="No. of cigs. :")
        self.lab2.pack()
        self.wcig=Tkinter.Scale(master=self,orient=Tkinter.HORIZONTAL,from_=0,to=70,command=self.getValue1)
        self.wcig.pack()
        self.wcig.set(f2)
        self.lab3=Tkinter.Label(master=self,text="Tot. Chol :")
        self.lab3.pack()
        self.wchol=Tkinter.Scale(master=self,orient=Tkinter.HORIZONTAL,from_=100,to=700,command=self.getValue2)
        self.wchol.pack()
        self.wchol.set(f3)
        self.lab4=Tkinter.Label(master=self,text="Systolic Blood Pressure :")
        self.lab4.pack()
        self.wsysbp=Tkinter.Scale(master=self,orient=Tkinter.HORIZONTAL,from_=80,to=300,command=self.getValue3)
        self.wsysbp.pack()
        self.wsysbp.set(f4)
        self.lab5=Tkinter.Label(master=self,text="Glucose :")
        self.lab5.pack()
        self.wglucose=Tkinter.Scale(master=self,orient=Tkinter.HORIZONTAL,from_=40,to=400,command=self.getValue4)
        self.wglucose.pack()
        self.wglucose.set(f5)
        self.v=Tkinter.StringVar()
        self.labelres=Tkinter.Label(master=self,text="Risk Factor : " )
        self.labelres.pack()
        self.gender=gen
        self.ansmain=self.analyse(self.wage.get(),self.wcig.get(),self.wchol.get(),self.wsysbp.get(),self.wglucose.get())
        
        
        #self.buttoni=ttk.Button(master=self,text="Check!!",command=lambda:self.tocalc)
        #self.buttoni.pack()        
        
        
    #def tocalc(self):
        
        #self.ansmain=self.analyse(self.wage,self)
        #self.labelres=Tkinter.Label(master=self,text="Risk Factor : " +str(self.ansmain))
        #self.labelres.pack()
        

            
    
    def getValue(self,Event):
        self.analyse(self.wage.get(),self.wcig.get(),self.wchol.get(),self.wsysbp.get(),self.wglucose.get())
        return self.wage.get()
        
    def getValue1(self,Event):
        self.analyse(self.wage.get(),self.wcig.get(),self.wchol.get(),self.wsysbp.get(),self.wglucose.get())
        return self.wcig.get()
        
    def getValue2(self,Event):
        self.analyse(self.wage.get(),self.wcig.get(),self.wchol.get(),self.wsysbp.get(),self.wglucose.get())
        return self.wchol.get()
        
    def getValue3(self,Event):
        self.analyse(self.wage.get(),self.wcig.get(),self.wchol.get(),self.wsysbp.get(),self.wglucose.get())
        return self.wsysbp.get()
        
    def getValue4(self,Event):
        self.analyse(self.wage.get(),self.wcig.get(),self.wchol.get(),self.wsysbp.get(),self.wglucose.get())
        return self.wglucose.get() 
     
    def analyse(self,p2,p3,p4,p5,p6):
        self.data=pd.read_csv("framingham.csv")
        self.data.insert(15,'intercept',1.0)
        np.random.seed(1000)
    
        self.a1=self.gender
        self.a2=p2
        self.a3=p3
        self.a4=p4
        self.a5=p5
        self.a6=p6
        #a7=(1)
        #data=[(a1,a2,a3,a4,a5,a6,a7)]
        #combos=pd.DataFrame(data,columns=['male','age','cigsPerDay','totChol','sysBP','glucose','intercept'])
       
    
        combos = pd.DataFrame({'male':[int(self.a1)],'age': [int(self.a2)],'cigsPerDay':[int(self.a3)],'totChol':[int(self.a4)],'sysBP':[int(self.a5)],'glucose':[int(self.a6)],'intercept':[1]})
        train_cols=self.data[['male','age','cigsPerDay','totChol','sysBP','glucose','intercept']]
        trainf=train_cols.columns[:]
        xx=self.data['TenYearCHD']
        logit=sm.GLM(xx,train_cols,family=sm.families.Binomial(),missing='drop')
        result=logit.fit(method="bfgs")
        combos['TenYearCHD']=result.predict(combos[trainf])
        #fb=combos.plot(kind='bar')
        self.ansmain=combos.iloc[0]['TenYearCHD']*100
        #self.v.set(str(self.ansmain))
        self.labelres.config(text="Risk Factor :"+str(self.ansmain))
        #self.labelres.update_idletasks()
        
        return combos.iloc[0]['TenYearCHD']
    
def graph1():
    roota=Tkinter.Tk()
    roota.wm_title("Age vs Cigarettes Per Day")
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(8,6),dpi=100)
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    a=Axes3D(f)
    
    data=data[:200]
        
    colors = ['r', 'b']

    risk=data["TenYearCHD"]
    risk=risk[:200]
    #a.scatter(dil,fil,label='My Data')
    for i in range(0,199):
        if risk[i]==1:
            a.scatter(data["age"][i], data["cigsPerDay"][i], marker='.', color=colors[0])
        else:
            a.scatter(data["age"][i],data["cigsPerDay"][i],color='blue',s=5,edgecolor='none')
    a.set_xlabel("Age")
    a.set_ylabel("Cigarettes Per Day")
    a.set_zlabel("Ten Year CHD")
    

    
    roota.mainloop()
    
def graph2():
    roota=Tkinter.Tk()
    roota.wm_title("Total Cholestrol vs Cigarettes Per Day")
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(8,6),dpi=100)
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    a=Axes3D(f)
    
    data=data[:200]
        
    colors = ['r', 'b']

    risk=data["TenYearCHD"]
    risk=risk[:200]
    #a.scatter(dil,fil,label='My Data')
    for i in range(0,199):
        if risk[i]==1:
            a.scatter(data["totChol"][i], data["cigsPerDay"][i], marker='.', color=colors[0])
        else:
            a.scatter(data["totChol"][i],data["cigsPerDay"][i],color='blue',s=5,edgecolor='none')
    a.set_xlabel("Total Cholestrol")
    a.set_ylabel("Cigarettes Per Day")
    a.set_zlabel("Ten Year CHD")
    

    
    roota.mainloop()
    
def graph3():
    roota=Tkinter.Tk()
    roota.wm_title("Systolic Blood Pressure vs Cigarettes Per Day")
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(8,6),dpi=100)
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    a=Axes3D(f)
    
    data=data[:200]
        
    colors = ['r', 'b']

    risk=data["TenYearCHD"]
    risk=risk[:200]
    #a.scatter(dil,fil,label='My Data')
    for i in range(0,199):
        if risk[i]==1:
            a.scatter(data["sysBP"][i], data["cigsPerDay"][i], marker='.', color=colors[0])
        else:
            a.scatter(data["sysBP"][i],data["cigsPerDay"][i],color='blue',s=5,edgecolor='none')
    a.set_xlabel("Systolic Blood Pressure")
    a.set_ylabel("Cigarettes Per Day")
    a.set_zlabel("Ten Year CHD")
    

    
    roota.mainloop()
    
def graph4():
    roota=Tkinter.Tk()
    roota.wm_title("Glucose vs Cigarettes Per Day")
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(8,6),dpi=100)
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    a=Axes3D(f)
    
    data=data[:200]
        
    colors = ['r', 'b']

    risk=data["TenYearCHD"]
    risk=risk[:200]
    #a.scatter(dil,fil,label='My Data')
    for i in range(0,199):
        if risk[i]==1:
            a.scatter(data["glucose"][i], data["cigsPerDay"][i], marker='.', color=colors[0])
        else:
            a.scatter(data["glucose"][i],data["cigsPerDay"][i],color='blue',s=5,edgecolor='none')
    a.set_xlabel("Glucose")
    a.set_ylabel("Cigarettes Per Day")
    a.set_zlabel("Ten Year CHD")
    

    
    roota.mainloop()
    
def graph5():
    roota=Tkinter.Tk()
    roota.wm_title("Total Cholestrol vs Systolic Blood Pressure")
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(8,6),dpi=100)
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    a=Axes3D(f)
    
    data=data[:200]
        
    colors = ['r', 'b']

    risk=data["TenYearCHD"]
    risk=risk[:200]
    #a.scatter(dil,fil,label='My Data')
    for i in range(0,199):
        if risk[i]==1:
            a.scatter(data["totChol"][i], data["sysBP"][i], marker='.', color=colors[0])
        else:
            a.scatter(data["totChol"][i],data["sysBP"][i],color='blue',s=5,edgecolor='none')
    a.set_xlabel("Total Cholestrol")
    a.set_ylabel("Systolic Blood Pressure")
    a.set_zlabel("Ten Year CHD")
    

    
    roota.mainloop()
    
def graph6():
    roota=Tkinter.Tk()
    roota.wm_title("Total Cholestrol vs Glucose")
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(8,6),dpi=100)
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    a=Axes3D(f)
    
    data=data[:200]
        
    colors = ['r', 'b']

    risk=data["TenYearCHD"]
    risk=risk[:200]
    #a.scatter(dil,fil,label='My Data')
    for i in range(0,199):
        if risk[i]==1:
            a.scatter(data["totChol"][i], data["glucose"][i], marker='.', color=colors[0])
        else:
            a.scatter(data["totChol"][i],data["glucose"][i],color='blue',s=5,edgecolor='none')
    a.set_xlabel("Total Cholestrol")
    a.set_ylabel("Glucose")
    a.set_zlabel("Ten Year CHD")
    

    
    roota.mainloop()
    
def graph7():
    roota=Tkinter.Tk()
    roota.wm_title("Glucose vs Systolic Blood Pressure")
    data=pd.read_csv("framingham.csv")
    f=Figure(figsize=(8,6),dpi=100)
    
    canvas=FigureCanvasTkAgg(f,master=roota)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    toolbar=NavigationToolbar2TkAgg(canvas,roota)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP,fill=Tkinter.BOTH,expand=1)
    
    a=Axes3D(f)
        
    data=data[:200]
        
    colors = ['r', 'b']

    risk=data["TenYearCHD"]
    risk=risk[:200]
    #a.scatter(dil,fil,label='My Data')
    for i in range(0,199):
        if risk[i]==1:
            a.scatter(data["glucose"][i], data["sysBP"][i], marker='.', color=colors[0])
        else:
            a.scatter(data["glucose"][i],data["sysBP"][i],color='blue',s=5,edgecolor='none')

    a.set_xlabel("Glucose")
    a.set_ylabel("Systolic Blood Pressure")
    a.set_zlabel("Ten Year CHD")
    

    
    roota.mainloop()
    
    
def OnClick2():
    Title3="Competetitve Analysis"
    root3=Tkinter.Tk()
    root3.title(Title3)
    root3.geometry("300x400")
    root3.resizable(width=False,height=False)
    #msg3=Tkinter.Label(root3,text="Choose an option to view the competitive analysis..")
    #msg3.grid(row=1)
    
    label3_2=Tkinter.Label(root3,text="Risk Factor Vs Age :")
    label3_2.grid(row=2)
    button3_2=ttk.Button(root3,text="Check!",command=lambda:risage(1,0))
    button3_2.grid(row=2,column=10)
    
    label3_1=Tkinter.Label(root3,text="Risk Factor Vs cigsPerDay  :")
    label3_1.grid(row=3)
    button3_1=ttk.Button(root3,text="Check!",command=lambda:risage(2,0))
    button3_1.grid(row=3,column=10)
    
    label3_3=Tkinter.Label(root3,text="Risk Factor Vs totChol :")
    label3_3.grid(row=4)
    button3_3=ttk.Button(root3,text="Check!",command=lambda:risage(3,0))
    button3_3.grid(row=4,column=10)
    
    label3_4=Tkinter.Label(root3,text="Risk Factor Vs sysBP :")
    label3_4.grid(row=5)
    button3_4=ttk.Button(root3,text="Check!",command=lambda:risage(4,0))
    button3_4.grid(row=5,column=10)
    
    label3_5=Tkinter.Label(root3,text="Risk Factor Vs glucose :")
    label3_5.grid(row=6)
    button3_5=ttk.Button(root3,text="Check!",command=lambda:risage(5,0))
    button3_5.grid(row=6,column=10)
    
    label3_6=Tkinter.Label(root3,text="Age Vs cigsPerDay :")
    label3_6.grid(row=7)
    button3_6=ttk.Button(root3,text="Check!",command=lambda:graph1())
    button3_6.grid(row=7,column=10)
    
    label3_7=Tkinter.Label(root3,text="totChol Vs cigsPerDay :")
    label3_7.grid(row=8)
    button3_7=ttk.Button(root3,text="Check!",command=lambda:graph2())
    button3_7.grid(row=8,column=10)
    
    label3_8=Tkinter.Label(root3,text="sysBP Vs cigsPerDay :")
    label3_8.grid(row=9)
    button3_8=ttk.Button(root3,text="Check!",command=lambda:graph3())
    button3_8.grid(row=9,column=10)
    
    label3_9=Tkinter.Label(root3,text="glucose Vs cigsPerDay :")
    label3_9.grid(row=10)
    button3_9=ttk.Button(root3,text="Check!",command=lambda:graph4())
    button3_9.grid(row=10,column=10)
    
    label3_10=Tkinter.Label(root3,text="totChol Vs sysBP :")
    label3_10.grid(row=11)
    button3_10=ttk.Button(root3,text="Check!",command=lambda:graph5())
    button3_10.grid(row=11,column=10)
    
    label3_11=Tkinter.Label(root3,text="totChol Vs glucose :")
    label3_11.grid(row=12)
    button3_11=ttk.Button(root3,text="Check!",command=lambda:graph6())
    button3_11.grid(row=12,column=10)
    
    label3_12=Tkinter.Label(root3,text="glucose Vs sysBP :")
    label3_12.grid(row=13)
    button3_12=ttk.Button(root3,text="Check!",command=lambda:graph7())
    button3_12.grid(row=13,column=10)
    
    root3.mainloop()
'''
def ClickAction():
    
    a1=select()
    a2=(entry_2.get())
    a3=(entry_5.get())
    a4=(entry_10.get())
    a5=(entry_11.get())
    a6=(entry_15.get())
    a7=(1.0)
    data=[(a1,a2,a3,a4,a5,a6,a7)]
    combos=pd.DataFrame(data,columns=['male','age','cigsPerDay','totChol','sysBP','glucose','intercept'])
    return (test_df)    
'''
def analyse():
    data=pd.read_csv("framingham.csv")
    data.insert(15,'intercept',1.0)
    np.random.seed(1000)
    
    a1=select()
    
        
    a2=(entry_2.get())
    a3=(entry_5.get())
    a4=(entry_10.get())
    a5=(entry_11.get())
    a6=(entry_15.get())

    #a7=(1)
    #data=[(a1,a2,a3,a4,a5,a6,a7)]
    #combos=pd.DataFrame(data,columns=['male','age','cigsPerDay','totChol','sysBP','glucose','intercept'])
       
    
    combos = pd.DataFrame({'male':[int(a1)],'age': [int(a2)],'cigsPerDay':[int(a3)],'totChol':[int(a4)],'sysBP':[int(a5)],'glucose':[int(a6)],'intercept':[1]})
    train_cols=data[['male','age','cigsPerDay','totChol','sysBP','glucose','intercept']]
    trainf=train_cols.columns[:]
    xx=data['TenYearCHD']
    logit=sm.GLM(xx,train_cols,family=sm.families.Binomial(),missing='drop')
    result=logit.fit(method="bfgs")
    combos['TenYearCHD']=result.predict(combos[trainf])
    #fb=combos.plot(kind='bar')
    
    return combos.iloc[0]['TenYearCHD']
    
def OnClickFun2(c0,c1,c2,c3,c4,c5):
    rootfl=Tkinter.Tk()
    rootfl.geometry("300x400")
    rootfl.wm_title("Individual Analysis")
    rootfl.resizable(width=False,height=False)
    app=Fun(c0,c1,c2,c3,c4,c5,master=rootfl)
    app.mainloop()
        

def OnCheck():
    Title2="Heart Risk Report"
    root2=Tkinter.Tk()
    root2.title(Title2)
    root2.geometry("300x400")
    root2.resizable(width=False,height=False)
    a1=select()
    a22=(entry_2.get())
    a3=(entry_5.get())
    a4=(entry_10.get())
    a25=((entry_11.get()))
    a26=(entry_15.get())
    if a22  in str(range(20,100)) and a22:
        print "Correct!"
    else:
        root2.destroy()      
        tkMessageBox.showinfo('Error','Age should be entered between 20 to 100')
        root.destroy()
       
        
    if   a3 in str(range(0,70)) and a3:
        print "Correct!"
    else:
        root2.destroy()
        tkMessageBox.showinfo('Error','No. of cigarettes should be entered between 0 to 70')
        root.destroy()
        
        
    if  a4 in str(range(100,700)) and a4:
        print "Correct!"
    else:
        root2.destroy()
        tkMessageBox.showinfo('Error','Total cholesterol value should be entered between 100 to 700')
        root.destroy()
         
        
    if  a25  in str(range(80,300)) and a25:
        print "Correct!"
    else:
        root2.destroy()
        tkMessageBox.showinfo('Error','Value of Systolic BP should be entered between 80 to 300')
        root.destroy()
        
    if  a26  in str(range(40,400)) and a26:
        print "Correct!"
    else:
        root2.destroy()
        
        tkMessageBox.showinfo('Error','Value of Glucose should be entered between 40 to 400')
        root.destroy()
        
    if a1=='1':
        vargen="Male"
    else:
        vargen="Female"
    
    result=analyse()    
    msg2=Tkinter.Label(root2,text="Your Checkup Reports Are..........")
    msg2.pack()
    
    label2_1=Tkinter.Label(root2,text="Gender  :  "+vargen)
    label2_1.pack()
    
    label2_2=Tkinter.Label(root2,text="Age  : "+str(a22))
    label2_2.pack()
    
    label2_3=Tkinter.Label(root2,text="Cigarettes Per Day  : "+str(a3))
    label2_3.pack()
    
    label2_4=Tkinter.Label(root2,text="Total Cholesterol  :  "+str(a4))
    label2_4.pack()
    
    label2_5=Tkinter.Label(root2,text="Systolic Blood Pressure  : "+str(a25))
    label2_5.pack()
    
    label2_6=Tkinter.Label(root2,text="Glucose Level  :  "+ str(a26))
    label2_6.pack()
    
    label2_7=Tkinter.Label(root2,text="Risk Factor Is  :  "+ str(result*100))
    label2_7.pack()
    
    button2_1=ttk.Button(root2,text="Competetitve Analysis",command=OnClick2)
    button2_1.pack(side=Tkinter.BOTTOM)
    
    button2_2=ttk.Button(root2,text="Fun Analysis",command=lambda:OnClickFun2(a1,a22,a3,a4,a25,a26))
    button2_2.pack(side=Tkinter.BOTTOM)
    
    root2.mainloop()


msg=Tkinter.Label(root,text="Please enter your Medical Information.......")
msg.pack()
msg2=Tkinter.Label(root,text="[Enter to the nearest integer ]")
msg2.pack()
#test_df=pd.DataFrame({'male':[],'age':[],'cigsPerDay':[],'totChol':[],'sysBP':[],'glucose':[],'intercept':[]})
var=Tkinter.StringVar()
label_1=Tkinter.Label(root,text="Gender :")
label_1.pack()
ml=ttk.Radiobutton(root,text="Male",value=1,variable=var,command=select)
ml.pack()
fm=ttk.Radiobutton(root,text="Female",value=0,variable=var,command=select)

fm.pack()

label_2=Tkinter.Label(root,text="Age [Enter value between 20 to 100] :",anchor=Tkinter.W,justify=Tkinter.LEFT)
label_2.pack()
entry_2=Tkinter.Entry(root)
entry_2.pack()

label_5=Tkinter.Label(root,text="Ciggaretes per day  [Enter value between 0 to 70] :")
label_5.pack()
entry_5=Tkinter.Entry(root)
entry_5.pack()

label_10=Tkinter.Label(root,text="Tol Chol  [Enter value between 100 to 700] :")
label_10.pack()
entry_10=Tkinter.Entry(root)
entry_10.pack()

label_11=Tkinter.Label(root,text="Sys BP  [Enter value between 80 to 300] :")
label_11.pack()
entry_11=Tkinter.Entry(root)
entry_11.pack()

label_15=Tkinter.Label(root,text="Glucose [Enter value between 40 to 400] :")
label_15.pack()
entry_15=Tkinter.Entry(root)
entry_15.pack()

#Button2=tkinter.Button(root,text="Submit!",command=ClickAction)
#Button2.pack(side=tkinter.BOTTOM,expand=tkinter.NO)

button1=ttk.Button(root,text="Check!",command=OnCheck)
button1.pack(side=Tkinter.BOTTOM,expand=Tkinter.NO)

#print(test_df)
root.mainloop()
