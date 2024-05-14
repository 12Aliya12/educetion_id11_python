menu = ["щи", "борщ", "щавельный суп", "овсяной суп", "суп по-чабански"]
for i in range(int(input())):
    print(menu[i%5])