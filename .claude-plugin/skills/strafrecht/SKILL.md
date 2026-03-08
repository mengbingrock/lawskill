---
name: strafrecht
description: "Use when user asks about 3 Strafrecht, Criminal Law, StGB, Strafgesetzbuch, penal code, criminal law, Strafrecht, Jugendstrafrecht, Strafprozessordnung, SR 3xx. Covers SR category 3 of the Systematische Rechtssammlung."
---

# SR 3 – 3 Strafrecht

## Overview

Category **3** of the Swiss Systematische Rechtssammlung (SR) covers **Criminal Law**. Contains **65 laws** across **7 subcategories**.

## Usage

- Search by SR number or keyword in the table of contents below
- Full URLs: prefix relative ELI paths with `https://www.fedlex.admin.ch`
- For detailed article listings, see `references/articles.md`

### Extracting Article Text from Fedlex with Playwright

Fedlex pages require JavaScript rendering, so `WebFetch` / `curl` will not return article content. Use the Playwright-based script `extract_fedlex.py` to extract full article text (including all Abs. and lit.) directly from Fedlex.

**Prerequisites:**
```bash
pip3 install --break-system-packages playwright && python3 -m playwright install chromium
```

**Script:** `extract_fedlex.py` (project root)

The script navigates to Fedlex ELI URLs with a headless Chromium browser, waits for JS rendering (`networkidle` + 5s), then extracts article text by regex from the rendered page body. It takes screenshots for debugging.

**How to use for verification:**
1. Edit `STPO_ARTICLES`, `BV_ARTICLES`, or `STGB_ARTICLES` lists in the script to target the articles you need
2. Add additional law URLs and article lists as needed (e.g., EMRK, OR)
3. Run: `python3 extract_fedlex.py`
4. The script prints each article's full text with all Absätze and Litera, enabling verification of citation specificity (e.g., confirming `Art. 227 Abs. 7 StPO` exists)

**Example — verifying pre-trial detention citations (Kollusionsgefahr):**

See `swiss_citations_kollusionsgefahr.py` for a verified list of 31 citations relevant to extending Untersuchungshaft under Art. 221 Abs. 1 lit. b StPO, covering:
- BV (Art. 5, 10, 31, 36) — constitutional basis
- EMRK (Art. 5) — convention rights
- StPO (Art. 197, 212, 221, 226, 227, 228, 237) — procedural provisions
- StGB (Art. 30) — Strafantrag/withdrawal of complaint
- BGE leading cases — Kollusionsgefahr, proportionality, Ersatzmassnahmen

## Table of Contents

### 31 Bürgerliches Strafrecht

