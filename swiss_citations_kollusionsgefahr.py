"""
Swiss legal citations relevant to extending pre-trial detention (Untersuchungshaft)
under Art. 221 Abs. 1 lit. b StPO (Kollusionsgefahr / risk of collusion),
including proportionality, withdrawal of complaint, and Ersatzmassnahmen issues.

All Abs./lit. references verified against Fedlex (fedlex.admin.ch) on 2026-03-07.
BGE citations spot-checked against bger.ch on 2026-03-07.
"""

citations = [
    # ── Bundesverfassung (BV) – Constitutional basis ──
    "Art. 5 Abs. 2 BV",           # Verhältnismässigkeit staatlichen Handelns
    "Art. 10 Abs. 2 BV",          # Recht auf persönliche Freiheit / Bewegungsfreiheit
    "Art. 31 Abs. 1 BV",          # Freiheitsentzug nur gesetzlich vorgesehen
    "Art. 31 Abs. 3 BV",          # Anspruch auf richterliche Überprüfung der U-Haft
    "Art. 36 Abs. 1 BV",          # Gesetzliche Grundlage für Grundrechtseinschränkungen
    "Art. 36 Abs. 2 BV",          # Öffentliches Interesse / Schutz Dritter
    "Art. 36 Abs. 3 BV",          # Verhältnismässigkeit von Grundrechtseinschränkungen
    # ── EMRK – European Convention on Human Rights ──
    "Art. 5 Ziff. 1 lit. c EMRK",  # Freiheitsentzug bei hinreichendem Tatverdacht
    "Art. 5 Ziff. 3 EMRK",         # Recht auf Vorführung / Urteil innert angemessener Frist
    # ── Strafprozessordnung (StPO) – Criminal Procedure Code ──
    "Art. 197 Abs. 1 lit. a StPO",  # Zwangsmassnahmen: gesetzlich vorgesehen
    "Art. 197 Abs. 1 lit. b StPO",  # Zwangsmassnahmen: hinreichender Tatverdacht
    "Art. 197 Abs. 1 lit. c StPO",  # Zwangsmassnahmen: Subsidiarität (mildere Massnahmen)
    "Art. 197 Abs. 1 lit. d StPO",  # Zwangsmassnahmen: Verhältnismässigkeit
    "Art. 212 Abs. 3 StPO",         # Haftdauer darf erwartete Freiheitsstrafe nicht übersteigen
    "Art. 221 Abs. 1 StPO",         # Voraussetzungen U-Haft (dringender Tatverdacht + Haftgrund)
    "Art. 221 Abs. 1 lit. b StPO",  # Kollusionsgefahr (Beeinflussung / Beweisverdunkelung)
    "Art. 221 Abs. 1 lit. c StPO",  # Wiederholungsgefahr (ggf. alternativ relevant)
    "Art. 226 Abs. 2 StPO",         # Eröffnung Entscheid Zwangsmassnahmengericht
    "Art. 227 Abs. 1 StPO",         # Haftverlängerungsgesuch der Staatsanwaltschaft
    "Art. 227 Abs. 7 StPO",         # Maximale Verlängerungsdauer (3 bzw. 6 Monate)
    "Art. 228 Abs. 1 StPO",         # Haftentlassungsgesuch der beschuldigten Person
    "Art. 237 Abs. 1 StPO",         # Ersatzmassnahmen statt Haft
    "Art. 237 Abs. 2 StPO",         # Katalog der Ersatzmassnahmen (lit. a–g)
    # ── Strafgesetzbuch (StGB) ──
    "Art. 30 Abs. 5 StGB",          # Endgültiger Verzicht auf Strafantrag
    # ── Leitentscheide BGE – Kollusionsgefahr ──
    "BGE 137 IV 122 E. 5.2",        # Kollusionsgefahr – Anforderungen
    "BGE 143 IV 330 E. 2.1",        # Kollusionsgefahr – Konkretisierung
    "BGE 145 IV 179 E. 3.4",        # Haftüberprüfung / Fortdauer der Kollusionsgefahr
    # ── Leitentscheide BGE – Verhältnismässigkeit ──
    "BGE 117 Ia 257 E. 4b",         # Verhältnismässigkeit der U-Haft
    "BGE 132 I 21 E. 3.2",          # Verhältnismässigkeit / Überhaft
    "BGE 143 IV 9",                  # Verhältnismässigkeit als äussere Grenze der U-Haft
    # ── Leitentscheide BGE – Haftvoraussetzungen / Verlängerung ──
    "BGE 143 IV 316",               # Haftvoraussetzungen – Zusammenfassung
    "BGE 141 IV 190",               # Art. 227 Abs. 7 – 3-Monats-Maximum, periodische Überprüfung
    # ── Leitentscheide BGE – Ersatzmassnahmen ──
    "BGE 146 IV 136 E. 2.2",        # Ersatzmassnahmen bei Kollusionsgefahr
    "BGE 142 IV 367",               # Pflicht zur Prüfung von Ersatzmassnahmen
    # ── Leitentscheide BGE – Strafantrag / Wiederholungsgefahr ──
    "BGE 139 IV 270 E. 3.1",        # Strafantrag und Haft
    "BGE 146 IV 297",               # Wiederholungsgefahr (alternativ geltend gemacht)
]

if __name__ == "__main__":
    print(f"Total citations: {len(citations)}\n")
    for c in citations:
        print(f"  {c}")
