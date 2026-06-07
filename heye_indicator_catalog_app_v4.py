from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "processed" / "heye_indicators_long.csv"

st.set_page_config(page_title="HEYE-DEEP Dashboard", layout="wide")


# ----------------------------
# Interface copy
# ----------------------------
UI = {
    "it": {
        "language": "Lingua",
        "title": "HEYE-DEEP Dashboard",
        "subtitle": "Cruscotto territoriale su demografia, istruzione superiore, lavoro e transizione alla vita adulta",
        "menu": "Menu",
        "go_to": "Vai a",
        "data_status": "Stato dati",
        "source": "Fonte",
        "territories": "Territori",
        "territorial_level": "Livello territoriale",
        "sex_split": "Disaggregazione per sesso",
        "yes": "Si",
        "no": "No",
        "indicator_catalog": "Catalogo indicatori",
        "input_datasets": "Dataset input",
        "csv_contract": "Formato CSV standard",
        "download_indicators": "Scarica catalogo indicatori",
        "download_inputs": "Scarica catalogo input",
        "download_template": "Scarica template CSV dati",
        "real_data": "Dati reali caricati dal CSV standardizzato.",
        "demo_data": "CSV dati non trovato: i grafici mostrano dati dimostrativi e non vanno interpretati come risultati.",
        "bad_data": "CSV dati trovato, ma mancano colonne obbligatorie:",
        "schema_intro": "Questa pagina organizza la dashboard come infrastruttura di ricerca: indicatori, fonti, disponibilita territoriale e input da integrare.",
        "planned_sections": "Sezioni operative",
        "data_methods_intro": "Il modello dati e pensato per separare cio che e gia scaricabile, cio che richiede accordi o microdati, e cio che andra costruito come indicatore composito.",
        "required_columns": "Colonne obbligatorie",
        "optional_columns": "Colonne consigliate",
        "data_path": "Percorso dati atteso",
        "unit": "Unita",
        "chart_note": "Visualizzazione",
        "latest_year": "Ultimo anno disponibile",
        "all_years": "Tutti gli anni",
        "year_filter": "Anno",
        "sex": "Sesso",
        "entry_age": "Eta di ingresso",
        "territory": "Territorio",
        "age_group": "Classe di eta",
        "education": "Titolo di studio",
        "value": "Valore",
        "year": "Anno",
        "status_public": "Pubblico da scaricare/normalizzare",
        "status_agreement": "Richiede accordo, microdati o accesso riservato",
        "status_local": "Da richiedere a stakeholder o fonti locali",
        "status_composite": "Da costruire come indicatore composito",
        "status_demo": "Solo struttura demo nell'app",
        "overview": "Quadro operativo",
        "data_quality": "Nota di qualita",
        "data_quality_text": "La dashboard distingue sempre dati reali, dati dimostrativi e dati da richiedere. Questo evita di presentare come integrati indicatori non ancora disponibili.",
    },
    "en": {
        "language": "Language",
        "title": "HEYE-DEEP Dashboard",
        "subtitle": "Territorial dashboard on demography, higher education, employment and transition to adulthood",
        "menu": "Menu",
        "go_to": "Go to",
        "data_status": "Data status",
        "source": "Source",
        "territories": "Territories",
        "territorial_level": "Territorial level",
        "sex_split": "Sex split",
        "yes": "Yes",
        "no": "No",
        "indicator_catalog": "Indicator catalog",
        "input_datasets": "Input datasets",
        "csv_contract": "Standard CSV format",
        "download_indicators": "Download indicator catalog",
        "download_inputs": "Download input catalog",
        "download_template": "Download data CSV template",
        "real_data": "Real data loaded from the standardized CSV.",
        "demo_data": "Data CSV not found: charts use demonstration data and should not be read as results.",
        "bad_data": "Data CSV found, but required columns are missing:",
        "schema_intro": "This page organizes the dashboard as a research infrastructure: indicators, sources, territorial availability and inputs to integrate.",
        "planned_sections": "Operational sections",
        "data_methods_intro": "The data model separates what can already be downloaded, what requires agreements or microdata, and what must be built as a composite indicator.",
        "required_columns": "Required columns",
        "optional_columns": "Recommended columns",
        "data_path": "Expected data path",
        "unit": "Unit",
        "chart_note": "Visualization",
        "latest_year": "Latest available year",
        "all_years": "All years",
        "year_filter": "Year",
        "sex": "Sex",
        "entry_age": "Entry age",
        "territory": "Territory",
        "age_group": "Age group",
        "education": "Education",
        "value": "Value",
        "year": "Year",
        "status_public": "Public data to download/normalize",
        "status_agreement": "Requires agreement, microdata or restricted access",
        "status_local": "To be requested from stakeholders or local sources",
        "status_composite": "To be built as a composite indicator",
        "status_demo": "Demo structure only in the app",
        "overview": "Operational overview",
        "data_quality": "Quality note",
        "data_quality_text": "The dashboard always separates real data, demonstration data and data to be requested. This avoids presenting indicators as integrated before they are available.",
    },
}


SECTION_LABELS = {
    "schema": {
        "it": "Schema operativo",
        "en": "Operational schema",
    },
    "population_pipeline": {
        "it": "Popolazione e pipeline educativa",
        "en": "Population and educational pipeline",
    },
    "employment_quality": {
        "it": "Lavoro giovanile e qualita del lavoro",
        "en": "Youth employment and job quality",
    },
    "mobility_retention": {
        "it": "Mobilita e retention",
        "en": "Mobility and retention",
    },
    "autonomy_vulnerability": {
        "it": "Autonomia economica e vulnerabilita",
        "en": "Economic autonomy and vulnerability",
    },
    "wellbeing": {
        "it": "Benessere e percezioni",
        "en": "Well-being and perceptions",
    },
    "projections": {
        "it": "Proiezioni demografiche",
        "en": "Demographic projections",
    },
    "data_methods": {
        "it": "Dati e metodi",
        "en": "Data and methods",
    },
}


SECTIONS_ORDER = [
    "schema",
    "population_pipeline",
    "employment_quality",
    "mobility_retention",
    "autonomy_vulnerability",
    "wellbeing",
    "projections",
    "data_methods",
]


