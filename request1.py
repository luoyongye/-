# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:30:50 2018

@author: lenovo
"""

import pandas as pd
import csv
import numpy as np
from pyecharts import Geo
##任意的多组列表
#a = [1,2,3]
#b = [4,5,6]    
#
##字典中的key值即为csv中列名
#dataframe = pd.DataFrame({'a_name':a,'b_name':b})
#
##将DataFrame存储为csv,index表示是否显示行名，default=True
#dataframe.to_csv("test.csv",index=False,sep=',')

# 读取csv文件方式1
#csvFile = open("test.csv", "r")
#reader = csv.DictReader(csvFile)  # 返回的是迭代类型
#column = list(map(float,([row['Longitude'] for row in reader])))
#print(column)
#csvFile.close()
def main():
    data = pd.read_csv('directory.csv')
    data_jingwei = data.values[:,11:].tolist()
    data_name = data.values[:,2].tolist()
    weizhi = dict(zip(data_name,data_jingwei))
    attr = data_name
    value = data.values[:,(0,1,3,4,5,6,7,8,9,10)].tolist()
    for i in range(len(value)):
        value[i][0]=str("品牌:")+str(value[i][0])
        value[i][1]=str("编号:")+str(value[i][1])
        value[i][2]=str("所有权:")+str(value[i][2])
        value[i][3]=str("街道:")+str(value[i][3])
        value[i][4]=str("城市:")+str(value[i][4])
        value[i][5]=str("省份:")+str(value[i][5])
        value[i][6]=str("国家:")+str(value[i][6])
        value[i][7]=str("邮政编码:")+str(value[i][7])
        value[i][8]=str("电话号码:")+str(value[i][8])
        value[i][9]=str("时区:")+str(value[i][9])
        
    #print(value)
    geo = Geo("星巴克门店在全球各地的分布情况", "data from pm2.5", title_color="#fff",
              title_pos="center", width=1200,height=600, background_color='#404a59')
    geo.add("",attr,value, visual_text_color="#fff",maptype="world",
            symbol_size=15,geo_cities_coords=weizhi,is_visualmap=True)
    geo.render("all.html")
    
if __name__ == "__main__":
    main()