#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request

g_base_url = 'http://api.worldbank.org/zh/countries/all/indicators/'

g_tyep_dict = {
        'gdp':'NY.GDP.MKTP.CD',
        'population':'SP.POP.TOTL'
}

g_head_index = 0
g_content_index = 1
g_total_key = 'total'
g_date_key = 'date'
g_country_key = 'country'
g_country_v_key = 'value'
g_value_key = 'value'

g_once_count = 2000

def parse_data(data):
    """
    格式
    {(year,国):值}}
    """
    parsed_data = {}

    content_all = data[g_content_index]
    for content in content_all:
        date = content[g_date_key]
        country = content[g_country_key][g_country_v_key]
        value = content[g_value_key]

        if None == date:
            date = 'None'

        if None == country:
            country = 'None'

        if None == value:
            value = 'None'

        parsed_data[(date,country)] = value

    return parsed_data

def parse_count(data):
    head = data[g_head_index]
    total = head[g_total_key]

    return total

def get_net_data(url):
    response = urllib.request.urlopen(url)
    buff = response.read()
    buff_utf8 = buff.decode("utf8")
    data = json.loads(buff_utf8)

    return data

def mkdir_url(value_type, per_page, page):
    url = g_base_url + g_tyep_dict[value_type]
    url += '?format=json&per_page=' + str(per_page)
    url += '&page=' + str(page)

    #print(url)

    return url

def get_count(value_type):
    url = mkdir_url(value_type, 1, 1)
    data = get_net_data(url)
    count = parse_count(data)

    return count;

def get_data(value_type, per_page, page):
    url = mkdir_url(value_type, per_page, page)
    data = get_net_data(url)
    parsed_data = parse_data(data)

    return parsed_data

def get_all_data(value_type):
    total = get_count(value_type)
    page_max = int(total / g_once_count) + 1

    all_data = {}

    for i in range(1, page_max): 
        data = get_data(value_type, g_once_count, i)
        rate = 100.0 * i * g_once_count / total
        print("%.2f%%" % rate)

        # 合并入新数据
        all_data.update(data)

    return all_data

if __name__ == '__main__':
    gdp_data = get_all_data ('gdp')
    population_data = get_all_data('population')

    """
    格式
    {'(year,国)':(值1, 值2,......}}
    """
    all_data = {}
    for k in gdp_data:
        all_data[str(k)] = (gdp_data[k], population_data[k])

    out = open('data.txt', 'w')
    json_str = json.dumps(all_data, ensure_ascii=False, indent=4)
    out.write(json_str)
    out.close()

