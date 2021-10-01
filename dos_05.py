# Создан по мотивам DOS 0.9 Бат версии (Bat)
# Не используются все модули, кроме os, random, time
# Оригинал: https://github.com/ArtikUSB/DOS_bat (мой старый проект)

import random
import os
import time

os.system("title DOS Русская версия")
os.system("cls")
print("╔════════════════╗")
print("║  Запуск ДОС'a. ║")
print("╚════════════════╝ ")
os.system("timeout /t 1 /NOBREAK >nul")
os.system("cls")
print("╔════════════════╗")
print("║ Запуск ДОС'a.. ║")
print("╚════════════════╝ ")
os.system("timeout /t 1 /NOBREAK >nul")
os.system("cls")
print("╔═════════════════╗")
print("║ Запуск ДОС'a... ║")
print("╚═════════════════╝ ")
os.system("timeout /t 1 /NOBREAK >nul")
os.system("cls")
print("""╔═════════════════╗
║  Загружено []  ║
║   строчек кода  ║
║ и [] символов ║
╚═════════════════╝""")
os.system("cls")
print("""╔═════════════════╗
║ ДОС Версия 0.9d ║
║    2019-2021    ║
╚═════════════════╝""")

def cmd():
    cmd = input("> ")
    cmd = cmd.lower()
    while cmd != "exit":
        if cmd == "help":
            print("""╔══════════════════════════════╗
║        Помощь по досу        ║
╠══════════════════════════════╣
║help -Помощь                  ║
║ver - Версия Дос`a            ║
║random - Рандомное число      ║
║time - Время и дата           ║
║exit - Выйти из доса          ║
║clear - Очистка сообщений     ║
║history - история DOS         ║
╠══════════════════════════════╣
║          Приложения          ║
╠══════════════════════════════╣
║discord - чат с ботом         ║
╠══════════════════════════════╣
║             Игры             ║
╠══════════════════════════════╣
║games - запуск хелпера игр    ║
╚══════════════════════════════╝""")
            cmd = input("> ")
        if cmd == "ver":
            print("""╔═════════════════╗
║ DOS Версия 0.9b ║
╚═════════════════╝ 
            """)
            cmd = input("> ")

        if cmd == "random":
            rnd_n = random.randint(1,100)
            if len(str(rnd_n)) == 1:
                print(f"""╔══════════════╗
║      {rnd_n}       ║
╚══════════════╝""")
            elif len(str(rnd_n)) == 2:
                print(f"""╔══════════════╗
║      {rnd_n}      ║
╚══════════════╝""")  
            else:
                print(f"""╔═══════════════╗
║      {rnd_n}      ║
╚═══════════════╝""") 
            cmd = input("> ")

        if cmd == "time":
            def day():
                global test
                test = time.strftime("%A")
                if test == "Saturday":
                    return 'Сб'
                elif test == "Monday":
                    return 'Пн'
                elif test == "Tuesday":
                    return 'Вт'
                elif test == "Wednesday":
                    return 'Ср'
                elif test == "Thursday":
                    return 'Чт'
                elif test == "Friday":
                    return 'Пт'
                elif test == "Sunday":
                    return 'Вс'
                else:
                    return test
            num = time.strftime("%d.%m")
            s = time.strftime("%H:%M")
            print(f"""╔═════════════════════════╗
║  Дата: {day()} {num}.{time.strftime("%Y")} Г  ║
║  Время: {s}           ║
╚═════════════════════════╝""")
            cmd = input("> ")

        if cmd == "clear":
            print("""╔════════════════════╗
║ Выполнение очистки ║
╚════════════════════╝""")
            os.system("timeout /t 2 /nobreak >nul")
            os.system("cls")
            print("""╔════════════════════╗
║ очистка выполнена! ║
╚════════════════════╝""")
            os.system("timeout /t 2 /nobreak >nul")
            os.system("cls")
            print("""╔═════════════════╗
║ ДОС Версия 0.9d ║
║    2019-2021    ║
╚═════════════════╝""")
        if cmd == "discord":
            os.system("cls")
            print("(0) Загрузка дискорда")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(10) Загрузка дискорда.")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(20) Загрузка дискорда..")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(30) Загрузка дискорда...")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(40) Загрузка дискорда....")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(50) Загрузка дискорда.....")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(60) Загрузка дискорда......")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(70) Загрузка дискорда.......")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(80) Загрузка дискорда........")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(90) Загрузка дискорда.........")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("(100) Загрузка дискорда.........")
            os.system("timeout /t 1 /nobreak >nul")
            os.system("cls")
            print("""╔═════════════════╗
║Добро пожаловать!║
╚═════════════════╝ """)
            mail = input("Имя-Бота: ")
            mess = input("Сообщение Бота:")
            while True:
                if mess.lower() == "хай":
                    print("Bot: Хай!")
                    mess = input("Сообщение Бота:")
                if mess.lower() == "пока":
                    print("Увидемся в следующий раз!")
                    os.system("timeout /t 3 /nobreak >nul")
                    break

                else:
                    print(mail,":",mess)
                    mess = input("Сообщение Бота:")
        
        if cmd == "history":
            print("""╔══════════════════════════════════════════════════════╗
║                      История                         ║
╠══════════════════════════════════════════════════════╣
║ 0.1 - Первое обновление                              ║
║ 0.2b - Добавленно больше команд                      ║
║ 0.3b - Мелкие поправления с кодом                    ║
║ 0.4 - (УБРАНО) Появилась поддержка                   ║
║ Windows 2000 и Windows xp                            ║
║ 0.5d - Добавлена поддержка стандартных               ║
║ игр Windows 2000, XP 7, Добавленная команда clear,   ║
║ Теперь ещё можно выходить из discord где чат с ботом ║
║ (Команда Exit Discord).                              ║
║ 0.9d - Используемая версия. Перепись кода на Python  ║
║ (Стандартные комманды выполняються через os либо     ║
║ специальными модулями (типа: time, random) )         ║
╚══════════════════════════════════════════════════════╝""")
            cmd = input("> ")

        if cmd == "games":
            print("""╔═════════════════════════════════╗
║           Запускаю...           ║
╚═════════════════════════════════╝ """)
            os.system("timeout /t 3 /nobreak >nul")
            os.system("cls")
            print("""╔═════════════════════════════════╗
║        Хелпер по играм          ║
╠═════════════════════════════════╣
║         Игры Windows 7          ║
╠═════════════════════════════════╣
║    chess - играть в шахматы     ║
║   freecell - играть в солитер   ║
║     hearts - играть в червы     ║
║    mahjong - играть в маджонг   ║
║     mines - играть в сапер      ║
║ purble - играть в Purble Place  ║
║   solitaire - играть в косынку  ║
║     spider - играть в паук      ║
╠═════════════════════════════════╣
║        Игры Windows XP          ║
╠═════════════════════════════════╣
║   pinball - играть в пинбол     ║
║   soliter - играть в солитер    ║
║   heartsxp - играть в червы XP  ║
║   minesXP - играть в сапер XP   ║
║   spiderXP - играть в паук XP   ║
╚═════════════════════════════════╝""")

            print("""╔═════════════════════════════════════╗
║ Чтобы вернутся в                    ║
║ Дос, команда: dos_e ║
╚═════════════════════════════════════╝""")
            while True:
                d = input("> ")
                d = d.lower()
                if d == "dos_e":
                    print("""╔════════════════╗
    ║    Выходим...  ║
    ╚════════════════╝  """)
                    os.system("timeout /t 1 /nobreak >nul")
                    break
                if d == "chess":
                    os.system("start Games\Windows_7\Chess\chess.exe")
                if d=="soliter":
                    os.system("start Games\WinXP\soliter.exe")
                if d=="heartsXP":
                    os.system("start Games\WinXP\hearts.exe")
                if d=="spiderXP":
                    os.system("start Games\WinXP\spider.exe")
                if d=="minesXP":
                    os.system("start Games\WinXP\Mineswepper.exe")
                if d=="pinball":
                    os.system("start Games\WinXP\Pinball\pinball.exe")
                if d=="freecell":
                    os.system("start Games\Windows_7\FreeCell\FreeCell.exe")
                if d=="hearts":
                    os.system("start Games\Windows_7\Hearts\Hearts.exe")
                if d=="mahjong":
                    os.system("start Games\Windows_7\Mahjong\Mahjong.exe")
                if d=="mines":
                    os.system("start Games\Windows_7\Mineswepper\Mineswepper.exe")
                if d=="purble":
                    os.system("start Games\Windows_7\Purble_Place\PurblePlace.exe")
                if d=="solitaire":
                    os.system("start Games\Windows_7\Solitaire\Solitaire.exe")
                if d=="spider":
                    os.system("start Games\Windows_7\SpiderSolitaire\SpiderSolitaire.exe")

        else:
            print("""╔═════════════════════════╗
║  Я не знаю этой команды ║
╚═════════════════════════╝""")
            cmd = input("> ")


    print("""╔════════════════╗
    ║    Выходим...  ║
    ╚════════════════╝ """)
    os.system("timeout /t 1 /nobreak >nul")
    exit()
cmd()