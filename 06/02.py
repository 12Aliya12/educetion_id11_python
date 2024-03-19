chislo_city = int(input())
name_city = set()
last_name_city = set()
for i in range(chislo_city):
    name_city.add(input())
last_name_city.add(input())
povt = name_city & last_name_city
if povt:
    print("TRY ANOTHER")
else:
    print("OK")