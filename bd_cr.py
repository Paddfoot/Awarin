import os
import json

from bs4 import BeautifulSoup
import requests
import json
import codecs

def name(n):
    #temp = bs.find('h2', 'pi-item pi-item-spacing pi-title pi-secondary-background')
    #print(temp.text)
    url = 'https://genshin-impact.fandom.com/wiki/' + n
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('h2', 'pi-item pi-item-spacing pi-title pi-secondary-background')
    #print(temp)
    if temp == None:
        print(temp)
    else:
        return temp.text

def weap(n):
    #temp = bs.find('h2', 'pi-item pi-item-spacing pi-title pi-secondary-background')
    #print(temp.text)
    url = 'https://genshin-impact.fandom.com/wiki/' + n
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('span', 'no-wrap')
    #print(temp)
    if temp == None:
        print(temp)
    else:
        return temp.text.replace(' ', '')

def rarity(n):
    #temp = bs.find('h2', 'pi-item pi-item-spacing pi-title pi-secondary-background')
    #print(temp.text)
    url = 'https://genshin-impact.fandom.com/wiki/' + n
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('td', 'pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing')
    #print(temp)
    if temp == None:
        print(temp)
    else:
        return temp.find('img').attrs['alt'][0]
        
def el(n):
    #temp = bs.find('h2', 'pi-item pi-item-spacing pi-title pi-secondary-background')
    #print(temp.text)
    url = 'https://genshin-impact.fandom.com/wiki/' + n
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find_all('td', 'pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing')
    #print(temp)
    if temp == []:
        print('temp')
    else:
        return temp[2].find('img').attrs['alt'][8:]

directory = "data/characters/"
files = os.listdir(directory)

data = {'data': {
            'characters': []
            }
        }

for i in files:
    data['data']['characters'].append({'nid': i,
                                       'name': name(i),
                                       'name_ru': '',
                                       'element': el(i),
                                       'weapon': weap(i),
                                       'rarity': rarity(i),
                                       'element_icon': 'https://raw.githubusercontent.com/Paddfoot/Awarin/main/data/elements/anemo.webp',
                                       'icon': 'https://raw.githubusercontent.com/Paddfoot/Awarin/main/data/characters/' + i + '/UI_AvatarIcon_' + i + '.png',
                                       'gacha_img': 'https://raw.githubusercontent.com/Paddfoot/Awarin/main/data/characters/' + i + '/UI_Gacha_AvatarImg_' + i + '.webp',
                                       'namecard': 'https://raw.githubusercontent.com/Paddfoot/Awarin/main/data/characters/' + i + '/UI_NameCardPic_' + i + '_P.jpg'
                                       })
print(data)