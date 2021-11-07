import json
import sys


def finder(dict_name):
    lst = []
    for index_1 in dict_name:
        for index_2 in dict_name[index_1]:
            if type(index_2) is dict:
                lst.append(index_2)
    return lst


def opener(dict_base, lst_index):
    dict_search = finder(dict_base)[lst_index]
    name_loc = tuple(dict_search.keys())[0]
    field_names[0] = name_loc
    field_names[2] -= float(name_loc[name_loc.find('m') + 1:])
    with open('journal.txt', mode='a') as journal:
        str_field_names = field_names.copy()
        str_field_names[1], str_field_names[2] = str(field_names[1]), str(field_names[2])
        journal.write(''.join(str_field_names))
        journal.write('\n')
    print(field_names)
    return dict_search


def fight(dit, num, list_or_not):
    global name
    if list_or_not == 'not':
        name = dit[tuple(dit.keys())[0]][num]
    elif list_or_not == 'list':
        name = dit[tuple(dit.keys())[0]][0][num]
    else:
        print('Ошибка')
    print('Сейчас вы ведете бой с ', name)
    exp = name[name.find('p') + 1:name.find('_t')]
    tm = name[name.find('m') + 1:]
    if type(field_names[1]) is int:
        field_names[1] += int(exp)
    else:
        field_names[1] = int(exp)
    field_names[2] -= float(tm)
    print('Монстр убит \n')
    with open('journal.txt', mode='a') as journal:
        str_field_names = field_names.copy()
        str_field_names[1], str_field_names[2] = str(field_names[1]), str(field_names[2])
        journal.write(''.join(str_field_names))
        journal.write('\n')
    print(field_names)


def while_fight(count, fight_loc, list_or_not):
    counter = 0
    while counter < count:
        comand = input('Ввод: ')
        if comand == 'x':
            if list_or_not == 'not':
                fight(fight_loc, counter, list_or_not='not')
            elif list_or_not == 'list':
                fight(fight_loc, counter, list_or_not='list')
            else:
                break
            counter += 1
            if counter == count:
                print('Вы убили всех монстров тут ')
        elif comand == 'z':
            print('Вы вышли из режима битвы\n')
            break


with open('journal.txt', mode='w') as fil:
    fil.flush()

remaining_time = '1234567890.0987654321'
field_names = ['current_location', 'current_experience', 'current_date']
field_names[2] = float(remaining_time)

with open('rpg.json') as file:
    data = json.load(file)
field_names[0] = tuple(data.keys())[0]
print('Вы в локации 0, тут есть монстр и входы в локации 1 и 2, \n'
      'чтобы убить монстра нажмите "с", чтобы пойти в другие локации введите 1 или 2, \n'
      'для выхода нажмите "z"\n')

