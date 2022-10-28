tst = "0123456789"
while tst[0] != "5":
    tst = tst[1:]
    print(tst)
tst+='0'
print(tst)