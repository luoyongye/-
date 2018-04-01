# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:23:59 2018

@author: lenovo
"""
import pandas as pd
from pyecharts import Pie
from pyecharts import Bar
from pyecharts import Geo
from pyecharts import Map
from collections import Counter
import numpy as np


def drawPie_CountOfDifferentCountry(attr,v1):
    pie = Pie("各个国家的店铺数量的饼图示例",width=1200, height=600,title_pos='center')
    pie.add("", attr, v1, is_label_show=True,center=[50, 60],is_legend_show=False,legend_orient='vertical',legend_pos='left')
    pie.render("Pie_CountOfDifferentCountry.html")
    
def drawBar_CountOfDifferentCountry(attr,v):
    bar = Bar("各个国家的店铺数量的柱状图示例")
    bar.add("", attr, v,is_datazoom_show=True, datazoom_type='both',mark_line=["min", "max"])
    bar.render("Bar_CountOfDifferentCountry.html")
    
def drawCountOfDifferentCountry(attr,value):
#    data = pd.read_csv('directory.csv')
#    data_jingwei = data.values[:,11:].tolist()
#    data_name = data.values[:,2].tolist()
#    weizhi = dict(zip(data_name,data_jingwei))
#    attr = data_name
#    value1 = data.values[:,7].tolist()
#    dict1 = Counter(value1)
#    attr =['Andorra', 'United Arab Emirates', 'Argentina', 'Austria', 'Australia', 'Aruba', 'Azerbaijan', 'Belgium', 'Bulgaria', 'Bahrain', 'Brunei', 'Bolivia', 'Brazil', 'Bahamas', 'Canada', 'Switzerland', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Cornwall', 'Cyprus', 'Czech Republic', 'Germany', 'Denmark', 'Egypt', 'Spain', 'Finland', 'France', 'United Kiongdom', 'Greece', 'Guatemala', 'Hungary', 'Indonesia', 'Ireland', 'India', 'Jordan', 'Japan', 'Cambodia', 'Korea', '	Kuwait', 'Kazakstan', 'Lebanon', 'Luxembourg', 'Morocco', 'Monaco', 'Mexico', 'Malaysia', 'Netherlands', 'Norway', 'New Zealand', 'Oman', 'Panama', 'Peru', 'Philippines', 'Poland', 'Puerto Rico', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Saudi Arabia', 'Sweden', 'Singapore', 'Slovakia', 'EI Salvador', 'Thailand', 'Turkey', 'Trinidad and Tobago', 'Taiwan', 'United States', 'Vietnam', 'South Africa']
#    value = dict1.values()
    map = Map("星巴克在各个国家的分布密度","颜色越深代表分布的密度越大", width=1200, height=600,title_pos='center')
    map.add("", attr, value,visual_range=[1,300],type="heatmap",maptype="world", is_visualmap=True,
        visual_text_color='#000', is_map_symbol_show=True)
    map.render("drawCountOfDifferentCountry.html")


            
def main():
    data = pd.read_csv('directory.csv')
    value1 = data.values[:,7].tolist()
    dict1 = Counter(value1)
    attr =['Andorra', 'United Arab Emirates', 'Argentina', 'Austria', 'Australia', 'Aruba', 'Azerbaijan', 'Belgium', 'Bulgaria', 'Bahrain', 'Brunei', 'Bolivia', 'Brazil', 'Bahamas', 'Canada', 'Switzerland', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Cornwall', 'Cyprus', 'Czech Republic', 'Germany', 'Denmark', 'Egypt', 'Spain', 'Finland', 'France', 'United Kiongdom', 'Greece', 'Guatemala', 'Hungary', 'Indonesia', 'Ireland', 'India', 'Jordan', 'Japan', 'Cambodia', 'Korea', '	Kuwait', 'Kazakstan', 'Lebanon', 'Luxembourg', 'Morocco', 'Monaco', 'Mexico', 'Malaysia', 'Netherlands', 'Norway', 'New Zealand', 'Oman', 'Panama', 'Peru', 'Philippines', 'Poland', 'Puerto Rico', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Saudi Arabia', 'Sweden', 'Singapore', 'Slovakia', 'EI Salvador', 'Thailand', 'Turkey', 'Trinidad and Tobago', 'Taiwan', 'United States', 'Vietnam', 'South Africa']
    value = list(dict1.values())
    
    drawCountOfDifferentCountry(attr,value)
    
    drawPie_CountOfDifferentCountry(attr,value)
    
    drawBar_CountOfDifferentCountry(attr,value)
    
    
if __name__ == "__main__":
    main()