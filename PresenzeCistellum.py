import pandas as pd

lingua = "IT"  # EN
filtro_date = True  # Tiene conto della possibilità che ci siano doppie compilazioni del modulo
# In modo da non avere double counting si tiene in memoria solo l'ultima compilazione del modulo

def string_to_list(input_string):
    return [name.strip() for name in input_string.split(",")]


def count_names(nested_list):  # ritorna un dictionary del tipo: {'Andrea' = 2, 'Samuele' = 4, ...}
    name_counts = {}
    for sublist in nested_list:
        for name in sublist:
            if name in name_counts:
                name_counts[name] += 1
            else:
                name_counts[name] = 1
    return name_counts


def TotaleOre(vec):
    Presenze = []
    for x in vec:
        PresenzeGiornaliere = string_to_list(x)
        Presenze.append(PresenzeGiornaliere)

    NumeroPresenze = count_names(Presenze)  # dictionary contenente nome coach e numero presenze
    return NumeroPresenze


def ordinamento(listaTuple):
    return sorted(listaTuple, key=lambda x: x[1], reverse=True)


def CostruzioneClassifica(presenze):  # presenze è un vettore di tuple [('Andrea', 3), ('Samuele', 4), ...]
    classifica = []
    posizione = 0

    for i in range(len(presenze)):
        if presenze[i][1] == presenze[i - 1][1] and i != 0:  # viene assegnata la stessa posizione se il numero presenze è uguale
            classifica.append((posizione, presenze[i][0], presenze[i][1]))
        else:
            posizione += 1
            classifica.append((posizione, presenze[i][0], presenze[i][1]))
    return classifica


def data_filter(vec_ini, filter):
    max_range = len(vec_ini) - 1
    vec = []
    for i in range(max_range):
        if filter[i] != filter[i + 1]:
            vec.append(vec_ini[i])

    vec.append(vec_ini[max_range])
    return vec

NomeCorso = input("Inserire il nome del corso:\t")
NomeFile = input("\nInserire il nome del file '.csv':\t")
tab = pd.read_csv(NomeFile + ".csv")

date = tab["Informazioni cronologiche"]

giorni = []
mesi = []
if lingua == "IT":
    giorni = [data[:2] for data in date]
    mesi = [data[3:5] for data in date]
elif lingua == "EN":
    giorni = [data[3:5] for data in date]
    mesi = [data[:2] for data in date]

# Filtro date
if filtro_date:
    coach = data_filter(tab["Coach"], giorni)
    atleti = data_filter(tab["Atleti"], giorni)
    mesi = data_filter(mesi, giorni)
else:
    coach = tab["Coach"]
    atleti = tab["Atleti"]

# Calcolo ore per ogni mese
nomi_mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
ore_x_mese = {}

for mese in range(1, 13):
    mese_str = f"{mese:02}"  # Formatto il mese come stringa a due cifre
    coach_mensile = [coach[i] for i in range(len(mesi)) if mesi[i] == mese_str]
    atleti_mensili = [atleti[i] for i in range(len(mesi)) if mesi[i] == mese_str]

    if coach_mensile and atleti_mensili:
        NumeroOreAtleti = TotaleOre(atleti_mensili)
        NOAasLista = list(NumeroOreAtleti.items())  # Trasforma il dictionary in una lista di tuple
        classifica = CostruzioneClassifica(ordinamento(NOAasLista))

        NumeroOreCoach = TotaleOre(coach_mensile)
        ore_x_mese[nomi_mesi[mese - 1]] = {"classifica": classifica, "ore_coach": NumeroOreCoach}

# Stampa dei risultati
nome_file_destinazione = "Risultati_" + NomeCorso

with open(nome_file_destinazione + ".txt", "w") as file:
    for mese, risultati in ore_x_mese.items():
        file.write(f"=== Risultati per {mese} ===\n")
        file.write("Totale ore coach\n")
        for Allenatore, ore in risultati["ore_coach"].items():
            file.write(Allenatore + "\t" + str(ore) + "\n")

        file.write("\nClassifica\tNome\tNumero presenze\n")
        for risultato in risultati["classifica"]:
            file.write(str(risultato[0]) + "\t" + str(risultato[1]) + "\t" + str(risultato[2]) + "\n")
        file.write("\n")

print("\nClassifica completata\n")