STATUS_LABEL_KEYS = {
    "public": "status_public",
    "agreement": "status_agreement",
    "local_request": "status_local",
    "composite": "status_composite",
    "demo": "status_demo",
}


REQUIRED_COLUMNS = [
    "indicator_id",
    "year",
    "territory",
    "territory_level",
    "value",
    "unit",
    "source",
    "data_status",
]

OPTIONAL_COLUMNS = [
    "sex",
    "age_group",
    "age",
    "education_level",
    "disciplinary_area",
    "contract_type",
    "student_status",
    "cohort",
    "notes",
]


# ----------------------------
# Dataset requirements
# ----------------------------
INPUT_DATASETS = [
    {
        "dataset_id": "istat_demo_ppc",
        "source": "ISTAT Demo / Popolazione residente",
        "title_it": "Popolazione per eta, sesso e territorio",
        "title_en": "Population by age, sex and territory",
        "priority": "1",
        "status": "public",
        "territorial_level": "Provincia, regione, Italia",
        "suggested_file": "data/raw/istat_demo_ppc_population.csv",
        "required_fields": "anno, territorio, livello_territoriale, sesso, eta/classe_eta, popolazione",
        "used_for": "quota giovani; struttura per eta; rapporto giovani/anziani; coorti in ingresso; proiezioni",
    },
    {
        "dataset_id": "istat_migration",
        "source": "ISTAT Demo / Esplora Dati",
        "title_it": "Migrazioni interne e internazionali per eta",
        "title_en": "Internal and international migration by age",
        "priority": "1",
        "status": "public",
        "territorial_level": "Provincia dove disponibile, regione, Italia",
        "suggested_file": "data/raw/istat_migration_youth.csv",
        "required_fields": "anno, territorio, sesso, classe_eta, iscritti, cancellati, saldo",
        "used_for": "saldo migratorio giovanile; inflow/outflow; mobilita e retention",
    },
    {
        "dataset_id": "istat_lfs",
        "source": "ISTAT Forze di Lavoro / Esplora Dati",
        "title_it": "Mercato del lavoro giovanile",
        "title_en": "Youth labour market",
        "priority": "1",
        "status": "public",
        "territorial_level": "Provincia se disponibile, regione, Italia",
        "suggested_file": "data/raw/istat_lfs_youth.csv",
        "required_fields": "anno, territorio, sesso, eta, titolo_studio, occupati, disoccupati, inattivi, tassi",
        "used_for": "occupazione; disoccupazione; inattivita; NEET; contratti temporanei; part-time involontario",
    },
    {
        "dataset_id": "bes_best",
        "source": "ISTAT BES / BesT",
        "title_it": "Benessere, qualita del lavoro e vulnerabilita territoriale",
        "title_en": "Well-being, job quality and territorial vulnerability",
        "priority": "1",
        "status": "public",
        "territorial_level": "Provincia, regione, Italia dove disponibile",
        "suggested_file": "data/raw/istat_bes_best.csv",
        "required_fields": "anno, territorio, indicatore, valore, unita",
        "used_for": "benessere soggettivo; housing stress/proxy; fiducia; qualita del lavoro; vulnerabilita",
    },
    {
        "dataset_id": "ustat_mur",
        "source": "MUR USTAT",
        "title_it": "Iscritti, immatricolati e laureati universitari",
        "title_en": "University enrolments, first-year entrants and graduates",
        "priority": "1",
        "status": "public",
        "territorial_level": "Ateneo, regione, Italia",
        "suggested_file": "data/raw/mur_ustat_university_pipeline.csv",
        "required_fields": "anno, ateneo/territorio, sesso, corso/area, iscritti, immatricolati, laureati",
        "used_for": "pipeline universitaria; completamenti; differenze di genere; profilo locale UniBg",
    },
    {
        "dataset_id": "indire_its",
        "source": "INDIRE / ITS Academy",
        "title_it": "Percorsi ITS, diplomi ed esiti occupazionali",
        "title_en": "ITS programmes, diplomas and employment outcomes",
        "priority": "2",
        "status": "public",
        "territorial_level": "Fondazione/territorio, regione, Italia",
        "suggested_file": "data/raw/indire_its_outcomes.csv",
        "required_fields": "anno, territorio, area_tecnologica, sesso, iscritti, diplomati, occupati_post_diploma",
        "used_for": "istruzione professionalizzante; confronto ITS/universita; esiti post-diploma",
    },
    {
        "dataset_id": "almalaurea",
        "source": "AlmaLaurea",
        "title_it": "Esiti occupazionali dei laureati",
        "title_en": "Graduate employment outcomes",
        "priority": "1",
        "status": "agreement",
        "territorial_level": "Ateneo, area disciplinare, territorio di lavoro dove disponibile",
        "suggested_file": "data/raw/almalaurea_graduate_outcomes.csv",
        "required_fields": "anno_laurea, anno_intervista, ateneo, sesso, area, occupazione, salario, contratto, coerenza, territorio_lavoro",
        "used_for": "occupazione a 1/3/5 anni; salario; contratto; mismatch; mobilita post-studio",
    },
    {
        "dataset_id": "eu_silc",
        "source": "EU-SILC",
        "title_it": "Reddito, condizioni di vita, casa e autonomia",
        "title_en": "Income, living conditions, housing and autonomy",
        "priority": "2",
        "status": "agreement",
        "territorial_level": "Italia/regione, microdati individuali",
        "suggested_file": "data/raw/eu_silc_young_adults.csv",
        "required_fields": "anno, eta, sesso, titolo_studio, reddito, deprivazione, housing_costs, arrears, household_status",
        "used_for": "autonomia economica; vulnerabilita; housing burden; arrears; autonomia abitativa",
    },
    {
        "dataset_id": "bankitalia_shiw",
        "source": "Banca d'Italia SHIW",
        "title_it": "Risorse familiari, reddito, ricchezza e debiti",
        "title_en": "Family resources, income, wealth and debt",
        "priority": "2",
        "status": "agreement",
        "territorial_level": "Microdati individuali/familiari",
        "suggested_file": "data/raw/bankitalia_shiw_young_households.csv",
        "required_fields": "anno, eta, sesso, famiglia, reddito, ricchezza, debiti, trasferimenti, condizione_abitativa",
        "used_for": "dipendenza dalle risorse familiari; fragilita economica; capacita di sostenere studio, casa e autonomia",
    },
    {
        "dataset_id": "ess_cronos",
        "source": "ESS / CRONOS",
        "title_it": "Benessere, fiducia e percezioni soggettive",
        "title_en": "Well-being, trust and subjective perceptions",
        "priority": "3",
        "status": "agreement",
        "territorial_level": "Italia/comparativo europeo",
        "suggested_file": "data/raw/ess_cronos_subjective_measures.csv",
        "required_fields": "anno, paese, eta, sesso, fiducia, soddisfazione, sicurezza_economica, aspettative",
        "used_for": "componente percepita dell'indice stabilita/autonomia; confronto comparativo",
    },
    {
        "dataset_id": "ukhls",
        "source": "UKHLS",
        "title_it": "Sequenze longitudinali studio-lavoro",
        "title_en": "Longitudinal education-work sequences",
        "priority": "3",
        "status": "agreement",
        "territorial_level": "Microdati longitudinali",
        "suggested_file": "data/raw/ukhls_sequences.csv",
        "required_fields": "id, wave/anno, eta, sesso, SES, istruzione, lavoro, contratto, reddito, benessere",
        "used_for": "sequence analysis; traiettorie studio-lavoro; event history sul primo lavoro stabile",
    },
    {
        "dataset_id": "admin_local",
        "source": "INPS, COB, Porta Lavoro, Confindustria, dati imprese",
        "title_it": "Dati amministrativi e territoriali da richiedere",
        "title_en": "Administrative and local data to request",
        "priority": "1",
        "status": "local_request",
        "territorial_level": "Provincia/comune/impresa dove accordato",
        "suggested_file": "data/raw/local_admin_labour_transitions.csv",
        "required_fields": "id anonimo, anno/mese, eta, sesso, titolo_studio, contratto, settore, impresa, territorio, salario, eventi lavoro",
        "used_for": "traiettorie occupazionali; domanda di lavoro; mismatch; retention; mobilita laureati",
    },
]


