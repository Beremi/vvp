# Instrukce pro agenty: úpravy Jupyter notebooků

## 1. Účel dokumentu
Tento dokument je závazný postup pro agenty, kteří upravují výukové notebooky v tomto repozitáři.
Cíl je držet výklad věcný, lidský, stylisticky jednotný a obsahově pravdivý vůči reálné osnově kurzu.

## 2. Povinný postup při každém požadavku
1. Urči cílovou složku týdne `Week_XX`.
2. Projdi celou lekci v pořadí výkladu: notebooky `XXa_...`, `XXb_...`, `XXc_...` ... a `XX_ukoly`.
3. Notebooky s `DUX` v názvu v této fázi ignoruj.
4. Další soubory ve složce neupravuj; použij je jen tehdy, když na ně notebook explicitně odkazuje a jsou nutné pro věcnou kontrolu.
5. Před úpravou konkrétního notebooku ověř návaznost na předchozí a následující notebooky stejného týdne.
6. Zkontroluj, že tvrzení odpovídají skutečnému obsahu kurzu v repozitáři.
7. Uprav text tak, aby byl stručný, přirozený a bez výplně.
8. Pokud upravuješ kódové buňky, spusť notebook po změně buňku po buňce v logickém pořadí.
9. Pokud běh spadne na chybě, ověř kontext: rozliš záměrnou výukovou chybu od nezáměrné chyby.
10. Po úpravě vždy projdi `git diff` oproti poslednímu commitu a zkontroluj konzistenci stylu.
11. Pokud uživatel během chatu opraví termín, formulaci nebo pravidlo, převeď to na obecné pravidlo a zapiš ho do sekce `6. Terminologie a jazykové preference` a `8. Trvalé poznámky`.

## 3. Styl a struktura výkladu
- Používej přirozený jazyk. Nepoužívej syntetické štítky typu `Definice.` a `Kontext.`, pokud to uživatel výslovně nevyžádá.
- Drž jednotnou terminologii; po zavedení termínu používej stejný tvar.
- Čísluj jen hlavní kapitoly (`# 1. ...`, `# 2. ...`).
- Podnadpisy nečísluj (`## ...`), použij je jen když má část více samostatných bodů.
- Piš krátké aktivní věty. Odstraň redundance a výplň.
- Výčty piš odrážkami, postupy piš jako kroky v logickém pořadí.
- Dodržuj tok výkladu: motivace a kontext, postup, příklad, stručné shrnutí.

## 4. Pravidla pro příkazy a ukázky
- Každý příkaz nebo ukázku uváděj jako korektní blok kódu.
- Všechny víceřádkové příkazy dávej do bloků s jazykovým tagem (`bash`, `shell`, `python`).
- Příklady udržuj spustitelné a minimální.
- Terminálový ekvivalent uváděj jen tehdy, když jde o skutečně stejnou operaci a je věcně správný.
- Pokud GUI krok nemá přímý CLI ekvivalent (např. výběr kernelu), terminálový ekvivalent nevynucuj.

## 5. Obsahová přesnost
- Nepřidávej témata, která se v kurzu reálně neprobírají.
- Úvodní části musí odpovídat skutečné osnově notebooků v repozitáři.
- Drž návaznost mezi notebooky v rámci týdne; výklad v pozdější části nesmí odporovat dřívějším částem lekce.
- U historických nebo verzovacích informací nepoužívej marketingové ani rychle zastarávající formulace bez opory v kontextu kurzu.
- Když je něco nejisté, zvol obecné a pravdivé tvrzení místo konkrétního čísla/verze.
- Neuváděj „ekvivalenty“ jen kvůli symetrii výkladu; uváděj pouze informace, které jsou věcně správné.

