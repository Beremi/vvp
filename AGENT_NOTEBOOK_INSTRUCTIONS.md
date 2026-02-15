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
8. U notebooků s kódovými buňkami se pokus notebook spustit buňku po buňce v logickém pořadí i tehdy, když kódové buňky neupravuješ.
9. Pokud běh spadne na chybě, ověř kontext: rozliš záměrnou výukovou chybu od nezáměrné chyby.
10. Po úpravě vždy projdi `git diff` oproti poslednímu commitu a zkontroluj konzistenci stylu.
11. Pokud uživatel během chatu opraví termín, formulaci nebo pravidlo, převeď to na obecné pravidlo a zapiš ho do sekce `6. Terminologie a jazykové preference` a `8. Trvalé poznámky`.

## 3. Styl a struktura výkladu
- Používej přirozený jazyk. Nepoužívej syntetické štítky typu `Definice.` a `Kontext.`, pokud to uživatel výslovně nevyžádá.
- Drž jednotnou terminologii; po zavedení termínu používej stejný tvar.
- Čísluj hlavní kapitoly (`# 1. ...`, `# 2. ...`) tak, aby odpovídaly osnově notebooku.
- Hloubku podnadpisů (`##`, `###`) můžeš upravit podle čitelnosti; není nutné držet původní hierarchii.
- Podnadpisy standardně nečísluj (`## ...`, `### ...`), použij je jen když má část více samostatných bodů.
- Pokud má notebook jedno hlavní téma a více rovnocenných bloků, je vhodné podnadpisy číslovat konzistentně (`## 1.1 ...`, `## 1.2 ...`, případně `### 1.2.1 ...`).
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
- Hloubku nadpisů lze upravit podle čitelnosti; hlavní kapitoly čísluj podle osnovy notebooku.
- U notebooků s jedním hlavním tématem a více rovnocennými sekcemi (např. typy operátorů) je vhodné používat číslované podnadpisy, aby nezůstala jen izolovaná kapitola `# 1`.
- Při zkracování výkladu zachovej věcnou přesnost; nepoužívej formulace, které by mohly být zavádějící.
- V ukázkách kódu používej srozumitelné názvy proměnných a drž jejich konzistenci mezi navazujícími buňkami.
- Nepřidávej fallback kód pro chybějící balíčky nebo toolchain; když buňka padá kvůli prostředí, oprav prostředí a zachovej přímý výukový kód.
- V notebookových shell příkazech preferuj přímé volání přes `!` (např. `!python ...`); nepoužívej tvar `!{sys.executable} ...`.
- Při prvním použití zkratky v každém notebooku uveď její plný význam (např. `ABI (Application Binary Interface)`).
- U „povinných“ tagů/flagů/maker (např. přepínače kompilace, Cython magic, Python C API makra) přidej stručné vysvětlení významu, aby pojmy nepadaly „z nebe“.

## 7. Výstupní kontrola před odevzdáním
- Zkontroluj, že jsi prošel všechny notebooky dané lekce (`XXa_...`, `XXb_...`, ... `XX_ukoly`) a přeskočil `DUX` notebooky.
- Zkontroluj, že hlavní kapitoly jsou číslované a hierarchie nadpisů je konzistentní (nemusí kopírovat původní hloubku).
- Pokud notebook používá číslované podnadpisy (`1.1`, `1.2`, ...), zkontroluj, že číslování pokrývá rovnocenné části a není nahodilé.
- Zkontroluj, že nejsou použité zakázané nebo nevhodné formulace ze sekce 6.
- Zkontroluj, že každý uvedený příkaz je v kódovém bloku se správným jazykovým tagem.
- Zkontroluj, že označení `terminálový ekvivalent` je použito jen u skutečně ekvivalentních kroků.
- U notebooků s kódovými buňkami se pokus ověřit běh buňku po buňce i bez změny kódu a vyhodnoť případné chyby podle kontextu výkladu.
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
| 2026-02-12 | Upřesnění uživatele při revizi `Week_02`                              | U notebooků s kódovými buňkami se pokusit spouštět kód buňku po buňce i tehdy, když kód nebyl upraven. | Všechny notebooky s kódovými buňkami. |
| 2026-02-12 | Upřesnění uživatele k nadpisům v `Week_02/02a_promenne_a_typy.ipynb`  | Hloubku nadpisů lze upravit podle čitelnosti; hlavní kapitoly číslovat podle osnovy notebooku. | Všechny výkladové notebooky.          |
| 2026-02-12 | Upřesnění uživatele k číslování `Week_02/02b_operatory.ipynb`         | U notebooků s jedním hlavním tématem číslovat i rovnocenné podsekce (např. `1.1`, `1.2`), aby struktura nebyla jen na úrovni `# 1`. | Všechny výkladové notebooky.          |
| 2026-02-12 | Upřesnění uživatele při revizi `Week_03`                              | Držet výklad kompaktní, ale věcně přesný; zavádějící formulace přepisovat i bez rozšíření tématu. V ukázkách používat srozumitelné a konzistentní názvy proměnných. | Všechny výkladové notebooky a ukázky kódu. |
| 2026-02-12 | Upřesnění uživatele při revizi `Week_11`                              | Nepoužívat fallback kód pro chybějící balíčky v učebních noteboocích; chyby prostředí řešit konfigurací prostředí (venv/devcontainer), ne obcházením výkladu. | Všechny notebooky s externími závislostmi. |
| 2026-02-13 | Upřesnění uživatele ke stylu shell příkazů v noteboocích              | V kódových buňkách používat přímé shell volání přes `!` (např. `!python ...`), ne `!{sys.executable} ...`. | Všechny notebooky s terminálovými příkazy. |
| 2026-02-14 | Upřesnění uživatele při revizi `Week_13`                              | V každém notebooku při prvním použití zkratky uvést plný význam; u klíčových tagů/flagů/maker doplnit stručné vysvětlení významu. | Všechny výkladové notebooky. |