- **SR 311.0** Schweizerisches Strafgesetzbuch vom 21. Dezember 1937 ([ELI](/eli/cc/54/757_781_799/de))
- **SR 311.01** Verordnung vom 19. September 2006 zum Strafgesetzbuch, zum Militärstrafgesetz und zum Jugendstrafgesetz (V-StGB-MStG-JStG) ([ELI](/eli/cc/2006/693/de))
- **SR 311.039.1** Verordnung vom 11. Juni 2010 über Massnahmen zum Schutz von Kindern und Jugendlichen sowie zur Stärkung der Kinderrechte ([ELI](/eli/cc/2010/390/de))
- **SR 311.039.2** Verordnung vom 26. Juni 2013 über die Eidgenössische Fachkommission zur Beurteilung der Behandelbarkeit lebenslänglich verwahrter Straftäter ([ELI](/eli/cc/2013/447/de))
- **SR 311.039.3** Verordnung vom 23. Oktober 2013 über Massnahmen zur Verhütung von Straftaten im Zusammenhang mit Menschenhandel (Verordnung gegen Menschenhandel) ([ELI](/eli/cc/2013/680/de))
- **SR 311.039.4** Verordnung vom 18. November 2015 über Massnahmen zur Verhütung von Straftaten im Zusammenhang mit Prostitution ([ELI](/eli/cc/2015/800/de))
- **SR 311.039.5** Verordnung vom 16. Mai 2018 über Massnahmen zur Verhinderung und Bekämpfung von Radikalisierung und gewalttätigem Extremismus (Verordnung gegen Radikalisierung und Extremismus) ([ELI](/eli/cc/2018/335/de))
- **SR 311.039.6** Verordnung vom 9. Oktober 2019 über Massnahmen zur Unterstützung der Sicherheit von Minderheiten mit besonderen Schutzbedürfnissen (VSMS) ([ELI](/eli/cc/2019/584/de))
- **SR 311.039.7** Verordnung vom 13. November 2019 über Massnahmen zur Verhütung und Bekämpfung von Gewalt gegen Frauen und häuslicher Gewalt (Verordnung gegen Gewalt gegen Frauen und häusliche Gewalt) ([ELI](/eli/cc/2019/672/de))
- **SR 311.1** Bundesgesetz vom 20. Juni 2003 über das Jugendstrafrecht (Jugendstrafgesetz, JStG) ([ELI](/eli/cc/2006/551/de))
- **SR 311.6** Bundesgesetz vom 29. September 2023 über das Verbot der Verhüllung des Gesichts (BVVG) ([ELI](/eli/cc/2024/620/de))
- **SR 312.0** Schweizerische Strafprozessordnung vom 5. Oktober 2007 (Strafprozessordnung, StPO) ([ELI](/eli/cc/2010/267/de))
- **SR 312.057** Verordnung vom 3. Dezember 2010 über die Anlage beschlagnahmter Vermögenswerte ([ELI](/eli/cc/2010/863/de))
- **SR 312.1** Schweizerische Jugendstrafprozessordnung vom 20. März 2009 (Jugendstrafprozessordnung, JStPO) ([ELI](/eli/cc/2010/226/de))
- **SR 312.2** Bundesgesetz vom 23. Dezember 2011 über den ausserprozessualen Zeugenschutz (ZeugSG) ([ELI](/eli/cc/2012/814/de))
- **SR 312.21** Verordnung vom 7. November 2012 über den ausserprozessualen Zeugenschutz (ZeugSV) ([ELI](/eli/cc/2012/815/de))
- **SR 312.3** Verordnung vom 10. November 2004 über die Mitteilung kantonaler Strafentscheide ([ELI](/eli/cc/2004/729/de))
- **SR 312.4** Bundesgesetz vom 19. März 2004 über die Teilung eingezogener Vermögenswerte (TEVG) ([ELI](/eli/cc/2004/468/de))
- **SR 312.5** Bundesgesetz vom 23. März 2007 über die Hilfe an Opfer von Straftaten (Opferhilfegesetz, OHG) ([ELI](/eli/cc/2008/232/de))
- **SR 312.51** Verordnung vom 27. Februar 2008 über die Hilfe an Opfer von Straftaten (Opferhilfeverordnung, OHV) ([ELI](/eli/cc/2008/233/de))
- **SR 312.81** Verordnung vom 10. November 2004 über die verdeckte Ermittlung (VVE) ([ELI](/eli/cc/2004/702/de))
- **SR 313.0** Bundesgesetz vom 22. März 1974 über das Verwaltungsstrafrecht (VStrR) ([ELI](/eli/cc/1974/1857_1857_1857/de))
- **SR 313.041** Verordnung vom 20. September 2013 über das Informationssystem für Strafsachen des Bundesamts für Zoll und Grenzsicherheit (IStrV-BAZG) ([ELI](/eli/cc/2013/639/de))
- **SR 313.32** Verordnung vom 25. November 1974 über Kosten und Entschädigungen im Verwaltungsstrafverfahren ([ELI](/eli/cc/1974/1939_1939_1939/de))
- **SR 314.1** Ordnungsbussengesetz vom 18. März 2016 (OBG) ([ELI](/eli/cc/2017/725/de))
- **SR 314.11** Ordnungsbussenverordnung vom 16. Januar 2019 (OBV) ([ELI](/eli/cc/2019/93/de))

### 32 Militärstrafrecht

- **SR 321.0** Militärstrafgesetz vom 13. Juni 1927 (MStG) ([ELI](/eli/cc/43/359_375_369/de))
- **SR 321.1** Bundesgesetz vom 20. März 2009 über die Rehabilitierung der Freiwilligen im Spanischen Bürgerkrieg ([ELI](/eli/cc/2009/462/de))
- **SR 322.1** Militärstrafprozess vom 23. März 1979 (MStP) ([ELI](/eli/cc/1979/1059_1059_1059/de))
- **SR 322.2** Verordnung vom 24. Oktober 1979 über die Militärstrafrechtspflege (MStV) ([ELI](/eli/cc/1979/1880_1880_1880/de))

### 33 Strafregister

