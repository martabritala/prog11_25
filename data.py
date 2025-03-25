def ierakstit(teksts):  #Funkcija, lai failā ierakstītu tekstu
    fails = open("teksts.txt", "w", encoding='utf-8')
    fails.write(teksts)
    fails.write('\n')
    fails.close()

# ierakstit("Man iet labi!")

def klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts)
    fails.write('\n')
    fails.close()

# klat("Man arī")

def nolasit():
    fails = open("teksts.txt","r", encoding="utf-8")
    viss = fails.readlines()
    print(viss[0])

# nolasit()

def uztaisit_vienu_spamu(vards, vecums, dz):
    if dz == "s":
        galotne = "usi"
    else:
        galotne = "is"
    teksts = f"Sveiki, {vards}!\nJūs esat laimēj{galotne} {int(vecums)*10} EUR!"
    with open(f"spams/{vards}.txt", "w", encoding="utf-8") as fails:
        fails.write(teksts)

# uztaisit_vienu_spamu("Kate", 12, "s")

def viss_spams():
    with open("vardi.txt", "r", encoding="utf-8") as f:
        visi = f.readlines()
        for viens in visi:
            info = viens.split()
            print (info[0]) #Uzdevums - šo rindiņu nomainīt tā, lai izveidojas spama vēstule!

viss_spams()