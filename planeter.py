
class Planet:
    " En klasse for å beskrive en planet"
    def __init__(self,navn:str,solavstand:float,radius:float) -> None:

        self.navn=navn
        self.solavstand=solavstand
        self.radius = radius

jorden = Planet( "Jorden", 152, 6371)



