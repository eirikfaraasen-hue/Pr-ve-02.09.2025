alder = int(input("Skriv inn alderen din slik at du kan få en billetpris "))
if alder < 12:
    print("Billetprisen din er 80kr")
elif alder <= 17:
    print("Billetprisen din er 100kr")
else:
    print("Billetprisen din er 140kr")