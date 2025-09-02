karakterer = {
    "Eirik" : 6,
    "Henrik" : 5,
    "Jonas" : 4,
    "Ayman" : 3,
    "David" : 2,
    "Aryan" : 1,
}
total = 0
with open("karakterer.txt", "w") as fil:
    for i, j in list(karakterer.items()):
        fil.write(f"{i} {j} \n")
        total += j
        gjennomsnitt = total / len(karakterer)
    print("Gjennomsnitts karakteren er",gjennomsnitt)

with open("karakterer.txt", "r") as f:
    innhold = f.read()
    print(innhold)