- **SR 330** Bundesgesetz vom 17. Juni 2016 über das Strafregister-Informationssystem VOSTRA (Strafregistergesetz, StReG) ([ELI](/eli/cc/2022/600/de))
- **SR 331** Verordnung vom 19. Oktober 2022 über das Strafregister-Informationssystem VOSTRA (Strafregisterverordnung, StReV) ([ELI](/eli/cc/2022/698/de))

### 34 Strafvollzug

- **SR 341** Bundesgesetz vom 5. Oktober 1984 über die Leistungen des Bundes für den Straf- und Massnahmenvollzug ([ELI](/eli/cc/1986/1934_1934_1934/de))
- **SR 341.1** Verordnung vom 21. November 2007 über die Leistungen des Bundes für den Straf- und Massnahmenvollzug (LSMV) ([ELI](/eli/cc/2007/862/de))
- **SR 341.14** Verordnung des EJPD vom 19. November 2011 über die Baubeiträge des Bundes an Einrichtungen für den Straf- und Massnahmenvollzug ([ELI](/eli/cc/2011/788/de))

### 35 Rechtshilfe. Auslieferung

- **SR 351.1** Bundesgesetz vom 20. März 1981 über internationale Rechtshilfe in Strafsachen (Rechtshilfegesetz, IRSG) ([ELI](/eli/cc/1982/846_846_846/de))
- **SR 351.11** Verordnung vom 24. Februar 1982 über internationale Rechtshilfe in Strafsachen (Rechtshilfeverordnung, IRSV) ([ELI](/eli/cc/1982/878_878_878/de))
- **SR 351.12** Verordnung vom 23. September 2016 über das elektronische Personen-, Akten- und Geschäftsverwaltungssystem des Bundesamtes für Justiz (ELPAG-Verordnung) ([ELI](/eli/cc/2016/555/de))
- **SR 351.13** Verordnung vom 21. Dezember 2022 über die Zusammenarbeit mit der Europäischen Staatsanwaltschaft ([ELI](/eli/cc/2022/859/de))
- **SR 351.201.11** Verordnung vom 12. Februar 2003 über die Ausdehnung des Geltungsbereichs des Bundesbeschlusses über die Zusammenarbeit mit den Internationalen Gerichten zur Verfolgung von schwerwiegenden Verletzungen des humanitären Völkerrechts auf den Spezialgerichtshof für Sierra Leone ([ELI](/eli/cc/2003/70/de))
- **SR 351.201.12** Verordnung vom 8. Juni 2012 über die Ausdehnung des Geltungsbereichs des Bundesgesetzes über die Zusammenarbeit mit den Internationalen Gerichten zur Verfolgung schwerwiegender Verletzungen des humanitären Völkerrechts auf den Internationalen Residualmechanismus für die Ad-hoc-Strafgerichte ([ELI](/eli/cc/2012/382/de))
- **SR 351.6** Bundesgesetz vom 22. Juni 2001 über die Zusammenarbeit mit dem Internationalen Strafgerichtshof (ZISG) ([ELI](/eli/cc/2002/237/de))
- **SR 351.93** Bundesgesetz vom 3. Oktober 1975 zum Staatsvertrag mit den Vereinigten Staaten von Amerika über gegenseitige Rechtshilfe in Strafsachen ([ELI](/eli/cc/1977/17_17_17/de))
- **SR 354.1** Übereinkunft vom 23. Juni 1909 betreffend die Polizeitransporte ([ELI](/eli/cc/25/524_573_523/de))

### 36 Polizeikoordination und Dienstleistungen

