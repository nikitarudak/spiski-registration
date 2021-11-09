import random
login_list = ["A","B"]
pass_list = ["123","1234"]

def username(n: str, l: list):
    """
    Ищет логин в списке
    Возвращает True или False
    :param str n: ищет логин
    :rtype: bool
    """
    if n in l:
        t = True
    else:
        t = False
    return t
def auto_reg():
    """Salasõna genireerimine
    Tagastab salasõna str formaadis 
    :rtype: str
    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    pas = "".join([random.choice(ls) for x in range(12)])
    print(pas)
    return pas
def ise_reg():
    pass
def avtor():
    return
def reg(l: list, p: list):   
    """Inimese registreerimine
    Tagastab loginide ja salasõnade listid 
    :param str v: kasutaja parooli loomise viis
    :rtype: list,list
    """
    print("Регистрация".center(24, ))
    n = input("Введите логин: ")
    u = username(n, login_list)
    while u == True:
        n = input("Такой логин уже существует.\nВведите еще раз: ")
        u = username(n, login_list)
    v = input("Создать пароль автоматически или самостоятельно? y/n: ")
    if v == "y":
        p = auto_reg()
        login_list.append(n)
        pass_list.append(p)
    else:
        my_reg()
    return l, p
while 1:
    print("Регистрация, авторизация, показать списки или выход")
    v = input("1/2/3/4: ")
    if v == "1":
        reg(login_list, pass_list)
    elif v == "2":
        i = 0
        while i < 3:
            t = avtor() #True or False
            if avtor() == True:
                print("Добро пожаловать!")
            else:
                i+=1
    elif v == "3":
        print(login_list)
        print(pass_list)
    else:
        print("Выход...")
        break