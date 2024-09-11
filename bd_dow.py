import requests
import json
import codecs
import os

def dow(d):
    url = "https://enka.network/ui/UI_Gacha_AvatarImg_"+d+".webp"
    res = requests.get(url).content
    with open('data/characters/'+ d + '/' + url.split('/')[-1].split('?')[0], 'wb') as f:
        f.write(res)

fileObj = codecs.open( "bd.json", "r", "utf_8_sig" )
text = fileObj.read() # или читайте по строке

jess_dict = json.loads(text)

i = 0

while i < 89:
    print(jess_dict['data']['characters'][i]['name'])
    os.makedirs('data/characters/' + jess_dict['data']['characters'][i]['name'], exist_ok=True)
    dow(jess_dict['data']['characters'][i]['name'])
    i = i +1

fileObj.close()