class motorsykkel:
    def __init__(self, merke, hastighet, km):
        self.merke = merke
        self.hastighet = hastighet
        self.km = km

    def kjører(self, nyDistanse):
        self.km += nyDistanse
    
    def sykkelen(self):
        return print("Sykkelen er en", self.merke, "har kjørt", self.km, "km")

motorsykkel1 = motorsykkel("Harley", 180, 18000)
motorsykkel1.kjører(200)
motorsykkel1.sykkelen()

print(motorsykkel1.merke, motorsykkel1.hastighet, motorsykkel1.km) # var litt uskikker om du ønsket at jeg skulle printe ut hele, men jeg gjorde det bare.