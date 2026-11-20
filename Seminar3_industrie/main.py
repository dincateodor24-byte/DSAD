import os
import pandas as pd

os.makedirs("data_out", exist_ok=True)

industrie = pd.read_csv("data_in/IndustriaAlimentara.csv")
populatie = pd.read_csv("data_in/PopulatieLocalitati.csv")
coduri_judete = pd.read_csv("data_in/Coduri_Judete.csv")

activitati = list(industrie.columns[2:])

# Cerinta 1
total_angajati = industrie[activitati].sum(axis=1)
cerinta1 = industrie[total_angajati > 0]
cerinta1.to_csv("data_out/Cerinta1.csv", index=False)

# Cerinta 2
# Procentul se calculeaza doar pentru localitatile cu cel putin un angajat,
# pentru ca la cele cu 0 angajati ar iesi impartire la 0.
suma_pe_linie = cerinta1[activitati].sum(axis=1)
procente = cerinta1[activitati].div(suma_pe_linie, axis=0) * 100
cerinta2 = cerinta1[["Siruta", "Localitate"]].copy()
for activitate in activitati:
    cerinta2[activitate] = procente[activitate]
cerinta2.to_csv("data_out/Cerinta2.csv", index=False)

# Tabel comun: angajati + judet + populatie pentru fiecare localitate
date = industrie.merge(populatie[["Siruta", "Judet", "Populatie"]], on="Siruta")

# Totaluri pe judet
pe_judet = date.groupby("Judet")[activitati + ["Populatie"]].sum()

# Cerinta 3
angajati_judet = pe_judet[activitati].sum(axis=1)
pondere = angajati_judet / pe_judet["Populatie"]
cerinta3 = pondere.sort_values(ascending=False)
cerinta3.name = "Pondere"
cerinta3.to_csv("data_out/Cerinta3.csv")

# Cerinta 4
cerinta4 = pe_judet[activitati].idxmax(axis=1)
cerinta4.name = "Activitate"
cerinta4.to_csv("data_out/Cerinta4.csv")

# Cerinta 5
date_regiuni = date.merge(coduri_judete[["IndicativJudet", "Regiune"]], left_on="Judet", right_on="IndicativJudet")
rezultate = {}
for regiune, grup in date_regiuni.groupby("Regiune"):
    ponderi = grup["Populatie"] / grup["Populatie"].sum()
    rezultate[regiune] = grup[activitati].mul(ponderi, axis=0).sum()
cerinta5 = pd.DataFrame(rezultate).T
cerinta5.index.name = "Regiune"
cerinta5.to_csv("data_out/Cerinta5.csv")

# Cerinta 6
total_national = pe_judet.sum()
pondere_activitate = pe_judet[activitati].div(total_national[activitati], axis=1)
pondere_populatie = pe_judet["Populatie"] / total_national["Populatie"]
cerinta6 = pondere_activitate.div(pondere_populatie, axis=0)
cerinta6.to_csv("data_out/Cerinta6.csv")
