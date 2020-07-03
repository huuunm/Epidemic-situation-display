import requests
import re
import json


class Crawler():
    def getBaiduRTData(self):
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400"
        }
        req = requests.get(
            'https://voice.baidu.com/act/newpneumonia/newpneumonia/',
            headers=headers)
        req = req.text.encode('utf-8').decode(
            requests.utils.get_encodings_from_content(req.text)[0])
        regdata = re.compile(r'id="captain-config">(.*)</script><script>',
                             re.M | re.I)

        epidemicData = regdata.findall(req)
        return json.loads(epidemicData[0])