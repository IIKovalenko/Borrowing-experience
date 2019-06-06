#ЗДЕСЬ ПЕРЕЧИСЛЕНЫ СТАТИЧЕСКИЕ ДАННЫЕ public service
#Газ
gas = 67.64
#Домофон
domofon = 38
#Места общего пользования
common_areas = 127.25
#Содержание
content = 469.65
#Капитальный ремонт
overhaul = 196.95
#Отопление
heat = 932.63
#Сумма
total_static = gas + domofon + common_areas + content + overhaul + heat

print("Газ: ", gas, "рублей")
print("Домофон: ", domofon, "рублей")
print("Места общего поьзования: ", common_areas, "рублей")
print("Содержание: ", content, "рублей")
print("Капитальный ремонт: ", overhaul, "рублей")
print("Отопление: ", heat, "рублей")
print()
print("Итого: ",total_static, "рублей")
print()

#ЗДЕСЬ ПЕРЕЧИСЛЕНЫ ИЗМЕНЯЕМЫЕ ДАННЫЕ
#Горячая вода
hot_water_value = int(input("Введите количесво кубов горячей воды: "))
hot_water_index = 153.08
hot_water_total = hot_water_value * hot_water_index
print(hot_water_total, "рублей")

#Холодная вода   
cold_water_value = int(input("Введите количество кубов холодной воды: "))
cold_water_index = 21.89
cold_water_total = cold_water_value * cold_water_index
print(cold_water_total, "рублей")

#Канализация
sewerage_value = int(input("Введите сумму кубов горячей и холодной воды: "))
sewerage_index = 15.62
sewerage_total = sewerage_value * sewerage_index
print(sewerage_total, "рублей")

#Электричество
electricity_value = int(input("Введите количество КВ: "))
electricity_index = 4.8
electricity_total = electricity_value * electricity_index
print(electricity_total, "рублей")

#Коммуналка
utilities = total_static + hot_water_total + cold_water_total + sewerage_total + electricity_total
print("Коммунальные услуги составляют: ",utilities, "рублей")

#Аренда
rent = 82000
print("Аренда составляет: ",rent, "рублей")
print()

#Итоговая сумма
sum = utilities + rent

print("Итого: ", sum, "рублей" )

