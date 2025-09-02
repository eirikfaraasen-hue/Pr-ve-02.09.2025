def gjennomsnitt(liste):
    if liste:
        snittet = sum(liste) / len(liste)
        print(snittet)
    else:
        print("listen var tom")
    
gjennomsnitt([10,20,30])
gjennomsnitt([10,50,70])
gjennomsnitt([])
