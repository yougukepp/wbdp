#!/usr/bin/env python3
# -- coding utf-8 --

#from openpyxl import Workbook

import os
from openpyxl import Workbook

g_excel_file_name = 'data.xlsx'

g_gdp_file_name = 'gdp.csv'
g_population_file_name = 'population.csv'

g_gdp_file_name_output = 'gdp.txt'
g_population_file_name_output = 'population.txt'

g_start_year = 1980
g_end_year   = 2014
g_value_start_index = 4

g_sheet_row_offset = 2

def get_data_dict(file_name, start_year, end_year, value_start_index):
    """
    {国家:{年:value}}
    例如:
    {国家:{年:gdp}}
    {国家:{年:population}}
    """
    all_data = {}

    data_file = open(file_name, 'r', encoding='utf_8_sig')

    for line in data_file:
        data = []
        data = line.split(',')
        a_country_data = {}
        for y in range(start_year, end_year):
            index = y - (start_year - value_start_index)
            a_country_data[y] = data[index]
        country = data[2]
        all_data[country] = a_country_data

    data_file.close()
    return all_data

def print_data(file_name, data):
    """
    国 年 value
    例如:
    国 年 gdp
    国 年 population
    """
    data_file = open(file_name, 'w', encoding='utf_8_sig')
    for c in data:
        a_country_data = data[c]
        for y in a_country_data:
            a_line = "%s,%s,%s\n" % (c, y, data[c][y])
            data_file.write(a_line)
    data_file.close()

def combine_data(gdp_data, population_data, start_year, end_year):
    """
    {年:{国:[gdp,population]}}
    """
    all_data = {}

    # 生成国家列表
    country_list = []
    for c in all_gdp_data:
        country_list.append(c)

    for y in range(start_year, end_year):
        all_data[y] = {}
        for c in country_list:
            gdp = gdp_data[c][y]
            population = population_data[c][y]
            if '..' == gdp:
                gdp = 0
            if '..' == population:
                population = 0
            gdp = float(gdp)
            population = float(population)

            all_data[y][c] = (gdp, population)

    return all_data

def sort_data(data, sorted_key):
    """
    排序
    TODO:只实现gdp作为键
    """

    return data

def write_sheet(sheet, data):
    i = 1
    index_list = {}

    # 写入表头
    index = i + g_sheet_row_offset
    ranking_index = "B%d" % index
    country_index = "C%d" % index
    gdp_index =  "D%d" % index
    population_index =  "E%d" % index
    gdp_per_people_index = "F%d" % index

    sheet[ranking_index] = "排名"
    sheet[country_index] = "国家"
    sheet[gdp_index] = "GDP(万亿)"
    sheet[population_index] = "人口(亿)"
    sheet[gdp_per_people_index] = "万"

    # 写入内容
    for c in data:
        index = i + g_sheet_row_offset + 1
        country_index = "C%d" % index
        gdp_index =  "D%d" % index
        population_index =  "E%d" % index
        gdp_per_people_index =  "F%d" % index

        gdp = data[c][0] / 1000000000000
        population = data[c][1] / 100000000

        # 防止 除零
        if 0 == population:
            population = 1

        sheet[country_index] = c
        sheet[gdp_index] = gdp
        sheet[population_index] = population
        sheet[gdp_per_people_index] = gdp / population
        i += 1

def write_excel(data, start_year, end_year):
    """
    1. 删除文件  g_excel_file_name.
    2. 写入数据到g_excel_file_name.
    """

    if os.path.exists(g_excel_file_name):
        os.remove(g_excel_file_name)

    excel_file = Workbook()
    for y in range(start_year, end_year):
        # data[y]
        sheet = excel_file.create_sheet(y, str(y))
        write_sheet(sheet, data[y])
        print(y)

    excel_file.save(g_excel_file_name)

if __name__ == "__main__":

    all_gdp_data = get_data_dict(g_gdp_file_name,
            g_start_year, g_end_year, g_value_start_index)
    #print_data(g_gdp_file_name_output, all_gdp_data)

    all_population_data = get_data_dict(g_population_file_name,
            g_start_year, g_end_year, g_value_start_index)
    #print_data(g_population_file_name_output, all_population_data)

    all_data = combine_data(all_gdp_data, all_population_data, g_start_year, g_end_year)

    sorted_data = sort_data(all_data, 'gdp')

    write_excel(sorted_data, g_start_year, g_end_year)

    """
    all_data
    {年:{国:[gdp,population]}}
    """

