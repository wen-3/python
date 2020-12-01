import myclass

cs = myclass.Customer("小明", 20, "123@gmail.com", "0912345678")

nm = cs.getName()
ag = cs.getAge()
ml = cs.getMail()
tl = cs.getTel()

print(nm, "先生/小姐", ag, "歲")
print("E-mail：", ml, "手機號碼：", tl)