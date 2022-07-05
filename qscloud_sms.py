from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
def weather_com_cn(url):
    import requests
    from lxml import etree
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5042.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://www.nmc.cn/publish/forecast/ASN/xian.html",
    "Accept-Encoding": "utf-8, gb2312",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,es;q=0.7",
    }
    resp = requests.get(url,headers=headers)
    resp.encoding='utf-8'
    html = etree.HTML(resp.text)
    def first(ls):
        #格式化列表为字符串
        ls = ls[0]
        return ls
    '''
    今日天气：{1}
    今日温度：{2}
    日落时间：{3}

    近三日天气: 
    {4} , {5} , {6} 
    '''
    today_wea = []
    today_tem = []
    sunset = ['问后羿']
    wea_1_days = []
    wea_2_days = []
    wea_3_days = []

    today_wea = html.xpath('//*[@id="7d"]/ul/li[1]/p[1]/text()')
    today_tem.append(first(html.xpath('//*[@id="7d"]/ul/li[1]/p[2]/i/text()')))

    wea_1_days.append(first(html.xpath('//*[@id="7d"]/ul/li[2]/p[1]/text()')))
    wea_2_days.append(first(html.xpath('//*[@id="7d"]/ul/li[3]/p[1]/text()')))
    wea_3_days.append(first(html.xpath('//*[@id="7d"]/ul/li[4]/p[1]/text()')))
        
    msg = []
    msg.append(first(today_wea))
    msg.append(first(today_tem))
    msg.append(first(sunset))
    msg.append(first(wea_1_days))
    msg.append(first(wea_2_days))
    msg.append(first(wea_3_days))

    return msg 

def send_sms_single(phone_num, template_id, template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = " "  # 自己应用ID
    appkey = " "  # 自己应用Key
    sms_sign = ""  # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    except Exception as e:
        print("异常:",e)
    return response

def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量发送短信
    :param phone_num_list:手机号列表
    :param template_id:腾讯云短信模板ID
    :param param_list:短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = " "  # 自己应用ID
    appkey = " "  # 自己应用Key
    sms_sign = " "  # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response

url = 'http://www.weather.com.cn/weather/urlurl.shtml' #填写天气网站的URL weather.com.cn
phone_number = ['phone1','phone2','phone3']
template_id= ''#短信模板ID
print(__name__)

if __name__ == "__main__":
    send_sms_multi(phone_number,template_id,weather_com_cn(url))
