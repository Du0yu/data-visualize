# coding = utf-8
# 爬取KFC的门店数量与分布
import pandas as pd
import requests
# import pandas as pd
from bs4 import BeautifulSoup


def get_data():
    url = 'https://m.mxj.com.cn/map/5940.html'

    resp = requests.get(url)
    # print(resp.text)#获取文本
    html = resp.content.decode('utf-8')  # 二进制返回页面内容
    # print(html)
    # 3
    soup = BeautifulSoup(html, 'html.parser')

    span_list = soup.find_all('span')  # 接收并转化为列表
    # print(span_list)   #test

    # for data in span_list[36:]:#遍历循环
    #     sub_data = data.text.split('* 信息仅供参考')
    #     # print(sub_data)
    province = []
    province_number = []  # 创建两个空列表
    content = str(span_list)
    content = content[48:]
    split_index = content.find('<span>* 信息仅供参考</span>')
    province_content = content[0:split_index]
    city_content_start_index = split_index + 22
    city_content = content[city_content_start_index:]
    province_res = province_content.split('<em>')
    del province_res[0]
    for province_data in province_res:
        province_num_end_index = province_data.find('</em>')
        province_num_temp = province_data[0:province_num_end_index]
        province_number.append(province_num_temp)
        province_start_index = province_num_end_index + 5
        province_end_index = province_data.find('</span>')
        province_temp = province_data[province_start_index:province_end_index]
        province_temp = province_temp[2:-2]
        province.append(province_temp)

    city = []
    city_number = []
    city_res = city_content.split('<span>')
    del city_res[0]
    del_times = city_res.count(city_res[1])
    del_key = city_res[1]

    for i in range(del_times):
        city_res.remove(del_key)
    # print(city_res)
    for city_data in city_res:
        if '<a href=' not in city_data:
            city_end_index = city_data.find('(')
            city_temp = city_data[:city_end_index - 1]
            city.append(city_temp)
            city_number_start_index = city_data.find('(')
            city_number_end_index = city_data.find(')')
            city_number_temp = city_data[city_number_start_index + 1:city_number_end_index]
            city_number.append(city_number_temp)
        else:
            city_data = city_data[:-13]
            city_temp = city_data[city_data.find('>')+1:city_data.find('(')-1]
            city.append(city_temp)
            city_number_temp = city_data[city_data.find('(') + 1:city_data.find(')')]
            city_number.append(city_number_temp)
    '''
    print(province)
    print(province_number)
    print(city)
    print(city_number)
    '''
    _data = pd.DataFrame()
    _data["省份"] = province
    _data["KFC总数"] = province_number

    _data2 = pd.DataFrame()
    _data2["城市"] = city
    _data2["KFC数量"] = city_number
    _data3 = _data2.sort_values(by='KFC数量', ascending=False)

    # return _data2
    return _data


def get_data2():
    url = 'https://m.mxj.com.cn/map/5940.html'

    resp = requests.get(url)
    # print(resp.text)#获取文本
    html = resp.content.decode('utf-8')  # 二进制返回页面内容
    # print(html)
    # 3
    soup = BeautifulSoup(html, 'html.parser')

    span_list = soup.find_all('span')  # 接收并转化为列表
    # print(span_list)   #test

    # for data in span_list[36:]:#遍历循环
    #     sub_data = data.text.split('* 信息仅供参考')
    #     # print(sub_data)
    province = []
    province_number = []  # 创建两个空列表
    content = str(span_list)
    content = content[48:]
    split_index = content.find('<span>* 信息仅供参考</span>')
    province_content = content[0:split_index]
    city_content_start_index = split_index + 22
    city_content = content[city_content_start_index:]
    province_res = province_content.split('<em>')
    del province_res[0]
    for province_data in province_res:
        province_num_end_index = province_data.find('</em>')
        province_num_temp = province_data[0:province_num_end_index]
        province_number.append(province_num_temp)
        province_start_index = province_num_end_index + 5
        province_end_index = province_data.find('</span>')
        province_temp = province_data[province_start_index:province_end_index]
        province_temp = province_temp[2:-2]
        province.append(province_temp)

    city = []
    city_number = []
    city_res = city_content.split('<span>')
    del city_res[0]
    del_times = city_res.count(city_res[1])
    del_key = city_res[1]

    for i in range(del_times):
        city_res.remove(del_key)
    # print(city_res)
    for city_data in city_res:
        if '<a href=' not in city_data:
            city_end_index = city_data.find('(')
            city_temp = city_data[:city_end_index - 1]
            city.append(city_temp)
            city_number_start_index = city_data.find('(')
            city_number_end_index = city_data.find(')')
            city_number_temp = city_data[city_number_start_index + 1:city_number_end_index]
            city_number.append(city_number_temp)
        else:
            city_data = city_data[:-13]
            city_temp = city_data[city_data.find('>')+1:city_data.find('(')-1]
            city.append(city_temp)
            city_number_temp = city_data[city_data.find('(') + 1:city_data.find(')')]
            city_number.append(city_number_temp)
    '''
    print(province)
    print(province_number)
    print(city)
    print(city_number)
    '''
    _data = pd.DataFrame()
    _data["省份"] = province
    _data["KFC总数"] = province_number

    _data2 = pd.DataFrame()
    _data2["城市"] = city
    _data2["KFC数量"] = city_number
    _data3 = _data2.sort_values(by='KFC数量', ascending=False)

    return _data3


province_csv = get_data()
province_csv.to_csv('KFC_province_number.csv', index=False, encoding='utf-8')  # 导出文件

city_csv = get_data2()
city_csv.to_csv('KFC_city_number.csv', index=False, encoding='utf-8')  # 导出文件
