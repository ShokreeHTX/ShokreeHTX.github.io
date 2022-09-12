print("Hvor mange dollars vil du væksle?")

mdollar = input()
if int(mdollar) < 0.5 :
    print("naah thats to little")
else :
    print("Du får " + str(int(mdollar) * 0.98 * 0.98) + " euro efter kommision")