# ----------------------------
# Indicator catalog
# ----------------------------
INDICATORS = [
    {
        "indicator_id": "youth_share",
        "section_id": "population_pipeline",
        "indicator_it": "Quota di giovani",
        "indicator_en": "Share of young people",
        "description_it": "Peso delle classi giovani sul totale della popolazione residente.",
        "description_en": "Weight of young age groups in the resident population.",
        "source": "ISTAT Demo / PPC",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "age_structure",
        "data_status": "public",
        "input_dataset_ids": ["istat_demo_ppc"],
    },
    {
        "indicator_id": "entry_cohorts",
        "section_id": "population_pipeline",
        "indicator_it": "Coorti in ingresso in eta lavorativa",
        "indicator_en": "Cohorts entering working age",
        "description_it": "Numero e indice delle coorti che raggiungono 19, 21 e 25 anni.",
        "description_en": "Number and index of cohorts reaching ages 19, 21 and 25.",
        "source": "ISTAT Demo / PPC",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Indice o numero",
        "unit_en": "Index or count",
        "chart": "entry_cohorts",
        "data_status": "public",
        "input_dataset_ids": ["istat_demo_ppc"],
    },
    {
        "indicator_id": "youth_population_change",
        "section_id": "population_pipeline",
        "indicator_it": "Variazione della popolazione giovane",
        "indicator_en": "Change in the young population",
        "description_it": "Andamento nel tempo delle coorti giovani e confronto Bergamo, Lombardia, Italia.",
        "description_en": "Time trend of young cohorts and comparison between Bergamo, Lombardy and Italy.",
        "source": "ISTAT Demo / PPC",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Indice o variazione percentuale",
        "unit_en": "Index or percentage change",
        "chart": "trend",
        "data_status": "public",
        "input_dataset_ids": ["istat_demo_ppc"],
    },
    {
        "indicator_id": "youth_elderly_ratio",
        "section_id": "population_pipeline",
        "indicator_it": "Rapporto giovani/anziani",
        "indicator_en": "Young-to-old ratio",
        "description_it": "Rapporto tra popolazione giovane e popolazione anziana, utile per leggere pressioni demografiche e sostituzione generazionale.",
        "description_en": "Ratio between young and older population, useful for demographic pressure and generational replacement.",
        "source": "ISTAT Demo / PPC",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": False,
        "unit_it": "Rapporto",
        "unit_en": "Ratio",
        "chart": "trend",
        "data_status": "public",
        "input_dataset_ids": ["istat_demo_ppc"],
    },
    {
        "indicator_id": "tertiary_attainment",
        "section_id": "population_pipeline",
        "indicator_it": "Istruzione terziaria",
        "indicator_en": "Tertiary attainment",
        "description_it": "Quota o numero di giovani con istruzione terziaria, con disaggregazione per sesso e territorio.",
        "description_en": "Share or number of young people with tertiary education, by sex and territory.",
        "source": "USTAT MUR + ISTAT/Eurostat per contesto",
        "territorial_level": "Ateneo, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale o numero",
        "unit_en": "Percentage or count",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["ustat_mur", "istat_lfs"],
    },
    {
        "indicator_id": "university_enrolments",
        "section_id": "population_pipeline",
        "indicator_it": "Iscritti universitari",
        "indicator_en": "University enrolments",
        "description_it": "Studenti iscritti all'universita per anno, sesso, territorio o ateneo.",
        "description_en": "University students enrolled by year, sex, territory or university.",
        "source": "MUR USTAT",
        "territorial_level": "Ateneo, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["ustat_mur"],
    },
    {
        "indicator_id": "university_graduates",
        "section_id": "population_pipeline",
        "indicator_it": "Laureati e completamenti",
        "indicator_en": "Graduates and completions",
        "description_it": "Numero di laureati e completamenti universitari, per sesso e area disciplinare dove disponibile.",
        "description_en": "Number of graduates and completions, by sex and disciplinary area where available.",
        "source": "MUR USTAT",
        "territorial_level": "Ateneo, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["ustat_mur"],
    },
    {
        "indicator_id": "its_pipeline",
        "section_id": "population_pipeline",
        "indicator_it": "Percorsi ITS, iscritti e diplomi",
        "indicator_en": "ITS programmes, enrolments and diplomas",
        "description_it": "Profilo dei percorsi ITS Academy e dei relativi esiti occupazionali.",
        "description_en": "Profile of ITS Academy pathways and related employment outcomes.",
        "source": "INDIRE / ITS Academy",
        "territorial_level": "Fondazione/territorio, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero o tasso",
        "unit_en": "Count or rate",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["indire_its"],
    },
    {
        "indicator_id": "youth_employment_rate",
        "section_id": "employment_quality",
        "indicator_it": "Tasso di occupazione giovanile",
        "indicator_en": "Youth employment rate",
        "description_it": "Occupazione giovanile per sesso, eta, titolo di studio e territorio.",
        "description_en": "Youth employment by sex, age, education and territory.",
        "source": "ISTAT Forze di Lavoro / Esplora Dati",
        "territorial_level": "Provincia se disponibile, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["istat_lfs"],
    },
    {
        "indicator_id": "youth_unemployment_rate",
        "section_id": "employment_quality",
        "indicator_it": "Tasso di disoccupazione giovanile",
        "indicator_en": "Youth unemployment rate",
        "description_it": "Disoccupazione nelle classi giovani, con confronto territoriale e differenze di genere.",
        "description_en": "Unemployment among young age groups, with territorial comparison and gender differences.",
        "source": "ISTAT Forze di Lavoro / Esplora Dati",
        "territorial_level": "Provincia se disponibile, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["istat_lfs"],
    },
    {
        "indicator_id": "neet_rate",
        "section_id": "employment_quality",
        "indicator_it": "Tasso NEET",
        "indicator_en": "NEET rate",
        "description_it": "Giovani non occupati e non inseriti in istruzione o formazione.",
        "description_en": "Young people not in employment, education or training.",
        "source": "ISTAT / Eurostat / Forze di Lavoro",
        "territorial_level": "Regione e Italia, provincia dove disponibile",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["istat_lfs"],
    },
    {
        "indicator_id": "temporary_contracts",
        "section_id": "employment_quality",
        "indicator_it": "Contratti a tempo determinato",
        "indicator_en": "Temporary contracts",
        "description_it": "Incidenza del lavoro temporaneo tra i giovani occupati.",
        "description_en": "Incidence of temporary employment among young workers.",
        "source": "ISTAT Forze di Lavoro, INPS/COB per dettaglio amministrativo",
        "territorial_level": "Regione/Italia; provincia con dati amministrativi",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "local_request",
        "input_dataset_ids": ["istat_lfs", "admin_local"],
    },
    {
        "indicator_id": "involuntary_part_time",
        "section_id": "employment_quality",
        "indicator_it": "Part-time involontario",
        "indicator_en": "Involuntary part-time",
        "description_it": "Quota di giovani in part-time non scelto, indicatore di qualita e vulnerabilita lavorativa.",
        "description_en": "Share of young people in non-voluntary part-time work, a job-quality and vulnerability indicator.",
        "source": "ISTAT Forze di Lavoro",
        "territorial_level": "Regione/Italia; provincia dove disponibile",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["istat_lfs"],
    },
    {
        "indicator_id": "mismatch_overskill",
        "section_id": "employment_quality",
        "indicator_it": "Mismatch e overskill",
        "indicator_en": "Mismatch and overskilling",
        "description_it": "Coerenza tra titolo di studio e lavoro, specialmente nei primi anni dopo il titolo.",
        "description_en": "Match between education and job, especially in the first years after graduation.",
        "source": "AlmaLaurea, COB/INPS se disponibili",
        "territorial_level": "Ateneo/territorio di lavoro",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "agreement",
        "input_dataset_ids": ["almalaurea", "admin_local"],
    },
    {
        "indicator_id": "post_degree_employment",
        "section_id": "employment_quality",
        "indicator_it": "Occupazione dopo il titolo",
        "indicator_en": "Employment after graduation",
        "description_it": "Esiti occupazionali a 1, 3 e 5 anni dal titolo.",
        "description_en": "Employment outcomes 1, 3 and 5 years after graduation.",
        "source": "AlmaLaurea",
        "territorial_level": "Ateneo, area disciplinare, territorio",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "education_years_since",
        "data_status": "agreement",
        "input_dataset_ids": ["almalaurea"],
    },
    {
        "indicator_id": "graduate_salary",
        "section_id": "employment_quality",
        "indicator_it": "Salario dopo il titolo",
        "indicator_en": "Salary after graduation",
        "description_it": "Retribuzione dei laureati nei primi anni dopo il titolo, per genere, area e territorio.",
        "description_en": "Graduate earnings in the first years after graduation, by gender, field and territory.",
        "source": "AlmaLaurea, INPS dove accessibile",
        "territorial_level": "Ateneo/territorio di lavoro",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Euro o indice",
        "unit_en": "Euro or index",
        "chart": "education_years_since",
        "data_status": "agreement",
        "input_dataset_ids": ["almalaurea", "admin_local"],
    },
    {
        "indicator_id": "youth_migration_balance",
        "section_id": "mobility_retention",
        "indicator_it": "Saldo migratorio giovanile",
        "indicator_en": "Youth migration balance",
        "description_it": "Saldo tra ingressi e uscite dei giovani, con dettaglio per eta e sesso.",
        "description_en": "Balance between youth inflows and outflows, by age and sex.",
        "source": "ISTAT Demo / Esplora Dati",
        "territorial_level": "Provincia dove disponibile, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero o tasso",
        "unit_en": "Count or rate",
        "chart": "migration_balance",
        "data_status": "public",
        "input_dataset_ids": ["istat_migration"],
    },
    {
        "indicator_id": "youth_inflow_outflow",
        "section_id": "mobility_retention",
        "indicator_it": "Inflow e outflow dei giovani",
        "indicator_en": "Youth inflow and outflow",
        "description_it": "Separazione tra giovani che entrano e giovani che lasciano il territorio.",
        "description_en": "Separate view of young people entering and leaving the territory.",
        "source": "ISTAT migrazioni, dati locali",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero o tasso",
        "unit_en": "Count or rate",
        "chart": "migration_balance",
        "data_status": "public",
        "input_dataset_ids": ["istat_migration"],
    },
    {
        "indicator_id": "graduate_mobility",
        "section_id": "mobility_retention",
        "indicator_it": "Mobilita dei giovani laureati",
        "indicator_en": "Mobility of young graduates",
        "description_it": "Dove studiano, lavorano e si spostano i laureati: chi resta, chi si muove, chi lascia il territorio.",
        "description_en": "Where graduates study, work and move: who stays, moves or leaves the territory.",
        "source": "AlmaLaurea, ISTAT, INPS/COB se accessibili",
        "territorial_level": "Ateneo, provincia, regione",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale o flusso",
        "unit_en": "Percentage or flow",
        "chart": "bars_territory_sex",
        "data_status": "agreement",
        "input_dataset_ids": ["almalaurea", "admin_local"],
    },
    {
        "indicator_id": "retention_rate",
        "section_id": "mobility_retention",
        "indicator_it": "Retention territoriale",
        "indicator_en": "Territorial retention",
        "description_it": "Capacita del territorio di trattenere giovani qualificati e forza lavoro giovane.",
        "description_en": "Territory's capacity to retain qualified young people and young workers.",
        "source": "AlmaLaurea, ISTAT, COB/INPS, Porta Lavoro",
        "territorial_level": "Provincia/regione",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "local_request",
        "input_dataset_ids": ["almalaurea", "admin_local"],
    },
    {
        "indicator_id": "disposable_income",
        "section_id": "autonomy_vulnerability",
        "indicator_it": "Reddito disponibile",
        "indicator_en": "Disposable income",
        "description_it": "Risorse economiche disponibili per giovani e giovani famiglie.",
        "description_en": "Economic resources available to young people and young households.",
        "source": "EU-SILC, Banca d'Italia SHIW",
        "territorial_level": "Microdati/regione/Italia",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Euro o indice",
        "unit_en": "Euro or index",
        "chart": "trend",
        "data_status": "agreement",
        "input_dataset_ids": ["eu_silc", "bankitalia_shiw"],
    },
    {
        "indicator_id": "economic_fragility",
        "section_id": "autonomy_vulnerability",
        "indicator_it": "Fragilita economica",
        "indicator_en": "Economic fragility",
        "description_it": "Rischio di vulnerabilita economica, difficolta materiali o bassa capacita di assorbire shock.",
        "description_en": "Risk of economic vulnerability, material hardship or low capacity to absorb shocks.",
        "source": "EU-SILC, SHIW, BES",
        "territorial_level": "Microdati/regione/Italia",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale o indice",
        "unit_en": "Percentage or index",
        "chart": "bars_territory_sex",
        "data_status": "agreement",
        "input_dataset_ids": ["eu_silc", "bankitalia_shiw", "bes_best"],
    },
    {
        "indicator_id": "housing_burden",
        "section_id": "autonomy_vulnerability",
        "indicator_it": "Housing burden / stress abitativo",
        "indicator_en": "Housing burden / housing stress",
        "description_it": "Peso dei costi abitativi su reddito e condizioni materiali.",
        "description_en": "Weight of housing costs on income and material conditions.",
        "source": "EU-SILC, BES/BesT",
        "territorial_level": "Provincia dove disponibile, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale o proxy",
        "unit_en": "Percentage or proxy",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["eu_silc", "bes_best"],
    },
    {
        "indicator_id": "arrears",
        "section_id": "autonomy_vulnerability",
        "indicator_it": "Arretrati e difficolta nei pagamenti",
        "indicator_en": "Arrears and payment difficulties",
        "description_it": "Difficolta nel pagamento di affitto, mutuo, bollette o altre spese essenziali.",
        "description_en": "Difficulties paying rent, mortgage, utilities or essential expenses.",
        "source": "EU-SILC",
        "territorial_level": "Microdati/regione/Italia",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "agreement",
        "input_dataset_ids": ["eu_silc"],
    },
    {
        "indicator_id": "residential_autonomy",
        "section_id": "autonomy_vulnerability",
        "indicator_it": "Autonomia abitativa",
        "indicator_en": "Residential autonomy",
        "description_it": "Quota di giovani che vivono fuori dalla famiglia di origine o in nuclei autonomi.",
        "description_en": "Share of young people living outside the parental household or in autonomous households.",
        "source": "EU-SILC, ISTAT famiglie",
        "territorial_level": "Regione/Italia; provincia dove disponibile",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "bars_territory_sex",
        "data_status": "agreement",
        "input_dataset_ids": ["eu_silc", "istat_demo_ppc"],
    },
    {
        "indicator_id": "subjective_wellbeing",
        "section_id": "wellbeing",
        "indicator_it": "Benessere soggettivo",
        "indicator_en": "Subjective well-being",
        "description_it": "Soddisfazione per la vita e benessere percepito nelle classi giovani.",
        "description_en": "Life satisfaction and perceived well-being among young people.",
        "source": "BES/BesT, ESS/CRONOS",
        "territorial_level": "Provincia/regione/Italia dove disponibile",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Punteggio o percentuale",
        "unit_en": "Score or percentage",
        "chart": "bars_territory_sex",
        "data_status": "public",
        "input_dataset_ids": ["bes_best", "ess_cronos"],
    },
    {
        "indicator_id": "trust_future",
        "section_id": "wellbeing",
        "indicator_it": "Fiducia nel futuro",
        "indicator_en": "Trust in the future",
        "description_it": "Percezione di prospettive future, sicurezza e stabilita attesa.",
        "description_en": "Perceived future prospects, security and expected stability.",
        "source": "ESS/CRONOS, indagini comparative o survey HEYE future",
        "territorial_level": "Italia/comparativo; locale solo con survey dedicata",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Punteggio o percentuale",
        "unit_en": "Score or percentage",
        "chart": "bars_territory_sex",
        "data_status": "agreement",
        "input_dataset_ids": ["ess_cronos"],
    },
    {
        "indicator_id": "perceived_stability",
        "section_id": "wellbeing",
        "indicator_it": "Stabilita percepita",
        "indicator_en": "Perceived stability",
        "description_it": "Percezione di sicurezza economica, lavorativa e abitativa.",
        "description_en": "Perceived economic, employment and housing security.",
        "source": "ESS/CRONOS, survey HEYE future",
        "territorial_level": "Italia/comparativo; locale solo con survey dedicata",
        "territories": ["Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Punteggio o percentuale",
        "unit_en": "Score or percentage",
        "chart": "bars_territory_sex",
        "data_status": "agreement",
        "input_dataset_ids": ["ess_cronos"],
    },
    {
        "indicator_id": "stability_autonomy_index",
        "section_id": "wellbeing",
        "indicator_it": "Indice di stabilita/autonomia giovanile",
        "indicator_en": "Youth stability/autonomy index",
        "description_it": "Indicatore multidimensionale: lavoro, reddito, casa, vulnerabilita e componente percepita.",
        "description_en": "Multidimensional indicator: work, income, housing, vulnerability and perceived component.",
        "source": "EU-SILC, SHIW, BES, ESS/CRONOS",
        "territorial_level": "Da costruire su dati armonizzati",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Indice composito",
        "unit_en": "Composite index",
        "chart": "trend",
        "data_status": "composite",
        "input_dataset_ids": ["eu_silc", "bankitalia_shiw", "bes_best", "ess_cronos"],
    },
    {
        "indicator_id": "working_age_entry_projection",
        "section_id": "projections",
        "indicator_it": "Proiezione ingressi in eta lavorativa",
        "indicator_en": "Projection of entry into working age",
        "description_it": "Stima delle coorti che entreranno nel mercato del lavoro nei prossimi 10-20 anni, sotto scenari di istruzione, partecipazione e pensionamento.",
        "description_en": "Estimate of cohorts entering the labour market over the next 10-20 years under education, participation and retirement scenarios.",
        "source": "ISTAT Demo / PPC, Forze di Lavoro",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero o indice",
        "unit_en": "Count or index",
        "chart": "entry_cohorts",
        "data_status": "composite",
        "input_dataset_ids": ["istat_demo_ppc", "istat_lfs"],
    },
]


# ----------------------------
# Data helpers
# ----------------------------
def text(key, lang):
    return UI[lang][key]


def label(value, lang):
    if isinstance(value, dict):
        return value.get(lang) or value.get("it") or value.get("en") or ""
    return value


def section_label(section_id, lang):
    return SECTION_LABELS[section_id][lang]


def status_label(status, lang):
    return text(STATUS_LABEL_KEYS.get(status, "status_demo"), lang)


def indicator_name(ind, lang):
    return ind[f"indicator_{lang}"]


def indicator_description(ind, lang):
    return ind[f"description_{lang}"]


def indicator_unit(ind, lang):
    return ind[f"unit_{lang}"]


@st.cache_data
def load_standard_data(path):
    if not path.exists():
        return pd.DataFrame(), "missing", []
    df = pd.read_csv(path)
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        return pd.DataFrame(), "bad_schema", missing
    return df, "ok", []


def indicator_catalog_df(lang):
    rows = []
    for ind in INDICATORS:
        rows.append({
            "indicator_id": ind["indicator_id"],
            "section": section_label(ind["section_id"], lang),
            "indicator": indicator_name(ind, lang),
            "description": indicator_description(ind, lang),
            "source": ind["source"],
            "territorial_level": ind["territorial_level"],
            "territories": ", ".join(ind["territories"]),
            "sex_split": text("yes", lang) if ind["sex_split"] else text("no", lang),
            "unit": indicator_unit(ind, lang),
            "data_status": status_label(ind["data_status"], lang),
            "input_dataset_ids": ", ".join(ind["input_dataset_ids"]),
        })
    return pd.DataFrame(rows)


def input_datasets_df(lang):
    rows = []
    for ds in INPUT_DATASETS:
        rows.append({
            "dataset_id": ds["dataset_id"],
            "priority": ds["priority"],
            "source": ds["source"],
            "dataset": ds[f"title_{lang}"],
            "territorial_level": ds["territorial_level"],
            "data_status": status_label(ds["status"], lang),
            "suggested_file": ds["suggested_file"],
            "required_fields": ds["required_fields"],
            "used_for": ds["used_for"],
        })
    return pd.DataFrame(rows)


def template_df():
    return pd.DataFrame([{
        "indicator_id": "youth_employment_rate",
        "year": 2024,
        "territory": "Bergamo",
        "territory_level": "province",
        "sex": "Total",
        "age_group": "15-34",
        "age": "",
        "education_level": "all",
        "disciplinary_area": "",
        "contract_type": "",
        "student_status": "",
        "cohort": "",
        "value": 0.0,
        "unit": "%",
        "source": "ISTAT LFS",
        "data_status": "real",
        "notes": "Replace this row with real harmonized data.",
    }])


def real_rows_for_indicator(data_df, indicator_id):
    if data_df.empty:
        return pd.DataFrame()
    rows = data_df[data_df["indicator_id"] == indicator_id].copy()
    if "sex" not in rows.columns:
        rows["sex"] = "Total"
    if "age_group" not in rows.columns:
        rows["age_group"] = ""
    return rows


# ----------------------------
# Demonstration data
# ----------------------------
def territory_sex_values(territories):
    rows = []
    base = {"Bergamo": 62, "Lombardia": 66, "Italia": 59}
    shift = {"Total": 0, "Female": -4, "Male": 3}
    for territory in territories:
        for sex in ["Total", "Female", "Male"]:
            rows.append({
                "territory": territory,
                "sex": sex,
                "value": base.get(territory, 60) + shift[sex],
            })
    return pd.DataFrame(rows)


def trend_values(territories, sex_split=True):
    rows = []
    years = [2018, 2020, 2022, 2024, 2026]
    base = {"Bergamo": 100, "Lombardia": 103, "Italia": 98}
    sex_shift = {"Total": 0, "Female": 2, "Male": -1}
    for territory in territories:
        sexes = ["Total", "Female", "Male"] if sex_split else ["Total"]
        for sex in sexes:
            for i, year in enumerate(years):
                rows.append({
                    "year": year,
                    "territory": territory,
                    "sex": sex,
                    "value": base.get(territory, 100) + i * 2 + sex_shift.get(sex, 0),
                })
    return pd.DataFrame(rows)


def age_structure_values(territories):
    rows = []
    age_groups = ["0-14", "15-24", "25-34", "35-64", "65+"]
    profiles = {
        "Bergamo": [12, 10, 12, 42, 24],
        "Lombardia": [12, 10, 13, 41, 24],
        "Italia": [12, 9, 11, 41, 27],
    }
    sex_adjustments = {
        "Total": [0, 0, 0, 0, 0],
        "Female": [0, 0, -1, -1, 2],
        "Male": [0, 0, 1, 1, -2],
    }
    for territory in territories:
        for sex in ["Total", "Female", "Male"]:
            for age_group, value, adjustment in zip(age_groups, profiles.get(territory, profiles["Italia"]), sex_adjustments[sex]):
                rows.append({
                    "territory": territory,
                    "sex": sex,
                    "age_group": age_group,
                    "value": value + adjustment,
                })
    return pd.DataFrame(rows)


def migration_values(territories):
    rows = []
    age_groups = ["15-19", "20-24", "25-29", "30-34"]
    base = {
        "Bergamo": [1, 5, 7, 3],
        "Lombardia": [2, 6, 8, 4],
        "Italia": [0, 2, 3, 1],
    }
    sex_adjustment = {"Total": 0, "Female": -1, "Male": 1}
    for territory in territories:
        for sex in ["Total", "Female", "Male"]:
            for age_group, value in zip(age_groups, base.get(territory, base["Italia"])):
                rows.append({
                    "territory": territory,
                    "sex": sex,
                    "age_group": age_group,
                    "value": value + sex_adjustment[sex],
                })
    return pd.DataFrame(rows)


def education_years_values(territories):
    rows = []
    years_since = [1, 2, 3, 4, 5]
    education_levels = ["Low", "Medium", "High"]
    territory_adjustment = {"Bergamo": 1, "Lombardia": 2, "Italia": 0}
    sex_adjustment = {"Total": 0, "Female": -3, "Male": 2}
    education_base = {"Low": 55, "Medium": 68, "High": 79}
    for territory in territories:
        for sex in ["Total", "Female", "Male"]:
            for education in education_levels:
                for i, years in enumerate(years_since):
                    rows.append({
                        "territory": territory,
                        "sex": sex,
                        "years_since_completion": years,
                        "education_level": education,
                        "value": education_base[education] + i * 2 + territory_adjustment.get(territory, 0) + sex_adjustment[sex],
                    })
    return pd.DataFrame(rows)


def entry_cohorts_values(territories):
    rows = []
    years = [2024, 2026, 2028, 2030, 2032]
    entry_ages = ["19", "21", "25"]
    base = {
        "Bergamo": {"19": 100, "21": 100, "25": 100},
        "Lombardia": {"19": 100, "21": 101, "25": 102},
        "Italia": {"19": 100, "21": 99, "25": 98},
    }
    sex_adjustment = {"Total": 0, "Female": -1, "Male": 1}
    for territory in territories:
        for sex in ["Total", "Female", "Male"]:
            for entry_age in entry_ages:
                for i, year in enumerate(years):
                    decline = 2 if entry_age == "19" else 1 if entry_age == "21" else 0.5
                    rows.append({
                        "year": year,
                        "territory": territory,
                        "sex": sex,
                        "entry_age": entry_age,
                        "value": base[territory][entry_age] - i * decline + sex_adjustment[sex],
                    })
    return pd.DataFrame(rows)


# ----------------------------
# Chart renderers
# ----------------------------
def filter_by_sex(df, ind, lang, key_prefix):
    if not ind["sex_split"] or "sex" not in df.columns:
        return df
    options = [x for x in ["Total", "Female", "Male"] if x in set(df["sex"].dropna())]
    if not options:
        options = sorted(df["sex"].dropna().unique().tolist())
    if len(options) <= 1:
        return df
    selected = st.radio(text("sex", lang), options, horizontal=True, key=f"{key_prefix}_sex")
    return df[df["sex"] == selected]


def render_real_chart(df, ind, lang):
    df = filter_by_sex(df, ind, lang, f"real_{ind['indicator_id']}")
    y_title = indicator_unit(ind, lang)

    if "year" in df.columns and df["year"].nunique() > 1:
        chart = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("territory:N", title=text("territory", lang)),
            tooltip=["year", "territory", "sex", "value", "unit", "source"],
        )
    elif "age_group" in df.columns and df["age_group"].replace("", pd.NA).dropna().nunique() > 1:
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("age_group:N", title=text("age_group", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("territory:N", title=text("territory", lang)),
            xOffset="territory:N",
            tooltip=["age_group", "territory", "sex", "value", "unit", "source"],
        )
    else:
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("territory:N", title=text("territory", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("territory:N", title=text("territory", lang)),
            tooltip=["territory", "sex", "value", "unit", "source"],
        )
    st.altair_chart(chart.properties(height=330), width="stretch")


def render_demo_chart(ind, lang):
    chart_type = ind["chart"]
    y_title = indicator_unit(ind, lang)

    if chart_type == "trend":
        df = trend_values(ind["territories"], sex_split=ind["sex_split"])
        df = filter_by_sex(df, ind, lang, f"demo_{ind['indicator_id']}")
        chart = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("territory:N", title=text("territory", lang)),
            tooltip=["year", "territory", "sex", "value"],
        )
    elif chart_type == "age_structure":
        df = age_structure_values(ind["territories"])
        df = filter_by_sex(df, ind, lang, f"demo_{ind['indicator_id']}")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("age_group:N", title=text("age_group", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("territory:N", title=text("territory", lang)),
            xOffset="territory:N",
            tooltip=["age_group", "territory", "sex", "value"],
        )
    elif chart_type == "migration_balance":
        df = migration_values(ind["territories"])
        df = filter_by_sex(df, ind, lang, f"demo_{ind['indicator_id']}")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("age_group:N", title=text("age_group", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("territory:N", title=text("territory", lang)),
            xOffset="territory:N",
            tooltip=["age_group", "territory", "sex", "value"],
        )
    elif chart_type == "education_years_since":
        df = education_years_values(ind["territories"])
        df = filter_by_sex(df, ind, lang, f"demo_{ind['indicator_id']}")
        territory = st.radio(text("territory", lang), ind["territories"], horizontal=True, key=f"demo_{ind['indicator_id']}_territory")
        df = df[df["territory"] == territory]
        chart = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X("years_since_completion:Q", title="Years since completion"),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("education_level:N", title=text("education", lang)),
            tooltip=["years_since_completion", "education_level", "value"],
        )
    elif chart_type == "entry_cohorts":
        df = entry_cohorts_values(ind["territories"])
        df = filter_by_sex(df, ind, lang, f"demo_{ind['indicator_id']}")
        entry_age = st.radio(text("entry_age", lang), ["19", "21", "25"], horizontal=True, key=f"demo_{ind['indicator_id']}_entry_age")
        df = df[df["entry_age"] == entry_age]
        chart = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("territory:N", title=text("territory", lang)),
            tooltip=["year", "territory", "sex", "entry_age", "value"],
        )
    else:
        df = territory_sex_values(ind["territories"])
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("territory:N", title=text("territory", lang)),
            y=alt.Y("value:Q", title=y_title),
            color=alt.Color("sex:N", title=text("sex", lang)),
            xOffset="sex:N",
            tooltip=["territory", "sex", "value"],
        )

    st.altair_chart(chart.properties(height=330), width="stretch")


