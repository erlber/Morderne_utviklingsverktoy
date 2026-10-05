navn = input("Hva heter du? ")
alder = input("Hvor gammel er du? ")

if alder >= 18:
    print(f"{navn} er myndig")
else:
    print(f"{navn} er ikke myndig")