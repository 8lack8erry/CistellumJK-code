# Cistellum Judo-Karate Attendance Tracker

![Cistellum Judo-Karate Logo](Progetto%20senza%20titolo.png)

Questo repository contiene un programma Python sviluppato per la società sportiva **Cistellum Judo-Karate**. Il codice permette di analizzare la frequenza di coach e atleti ai corsi offerti dalla società, elaborando classifiche e statistiche mensili.

## Funzionalità

- **Conteggio ore**: Calcola il totale di ore per ogni coach e atleta in base alle loro presenze registrate.
- **Classifica mensile**: Genera una classifica degli atleti basata sul numero di presenze.
- **Filtro date**: Gestisce doppie registrazioni selezionando solo l'ultima compilazione del modulo.
- **Output organizzato**: Salva i risultati in un file `.txt` suddiviso per mese.

## Come Utilizzare il Programma
Assicurati che i dati siano organizzati in un file `.csv` con le seguenti colonne:
  - **Informazioni cronologiche**: Data in formato `DD/MM/YYYY` (per la lingua italiana) o `MM/DD/YYYY` (per l'inglese).
  - **Coach**: Nomi dei coach separati da virgole.
  - **Atleti**: Nomi degli atleti separati da virgole
Gli ultimi due punti sono verificati di default se scarichi il file come `.csv` da google moduli

