/*
Karātavu spēles process:
1. Jāuzzina meklējamais vārds, jāuzzīmē svītriņas, pirmais burts(?) uz ekrāna
Katru reizi, kad cilvēks piespiež pogu:
2. Jāuzzina, kura poga nospiesta (burts), 
3. Izslēdz, lai pogu nevar nospiest
4. Jāatrod visas vietas, kur burts ir vārdā (ja nav, pāriet uz 7.punktu)
5. Nomaina svītriņas pret burtu ekrānā
6. Jāpārbauda, vai nav atminēts vārds
7. Ja burts nav vārdā: Pazūd dzīvība
8. Jāpārbauda, vai spēlētājs nav zaudējis.
*/
let minamaisVards = ""
let atminetais = []
let dzivibas = 5

function uzzimetVardu(){
    minamaisVards = document.getElementById("vards").textContent.trim().toUpperCase()
    console.log(minamaisVards)
    for(burts of minamaisVards){
        atminetais.push("_") 
    }
    console.log(atminetais)
    document.getElementById("vardaVieta").innerHTML = atminetais.join(" ")
    document.getElementById("dzivibas").innerHTML = dzivibas
}

function minetBurtu(burts){
    document.getElementById(burts).disabled=true
    let atrada = -1
//Meklēšana, ja atrodas burts, tad atrada=0
    burts = burts.toUpperCase()
    for(indekss in minamaisVards){
        console.log(indekss)
        if(minamaisVards[indekss] == burts){
            atrada = 0
            atminetais[indekss] = burts
            console.log(burts, atminetais[indekss])
        }
    }
    dzivibas += atrada
    document.getElementById("vardaVieta").innerHTML = atminetais.join(" ")
    document.getElementById("dzivibas").innerHTML = dzivibas
}