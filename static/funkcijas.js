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
let atminetais = ""

function uzzimetVardu(){
    minamaisVards = document.getElementById("vards").textContent
    console.log(minamaisVards)
    for(burts of minamaisVards){
        atminetais +="_ "
    }
    console.log(atminetais)
}