## 6. Terminologie a jazykové preference
- Používej formulaci `v prostředí Jupyter notebooků`.
- Nepoužívej formulaci `v Jupyter notebookech`.
- Kde to pomůže čitelnosti, může být český termín doplněn anglickým ekvivalentem v závorce, např. `odeslání (push)`.
- Formulaci `terminálový ekvivalent` používej jen tam, kde je ekvivalence skutečná; jinak popiš GUI krok samostatně.
- Při komentování chyb rozlišuj formulace `záměrná výuková chyba` a `nezáměrná chyba`.

## 7. Výstupní kontrola před odevzdáním
- Zkontroluj, že jsi prošel všechny notebooky dané lekce (`XXa_...`, `XXb_...`, ... `XX_ukoly`) a přeskočil `DUX` notebooky.
- Zkontroluj, že hlavní kapitoly jsou číslované a podnadpisy nejsou číslované.
- Zkontroluj, že nejsou použité zakázané nebo nevhodné formulace ze sekce 6.
- Zkontroluj, že každý uvedený příkaz je v kódovém bloku se správným jazykovým tagem.
- Zkontroluj, že označení `terminálový ekvivalent` je použito jen u skutečně ekvivalentních kroků.
- Pokud byly měněny kódové buňky, zkontroluj jejich běh buňku po buňce a vyhodnoť případné chyby podle kontextu výkladu.
- Zkontroluj, že nebyly změněny jiné soubory mimo cílové notebooky (pokud to nebylo nutné kvůli explicitní vazbě ve výkladu).
- Zkontroluj, že text působí přirozeně a není přeformalizovaný.
- Zkontroluj `git diff`, zda úpravy nepřidaly zbytečný balast.

## 8. Trvalé poznámky
Tuto sekci agent průběžně aktualizuje. Každá nová uživatelská oprava má být převedena na přenositelné pravidlo.

| Datum      | Spouštěč                                                              | Pravidlo                                                                                             | Aplikace                              |
| ---------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 2026-02-12 | Uživatel odmítl syntetické členění textu                              | Nepoužívat štítky `Definice.` a `Kontext.` v tomto kurzu, pokud nejsou explicitně vyžádány.          | Všechny výkladové notebooky.          |
| 2026-02-12 | Upřesnění obsahu kurzu                                                | Neuvádět automatizaci jako hlavní výukové téma kurzu, pokud to není v dané části skutečně probíráno. | Úvody a přehledové části.             |
| 2026-02-12 | Jazyková korekce uživatele                                            | Používat tvar `v prostředí Jupyter notebooků`; nepoužívat `v Jupyter notebookech`.                   | Všechny notebooky a instrukční texty. |
| 2026-02-12 | Revize diffu `Week_01/01a_git.ipynb`                                  | U GUI postupů lze uvést terminálový ekvivalent jako kódový blok jen pokud jde o skutečně stejnou operaci. | Výukové části s nástrojovým workflow. |
| 2026-02-12 | Revize diffu `Week_01/01a_git.ipynb`, `Week_01/01b_proc_python.ipynb` | Preferovat kratší odstavce a explicitní strukturu přes odrážky/kroky místo dlouhých bloků textu.     | Všechny výkladové notebooky.          |
| 2026-02-12 | Korekce uživatele k notebooku `Week_01/01c_VSCode_Jupyter.ipynb`      | Neuvádět „terminálový ekvivalent“, pokud nejde o stejnou operaci; u GUI kroků bez CLI obdoby ekvivalent nepsat. | Všechny výkladové notebooky.          |
| 2026-02-12 | Korekce uživatele k běhu kódových buněk                               | Při změně kódových buněk notebook spouštět buňku po buňce; při pádu rozlišit záměrnou výukovou chybu a nezáměrnou chybu. | Všechny notebooky s kódovými buňkami. |
| 2026-02-12 | Korekce uživatele k rozsahu průchodu lekce                            | Vždy projít celou lekci v týdnu (`XXa...` až `XX_ukoly`), ignorovat `DUX` notebooky a nesahat na další soubory bez nutné explicitní vazby. | Všechny týdenní složky.               |
