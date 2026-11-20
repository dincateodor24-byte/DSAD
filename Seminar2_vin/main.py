import os
import pandas as pd
from scipy.spatial.distance import cdist
from functii_online import nan_replace_df, salvare_matrice

os.makedirs("data_out", exist_ok=True)

# Cerinta 1
tabel = pd.read_csv("data_in/winequality-red.csv", sep=";")
print(tabel.shape)
print(tabel.head())
print(tabel.dtypes)

# Cerinta 2
tabel = nan_replace_df(tabel)
print("NaN ramase:", tabel.isna().sum().sum())

# Cerinta 3
vinuri_min7 = tabel[tabel["quality"] >= 7]
vinuri_min7.to_csv("data_out/vinuri_calitate_min7.csv", index=False)

# Cerinta 4
top50 = tabel.sort_values("alcohol", ascending=False, kind="stable").head(50)
top50.to_csv("data_out/top50_alcool.csv", index=False)

# Cerinta 5
medii = tabel.groupby("quality")[["alcohol", "pH"]].mean()
medii.to_csv("data_out/medii_pe_calitate.csv")

# Cerinta 6
tabel["aciditate_totala"] = tabel["fixed acidity"] + tabel["volatile acidity"] + tabel["citric acid"]
tabel[["quality", "alcohol", "aciditate_totala", "pH"]].to_csv("data_out/vinuri_cu_aciditate.csv", index=False)

# Cerinta 7
calitate_max = tabel.groupby("quality")["alcohol"].mean().idxmax()
pd.DataFrame({"quality": [calitate_max]}).to_csv("data_out/calitate_max_alcool.csv", index=False)

# Cerinta 8
coloane = ["fixed acidity", "volatile acidity", "citric acid", "alcohol", "quality"]
tabel[coloane].corr().to_csv("data_out/R.csv")

# Cerinta 9
# Se foloseste deviatia standard de populatie (ddof=0), adica impartire la n.
tabel["alcohol_std"] = (tabel["alcohol"] - tabel["alcohol"].mean()) / tabel["alcohol"].std(ddof=0)
tabel[["alcohol", "alcohol_std"]].to_csv("data_out/alcohol_standardizat.csv", index=False)

# Cerinta 10
vinuri = tabel[["fixed acidity", "volatile acidity", "alcohol"]].head(20)
vinuri_std = (vinuri - vinuri.mean()) / vinuri.std(ddof=0)
distante = cdist(vinuri_std, vinuri_std, metric="euclidean")
salvare_matrice(distante, vinuri.index, vinuri.index, "data_out/d_euclid_20.csv")
