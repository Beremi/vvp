# Instrukce pro agenty: úpravy Jupyter notebooků

## 1. Účel dokumentu
Tento dokument je závazný postup pro agenty, kteří upravují výukové notebooky v tomto repozitáři.
Cíl je držet výklad věcný, lidský, stylisticky jednotný a obsahově pravdivý vůči reálné osnově kurzu.

## 2. Povinný postup při každém požadavku
1. Přečti cílový notebook a podle potřeby i sousední notebooky ve stejném týdnu (`a`, `b`, `c`...), aby úprava seděla do pořadí výkladu.
2. Zkontroluj, že tvrzení odpovídají skutečnému obsahu kurzu v repozitáři.
3. Uprav text tak, aby byl stručný, přirozený a bez výplně.
4. Po úpravě vždy projdi `git diff` oproti poslednímu commitu a zkontroluj konzistenci stylu.
5. Pokud uživatel během chatu opraví termín, formulaci nebo pravidlo, převeď to na obecné pravidlo a zapiš ho do sekce `6. Terminologie a jazykové preference` a `8. Trvalé poznámky`.

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
- Pokud je výklad primárně přes GUI (např. VS Code), uveď i terminálový ekvivalent.

## 5. Obsahová přesnost
- Nepřidávej témata, která se v kurzu reálně neprobírají.
- Úvodní části musí odpovídat skutečné osnově notebooků v repozitáři.
- U historických nebo verzovacích informací nepoužívej marketingové ani rychle zastarávající formulace bez opory v kontextu kurzu.
- Když je něco nejisté, zvol obecné a pravdivé tvrzení místo konkrétního čísla/verze.

## 6. Terminologie a jazykové preference
- Používej formulaci `v prostředí Jupyter notebooků`.
- Nepoužívej formulaci `v Jupyter notebookech`.
- Kde to pomůže čitelnosti, může být český termín doplněn anglickým ekvivalentem v závorce, např. `odeslání (push)`.

## 7. Výstupní kontrola před odevzdáním
- Zkontroluj, že hlavní kapitoly jsou číslované a podnadpisy nejsou číslované.
- Zkontroluj, že nejsou použité zakázané nebo nevhodné formulace ze sekce 6.
- Zkontroluj, že každý uvedený příkaz je v kódovém bloku se správným jazykovým tagem.
- Zkontroluj, že text působí přirozeně a není přeformalizovaný.
- Zkontroluj `git diff`, zda úpravy nepřidaly zbytečný balast.

## 8. Trvalé poznámky
Tuto sekci agent průběžně aktualizuje. Každá nová uživatelská oprava má být převedena na přenositelné pravidlo.

| Datum      | Spouštěč                                                              | Pravidlo                                                                                             | Aplikace                              |
| ---------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 2026-02-12 | Uživatel odmítl syntetické členění textu                              | Nepoužívat štítky `Definice.` a `Kontext.` v tomto kurzu, pokud nejsou explicitně vyžádány.          | Všechny výkladové notebooky.          |
| 2026-02-12 | Upřesnění obsahu kurzu                                                | Neuvádět automatizaci jako hlavní výukové téma kurzu, pokud to není v dané části skutečně probíráno. | Úvody a přehledové části.             |
| 2026-02-12 | Jazyková korekce uživatele                                            | Používat tvar `v prostředí Jupyter notebooků`; nepoužívat `v Jupyter notebookech`.                   | Všechny notebooky a instrukční texty. |
| 2026-02-12 | Revize diffu `Week_01/01a_git.ipynb`                                  | U GUI postupů uvádět i terminálový ekvivalent jako kódový blok.                                      | Výukové části s nástrojovým workflow. |
| 2026-02-12 | Revize diffu `Week_01/01a_git.ipynb`, `Week_01/01b_proc_python.ipynb` | Preferovat kratší odstavce a explicitní strukturu přes odrážky/kroky místo dlouhých bloků textu.     | Všechny výkladové notebooky.          |

