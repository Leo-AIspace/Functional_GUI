#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import font
from tkinter import PhotoImage
import Stock_Prediction_GUI


# In[2]:


class mainmenu():
    def __init__(self):
        self.menu = Tk()
        self.menu.geometry("500x300+600+250")
        self.menu.title("main_menu")
        
        self.fontstyle = font.Font(family='標楷體', size=32, weight='bold')
        self.fontstyle2 = font.Font(family='標楷體', size=18)
        self.title = Label(self.menu,text="主選單",font=self.fontstyle)
        self.title.pack(side='top',pady=5)
    #選項設置
        self.stockprediction_but = Button(self.menu,text="趨勢預測",font=self.fontstyle2,width=12,height=3,relief="raised",
                                         command=lambda:[self.call_stockprediction()])
        self.stockprediction_but.place(x=70,y=70)

        self.menu.mainloop()
    #呼叫stockprediction
    def call_stockprediction(self):
        self.menu.destroy()
        app = Stock_Prediction_GUI.StockPG() 