def render_indicator(ind, data_df, data_state, lang):
    st.markdown(f"### {indicator_name(ind, lang)}")
    st.write(indicator_description(ind, lang))

    meta1, meta2, meta3 = st.columns([1.4, 1.1, 1])
    with meta1:
        st.markdown(f"**{text('source', lang)}:** {ind['source']}")
        st.markdown(f"**{text('territories', lang)}:** {', '.join(ind['territories'])}")
    with meta2:
        st.markdown(f"**{text('territorial_level', lang)}:** {ind['territorial_level']}")
        st.markdown(f"**{text('unit', lang)}:** {indicator_unit(ind, lang)}")
    with meta3:
        st.markdown(f"**{text('data_status', lang)}:** {status_label(ind['data_status'], lang)}")
        st.markdown(f"**{text('sex_split', lang)}:** {text('yes', lang) if ind['sex_split'] else text('no', lang)}")

    real_df = real_rows_for_indicator(data_df, ind["indicator_id"])
    if data_state == "ok" and not real_df.empty:
        st.caption(text("real_data", lang))
        render_real_chart(real_df, ind, lang)
    else:
        st.caption(text("demo_data", lang))
        render_demo_chart(ind, lang)


def render_schema_page(data_df, data_state, missing_cols, lang):
    st.subheader(text("overview", lang))
    st.write(text("schema_intro", lang))

    if data_state == "ok":
        st.success(text("real_data", lang))
    elif data_state == "bad_schema":
        st.warning(f"{text('bad_data', lang)} {', '.join(missing_cols)}")
    else:
        st.warning(text("demo_data", lang))

    m1, m2, m3, m4 = st.columns(4)
    m1.metric(text("indicator_catalog", lang), len(INDICATORS))
    m2.metric(text("input_datasets", lang), len(INPUT_DATASETS))
    m3.metric(text("territories", lang), "Bergamo / Lombardia / Italia")
    m4.metric(text("data_path", lang), "data/processed")

    tabs = st.tabs([text("indicator_catalog", lang), text("input_datasets", lang), text("csv_contract", lang)])
    indicators_df = indicator_catalog_df(lang)
    datasets_df = input_datasets_df(lang)

    with tabs[0]:
        st.dataframe(indicators_df, width="stretch", hide_index=True)
        st.download_button(
            text("download_indicators", lang),
            indicators_df.to_csv(index=False).encode("utf-8"),
            file_name=f"heye_indicator_catalog_{lang}.csv",
            mime="text/csv",
        )

    with tabs[1]:
        st.dataframe(datasets_df, width="stretch", hide_index=True)
        st.download_button(
            text("download_inputs", lang),
            datasets_df.to_csv(index=False).encode("utf-8"),
            file_name=f"heye_input_dataset_requirements_{lang}.csv",
            mime="text/csv",
        )

    with tabs[2]:
        st.markdown(f"**{text('data_path', lang)}:** `{DATA_FILE}`")
        st.markdown(f"**{text('required_columns', lang)}:** `{', '.join(REQUIRED_COLUMNS)}`")
        st.markdown(f"**{text('optional_columns', lang)}:** `{', '.join(OPTIONAL_COLUMNS)}`")
        st.dataframe(template_df(), width="stretch", hide_index=True)
        st.download_button(
            text("download_template", lang),
            template_df().to_csv(index=False).encode("utf-8"),
            file_name="heye_indicators_long_template.csv",
            mime="text/csv",
        )


