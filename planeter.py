
class Planet:
    " En klasse for å beskrive en planet"
    def __init__(self,navn:str,solavstand:float,radius:float) -> None:

        self.navn=navn
        self.solavstand=solavstand
        self.radius = radius

jorden = Planet( "Jorden", 152, 6371)

# Oppgave 1: 
# Lag et objekt for Mars, Jupiter og Jorda, der du lagrer informasjon om navn, solavstand og radius. Lagre disse objektene i egne variabler

# Hva skjer om du skriver print(Jorda)?
# Hva skjer om du skriver print(Jorda.navn)?
# Prøv å skriv ut de andre attributtene til klassen

# OBS: pass på rekkefølgen i argumentene til konstruktøren.


