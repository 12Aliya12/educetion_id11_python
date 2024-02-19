text = input()
long = float(len(text))
rubl = int(long * 40) // 100
kop = int(long * 40) % 100
print(str(rubl) + " p." + str(kop) + "коп.")