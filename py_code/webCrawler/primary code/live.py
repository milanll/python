import re
import requests
from lxml import etree
import json
import time
import os
names = {
    "sp": "胜负奖金",
    "rqsp": "让球奖金",
    '0':"平均欧赔",
    "293": "威廉希尔",
    "5": "澳门彩票",
    "3":"bet365",
    "280": "皇冠",
}


def get_id(url):
    """
        >>> get_id('http://live.500.com/')
        json out file to now path live.json
    :param url:
    :return:
    """
    try:
        html_text = requests.get(url).content.decode('gbk')
        x_response = etree.HTML(html_text)
        id_dict = ''.join(re.findall(r'var.*?liveOddsList=(\{.*?\});', html_text, re.S))
        id_dict = json.loads(id_dict)
        data_dict = {}
        for key in id_dict:
            qiu_name, one, tow = x_response.xpath(f'//tr[@fid="{key}"]/@gy')[0].split(',')
            bi_feng_one = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td/div[@class="pk"]/a[1]/text()'))
            bi_feng_tow = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td/div[@class="pk"]/a[3]/text()'))
            # 比分的中文描述
            bi_feng_name = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td/div[@class="pk"]/a[2]/text()'))
            # 半场
            sheng_fu = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[@class="red"][1]/text()'))
            # 胜负
            sheng_win_or = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[@class="red"][2]/text()'))

            data_dict[f"{qiu_name}_{one} vs {tow}"] = {
                f"{one}": bi_feng_one,
                f"{tow}": bi_feng_tow,
                "半场": sheng_fu,
                "胜负": sheng_win_or,
                "比分": bi_feng_name
            }

            for _key in id_dict[key]:
                try:
                    name_ = names[str(_key)]
                except:
                    continue
                data_dict[f"{qiu_name}_{one} vs {tow}"].update(**{name_:id_dict[key][_key]})
        # print(data_dict)
        with open('./live.json', 'wb') as f:
            f.write(json.dumps(data_dict, ensure_ascii=False).encode())
            # json.dump(f, data_dict), ensure_ascii=False)

        print(f"ok data file path: {os.getcwd()}\live.json")
        time.sleep(10)
    except:
        import traceback
        print(f"error: url: {url}\n")
        traceback.print_exc()
        time.sleep(20)
get_id(input('url: '))