def render_data_methods_page(lang):
    st.subheader(section_label("data_methods", lang))
    st.write(text("data_methods_intro", lang))
    st.info(text("data_quality_text", lang))

    st.markdown(f"**{text('data_path', lang)}:** `{DATA_FILE}`")
    st.markdown(f"**{text('required_columns', lang)}:** `{', '.join(REQUIRED_COLUMNS)}`")
    st.markdown(f"**{text('optional_columns', lang)}:** `{', '.join(OPTIONAL_COLUMNS)}`")

    st.markdown(f"### {text('input_datasets', lang)}")
    st.dataframe(input_datasets_df(lang), width="stretch", hide_index=True)


# ----------------------------
# App layout
# ----------------------------
data_df, data_state, missing_cols = load_standard_data(DATA_FILE)

with st.sidebar:
    language_label = st.radio("Lingua / Language", ["Italiano", "English"], horizontal=True)
    lang = "it" if language_label == "Italiano" else "en"

    st.header(text("menu", lang))
    page = st.radio(
        text("go_to", lang),
        SECTIONS_ORDER,
        format_func=lambda section_id: section_label(section_id, lang),
    )
    st.markdown("---")
    st.markdown(f"**{text('data_status', lang)}**")
    if data_state == "ok":
        st.success(text("real_data", lang))
    elif data_state == "bad_schema":
        st.warning(f"{text('bad_data', lang)} {', '.join(missing_cols)}")
    else:
        st.warning(text("demo_data", lang))
    st.caption(str(DATA_FILE))

st.title(text("title", lang))
st.caption(text("subtitle", lang))

if page == "schema":
    render_schema_page(data_df, data_state, missing_cols, lang)
elif page == "data_methods":
    render_data_methods_page(lang)
else:
    st.subheader(section_label(page, lang))
    section_indicators = [ind for ind in INDICATORS if ind["section_id"] == page]
    for indicator in section_indicators:
        with st.container(border=True):
            render_indicator(indicator, data_df, data_state, lang)
