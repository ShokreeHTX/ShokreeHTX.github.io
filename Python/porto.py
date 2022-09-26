print("Hvor meget vejer din brev")
vægt = input("Vægten ") #her skriver man vægtne på brevet
if vægt < 50:
    print("Dit brev koster 12 kr at sende")
else :
    print("Dit brev koster " + vægt * 4,166)
