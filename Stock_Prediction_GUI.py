#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import PhotoImage
import Stockprediction
import main_menu_GUI


# In[6]:


class StockPG():
    def __init__(self):
        self.StockPG=Tk()
        self.StockPG.geometry("550x250+600+250")
        self.StockPG.title('Stock_prediction')
        self.fontStyle = font.Font(family="標楷體", size=32,weight='bold')
        self.fs2 = font.Font(family="標楷體", size=14)
        self.title = Label(self.StockPG,text='漲跌預測',font=self.fontStyle,height=1,width=9)
        self.title.grid(row=0,column=0)
      #主選單按鈕
        load_photo= PhotoImage(file=r'./images/home.png')
        self.photo=load_photo.subsample(11,11)
        self.home = Button(self.StockPG,image=self.photo,command=lambda:[self.go_home()])
        self.home.grid(row=0,column=0,sticky='w')

        self.mylabel = Label(self.StockPG, text='可信度: ',font=self.fs2,height=1)
        self.mylabel.grid(row=1,column=0,sticky='E')
        
      #上漲
        self.rise_label = Label(self.StockPG,text='上漲',font=self.fs2,borderwidth=3,relief='sunken',width=6,height=2)
        self.rise_label.grid(row=2,column=0,sticky='EW',padx=5)
        self.rise_color = Label(self.StockPG,borderwidth=3,relief='sunken',bg=None,width=6,height=2)
        self.rise_color .grid(row=2,column=1,sticky='W',padx=5)
      #持平 
        self.falt_label = Label(self.StockPG,text='持平',font=self.fs2,borderwidth=3,relief='sunken',width=6,height=2)
        self.falt_label .grid(row=3,column=0,sticky='EW',padx=5)
        self.falt_color = Label(self.StockPG,borderwidth=3,relief='sunken',bg=None,width=6,height=2)
        self.falt_color .grid(row=3,column=1,sticky='W',padx=5)
      #下跌
        self.fall_label = Label(self.StockPG,text='下跌',font=self.fs2,borderwidth=3,relief='sunken',width=6,height=2)
        self.fall_label .grid(row=4,column=0,sticky='EW',padx=5)
        self.fall_color = Label(self.StockPG,borderwidth=3,relief='sunken',bg=None,width=6,height=2)
        self.fall_color.grid(row=4,column=1,sticky='W',padx=5)
      #控制區
        self.Pathtext = Label(self.StockPG,text='',borderwidth=3,relief='sunken',font=12,width=48,height=1,bg='white')
        self.Pathtext.grid(row=5,column=0,padx=5)
        self.Getpath = Button(self.StockPG,text='...',font=18,borderwidth=6,relief='raised',width=3,height=1,
                        command = self.get_path)
        self.Getpath.grid(row=5,column=1,sticky='W',padx=5)
        self.Prediction = Button(self.StockPG,text='預測',font=self.fs2,borderwidth=6,relief='raised',width=3,height=1,
                      command = lambda:[self.start_prediction(self.Pathtext['text'])])
        self.Prediction.grid(row=5,column=1,padx=50)
        self.StockPG.mainloop()
#選取CSV資料路徑
    def get_path(self):
        self.get_path = Tk()

        self.get_path.filename = filedialog.askopenfilename(initialdir="/Users/USER/Desktop",
                                               title='Select A File',
                                              filetypes=(('csv files','*.csv'),('all files','*.*')))
        self.get_path.destroy()
        self.Pathtext['text'] = self.get_path.filename
        self.get_path.mainloop
#執行預測
    def start_prediction(self,path):
        result,probility = Stockprediction.predict(path)
        self.mylabel["text"]='可信度: '+probility[:5]
        if result=='0':
            bg_color = [None,'yellow',None]
        elif result=='1':
            bg_color = ['red',None,None]
        else:
            bg_color = [None,None,'green']
        self.rise_color['bg']= bg_color[0]
        self.falt_color['bg']= bg_color[1]
        self.fall_color['bg']= bg_color[2]
#回主選單
    def go_home(self):
        self.StockPG.destroy()
        app = main_menu_GUI.mainmenu()

