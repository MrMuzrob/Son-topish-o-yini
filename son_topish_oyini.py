import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1dan {x} gacha son o'yladim! Topa olsizmi?", end = "")
    taxminlar = 0
    while True:
        taxminlar +=1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato,men o'ylagan son bundan kattaroq edi.Yana urinib ko'ring:",end = "")
        elif taxmin > tasodifiy_son:
            print("Xato,men o'ylagan son bundan kichikroq edi.Yana urinib ko'ring:",end = "")
        else :
            break
        
    print(f"Tabriklayman! {taxminlar}ta taxmin bilan topdingiz")
    return taxminlar
    
def find_number(x=10):
    input("1dan 10gacha son o'ylang. Men topishga harakat qilaman. Istalgan tugmani bosing")
    quyi = 1
    yuqori = x
    taxmin_soni = 0
    while True:
        taxmin_soni +=1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} ni o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), kichikroq (-) ".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
        
    print(f"Urra, {taxmin_soni} ta taxmin bilan o'ylangan sonni topdim! ")
    return taxmin_soni

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = find_number(x)
        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} ta taxmin bilan yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} ta taxmin bilan yutdingiz!")
        else:
            print(f"Durrang! Siz ham men ham {taxminlar_user}ta taxmin bilan topdik ")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))
    
play()