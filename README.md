# Vědecké výpočty v Pythonu (LS 25/26)

Repozitář obsahuje výkladové notebooky, týdenní úkoly a navazující materiály k předmětu **Vědecké výpočty v Pythonu** pro běh **letního semestru 2025/2026 (LS 25/26)**.

Harmonogram, organizační informace a deadliny jsou na [LMS](https://lms.vsb.cz).

## Rychlý start (Codespaces / devcontainer)

Repozitář můžete otevřít přímo v GitHub Codespaces:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=596636028)

Po vytvoření prostředí:
1. Automaticky se vytvoří `.venv` a doinstalují se závislosti z `.devcontainer/requirements-week11.txt`.
2. Zaregistruje se Jupyter kernel `Python (vvp .venv)`.
3. V prostředí Jupyter notebooků používejte tento kernel.

## Struktura repozitáře

- `Week_01` až `Week_13`: výkladové notebooky a týdenní úkoly (`XX_ukoly.ipynb`).
- `DU1.ipynb` až `DU5.ipynb`: samostatné domácí úkoly.
- `.devcontainer/`: konfigurace pro Codespaces / VS Code Dev Containers.

## Podrobná osnova kurzu

### Týden 1 (`Week_01`)
- `01a_git.ipynb`: základy Git workflow.
- `01b_proc_python.ipynb`: úvod do kurzu, proč Python, nástroje.
- `01c_VSCode_Jupyter.ipynb`: práce ve VS Code a v prostředí Jupyter notebooků.
- `01d_hello_world.ipynb`: první Python skript a základní spuštění.
- `01_ukoly.ipynb`: procvičení Git + úvod do Pythonu.

### Týden 2 (`Week_02`)
- `02a_promenne_a_typy.ipynb`: proměnné, datové typy, konverze.
- `02b_operatory.ipynb`: operátory a precedence.
- `02c_funkce_a_rizeni_toku.ipynb`: funkce, podmínky, cykly.
- `02d_ladeni.ipynb`: ladění a práce s chybami.
- `02_ukoly.ipynb`: úlohy na základy jazyka.

### Týden 3 (`Week_03`)
- `03a_lambda_a_rizeni_toku_II.ipynb`: lambda, pokročilejší řízení toku.
- `03b_vyjimky_iteratory_comprehension.ipynb`: výjimky, iterátory, comprehension.
- `03c_magics_retezce_soubory.ipynb`: IPython magics, řetězce, práce se soubory.
- `03_ukoly.ipynb`: průběžné procvičení.

### Týden 4 (`Week_04`)
- `04a_prostory_jmen.ipynb`: prostory jmen, LEGB pravidlo.
- `04b_tridy.ipynb`: OOP v Pythonu, třídy, metody.
- `04_ukoly.ipynb`: úlohy na namespace a OOP.

### Týden 5 (`Week_05`)
- `05a_ndarray.ipynb`: NumPy pole `ndarray`.
- `05b_vytvareni_poli.ipynb`: vytváření a inicializace polí.
- `05c_numpy_prace_se_soubory.ipynb`: načítání/ukládání dat (text, binární formáty, HDF5).
- `05_ukoly.ipynb`: úkoly k NumPy základům.

### Týden 6 (`Week_06`)
- `06a_indexovani_rezani.ipynb`: indexování a slicing.
- `06b_view_a_copy.ipynb`: view vs copy.
- `06c_linearni_algebra.ipynb`: lineární algebra v NumPy.
- `06d_funkce_nad_poli.ipynb`: vektorové operace a funkce nad poli.
- `06_ukoly.ipynb`: procvičení práce s poli.

### Týden 7 (`Week_07`)
- `07a_graf_funkce.ipynb`: první grafy v Matplotlib.
- `07b_vice_grafu_a_os.ipynb`: více os, více grafů v jedné figuře.
- `07c_formatovani_grafu.ipynb`: popisky, legenda, formátování.
- `07d_barvy_a_styly.ipynb`: styly a barevné mapy.
- `07e_dalsi_2d_grafy.ipynb`: další 2D typy grafů.
- `07f_3d_grafy.ipynb`: základy 3D grafů.
- `07_ukoly.ipynb`: úlohy k vizualizaci.

