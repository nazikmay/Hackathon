######################   Randomaizer    #############################

# Code:
        # from random import randint


        # def randomaizer(lst):
        #     print(lst[randint(0, len(lst)-1)])

        # randomaizer(['Aktan', 'Ulan', 'Arlen', 'Nurmuhammed', 'Azam', 'Belek', 'User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8'])




######################  1 zadanie  ######################

# Code:
from random import randint

def randomaizer_all():
    lst_num = ['0','1','2','3','4','5','6','7','8','9']
    lst_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lst_simbvol = ['!', '@','#','$', '%','^','&','*','(',')','_','+','}','{','/',':','?','>','<','|','~','}']
    lst = lst_abc+lst_num+lst_simbvol
    lsst_res = ""
    stoper = 0
    try:
        inp_size_len = int(input(': '))
        while inp_size_len > stoper:
            lsst_res += (lst[randint(0, len(lst)-1)])
            stoper+=1
    except:
        print("Ошибка")
    return lsst_res

def randomaizer_abc():
    lst_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lsst_res = ""
    stoper = 0
    try:
        inp_size_len = int(input(': '))
        while inp_size_len > stoper:
            lsst_res += (lst_abc[randint(0, len(lst_abc)-1)])
            stoper+=1
    except:
        print("Ошибка")
    return lsst_res
def randomaizer_num():
    lst_num = ['0','1','2','3','4','5','6','7','8','9']
    lsst_res = ""
    stoper = 0
    try:
        inp_size_len = int(input(': '))
        while inp_size_len > stoper:
            lsst_res += (lst_num[randint(0, len(lst_num)-1)])
            stoper+=1
    except:
        print("Ошибка")
    return lsst_res
def randomaizer_sibvol():
    lst_simbvol = ['!', '@','#','$', '%','^','&','*','(',')','_','+','}','{','/',':','?','>','<','|','~','}']
    lsst_res = ""
    stoper = 0
    try:
        inp_size_len = int(input(': '))
        while inp_size_len > stoper:
            lsst_res += (lst_simbvol[randint(0, len(lst_simbvol)-1)])
            stoper+=1
    except:
        print("Ошибка")
    return lsst_res

while True:
    inp_deis = input('1)Символы\n2)Номер\n3)Буквы\n4)Все сразу\nВыберите действие: ')
    if inp_deis == '1':
        print(randomaizer_sibvol()+'\n')
    elif inp_deis == '2':
        print(randomaizer_num()+'\n')
    elif inp_deis == '3':
        print(randomaizer_abc()+'\n')
    elif inp_deis == '4':
        print(randomaizer_sibvol()+'\n')
    else:
        print("Нет такого варианта!"+'\n')
    inp_res_or_stop = input('1)стоп\n2)Продолжить\nВыберите вариант:')
    if inp_res_or_stop == '1':
        break
    elif inp_res_or_stop == '2':
        continue
    else:
        print('Нет такого варианта')
        break