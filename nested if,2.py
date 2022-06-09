age=int(input("enter age"))
sex=input("enter sex")
marital=input(" are you merried")
if sex=="M":
    if age>=20 and age<40:
        print("he may work anywhere")
    elif age>=40 and age<60:
     print("he will work in urban area")
    else:
        print("he was married ")
elif sex==("F"):
    print("she will work only in urban")
else:
    print("error")
