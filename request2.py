# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:59:38 2018

@author: lenovo
"""

import pandas as pd
from pyecharts import Geo
from pyecharts import Pie
from pyecharts import Bar
from collections import Counter


def check_str(value):
    # 检查你输入的是否是字符类型
    if isinstance(value, str):
        # 判断字符串以什么开头
        if (value.startswith('GMT+0:00') or value.startswith('GMT+0000')):
            return 0
        elif (value.startswith('GMT+1:00') or value.startswith('GMT+01:00')):
            return 1
        elif (value.startswith('GMT+2:00') or value.startswith('GMT+02:00')):
            return 2
        elif (value.startswith('GMT+3:00') or value.startswith('GMT+03:00')):
            return 3
        elif (value.startswith('GMT+4:00') or value.startswith('GMT+04:00')):
            return 4
        elif (value.startswith('GMT+5:00') or value.startswith('GMT+05:00')):
            return 5
        elif (value.startswith('GMT+6:00') or value.startswith('GMT+06:00')):
            return 6
        elif (value.startswith('GMT+7:00') or value.startswith('GMT+07:00')):
            return 7
        elif (value.startswith('GMT+8:00') or value.startswith('GMT+08:00')):
            return 8
        elif (value.startswith('GMT+9:00') or value.startswith('GMT+09:00')):
            return 9
        elif (value.startswith('GMT+10:00') or value.startswith('GMT+010:00')):
            return 10
        elif (value.startswith('GMT-1:00') or value.startswith('GMT-01:00')):
            return -1
        elif (value.startswith('GMT-2:00') or value.startswith('GMT-02:00')):
            return -2
        elif (value.startswith('GMT-3:00') or value.startswith('GMT-03:00')):
            return -3
        elif (value.startswith('GMT-4:00') or value.startswith('GMT-04:00')):
            return -4
        elif (value.startswith('GMT-5:00') or value.startswith('GMT-05:00')):
            return -5
        elif (value.startswith('GMT-6:00') or value.startswith('GMT-06:00')):
            return -6
        elif (value.startswith('GMT-7:00') or value.startswith('GMT-07:00')):
            return -7
        elif (value.startswith('GMT-8:00') or value.startswith('GMT-08:00')):
            return -8
        elif (value.startswith('GMT-9:00') or value.startswith('GMT-09:00')):
            return -9
        elif (value.startswith('GMT-10:00') or value.startswith('GMT-010:00')):
            return -10
        elif (value.startswith('')):
            return 30
    else:
        return '%s is not str' % value

def drawAll_WithDifferentColor(weizhi,attr,value):
    #用不同的颜色表示不同的时区上的店
    geo = Geo("星巴克门店在全球不同时区的分布情况", "正代表东，负代表西，数字代表第几个时区,缺失时区值的店铺没有显示", title_color="#fff",
              title_pos="center", width=1200,height=600, background_color='#404a59')
    geo.add("",attr,value,visual_range=[-10,10], visual_text_color="#fff",maptype="world",
            symbol_size=15,geo_cities_coords=weizhi,is_visualmap=True,is_piecewise=True, visual_split_number=21)
    geo.render("timezone_geo.html")
    
def drawPie(value):
    #画出不同时区的店铺的分布数量饼状图
    dict1=Counter(value)
#    print(dict1.keys())
    attr = dict1.keys()
    v = dict1.values()
    pie = Pie("饼图示例","正代表东，负代表西，数字代表第几个时区,30代表这条记录缺失时区值",title_pos='center')
    pie.add("", attr, v,center=[50, 60],is_label_show=True,label_text_color=None,legend_orient='vertical',legend_pos='left')
    pie.render("timezone_pie.html")
    
def drawBar():
    #画出不同时区的店铺的分布数量的柱状图
#    dict1=Counter(value)
    attr = [1, 4, -3, 10, -4, 2, 0, 8, -5, -7, -8, -6, '缺失时区值', 7, 9, 3, 5, -9, -10]
    v = [710, 161, 210, 22, 162, 474, 1753, 3708, 5797, 1125, 4629, 3519, 119, 605, 2230, 222, 6, 49, 99]
    bar = Bar("柱状图示例","正代表东，负代表西，数字代表第几个时区")
    bar.add("", attr, v, is_stack=False,mark_line=["min", "max"], is_datazoom_show=True)
    bar.render("timezone_bar.html")
    
def main():
    data = pd.read_csv('directory.csv')
    data_jingwei = data.values[:,11:].tolist()
    data_name = data.values[:,2].tolist()
    weizhi = dict(zip(data_name,data_jingwei))
    attr = data_name
    value = data.values[:,10].tolist()
    for i in range(len(value)):
        value[i] = check_str(value[i])
    
    drawAll_WithDifferentColor(weizhi,attr,value);
    
    drawPie(value);
    
    drawBar();
    
if __name__ == "__main__":
    main()


#print(value)
#用不同的颜色表示不同的时区上的店
#geo = Geo("星巴克门店在全球各地的分布情况", "data from pm2.5", title_color="#fff",
#          title_pos="center", width=1200,height=600, background_color='#404a59')
#geo.add("",attr,value,visual_range=[-10, 10], visual_text_color="#fff",maptype="world",
#        symbol_size=15,geo_cities_coords=weizhi,is_visualmap=True,is_piecewise=True, visual_split_number=21)
#geo.render("时区.html")




#画出不同视同的店铺的柱状图
