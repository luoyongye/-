# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 12:31:51 2018

@author: lenovo
"""

import tkinter
import request1
import request2
import request34
import os

#调用os函数打开相应的生成文件
def open_all_Geo():  
    os.startfile("all.html" )
def open_timezone_Geo():  
    os.startfile("timezone_geo.html" )
def open_timezone_Bar():  
    os.startfile("timezone_bar.html" ) 
def open_timezone_Pie():  
    os.startfile("timezone_pie.html" ) 
def open_country_Geo():  
    os.startfile("drawCountOfDifferentCountry.html" ) 
def open_country_Bar():  
    os.startfile("Bar_CountOfDifferentCountry.html" ) 
def open_country_Pie():  
    os.startfile("Pie_CountOfDifferentCountry.html" )
def about():  
    print('星巴克数据分析')

def TK_GUI():
    #初始化界面
    root = tkinter.Tk()
    root.title("星巴克数据分析器")
    root.geometry('500x500')
    
    menubar = tkinter.Menu(root)
    
    #创建下拉菜单File，然后将其加入到顶级的菜单栏中  
    filemenu = tkinter.Menu(menubar,tearoff=0)  
    filemenu.add_command(label="在世界地图上显示所有店铺的位置", command=open_all_Geo)  
    filemenu.add_command(label="在世界地图显示各个时区的店铺分布", command=open_timezone_Geo) 
    filemenu.add_command(label="各个时区的店铺数量_柱图", command=open_timezone_Bar)
    filemenu.add_command(label="各个时区的店铺数量_饼图", command=open_timezone_Pie)
    filemenu.add_command(label="在世界地图显示各个国家的店铺分布", command=open_country_Geo)   
    filemenu.add_command(label="各个国家的店铺数量_柱图", command=open_country_Bar)   
    filemenu.add_command(label="各个国家的店铺数量_饼图", command=open_country_Pie)        
    filemenu.add_separator()  
    filemenu.add_command(label="Exit", command=root.quit)  
    menubar.add_cascade(label="File", menu=filemenu)  
      
    #创建下拉菜单Help  
    helpmenu = tkinter.Menu(menubar, tearoff=0)  
    helpmenu.add_command(label="About", command=about)  
    menubar.add_cascade(label="Help", menu=helpmenu)  
      
    #显示菜单  
    root.config(menu=menubar)
    root.mainloop()
    
def main():
    request1.main()
    request2.main()
    request34.main()
    TK_GUI()
    
if __name__ == "__main__":
    main()