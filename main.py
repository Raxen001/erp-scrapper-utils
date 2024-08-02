import requests
from requests import JSONDecodeError
import cap2txt
import re
from urllib.parse import unquote

from pprint import pprint

URL_LOGIN = "https://erp.rajalakshmi.org/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=iF6gEp4ArHiXP7jJ9QlgUyiC5t8GbTA5A/9xbk1Vtqk="
BASE_URL = 'https://erp.rajalakshmi.org/'

# debug
# USER = '211001084'
# PASS = 'Suck_my_cock69@'

PNG = "./temp.png"
def download_captcha_image(url, session):
    with open(PNG, 'wb') as f:
        data = session.get(url)
        if data.status_code != 200:
            print("ERROR 404 not found")
        f.write(data.content)

def get_captcha_text(data, session):
    pattern = re.compile('img src="(Captcha.*?)"')
    url = BASE_URL + pattern.findall(data.text)[0]
    download_captcha_image(url, session)
    captcha = cap2txt.cap2txt(PNG)
    return captcha

def get_view_state(data):
    pattern = re.compile('id="__VIEWSTATE".*?value="(.*?)"')
    view_state = pattern.findall(data.text)[0]
    return view_state
    

def login(session, CAPTCHA, viewstate):

    data = {
        'Script_water_HiddenField': ';;AjaxControlToolkit, Version=3.0.20229.20843, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:3b7d1b28-161f-426a-ab77-b345f2c428f5:e2e86ef9:1df13a87:8ccd9c1b:3858419b:9ea3f0e2:96741c43:c4c00916:c7c04611:cd120801:38ec41c0',
        '__EVENTTARGET': 'btnLogin',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': unquote(viewstate),
        '__VIEWSTATEGENERATOR': 'CA0B0334',
        '__VIEWSTATEENCRYPTED': '',
        'txt_username': '211001084',
        'txt_password': 'Suck_my_cock69@',
        'txtcaptcha': CAPTCHA,
        'txtdemo': '',
        'hdfuserno': '',
        'hdffirstlog': '',
        'hdflastlogout': '',
        'hdfAllowpopup': '',
        'hdnusername': 'MjExMDAxMDg0',
        'hdnpassword': 'U3Vja19teV9jb2NrNjlA',
        'txtName': '',
        'TextBoxWatermarkExtender2_ClientState': '',
        'txt_emailid': '',
        'TextBoxWatermarkExtender1_ClientState': '',
        'txt_captcha': '',
        'txt_captcha_TextBoxWatermarkExtender_ClientState': '',
    }
    session.post(
        'https://erp.rajalakshmi.org/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?%2f',
        data=data,
    )
    
    # login
    # pprint(session.cookies.get_dict())
    # print(response.text)


def get_attendance(session):
    URL = "https://erp.rajalakshmi.org/StudeHome.aspx/ShowAttendance"
    json_data = {}
    res = session.post(URL, json=json_data)
    try:
        data = res.json()
        if data['d']['AttendList'] != None:
            pprint(data)
            pprint(session.cookies.get_dict())
        else:
            print("Failed...")
    except JSONDecodeError:
        pprint("ERROR!!!!")
        if "<!-- Encrypt / Decrypt Username and PWD -->" not in res.text:
            pprint("LOGGED IN: ")
            pprint(session.cookies.get_dict())

def main():
    with requests.Session() as session:

        data = session.get(URL_LOGIN)
        CAPTCHA = get_captcha_text(data, session)
        viewstate = get_view_state(data) 
        #debug
        print('captcha: ', CAPTCHA)

        login(session, CAPTCHA, viewstate)
        get_attendance(session)

for i in range(100):
    main()