### Týden 8 (`Week_08`)
- `08a_scipy_uvod.ipynb`: úvod do SciPy.
- `08b_special.ipynb`: speciální funkce.
- `08c_sparse.ipynb`: sparse matice.
- `08d_fftpack.ipynb`: FFT.
- `08e_optimize.ipynb`: optimalizace.
- `08f_interpolate.ipynb`: interpolace.
- `08g_integrate.ipynb`: numerická integrace.
- `08_ukoly.ipynb`: úlohy ke SciPy.

### Týden 9 (`Week_09`)
- `09a_sympy_symboly.ipynb`: symboly v SymPy.
- `09b_sympy_vyrazy.ipynb`: symbolické výrazy.
- `09c_sympy_upravy.ipynb`: algebraické úpravy.
- `09d_sympy_derivace_a_integraly.ipynb`: derivace a integrály.
- `09e_sympy_rovnice.ipynb`: řešení rovnic.
- `09f_sympy_generovani_kodu.ipynb`: generování kódu.
- `09g_pandas.ipynb`: základy pandas.
- `09_ukoly.ipynb`: úlohy k SymPy/pandas.

### Týden 10 (`Week_10`)
- `10a_type_hints.ipynb`: type hints.
- `10b_navyky.ipynb`: návyky při psaní kódu.
- `10c_jednotkove_testy.ipynb`: unit testy.
- `10d_venv.ipynb`: virtuální prostředí.
- `10e_baliky.ipynb`: tvorba a struktura balíčků.
- `10f_sphinx.ipynb`: dokumentace přes Sphinx.
- `10_ukoly.ipynb`: úkoly k kvalitě kódu.

### Týden 11 (`Week_11`)
- `11a_venv_a_prostredi.ipynb`: příprava prostředí pro výkonové nástroje.
- `11b_profilovani.ipynb`: profilování výkonu.
- `11c_numexpr.ipynb`: výpočty přes NumExpr.
- `11d_numba.ipynb`: JIT akcelerace přes Numba.
- `11e_cython.ipynb`: základy Cythonu.
- `11f_ukazka_body.ipynb`: ukázka simulace těles.
- `11g_ukazka_graf.ipynb`: ukázka grafových výpočtů.
- `11_ukoly.ipynb`: výkonově orientované úlohy.

### Týden 12 (`Week_12`)
- `12a_prehled_paralelizmu.ipynb`: přehled paralelizace.
- `12b_numba_parallel.ipynb`: paralelní Numba.
- `12c_cython_parallel.ipynb`: paralelní Cython.
- `12d_threading.ipynb`: threading.
- `12e_multiprocessing.ipynb`: multiprocessing.
- `12f_ukazka_body_parallel.ipynb`: paralelní varianta výpočtu těles.
- `12_ukoly.ipynb`: úkoly k paralelizaci.

### Týden 13 (`Week_13`)
- `13a_mpi4py.ipynb`: základy MPI přes `mpi4py`.
- `13b_prehled_linkovani_C.ipynb`: přehled linkování C kódu.
- `13c_Ctypes_a_cffi.ipynb`: volání C přes `ctypes` a `cffi`.
- `13d_cython.ipynb`: Cython pro volání nativních funkcí.
- `13e_nativni_linkovani.ipynb`: nativní Python C extension.
- `13_ukoly.ipynb`: úlohy k MPI/linkování/Cythonu.

## Poděkování a inspirace

Část materiálů vychází z projektů:
- [Lectures on scientific computing with Python](http://github.com/jrjohansson/scientific-python-lectures)
- [numerical_python_course](https://gitlab.com/coobas/numerical_python_course)
