import pandas as pd


def nan_replace_df(tabel):
    coloane_numerice = tabel.select_dtypes(include="number").columns
    for coloana in coloane_numerice:
        tabel[coloana] = tabel[coloana].fillna(tabel[coloana].mean())
    return tabel


def salvare_matrice(x, index_linie, index_coloana, fisier):
    matrice = pd.DataFrame(x, index=index_linie, columns=index_coloana)
    matrice.to_csv(fisier)
