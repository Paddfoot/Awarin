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
        print(temp.text)

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
        print(temp.text.replace(' ', ''))

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
        print(temp.find('img').attrs['alt'][0])
        
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
        print(temp[2].find('img').attrs['alt'][8:])

fileObj = codecs.open( "bd.json", "r", "utf_8_sig" )
text = fileObj.read() # или читайте по строке
jess_dict = json.loads(text)
for o in jess_dict['data']['characters']:
    el(o['nid'])
    #rarity(o['nid'])
    #weap(o['nid'])
    #name(o['nid'])
fileObj.close()