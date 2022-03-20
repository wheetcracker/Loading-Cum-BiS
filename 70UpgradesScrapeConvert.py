import json
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://seventyupgrades.com/set/sEiWdfK4Z3PAfxBhVaq3dM"
filename = 'list.txt'
glob_gear_dict = {}

def getBisList(url):
    button_xpath = """//*[@id="root"]/main/div[6]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/button[2]"""
    json_xpath = """//*[@id="root"]/span[7]/div/div/div[2]/div[1]/div[1]/pre"""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
    button = driver.find_element(by = By.XPATH, value = button_xpath)
    button.click()
    json_blob = driver.find_element(by = By.XPATH, value = json_xpath).text
    return json_blob

def jsonParse(json_blob):
    char_dict = {}
    blob = json.loads(json_blob)
    char_dict['char'] = blob['character']['name']
    char_dict['class'] = blob['character']['gameClass']
    char_dict['items'] = []
    item_blob = blob['items']
    for x in item_blob:
        item_list = []
        item_list.append(str(x['id']))
        item_list.append(x['name'])
        item_list.append(x['slot'])
        char_dict['items'].append(item_list)
    return char_dict
        
def dictCreate(char_dict):
    for item in char_dict['items']:
        token_name,token_id = tokenReplace(char_dict,item[1],item[2])

        if token_name:
            if not token_id in glob_gear_dict.keys():
                glob_gear_dict[item[0]] = {}
                glob_gear_dict[item[0]]['loot_id'] = token_id
                glob_gear_dict[item[0]]['loot_name'] = token_name
                glob_gear_dict[item[0]]['prio'] = []
                glob_gear_dict[item[0]]['prio'].append(char_dict['char'])
            else:
                glob_gear_dict[item[0]]['prio'].append(char_dict['char'])
        elif not item[0] in glob_gear_dict.keys():
            glob_gear_dict[item[0]] = {}
            glob_gear_dict[item[0]]['loot_id'] = item[0]
            glob_gear_dict[item[0]]['loot_name'] = item[1]
            glob_gear_dict[item[0]]['prio'] = []
            glob_gear_dict[item[0]]['prio'].append(char_dict['char'])
        else:
            glob_gear_dict[item[0]]['prio'].append(char_dict['char'])

def importList(filename):
    linklist = open(filename, 'r')
    lines = linklist.readlines()
    return lines

def writeLua():
    output = open('pirate_loot_table.lua', 'w')
    output.write('Loading_bis_table = {\n')
    for k,v in glob_gear_dict.items():
        output.write('{{["loot_id"] = "{0}", ["loot_name"] = "{1}", ["prio"] = "{2}",}},\n'.format(v['loot_id'],v['loot_name'],', '.join(v['prio'])))
    output.write('}\n')
    output.close()

def tokenReplace(char_dict,item,slot):
    cclass = char_dict['class']
    token_name = ''
    token_id = ''
    if cclass == 'PALADIN' or cclass == 'PRIEST' or cclass == 'WARLOCK':
        if 'Lightbringer' in item or 'Absolution' in item or 'Malefic' in item:
            suffix = ' of the Forgotten Conqueror'
            if slot == 'HEAD':
                token_name = 'Helm' + suffix
                token_id = '31097'
            elif slot == 'CHEST':
                token_name = 'Chestguard' + suffix
                token_id = '31089'
            elif slot == 'SHOULDERS':
                token_name = 'Pauldrons' + suffix
                token_id = '31101'
            elif slot == 'HANDS':
                token_name = 'Gloves' + suffix
                token_id = '31092'
            elif slot == 'LEGS':
                token_name = 'Leggings' + suffix
                token_id = '31098'
            elif slot == 'WAIST':
                token_name = 'Belt' + suffix
                token_id = '34853'
            elif slot == 'WRIST':
                token_name = 'Bracers' + suffix
                token_id = '34848'
            elif slot == 'FEET':
                token_name = 'Boots' + suffix
                token_id = '34856'
    elif cclass == 'WARRIOR' or cclass == 'HUNTER' or cclass == 'SHAMAN':
        if 'Onslaught' in item or 'Gronnstalker' in item or 'Skyshatter' in item:
            suffix = ' of the Forgotten Protector'
            if slot == 'HEAD':
                token_name = 'Helm' + suffix
                token_id = '31095'
            elif slot == 'CHEST':
                token_name = 'Chestguard' + suffix
                token_id = '31091'
            elif slot == 'SHOULDERS':
                token_name = 'Pauldrons' + suffix
                token_id = '31103'
            elif slot == 'HANDS':
                token_name = 'Gloves' + suffix
                token_id = '31094'
            elif slot == 'LEGS':
                token_name = 'Leggings' + suffix
                token_id = '31100'
            elif slot == 'WAIST':
                token_name = 'Belt' + suffix
                token_id = '34854'
            elif slot == 'WRIST':
                token_name = 'Bracers' + suffix
                token_id = '34851'
            elif slot == 'FEET':
                token_name = 'Boots' + suffix
                token_id = '34857'
    elif cclass == 'ROGUE' or cclass == 'MAGE' or cclass == 'DRUID':
        if cclass == 'MAGE':
            if 'of Tirisfal' in item:
                suffix = ' of the Vanquished Hero'
                if slot == 'HEAD':
                    token_name = 'Helm' + suffix
                    token_id = '30244'
                elif slot == 'CHEST':
                    token_name = 'Chestguard' + suffix
                    token_id = '30238'
                elif slot == 'SHOULDERS':
                    token_name = 'Pauldrons' + suffix
                    token_id = '30250'
                elif slot == 'HANDS':
                    token_name = 'Gloves' + suffix
                    token_id = '30241'
                elif slot == 'LEGS':
                    token_name = 'Leggings' + suffix
                    token_id = '30247'
        if 'Slayer' in item or 'of the Tempest' in item or 'Thunderheart' in item:
            suffix = ' of the Forgotten Vanquisher'
            if slot == 'HEAD':
                token_name = 'Helm' + suffix
                token_id = '31096'
            elif slot == 'CHEST':
                token_name = 'Chestguard' + suffix
                token_id = '31090'
            elif slot == 'SHOULDERS':
                token_name = 'Pauldrons' + suffix
                token_id = '31102'
            elif slot == 'HANDS':
                token_name = 'Gloves' + suffix
                token_id = '31093'
            elif slot == 'LEGS':
                token_name = 'Leggings' + suffix
                token_id = '31099'
            elif slot == 'WAIST':
                token_name = 'Belt' + suffix
                token_id = '34855'
            elif slot == 'WRIST':
                token_name = 'Bracers' + suffix
                token_id = '34852'
            elif slot == 'FEET':
                token_name = 'Boots' + suffix
                token_id = '34858'
    return token_name,token_id

lines = importList(filename)
for line in lines:
    json_blob = getBisList(line)
    char_dict = jsonParse(json_blob)
    dictCreate(char_dict)
writeLua()
