#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import WBDPViewer

if __name__ == '__main__':
    viewer = WBDPViewer.WBDPViewer()
    viewer.show()

    """
    url = 'http://api.worldbank.org/zh/countries/all/indicators/NY.GDP.MKTP.CD?format=json&per_page=5000&page=1'

    print(1)
    response = urllib.request.urlopen(url)
    print(2)
    buff = response.read()
    print(3)
    buff_utf8 = buff.decode("utf8")
    print(4)
    data = json.loads(buff_utf8)
    print(5)

    out = open('data.txt', 'w')
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(6)
    out.write(json_str)
    out.close()
    print(7)
    """

