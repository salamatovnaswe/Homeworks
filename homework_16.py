# H-1
age = int(input("Jasinizdi kiriting: "))
if age >= 18:
    print("Siz erjetkensiz! ")
else:
    print("Siz erjetpegensiz! ")

# H-2
parol = int(input("Paroldi kiriting: "))
if parol == "python123":
    print("Xosh kelipsiz! ")
else:
    print("Parol naduris! ")

# H-3
baha = int(input("Bahasin kiriting: "))
if baha > 500000:
    chegirme = int(baha * 10)
else:
    chegirme = 0
uliwma_baha = baha - chegirme
print(f"Chegirme: {chegirme} som")
print(f"Uliwma baha: {uliwma_baha} som")

# H-4
araliq = int(input("Aralıqtı kirgiziń: "))

if araliq > 10:
    km_bahasi = 3000
else:
    km_bahasi = 2000

uliwma_bahasi = araliq * km_bahasi

print(f"1 km bahası: {km_bahasi} swm.")
print(f"Ulıwma bahası: {uliwma_bahasi} sum.")

# H-5
bahasi = int(input("Buyırtpa bahası: "))
jetkerip_beriw = 15000
jami_tolem = bahasi + jetkerip_beriw
if bahasi > 100000:
    print("Jetkiziw biypul!")
else:
    print(f"Jetkerip beriw: {jetkerip_beriw} sum.")
    print(f"Jámi tólem: {jami_tolem} sum.")

# H-6
ball = int(input("Ballingizni kiriting: "))

if 90 <= ball <= 100:
    baho = "A'lo"
elif 75 <= ball <= 89:
    baho = "Yaxshi"
elif 60 <= ball <= 74:
    baho = "Qoniqarli"
elif 0 <= ball <= 59:
    baho = "Qoniqarsiz"
else:
    baho = "Noto'g'ri ball kiritildi!"

print(f"Sizning bahoyingiz: {baho}")

# H-8
mevalar = ["olma", "banan", "uzum", "anor", "shaftoli"]

meva = input("Meva nomini kiriting: ")

if meva in mevalar:
    print(f"{meva} ro'yxatda mavjud!")
else:
    print(f"{meva} ro'yxatda mavjud emas!")

# H-9
oquvchilar = ["Ali", "Vali", "Sardor", "Malika", "Madina"]
ism = input("Ism kiriting: ")
if ism in oquvchilar:
    print("O'quvchi ro'yxatda mavjud!")
    print(f"Birinchi harfi: {ism[0]}")
else:
    print("O'quvchi ro'yxatda topilmadi!")

# H-10
numbers = [12, 5, 8, 17, 20, 3, 10, 7]

for san in numbers:
    if san % 2 == 0:
        print(f"{san} - Jup san")
    else:
        print(f"{san} - Taq san")

# H-11
numbers = [2, 5, 8, 11, 14, 17]

for i in range(len(numbers)):
    if numbers[i] < 10:
        numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5

print(numbers)

# H-12

products = ["Go'sht", "Non", "Sut", "Tuxum", "Guruch"]
prices = [90000, 4000, 12000, 1800, 15000]

print("Mahsulotlar:")
for i in range(len(products)):
    print(f"{i + 1}. {products[i]} - {prices[i]} so'm")

tanlov = int(input("Qaysi mahsulot kerak? "))
indeks = tanlov - 1

miqdor = int(input(f"{products[indeks]} qancha kerak? "))
umumiy_summa = prices[indeks] * miqdor

print(f"Mahsulot: {products[indeks]}")
print(f"Soni: {miqdor}")
print(f"Umumiy summa: {umumiy_summa} so'm")

# H-13
products = ["Non", "Sut", "Go'sht", "Olma", "Banan"]
prices = [4000, 12000, 90000, 8000, 15000]

izlangan = input("Qanday mahsulot olmoqchisiz? ")
topildi = False

for i in range(len(products)):
    if products[i] == izlangan:
        miqdor = int(input(f"{products[i]} qancha kerak? "))
        umumiy_summa = prices[i] * miqdor
        print(f"Umumiy summa: {umumiy_summa} so'm")
        topildi = True
        break
if not topildi:
    print("Bunday mahsulot yo'q!")