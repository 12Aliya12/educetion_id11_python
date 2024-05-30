def ask_password():
    password = "password"
    i = 0
    vod_paroll = input()
    while i != 2:
        if vod_paroll == password:
            print("Пароль принят")
        else:
            vod_paroll = input()
        i +=1
    print("В доступе отказано")


ask_password()