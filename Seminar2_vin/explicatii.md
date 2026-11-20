# Explicații — set vin roșu

**Cerința 1.** `read_csv` cu `sep=";"`, pentru că fișierul are punct și virgulă între coloane. Fără separator, tot rândul ar intra într-o singură coloană.

**Cerința 2.** `nan_replace_df` parcurge fiecare coloană. Dacă are NaN și e numerică, pune media coloanei. Dacă nu e numerică, pune valoarea cea mai frecventă. Pe acest set nu există lipsuri, dar funcția e scrisă general, ca la examen.

**Cerința 3.** Filtrare cu condiția `tabel["quality"] >= 7`. Rezultă 217 vinuri.

**Cerința 4.** `sort_values(by="alcohol", ascending=False)`, apoi `head(50)`.

**Cerința 5.** `groupby("quality")` și media pe `alcohol` și `pH`. Rezultă un rând pentru fiecare notă: 3, 4, 5, 6, 7, 8.

**Cerința 6.** Coloană nouă `aciditate_totala` = suma celor trei aciditați. Se salvează doar cele 4 coloane cerute.

**Cerința 7.** Media alcoolului pe fiecare notă, apoi `idxmax()` dă nota cu media cea mai mare. Rezultă nota 8 (media alcoolului 12.09).

**Cerința 8.** `corr()` pe cele 5 coloane. Matricea e simetrică, cu 1 pe diagonală.

**Cerința 9.** Standardizare: (x − medie) / deviație standard. Am folosit deviația standard de populație (`ddof=0`, împărțire la n). Alegerea e scrisă în comentariu în cod, cum cere cerința.

**Cerința 10.** Se iau primele 20 de vinuri și cele 3 coloane. Fiecare coloană se standardizează, apoi `cdist` calculează distanțele euclidiene. Rezultă o matrice 20×20 simetrică, cu 0 pe diagonală. Vinurile 0 și 4 sunt identice în date, deci distanța dintre ele e 0.

## Întrebări orale

**1. De ce corelația alcool–calitate nu implică cauzalitate?**
Corelația arată doar că cele două variabile cresc împreună (aici 0.48). Nu arată care o influențează pe cealaltă. Poate exista o a treia cauză comună, de exemplu calitatea strugurilor sau felul în care a fost făcut vinul. Poate fi și invers: vinurile mai bune sunt lăsate să fermenteze până ating mai mult alcool.

**2. De ce standardizăm înainte de distanțe euclidiene?**
Coloanele au unități și scări diferite. Distanța euclidiană adună diferențele la pătrat, deci coloana cu valorile cele mai mari ar domina distanța. Prin standardizare toate coloanele ajung la medie 0 și deviație 1 și contribuie la fel.
