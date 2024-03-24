#Prosi użytkownika o wprowadzenie wagi w kilogramach i wzrostu w metrach.
#Oblicza BMI i wyświetla kategorię BMI (niedowaga, prawidłowa masa ciała, nadwaga, otyłość).

print("Witamy w programie - Kalkulator BMI")

waga = int(input("Podaj swoją wage w kg ="))
wzrost = float(input("Podaj swój wzrost w m ="))
kategoria = "kategoria"

print()

bmi = waga / (wzrost*wzrost)

if (bmi < 18.50):
    kategoria = "niedowaga"
if (bmi > 18.50 and bmi < 25):
    kategoria = "waga prawidłowa"
if (bmi > 25 and bmi < 30):
    kategoria = "nadwaga"
if (bmi > 30):
    kategoria = "otyłość"
    

print("Twoje BMI wynosi", round(bmi,2), "twoja kategoria BMI to", kategoria)
