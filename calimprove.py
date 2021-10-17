# -*- coding:utf-8 -*-
import time
import requests
#æ¯é¦æ¸¯è®°èè¿å¿«ï¼  ???
#å¤ªæ¢äº   太慢了
#ç­æ¡éè¯¯  答案错误
url = 'http://49.235.111.14:5011/'
a = requests.session()
getul = a.get(url)
gettext = getul.text
starth = gettext.find('<div>')
endh = gettext.find('</div>')
shizi = gettext[starth + 5:endh]
shizi2 = shizi.replace(' ', '')
shizi3 = shizi2.replace('=', '==')
cal = eval(shizi3)
if cal:
    key = {"answer": "true"}
else:
    key = {"answer": "false"}
for i in  range(20):
    time.sleep(1)           #关键一步
    po = a.post(url, key).text
    print(po)
    starth = po.find('<div>')
    endh = po.find('</div>')
    shizi = po[starth + 5:endh]
    shizi2 = shizi.replace(' ', '')
    shizi3 = shizi2.replace('=', '==')
    cal = eval(shizi3)
    if cal:
        key = {"answer": "true"}
    else:
        key = {"answer": "false"}
