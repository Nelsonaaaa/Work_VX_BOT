#coding:utf-8
from urllib.parse import urlencode
import requests
import urllib
import json#处理网页数据
 
# while True:#循环
#     message = str(input("要查询的城市："))
 
#     url="https://api.iyk0.com/tq/?city={}".format(message)#获取用户输入的城市进行查询
#     request=url
#     re=requests.get(request)
#     rep = re.json()
#     '''
#     获取网页中的响应的元组变量
#     '''
#     code = rep.get('code')
#     msg = rep.get('msg')
#     city = rep.get('city')
#     up = rep.get('update_time')
#     wea = rep.get('wea')
#     wea_img = rep.get('wea_img')
#     tem = rep.get('tem')
#     tem_day = rep.get('tem_day')
#     tem_night = rep.get('tem_night')
#     win = rep.get('win')
#     win_speed = rep.get('win_speed')
#     win_meter = rep.get('win_meter')
#     air = rep.get('air')
#     time = rep.get('time')
#     print('\n城市名字：',city)
#     print('更新时间：',up)
#     print('天气情况：',wea)
#     print('时实温度：',tem)
#     print('高温：',tem_day)
#     print('低温：',tem_night)
#     print('风向：',win)
#     print('风力等：',win_speed)
#     print('风速：',win_meter)
#     print('空气质量：',air)
#     print('当天日期，星期：',time,'\n')

#     msg = '今日天气早知道\n\n日期:{}\n\n空气质量:{}\n\n温度:{}℃'.format(time,air,tem)

def forecast():
    import requests,json,urllib.parse
    city = urllib.parse.quote("高陵")
    url="https://api.iyk0.com/tq/?city="+city #获取用户输入的城市进行查询
    resp = requests.get(url).json()
    time = resp.get('time')
    up = resp.get('update_time')
    wea = resp.get('wea')
    tem = resp.get('tem')
    msg = '今日预报☁️\n\n日期: {}\n\n更新时间: {}\n\n天气情况: {}\n\n实时温度: {}℃'.format(time,up,wea,tem)
    return msg