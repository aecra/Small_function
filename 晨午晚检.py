import requests
import time

headers = {
    'Host': 'xxcapp.xidian.edu.cn',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0(Linux;Android7.0;wv litebaiduboxapp)AppleWebKit/ 537.36(KHTML,likeGecko)Version/ 4.0Chrome/78.0.3904.96MobileSafari/ 537.36T7/10.3SearchCraft/2.6.2(Baidu;P17.0)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://xxcapp.xidian.edu.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://xxcapp.xidian.edu.cn/site/ncov/xidiandailyup',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
data = {
    'sfzx': 1,
    'tw': 1,
    'area': '陕西省 西安市 长安区',
    'city': '西安市',
    'province': '陕西省',
    'address': '陕西省西安市长安区兴隆街道丁香路西安电子科技大学南校区',
    'geo_api_info': {"type": "complete",
                     "position": {"Q": 34.123646375869, "R": 108.82832438151098, "lng": 108.828324, "lat": 34.123646},
                     "location_type": "html5",
                     "message": "Get ipLocation failed.Get geolocation success.Convert Success.Get address success.",
                     "accuracy": 79,
                     "isConverted": 'true',
                     "status": 1,
                     "addressComponent": {
                         "citycode": "029",
                         "adcode": "610116",
                         "businessAreas": [],
                         "neighborhoodType": "",
                         "neighborhood": "",
                         "building": "",
                         "buildingType": "",
                         "street": "雷甘路",
                         "streetNumber": "266#",
                         "country": "中国",
                         "province": "陕西省",
                         "city": "西安市",
                         "district": "长安区",
                         "township": "兴隆街道"
                     },
                     "formattedAddress": "陕西省西安市长安区兴隆街道丁香路西安电子科技大学南校区",
                     "roads": [],
                     "crosses": [],
                     "pois": [],
                     "info": "SUCCESS"
                     },
    'sfcyglq': 0,
    'sfyzz': 0,
    'qtqk': '',
    'ymtys': 0,
}
cookies = {
    'UqZBpD3n3iPIDwJU': '',
    'eai-sess': '',
    'UUkey': '',
}
url = 'https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save'
s = requests.session()
result = s.post(url, data=data, headers=headers, cookies=cookies)

print(result.text)
