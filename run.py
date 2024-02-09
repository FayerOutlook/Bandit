import module
m = module # Для упрощения


def damage():
    m.playerHP = m.playerHP - 10
    print("Вы: Ай, меня ударили!")

def damageUP():
    m.playerHP = m.playerHP - 40
    print("Вы: АЙ, ОЧЕНЬ БОЛЬНО!")


while(m.otvet == False):
    print("-" * 50)
    if m.playerHP == 0:
        print("Вы: Я избит... надо отдохнуть..")
        print("-" * 50)
        input("Вы проиграли")
        m.otvet = True
        break
    choice = input("Бандит: Ты думаешь, я тебе ничего не сделаю?: ")
    if choice in m.peaceful:
        print("Бандит: Сорян, зря налетел")
        print("-" * 50)
        input("Вы выиграли")
        m.otvet = True
    elif m.playerHP <= 0:
        print("Вы: Я избит... надо отдохнуть..")
        print("-" * 50)
        input("Вы проиграли")
        m.otvet = True
    elif choice in m.agressive:
        damageUP()
        if m.playerHP < 0:
            m.playerHP = 0
        print("HP =", m.playerHP)
    else:
        damage()
        if m.playerHP < 0:
            m.playerHP = 0
        print("HP =", m.playerHP)
