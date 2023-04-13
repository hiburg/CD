CD ASSIGNMENT 

Voor deze opdracht heb ik een VPS server opgezet bij Digital Ocean. Hierop heb ik een simpele Flask applicatie draaien. Als ik nu een wijziging aan de Flask applicatie uitvoer, dan is het de bedoeling dat deze applicatie automatisch geupdated wordt op de VPS nadat ik mijn wijzigingen via git push naar github. Hiervoor heb ik de volgende elementen in mijn oplossing gebruikt:


GITHUB ACTIONS:
In de map .github/workflows op github staat een file “deploy.yml”. Dit bestand bevat de acties die uitgevoerd worden nadat een wijziging via git push naar github wordt doorgezet. Dit bestand bestaat uit 2 jobs (“run-tests” en “deploy”) en elke job bestaat uit een aantal steps. Als eerste wordt de job “run-tests” gestart. Deze stelt de applicatie beschikbaar voor github (step checkout) en daarna wordt de Flask applicatie geïnstalleerd en worden er tests op uitgevoerd via pytest.
Alleen als de step “run-tests” succesvol geeindigd is, wordt de volgende job “deploy” uitgevoerd, dit heb ik geregeld door middel van de needs: parameter.
In de volgende job “deploy” wordt daadwerkelijk aangelogd op de server en wordt de applicatie bijgewerkt en opnieuw opgestart zodat de wijzigingen direct beschikbaar zijn.


SSH-KEYS:
Voor het aanloggen vanaf github op de VPS heb ik gebruik gemaakt van SSH keys. Hiervoor heb ik lokaal een RSA key gegenereerd die bestaat uit een public en een private key. De public key (het “slot”) heb ik geplaatst in de map .ssh onder de map root op de VPS. Deze public key heb ik daar toegevoegd aan het bestand authorized_keys.
De private key (de “sleutel”) staat op mijn laptop onder Windows 10 (in de map .ssh onder User) en ook in Github onder Secrets (zie hierna).


GITHUB-SECRETS:
Aangezien je niet wilt dat in de .yml file login gegevens staan, heb ik dit opgelost door deze gegevens veilig op te slaan in Github secrets. Dit is een onderdeel van Github actions. Ik heb zowel de SSH private key, de username (root), het ip-adres van de VPS (host) als ook het poortnummer (port 22) toegevoegd in deze secrets. In de deploy.yml worden deze secrets daarna dan uitgelezen.



Een uitdaging voor deze assignment was het werken met het Ubuntu OS. Hiervoor heb ik wel even moeten oefenen met de diverse commando’s (ls etc) om te zien hoe dit werkte. Ik had nog een probleem met de .service file van mijn Flask applicatie onder Gunicorn. Ik kreeg een foutmelding (code 200) bij het opstarten van de service. Via google kwam ik erachter dat ik dit op kon lossen door “User=root” toe te voegen aan het bestand CD.service in de map \etc\systemd\system.
Nadat ik dit gedaan had werkte de VPS als bedoeld. Als ik nu een wijziging doorvoer op de Flask applicatie en deze dan push naar github wordt de server bijgewerkt en na een herstart is de wijziging zichtbaar. 
Ik heb voor het uitvoeren van de laatste acties in de deployment geen gebruik gemaakt van een .SH bestand maar deze acties in de .yml gezet zodat ze voor Winc ook zichtbaar zijn. Daarnaast leek het me beter om dit in de .yml te hebben dan in een .sh file op de server (bij een crash o.i.d. van de server zou je dan immers de .sh file kwijt zijn).