while True:

    command = input('Ввод: ')
    if command == 'c':
        fight(data, 0, list_or_not='not')
        print('Теперь вам осталось выбрать в какой проход пойти. \n'
              'Введите 1 или 2\n')
    elif command == '1':
        dit_1 = opener(data, 0)
        print('Вы вошли в локацию 1.\n'
              'Тут два одинаковых монстра, \n'
              'чтобы атаковать их введите "с",\n'
              'также тут проход в следующую локацию, чтобы попасть в нее, введите 3\n')
        while True:
            command = input('Ввод: ')
            if command == 'c':
                print('Вы в режиме битвы, чтобы выйти из него введите "z", \n'
                      'чтобы продолжить битву с монстрaми, введите "x", \n'
                      'всего тут находятся 2 монстра\n')
                while_fight(2, dit_1, list_or_not='not')
            elif command == '3':
                dit_3 = opener(dit_1, 0)
                print('Вы вошли в локацию 3, тут есть только вход в локацию 7, чтобы пойти туда, введите 7, \n'
                      'для выхода из игры введите "z"\n')
                command = input('Ввод: ')
                if command == '7':
                    dit_7 = opener(dit_3, 0)
                    print('Вы вошли в локацию 7, но тут опять только вход в следующую локацию, \n'
                          'чтобы пойти в нее, введите 10, \n'
                          'чтоб выйти из игры введите "z"\n')
                    command = input('Ввод: ')
                    if command == 'z':
                        print(field_names)
                        sys.exit()
                    elif command == '10':
                        dit_10 = opener(dit_7, 0)
                        print('Вы вошли в локацию 10, \n'
                              'тут 4 разных монстра,\n'
                              'чтобы начать бой, введите "с", \n'
                              'также тут есть проход в локацию 12, \n'
                              'чтобы пойти туда, введите 12, \n'
                              'чтоб выйти из игры, введите "z" \n')
                        while True:
                            command = input('Ввод: ')
                            if command == 'c':
                                print('Вы в режиме битвы, чтобы выйти из него введите "z", \n'
                                      'чтобы продолжить битву с монстрaми, введите "x", \n'
                                      'всего тут находятся 4 монстра\n')
                                while_fight(4, dit_10, list_or_not='list')
                                print(
                                    'Теперь вам осталось либо двигаться дальше (введите 12), либо выйти (введите "z")')
                            elif command == 'z':
                                print(field_names)
                                sys.exit()
                            elif command == '12':
                                dit_12 = opener(dit_10, 0)
                                print('Вы вошли в локацию 12 - тут два босса, \n'
                                      'чтобы вступить в бой введите "c", \n'
                                      'чтобы выйти введите "z"\n')
                                while True:
                                    command = input('Ввод: ')
                                    if command == 'z':
                                        print(field_names)
                                        sys.exit()
                                    elif command == 'c':
                                        print('Вы в режиме битвы, чтобы выйти из него введите "z", \n'
                                              'чтобы продолжить битву уже с монстрaми, введите "x", \n'
                                              'всего тут находятся 2 монстра\n')
                                        while_fight(2, dit_12, list_or_not='not')
                                        print(f'Вы дошли до конца подземелья и убили всех монстров'
                                              f' в выбранном вами направлении{field_names}')
                                        sys.exit()

    elif command == '2':
        dit_2 = opener(data, 1)
        print('Вы вошли в локацию 2.\n'
              'Тут есть один монстр, \n'
              'чтобы атаковать введите "c", \n'
              'также тут проходы в локации 4, 5 и 6 (введите номер локации, чтобы войти в нее)\n')
        while True:
            command = input('Ввод: ')
            if command == 'c':
                fight(dit_2, 0, 'not')
                print('Монстров больще нет, но тут проходы в локации 4, 5 и 6 '
                      '(введите номер локации, чтобы войти в нее)\n')
            elif command == 'z':
                print(field_names)
                sys.exit()
            elif command == '4':
                dit_4 = opener(dit_2, 0)
                print('Вы вошли в локацию 4.\n'
                      'Тут 4 монстра, \n'
                      'чтобы атаковать их введите "c", \n'
                      'чтобы выйти из игры, введите "z"\n')
                while True:

                    command = input('Ввод: ')
                    if command == 'c':
                        print('Вы в режиме битвы, чтобы выйти из него введите "z", \n'
                              'чтобы продолжить битву с монстрaми, введите "x", \n'
                              'всего тут находятся 3 монстра\n')
                        while_fight(3, dit_4, list_or_not='not')
                        print('Все монстры убиты, но вы зашли в тупик')
                        print(field_names)
                        sys.exit()
                    elif command == 'z':
                        sys.exit()
            elif command == '5':
                dit_5 = opener(dit_2, 1)
                print('Вы вошли в локацию 5.\n'
                      'Тут проходы в локации 8 и 9, \n'
                      'чтобы пройти, введите номер локации, \n'
                      'чтобы выйти из игры, введите "z"\n')
                while True:
                    command = input('Ввод: ')
                    if command == 'z':
                        print(field_names)
                        sys.exit()
                    elif command == '8':
                        while True:
                            dit_8 = opener(dit_5, 0)
                            print('Вы вошли в локацию 8.\n'
                                  'Тут 5 монстров, \n'
                                  'чтобы вступить в бой, введите "с"\n'
                                  'чтобы выйти из игры, введите "z"\n')
                            command = input('Ввод: ')
                            if command == 'c':
                                print('Вы в режиме битвы, чтобы выйти из него введите "z", \n'
                                      'чтобы продолжить битву с монстрaми, введите "x", \n'
                                      'всего тут находятся 5 монстра\n')
                                while_fight(5, dit_8, list_or_not='not')
                                print('Все монстры убиты')
                            elif command == 'z':
                                print(field_names)
                                sys.exit()
                    elif command == '9':
                        dit_9 = opener(dit_5, 1)
                        print('Вы вошли в локацию 9.\n'
                              'Тут 1 монстр и проход в локацию 11, \n'
                              'чтобы вступить в бой, введите "c", \n'
                              'чтобы пойти в следующую локацию, введите 11, \n'
                              'чтобы выйти из игры, введите "z"\n')
                        while True:

                            command = input('Ввод: ')
                            if command == 'z':
                                fight(dit_9, 0, list_or_not='not')
                            elif command == 'z':
                                print(field_names)
                                sys.exit()
                            elif command == '11':
                                dit_11 = opener(dit_9, 0)
                                print('Вы вошли в локацию 11.\n'
                                      'Тут 1 монстр-босс и проход в локацию В2, \n'
                                      'чтобы вступить в бой, введите "с", \n'
                                      'чтобы пойти в следующую локацию, введите В2, \n'
                                      'чтобы выйти из игры, введите "z"\n')
                                while True:
                                    command = input('Ввод:')
                                    if command == 'c':
                                        fight(dit_11, 0, list_or_not='not')
                                    elif command == 'z':
                                        print(field_names)
                                        sys.exit()
                                    elif command == 'b2' or command == 'B2':
                                        dit_b2 = opener(dit_11, 0)
                                        print('Вы вошли в локацию B2.\n'
                                              'Тут 3 монстра, \n'
                                              'чтобы вступить в бой, введите "c", \n'
                                              'чтобы выйти из игры, введите "z"\n')
                                        while True:
                                            command = input("Ввод: ")
                                            if command == 'z':
                                                print('Вы в режиме битвы, что бы выйти из него введите "z", \n'
                                                      'чтобы продолжить битву уже с монстрaми введите "x", \n'
                                                      'всего тут находятся 3 монстра\n')
                                                while_fight(3, dit_b2, list_or_not='not')
                                                print(field_names)
                                                print('Вы дошли до конца подземелья и убили всех монстров'
                                                      ' в выбранном вами направлении')
                                                sys.exit()
                                            elif command == 'z':
                                                print(field_names)
                                                sys.exit()
            elif command == '6':
                dit_6 = opener(dit_2, 2)
                print('Вы вошли в локацию 6.\n'
                      'Тут 1 монстр-босс и вход в локацию В1, \n'
                      'чтобы вступить в бой, введите "c"\n'
                      'чтобы перейти в следующую локацию, введите В1, \n'
                      'чтобы выйти из игры, введите "z"\n')
                while True:
                    command = input('Ввод: ')
                    if command == 'z':
                        print(field_names)
                        sys.exit()
                    elif command == "c":
                        fight(dit_6, 0, list_or_not='not')
                    elif command == 'B1' or command == 'b1':
                        dit_b1 = opener(dit_6, 0)
                        print('Вы вошли в локацию B1.\n'
                              'Тут 5 монстров, \n'
                              'чтобы вступить в бой, введите "c", \n'
                              'чтобы выйти из игры, введите "z"\n')
                        while True:
                            command = input('Ввод: ')
                            if command == 'c':
                                print('Вы в режиме битвы, чтобы выйти из него введите "z", \n'
                                      'чтобы продолжить битву уже с монстрaми введите "x", \n'
                                      'всего тут находятся 5 монстров\n')
                                while_fight(5, dit_b1, list_or_not='not')
                                print(field_names)
                                print('Вы зашли в тупик')
                                sys.exit()
                            elif command == 'z':
                                print(field_names)
                                sys.exit()

    elif command == 'z':
        print(field_names)
        break