- **SR 360** Bundesgesetz vom 7. Oktober 1994 über die kriminalpolizeilichen Zentralstellen des Bundes und gemeinsame Zentren für Polizei- und Zollzusammenarbeit mit anderen Staaten (ZentG) ([ELI](/eli/cc/1995/875_875_875/de))
- **SR 360.1** Verordnung vom 30. November 2001 über die Wahrnehmung kriminalpolizeilicher Aufgaben im Bundesamt für Polizei ([ELI](/eli/cc/2002/29/de))
- **SR 360.2** Verordnung vom 15. Oktober 2008 über das Nationale Ermittlungssystem (NES-Verordnung) ([ELI](/eli/cc/2008/697/de))
- **SR 360.4** Vereinbarung vom 2. April 2014 über den nationalen Betrieb gemeinsamer Polizei- und Zollkooperationszentren (CCPD) in Genf und Chiasso ([ELI](/eli/cc/2014/333/de))
- **SR 361** Bundesgesetz vom 13. Juni 2008 über die polizeilichen Informationssysteme des Bundes (BPI) ([ELI](/eli/cc/2008/698/de))
- **SR 361.0** Verordnung vom 26. Oktober 2016 über das automatisierte Polizeifahndungssystem (RIPOL-Verordnung) ([ELI](/eli/cc/2016/665/de))
- **SR 361.2** Verordnung vom 15. Oktober 2008 über das informatisierte Personennachweis, Aktennachweis- und Verwaltungssystem im Bundesamt für Polizei (IPAS-Verordnung) ([ELI](/eli/cc/2008/700/de))
- **SR 361.3** Verordnung vom 6. Dezember 2013 über die Bearbeitung biometrischer erkennungsdienstlicher Daten ([ELI](/eli/cc/2014/23/de))
- **SR 361.4** Verordnung vom 15. Oktober 2008 über den Nationalen Polizeiindex (Polizeiindex-Verordnung) ([ELI](/eli/cc/2008/701/de))
- **SR 362** Bundesbeschluss vom 17. Dezember 2004 über die Genehmigung und die Umsetzung der bilateralen Abkommen zwischen der Schweiz und der EU über die Assoziierung an Schengen und an Dublin ([ELI](/eli/cc/2008/112/de))
- **SR 362.0** Verordnung vom 8. März 2013 über den nationalen Teil des Schengener Informationssystems (N-SIS) und das SIRENE-Büro (N-SIS-Verordnung) ([ELI](/eli/cc/2013/179/de))
- **SR 362.1** Vereinbarung vom 20. März 2009 zwischen Bund und Kantonen betreffend Umsetzung, Anwendung und Entwicklung des Schengen/Dublin-Besitzstands ([ELI](/eli/cc/2009/185/de))
- **SR 362.2** Bundesgesetz vom 21. März 2025 über den Informationsaustausch zwischen den Strafverfolgungsbehörden der Schweiz und denjenigen der anderen Schengen-Staaten (Schengen-Informationsaustauschgesetz, SIAG) ([ELI](/eli/cc/2025/460/de))
- **SR 363** Bundesgesetz vom 20. Juni 2003 über die Verwendung von DNA-Profilen im Strafverfahren und zur Identifizierung von unbekannten oder vermissten Personen (DNA-Profil-Gesetz) ([ELI](/eli/cc/2004/811/de))
- **SR 363.1** Verordnung vom 3. Dezember 2004 über die Verwendung von DNA-Profilen im Strafverfahren und zur Identifizierung von unbekannten oder vermissten Personen (DNA-Profil-Verordnung) ([ELI](/eli/cc/2004/812/de))
- **SR 363.11** Verordnung des EJPD vom 8. Oktober 2014 über die Leistungs- und Qualitätsanforderungen für forensische DNA-Analyselabors (DNA-Analyselabor-Verordnung EJPD) ([ELI](/eli/cc/2014/605/de))
- **SR 364** Bundesgesetz vom 20. März 2008 über die Anwendung polizeilichen Zwangs und polizeilicher Massnahmen im Zuständigkeitsbereich des Bundes (Zwangsanwendungsgesetz, ZAG) ([ELI](/eli/cc/2008/759/de))
- **SR 364.3** Verordnung vom 12. November 2008 über die Anwendung polizeilichen Zwangs und polizeilicher Massnahmen im Zuständigkeitsbereich des Bundes (Zwangsanwendungsverordnung, ZAV) ([ELI](/eli/cc/2008/760/de))
- **SR 366.1** Verordnung vom 21. Juni 2013 über das Nationale Zentralbüro Interpol Bern (Interpol-Verordnung) ([ELI](/eli/cc/2013/466/de))
- **SR 367.1** Vereinbarung vom 2. September 2020 zwischen dem Bund und den Kantonen über die Harmonisierung und die gemeinsame Bereitstellung der Polizeitechnik und -informatik in der Schweiz (PTI-Vereinbarung) ([ELI](/eli/cc/2020/1053/de))

### 37 Flüchtlingshelferinnen und

- **SR 371** Bundesgesetz vom 20. Juni 2003 über die Aufhebung von Strafurteilen gegen Flüchtlingshelfer zur Zeit des Nationalsozialismus ([ELI](/eli/cc/2003/633/de))
