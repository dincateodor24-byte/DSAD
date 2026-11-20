# Explicații — industria alimentară (Seminar 3)

**Pregătire.** Se citesc cele 3 fișiere: `IndustriaAlimentara.csv`, `PopulatieLocalitati.csv` și `Coduri_Judete.csv`. Numele activităților se iau din antetul tabelului, de la a treia coloană încolo. Cele 3181 de localități din primele două fișiere au aceleași coduri Siruta, deci se pot lega fără pierderi cu `merge` pe `Siruta`.

**Cerința 1.** Se calculează totalul angajaților pe fiecare rând (`sum(axis=1)`) și se păstrează rândurile cu totalul mai mare decât 0. Rezultă 1372 de localități, cu aceleași coloane ca fișierul inițial.

**Cerința 2.** Fiecare valoare se împarte la totalul rândului și se înmulțește cu 100. Procentul se calculează doar pentru cele 1372 de localități cu angajați. La celelalte ar ieși 0/0 și ar apărea NaN.

**Cerința 3.** Se adună angajații și populația pe județ. Ponderea este angajați / populație, iar rezultatul se sortează descrescător. Primul județ este Ilfov (`if`).

**Cerința 4.** Pe totalurile județelor se ia, pentru fiecare județ, activitatea cu valoarea maximă (`idxmax(axis=1)`).

**Cerința 5.** Pentru fiecare regiune, ponderea unei localități este populația ei împărțită la populația regiunii. Media ponderată este suma valorilor înmulțite cu aceste ponderi. Regiunea vine din `Coduri_Judete.csv`, pe baza indicativului de județ.

**Cerința 6.** Indicele de localizare = (angajații județului în activitate / angajații din țară în activitate) / (populația județului / populația țării). Verificare: media indicilor, ponderată cu populația, dă 1 pentru fiecare activitate.
