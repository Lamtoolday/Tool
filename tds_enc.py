API
FAQ
ARCHIVE

lamdayne1
v1
public
lamdayne1  Aug 08, 2024  Never  0
Copy link
Share
Clone

Plaintext
v1
159 lines (159 loc)
12.09 KB

Raw
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= red + "[" + luc + "✓" + red + "] " + trang + "➩ "
#thư viện
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
import socket
from pystyle import Write,Colors
#TIME
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def is_connected():
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
#key_pass1 = ASCIITOOL
#key_pass2 = L-TOOL
os.system("cls" if os.name == "nt" else "clear")
Write.Print(f'              █████╗ ███████╗ ██████╗██╗██╗\n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ██╔══██╗██╔════╝██╔════╝██║██║\n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ███████║███████╗██║     ██║██║  \n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ██╔══██║╚════██║██║     ██║██║  \n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ██║  ██║███████║╚██████╗██║██║\n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝\n',Colors.cyan_to_green,interval=0.0001)
print(f' {vang}          Copyright © ASCII-Tool 2024 {red}|{vang} Version 1.0{trang}')
print(f"      {luc}           Ngày{trang}:{vang}{ngay_hom_nay}{red} |{luc} Tháng{trang}:{vang}{thang_nay} {red}| {luc}Năm{trang}:{vang}{nam_}\n")
print(f"{thanh_xau}{luc} TELE group{trang}:{vang} https://t.me/asciiforest")
print(f"{thanh_xau}{luc} Email{trang}:{vang} lamsalah180@gmail.com")
print(f"{thanh_xau}{luc} Youtube{trang}:{vang} https://www.youtube.com/@ASCII303{trang}")
print(f'{thanh_xau}{luc} IP hiện tại của bạn là{trang}:{vang} {ip}\n')
print(f"{red}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print(f"{red}│{vang} STT {red}│    {vang}         MENU TOOL      {red}        │ {vang}STATUS {red} │{vang} VERSION {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│{vang}  1 {red} │{lam} TDS FACEBOOK    {red}                   │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 2 {red} │{lam} TDS FACEBOOK PRO5     {red}             │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 3 {red} │{lam} TDS INSTAGRAM     {red}                 │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 4 {red} │{lam} TDS TIKTOK         {red}                │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 5 {red} │{lam} TDS TIKTOK MAX SPEED {red}              │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 6 {red} │{lam} TTC Facebook        {red}               │{luc} ONLINE {red} │ {lam} [1.0]  {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│{vang}  7 {red} │{lam} TTC TIKTOK    {red}                     │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 8 {red} │{lam} SHARE ẢO     {red}                      │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 9 {red} │{lam} GOLIKE TIKTOK    {red}                  │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 10{red} │{lam} SHARE ẢO MAXSPEED         {red}         │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 11{red} │{lam} NUÔI FB {red}                           │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 12{red} │{lam} TDS FB FIVEXTOOL       {red}            │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│{vang}  13 {red}│{lam} REG PRO5    {red}                       │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 14 {red}│{lam} GET TOKEN 16L     {red}                 │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 15 {red}│{lam} REG PAGE VITRI    {red}                 │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 16{red} │{lam} SPAM MESSENGER        {red}             │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 17{red} │{lam} SPAM CALLSMS {red}                      │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 18{red} │{lam} QUAY LẠI        {red}                   │{tim}   =.=   {red}│ {lam}  NEXT {red} │")
print(f"{red}└─────┴────────────────────────────────────┴─────────┴─────────┘\n")
chon = input(f"{thanh_dep}{luc}Nhập Lựa Chọn{trang}: ")
os.system("cls" if os.name == "nt" else "clear")
try:
        if chon == '1':
                run = requests.get(f'https://pastecode.dev/raw/8ago8w7w/tds').text
        elif chon == '2':
                run = requests.get(f'https://pastecode.dev/raw/5gbarf4l/tdspr5').text
        elif chon == '3':
                run = requests.get(f'https://pastecode.dev/raw/112zck57/ins').text
        elif chon == '4':
                run = requests.get(f'https://pastecode.dev/raw/bt0s0cdy/tdstt').text
        elif chon == '5':
                run = requests.get(f'https://pastecode.dev/raw/myb43ixz/tdsvip').text
        elif chon == '18':
                run = requests.get(f'https://pastecode.dev/raw/7dyz2nv8/exit').text               
        elif chon == '6':
        	run = requests.get(f'https://pastecode.dev/raw/efkqg87w/ttcpr5').text
        elif chon == '7':
                run = requests.get(f'https://pastecode.dev/raw/m9obwcfe/ttctiktok').text
        elif chon == '8':
                run = requests.get(f'https://pastecode.dev/raw/0zcj5hu3/shareao').text
        elif chon == '9':
                run = requests.get(f'https://raw.githubusercontent.com/Lamtoolday/Tool/main/goliketikv3_obf.py').text
        elif chon == '10':
                run = requests.get(f'https://pastecode.dev/raw/ae4bnb48/sepro5').text
        elif chon == '11':
                run = requests.get(f'https://pastecode.dev/raw/idxr3ywb/nuoifb').text
        elif chon == '12':
        	run = requests.get(f'https://testapi.io/api/Lamdayne18/fivex').text
        elif chon == '13':
                run = requests.get(f'https://raw.githubusercontent.com/Lamtoolday/Tool/main/regpr5.py').text
        elif chon == '14':
                run = requests.get(f'https://pastecode.dev/raw/ljd48pfk/gettk16l').text
        elif chon == '15':
                run = requests.get(f'https://pastecode.dev/raw/qwkxwizq/regpagevitri').text
        elif chon == '16':
                run = requests.get(f'https://pastecode.dev/raw/cz8g4jg4/spammes').text
        elif chon == '17':
                run = requests.get(f'https://pastecode.dev/raw/d82i8ajw/spamsms').text         
        else:
                run = print(f'{lam}Lựa Chọn Không Xác Định{trang}')
except:
        if not is_connected():
                print(f'{lam}Hãy Kiểm Tra Kết Nối Mạng !!! {trang}')
        else:
                print(f'{lam}Sever Gặp Lỗi Hãy Liên Hệ Admin !!! {trang}')
        exit()
exec(run)
API
FAQ
Privacy
Terms
Contact
System Status:
 
Stable
By using PasteCode you agree to our cookies policy to enhance your experience

Site design by Brill © 2023 PasteCode
