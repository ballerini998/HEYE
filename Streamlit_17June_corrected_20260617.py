from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
LOGO_FILE = BASE_DIR / "heyedeep.png"
HEYE_LOGO_FILE = BASE_DIR / "heye_logo.svg"

DATASETS = {
    "population_current": BASE_DIR / "data" / "processed" / "population_current.csv",
    "population_projections": BASE_DIR / "data" / "processed" / "population_projections.csv",
    "unemployment_youth": BASE_DIR / "data" / "processed" / "labour_market_youth.csv",
    "inactivity_youth": BASE_DIR / "data" / "processed" / "inactivity_youth.csv",
    "migration_youth": BASE_DIR / "data" / "processed" / "migration_youth.csv",
    "university_pipeline": BASE_DIR / "data" / "processed" / "university_pipeline.csv",
    "bes_best": BASE_DIR / "data" / "processed" / "bes_best_indicators.csv",
}

st.set_page_config(page_title="HEYE-DEEP Dashboard", layout="wide")


# ----------------------------
# Interface copy
# ----------------------------
UI = {
    "it": {
        "language": "Lingua",
        "title": "HEYE-DEEP Dashboard",
        "subtitle": "Cruscotto territoriale su demografia, istruzione superiore, lavoro giovanile, migrazioni, BesT e transizione alla vita adulta",
        "welcome_title": "Benvenuto/a nella dashboard dell'Osservatorio HEYE-DEEP",
        "welcome_text": "Questo strumento consente di confrontare numerosi indicatori demografici e socio-economici riferiti alle tendenze demografiche, all'istruzione e al lavoro.",
        "welcome_focus": "Il focus è sulla popolazione giovanile (15-34 anni).",
        "welcome_areas_intro": "La dashboard è strutturata in {count} aree:",
        "welcome_comparison": "La dashboard consente un rapido confronto tra la provincia di Bergamo, la Lombardia e l'Italia.",
        "menu": "Menu",
        "go_to": "Vai a",
        "comparison": "Confronto territoriale",
        "show_lombardy": "Mostra Lombardia",
        "show_italy": "Mostra Italia",
        "data_status": "Stato dati",
        "source": "Fonte",
        "territories": "Territori",
        "territorial_level": "Livello territoriale",
        "sex_split": "Disaggregazione per sesso",
        "yes": "Sì",
        "no": "No",
        "indicator_catalog": "Indicatori disponibili",
        "input_datasets": "Dataset input",
        "csv_contract": "File dati caricati",
        "download_indicators": "Scarica indicatori",
        "download_inputs": "Scarica dataset input",
        "real_data": "Dati reali caricati dai dataset disponibili.",
        "missing_data": "Dataset non trovato o indicatore non costruibile con i file disponibili.",
        "bad_data": "CSV trovato, ma mancano colonne obbligatorie:",
        "schema_intro": "",
        "data_methods_intro": "",
        "required_columns": "Colonne obbligatorie",
        "data_path": "Percorso dati",
        "unit": "Unità",
        "year": "Anno",
        "academic_year": "Anno accademico",
        "sex": "Sesso",
        "entry_age": "Età di ingresso",
        "territory": "Territorio",
        "university_area": "Ateneo / area",
        "domain": "Dominio",
        "indicator": "Indicatore",
        "territory_scope": "Territori da mostrare",
        "main_territories": "Bergamo + confronti selezionati",
        "all_lombardy_territories": "Tutti i territori lombardi",
        "age_group": "Classe di età",
        "citizenship": "Cittadinanza",
        "movement_category": "Origine/destinazione",
        "flow_direction": "Flusso",
        "value": "Valore",
        "overview": "Quadro operativo",
        "data_quality": "Nota di qualità",
        "data_quality_text": "",
        "status_ok": "OK",
        "status_missing": "Mancante",
        "status_empty": "Vuoto",
        "status_bad_schema": "Schema non valido",
        "displayed_rows": "Dati filtrati",
        "no_filtered_data": "Nessun dato disponibile per i filtri selezionati.",
        "integrated": "Integrato",
        "filters": "Filtri",
    },
    "en": {
        "language": "Language",
        "title": "HEYE-DEEP Dashboard",
        "subtitle": "Territorial dashboard on demography, higher education, youth labour market, migration, BesT and transition to adulthood",
        "welcome_title": "Welcome to the HEYE-DEEP Observatory dashboard",
        "welcome_text": "This tool allows users to compare demographic and socio-economic indicators related to demographic trends, education and employment.",
        "welcome_focus": "The focus is on the young population (15-34 years).",
        "welcome_areas_intro": "The dashboard is structured into {count} areas:",
        "welcome_comparison": "The dashboard allows a quick comparison between the province of Bergamo, Lombardy and Italy.",
        "menu": "Menu",
        "go_to": "Go to",
        "comparison": "Territorial comparison",
        "show_lombardy": "Show Lombardy",
        "show_italy": "Show Italy",
        "data_status": "Data status",
        "source": "Source",
        "territories": "Territories",
        "territorial_level": "Territorial level",
        "sex_split": "Sex split",
        "yes": "Yes",
        "no": "No",
        "indicator_catalog": "Available indicators",
        "input_datasets": "Input datasets",
        "csv_contract": "Loaded data files",
        "download_indicators": "Download indicators",
        "download_inputs": "Download input datasets",
        "real_data": "Real data loaded from available datasets.",
        "missing_data": "Dataset not found or indicator cannot be built with available files.",
        "bad_data": "CSV found, but required columns are missing:",
        "schema_intro": "",
        "data_methods_intro": "",
        "required_columns": "Required columns",
        "data_path": "Data path",
        "unit": "Unit",
        "year": "Year",
        "academic_year": "Academic year",
        "sex": "Sex",
        "entry_age": "Entry age",
        "territory": "Territory",
        "university_area": "University / area",
        "domain": "Domain",
        "indicator": "Indicator",
        "territory_scope": "Territories to show",
        "main_territories": "Bergamo + selected comparisons",
        "all_lombardy_territories": "All Lombardy territories",
        "age_group": "Age group",
        "citizenship": "Citizenship",
        "movement_category": "Origin/destination",
        "flow_direction": "Flow",
        "value": "Value",
        "overview": "Operational overview",
        "data_quality": "Quality note",
        "data_quality_text": "",
        "status_ok": "OK",
        "status_missing": "Missing",
        "status_empty": "Empty",
        "status_bad_schema": "Invalid schema",
        "displayed_rows": "Filtered data",
        "no_filtered_data": "No data available for the selected filters.",
        "integrated": "Integrated",
        "filters": "Filters",
    },
}


SECTION_LABELS = {
    "welcome": {
        "it": "Benvenuto",
        "en": "Welcome",
    },
    "schema": {
        "it": "Schema operativo",
        "en": "Operational schema",
    },
    "population_pipeline": {
        "it": "Popolazione",
        "en": "Population",
    },
    "higher_education": {
        "it": "Istruzione superiore",
        "en": "Higher education",
    },
    "employment_quality": {
        "it": "Lavoro giovanile",
        "en": "Youth labour market",
    },
    "mobility_retention": {
        "it": "Mobilità e retention",
        "en": "Mobility and retention",
    },
    "projections": {
        "it": "Proiezioni demografiche",
        "en": "Demographic projections",
    },
    "bes_best": {
        "it": "BesT Lombardia",
        "en": "BesT Lombardy",
    },
    "data_methods": {
        "it": "Dati e metodi",
        "en": "Data and methods",
    },
}


SECTIONS_ORDER = [
    "welcome",
    "population_pipeline",
    "higher_education",
    "employment_quality",
    "mobility_retention",
    "projections",
    "bes_best",
    "data_methods",
]


POPULATION_CURRENT_COLUMNS = [
    "dataset_id",
    "year",
    "territory",
    "sex",
    "age",
    "age_group",
    "population",
    "source",
]

POPULATION_PROJECTIONS_COLUMNS = [
    "dataset_id",
    "year",
    "territory",
    "sex",
    "age",
    "age_group",
    "scenario",
    "population_projected",
    "source",
]

UNEMPLOYMENT_COLUMNS = [
    "dataset_id",
    "indicator_id",
    "year",
    "territory",
    "sex",
    "age_group",
    "unemployment_rate",
    "unit",
    "source",
]

INACTIVITY_COLUMNS = [
    "dataset_id",
    "indicator_id",
    "year",
    "territory",
    "sex",
    "age_group",
    "inactivity_rate",
    "unit",
    "source",
]

MIGRATION_COLUMNS = [
    "dataset_id",
    "year",
    "territory",
    "sex",
    "age_group",
    "citizenship",
    "movement_category",
    "flow_direction",
    "value",
    "unit",
    "source",
]

UNIVERSITY_COLUMNS = [
    "dataset_id",
    "indicator_id",
    "academic_year",
    "academic_year_start",
    "academic_year_end",
    "university_area",
    "sex",
    "first_year_enrolments",
    "unit",
    "source",
]

BES_BEST_COLUMNS = [
    "dataset_id",
    "domain_id",
    "domain_it",
    "table_id",
    "indicator_id",
    "indicator_it",
    "year",
    "territory",
    "territory_level",
    "main_comparison",
    "value",
    "unit",
    "polarity",
    "source",
    "source_file",
    "pdf_page",
]


INPUT_DATASETS = [
    {
        "dataset_id": "population_current_istat",
        "source": "ISTAT Demo / Popolazione residente",
        "title_it": "Popolazione per età, sesso e territorio",
        "title_en": "Population by age, sex and territory",
        "processed_file": "data/processed/population_current.csv",
        "raw_file": "data/raw/01_popolazione_attuale_istat/istat_demo_ppc.csv",
        "required_fields": "Territorio, Sesso, Età, Anno, Pop1gen",
        "used_for": "quota giovani; coorti 19/21/25; variazione 15-34; rapporto giovani/anziani",
    },
    {
        "dataset_id": "population_projections_istat",
        "source": "ISTAT previsioni popolazione / scenario mediano",
        "title_it": "Popolazione proiettata per età, sesso e territorio",
        "title_en": "Projected population by age, sex and territory",
        "processed_file": "data/processed/population_projections.csv",
        "raw_file": "data/raw/02_popolazione_proiettata_istat/istat_proj.csv",
        "required_fields": "Territorio, Sesso, Età, Anno, Mediana",
        "used_for": "coorti future a 19/21/25 anni; stock e variazione annua 15-64; confronto proiettato 15-29 e 55-64",
    },
    {
        "dataset_id": "labour_market_unemployment_istat_lfs",
        "source": "ISTAT Forze di Lavoro / indicatori territoriali",
        "title_it": "Tassi di disoccupazione per età, sesso e territorio",
        "title_en": "Unemployment rates by age, sex and territory",
        "processed_file": "data/processed/labour_market_youth.csv",
        "raw_file": "data/raw/04_lavoro_giovanile_istat_lfs/disoccupazionetassi.csv",
        "required_fields": "Territorio, Sesso, Età, Anno, Tasso_Disoccupazione",
        "used_for": "tasso di disoccupazione per fasce di età selezionabili",
    },
    {
        "dataset_id": "labour_market_inactivity_istat_lfs",
        "source": "ISTAT Forze di Lavoro / indicatori territoriali",
        "title_it": "Tassi di inattività per età, sesso e territorio",
        "title_en": "Inactivity rates by age, sex and territory",
        "processed_file": "data/processed/inactivity_youth.csv",
        "raw_file": "data/raw/04_lavoro_giovanile_istat_lfs/inattivitassi.csv",
        "required_fields": "Territorio, Sesso, Età, Anno, Tasso_Inattivi",
        "used_for": "tasso di inattività per fasce di età selezionabili",
    },
    {
        "dataset_id": "migration_istat",
        "source": "ISTAT migrazioni / iscrizioni e cancellazioni",
        "title_it": "Immigrati, emigrati e saldo per età, sesso, cittadinanza e territorio",
        "title_en": "Immigration, emigration and balance by age, sex, citizenship and territory",
        "processed_file": "data/processed/migration_youth.csv",
        "raw_file": "data/raw/03_migrazioni_istat/immigrati.csv + emigrati.csv",
        "required_fields": "Territorio, Sesso, Età, Anno, Cittadinanza, From/To, Immigrati/Emigrati",
        "used_for": "saldo migratorio; ingressi/uscite; categorie di origine/destinazione",
    },
    {
        "dataset_id": "university_mur_ustat",
        "source": "MUR USTAT / dataset immatricolati fornito",
        "title_it": "Immatricolati universitari per ateneo/area e sesso",
        "title_en": "University first-year entrants by university/area and sex",
        "processed_file": "data/processed/university_pipeline.csv",
        "raw_file": "data/raw/06_universita_mur_ustat/immatricolati.csv",
        "required_fields": "Anno, Ateneo, Sesso, Immatricolati",
        "used_for": "trend degli immatricolati; confronto Bergamo, altro Lombardia, altro Italia; differenze per sesso",
    },
    {
        "dataset_id": "bes_best_istat",
        "source": "ISTAT BesT Lombardia 2025",
        "title_it": "Indicatori BesT Lombardia estratti dal PDF 2025",
        "title_en": "BesT Lombardy indicators extracted from the 2025 PDF",
        "processed_file": "data/processed/bes_best_indicators.csv",
        "raw_file": "data/raw/05_bes_best_istat/BesT2025_Lombardia.pdf",
        "required_fields": "dominio, indicatore, anno, territorio, valore, unita",
        "used_for": "benessere territoriale; istruzione; lavoro; economia; sicurezza; ambiente; servizi; confronto Bergamo/Lombardia/Italia",
    },
]


INDICATORS = [
    {
        "indicator_id": "youth_share",
        "section_id": "population_pipeline",
        "indicator_it": "Struttura per età della popolazione",
        "indicator_en": "Population age structure",
        "description_it": "Quota delle principali classi di età sul totale della popolazione residente nell'ultimo anno disponibile.",
        "description_en": "Share of main age groups in the resident population in the latest available year.",
        "source": "ISTAT Demo / Popolazione residente",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "age_structure",
        "input_dataset_ids": ["population_current_istat"],
    },
    {
        "indicator_id": "entry_cohorts",
        "section_id": "population_pipeline",
        "indicator_it": "Coorti in ingresso in età lavorativa",
        "indicator_en": "Cohorts entering working age",
        "description_it": "Numero di residenti che raggiungono 19, 21 e 25 anni, con confronto Bergamo, Lombardia e Italia.",
        "description_en": "Residents reaching ages 19, 21 and 25, comparing Bergamo, Lombardy and Italy.",
        "source": "ISTAT Demo / Popolazione residente",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "entry_cohorts",
        "input_dataset_ids": ["population_current_istat"],
    },
    {
        "indicator_id": "youth_population_change",
        "section_id": "population_pipeline",
        "indicator_it": "Variazione della popolazione giovane",
        "indicator_en": "Change in the young population",
        "description_it": "Indice della popolazione giovane per classi 15-24, 25-34 e 15-34, con base nel primo anno disponibile.",
        "description_en": "Index of the young population for 15-24, 25-34 and 15-34 age bands, based on the first available year.",
        "source": "ISTAT Demo / Popolazione residente",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Indice",
        "unit_en": "Index",
        "chart": "trend_age_select",
        "input_dataset_ids": ["population_current_istat"],
    },
    {
        "indicator_id": "youth_elderly_ratio",
        "section_id": "population_pipeline",
        "indicator_it": "Rapporto giovani/anziani",
        "indicator_en": "Young-to-old ratio",
        "description_it": "Rapporto tra popolazione 15-34 e popolazione 65+, utile per leggere sostituzione generazionale e pressione demografica.",
        "description_en": "Ratio between population aged 15-34 and population aged 65+, useful for reading generational replacement and demographic pressure.",
        "source": "ISTAT Demo / Popolazione residente",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": False,
        "unit_it": "Rapporto",
        "unit_en": "Ratio",
        "chart": "trend",
        "input_dataset_ids": ["population_current_istat"],
    },
    {
        "indicator_id": "university_first_year_enrolments",
        "section_id": "higher_education",
        "indicator_it": "Immatricolati universitari",
        "indicator_en": "University first-year entrants",
        "description_it": "Trend degli immatricolati per anno accademico, area/ateneo e sesso.",
        "description_en": "Trend in first-year university entrants by academic year, university/area and sex.",
        "source": "MUR USTAT / dataset immatricolati fornito",
        "territorial_level": "Ateneo / area geografica del dataset",
        "territories": ["Bergamo", "Altro Lombardia", "Altro Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "university_enrolments",
        "input_dataset_ids": ["university_mur_ustat"],
    },
    {
        "indicator_id": "youth_unemployment_rate",
        "section_id": "employment_quality",
        "indicator_it": "Tasso di disoccupazione",
        "indicator_en": "Unemployment rate",
        "description_it": "Tasso di disoccupazione per fasce di età selezionabili, sesso e territorio.",
        "description_en": "Unemployment rate by selectable age group, sex and territory.",
        "source": "ISTAT Forze di Lavoro / indicatori territoriali",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "rate",
        "input_dataset_ids": ["labour_market_unemployment_istat_lfs"],
    },
    {
        "indicator_id": "youth_inactivity_rate",
        "section_id": "employment_quality",
        "indicator_it": "Tasso di inattività",
        "indicator_en": "Inactivity rate",
        "description_it": "Tasso di inattività per fasce di età selezionabili, sesso e territorio.",
        "description_en": "Inactivity rate by selectable age group, sex and territory.",
        "source": "ISTAT Forze di Lavoro / indicatori territoriali",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Percentuale",
        "unit_en": "Percentage",
        "chart": "rate",
        "input_dataset_ids": ["labour_market_inactivity_istat_lfs"],
    },
    {
        "indicator_id": "youth_migration_balance",
        "section_id": "mobility_retention",
        "indicator_it": "Saldo migratorio",
        "indicator_en": "Migration balance",
        "description_it": "Saldo tra immigrati ed emigrati, filtrabile per età, sesso, cittadinanza e categoria di origine/destinazione.",
        "description_en": "Balance between immigration and emigration, filterable by age, sex, citizenship and origin/destination category.",
        "source": "ISTAT migrazioni / iscrizioni e cancellazioni",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "migration_balance",
        "input_dataset_ids": ["migration_istat"],
    },
    {
        "indicator_id": "youth_inflow_outflow",
        "section_id": "mobility_retention",
        "indicator_it": "Immigrati ed emigrati",
        "indicator_en": "Immigration and emigration",
        "description_it": "Lettura separata di ingressi e uscite, con filtri su età, sesso, cittadinanza e categoria di origine/destinazione.",
        "description_en": "Separate view of inflows and outflows, with filters on age, sex, citizenship and origin/destination category.",
        "source": "ISTAT migrazioni / iscrizioni e cancellazioni",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "migration_flows",
        "input_dataset_ids": ["migration_istat"],
    },
    {
        "indicator_id": "working_age_entry_projection",
        "section_id": "projections",
        "indicator_it": "Proiezione ingressi in età lavorativa",
        "indicator_en": "Projection of entry into working age",
        "description_it": "Stima delle coorti future che raggiungono 19, 21 e 25 anni nello scenario mediano ISTAT.",
        "description_en": "Estimate of future cohorts reaching ages 19, 21 and 25 in the ISTAT median scenario.",
        "source": "ISTAT previsioni popolazione / scenario mediano",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "entry_cohorts",
        "input_dataset_ids": ["population_projections_istat"],
    },
    {
        "indicator_id": "working_age_stock_change_projection",
        "section_id": "projections",
        "indicator_it": "Variazione annua della popolazione in età lavorativa",
        "indicator_en": "Annual change in the working-age population",
        "description_it": "Differenza, rispetto all'anno precedente, tra gli stock proiettati di residenti tra 15 e 64 anni. Valori negativi indicano una riduzione dello stock, non un saldo migratorio.",
        "description_en": "Year-on-year difference in the projected stock of residents aged 15 to 64. Negative values indicate a declining stock, not a migration balance.",
        "source": "ISTAT previsioni popolazione / scenario mediano",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Variazione annua (persone)",
        "unit_en": "Annual change (people)",
        "chart": "working_age_balance",
        "input_dataset_ids": ["population_projections_istat"],
    },
    {
        "indicator_id": "young_older_workers_projection",
        "section_id": "projections",
        "indicator_it": "Giovani e adulti prossimi all'uscita dall'età lavorativa",
        "indicator_en": "Young people and adults approaching working-age exit",
        "description_it": "Numero proiettato di residenti tra 15 e 29 anni e tra 55 e 64 anni, rappresentati sulla stessa scala per confrontare l'ampiezza dei due gruppi.",
        "description_en": "Projected residents aged 15 to 29 and 55 to 64, shown on the same scale to compare the size of the two groups.",
        "source": "ISTAT previsioni popolazione / scenario mediano",
        "territorial_level": "Provincia, regione, Italia",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": True,
        "unit_it": "Numero",
        "unit_en": "Count",
        "chart": "generation_projection",
        "input_dataset_ids": ["population_projections_istat"],
    },
    {
        "indicator_id": "bes_best_indicator",
        "section_id": "bes_best",
        "indicator_it": "Indicatori BesT Lombardia",
        "indicator_en": "BesT Lombardy indicators",
        "description_it": "Indicatori territoriali selezionabili per dominio e indicatore.",
        "description_en": "Territorial indicators selectable by domain and indicator.",
        "source": "ISTAT BesT Lombardia 2025",
        "territorial_level": "Provincia, regione, ripartizione, Italia; grandi comuni dove presenti",
        "territories": ["Bergamo", "Lombardia", "Italia"],
        "sex_split": False,
        "unit_it": "Valore indicatore",
        "unit_en": "Indicator value",
        "chart": "bes_best_indicator",
        "input_dataset_ids": ["bes_best_istat"],
    },
]


# ----------------------------
# Helpers
# ----------------------------
def text(key, lang):
    return UI[lang][key]


SEX_LABELS = {
    "it": {
        "Total": "Totale",
        "Female": "Donne",
        "Male": "Uomini",
    },
    "en": {
        "Total": "Total",
        "Female": "Female",
        "Male": "Male",
    },
}


def sex_label(value, lang):
    return SEX_LABELS.get(lang, {}).get(str(value), str(value))


def localize_display_values(df, lang):
    if lang != "it" or "sex" not in df.columns:
        return df
    df = df.copy()
    df["sex"] = df["sex"].map(lambda value: sex_label(value, lang))
    return df


def section_label(section_id, lang):
    return SECTION_LABELS[section_id][lang]


def indicator_name(ind, lang):
    return ind[f"indicator_{lang}"]


def indicator_description(ind, lang):
    return ind[f"description_{lang}"]


def indicator_unit(ind, lang):
    return ind[f"unit_{lang}"]


def sort_age_groups(values):
    def key(value):
        value = str(value)
        if value == "Total":
            return (999, 999, value)
        if value.endswith("+"):
            return (int(value[:-1]), 999, value)
        parts = value.split("-")
        if len(parts) == 2 and all(part.isdigit() for part in parts):
            return (int(parts[0]), int(parts[1]), value)
        return (500, 500, value)

    return sorted([str(v) for v in values if pd.notna(v) and str(v) != ""], key=key)


def preferred_index(options, preferred):
    if preferred in options:
        return options.index(preferred)
    return 0


def selected_territories(show_lombardy, show_italy):
    territories = ["Bergamo"]
    if show_lombardy:
        territories.append("Lombardia")
    if show_italy:
        territories.append("Italia")
    return territories


def university_areas_for_territories(territories):
    mapping = {
        "Bergamo": "Bergamo",
        "Lombardia": "Altro Lombardia",
        "Italia": "Altro Italia",
    }
    return [mapping[territory] for territory in territories if territory in mapping]


def apply_standard_territory_filter(df, territories):
    if "territory" in df.columns:
        return df[df["territory"].isin(territories)]
    if "university_area" in df.columns:
        return df[df["university_area"].isin(university_areas_for_territories(territories))]
    return df


@st.cache_data
def load_csv(path, required_columns, numeric_columns=None, int_columns=None):
    numeric_columns = numeric_columns or []
    int_columns = int_columns or []
    if not path.exists():
        return pd.DataFrame(), "missing", []
    if path.stat().st_size == 0:
        return pd.DataFrame(), "empty", required_columns
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(), "empty", required_columns
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        return pd.DataFrame(), "bad_schema", missing
    df = df.copy()
    for col in int_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    drop_cols = [col for col in numeric_columns + int_columns if col in df.columns]
    if drop_cols:
        df = df.dropna(subset=drop_cols)
    for col in int_columns:
        df[col] = df[col].astype(int)
    return df, "ok", []


def population_current_rows(population_df, ind):
    if population_df.empty:
        return pd.DataFrame()

    indicator_id = ind["indicator_id"]
    df = population_df[population_df["territory"].isin(ind["territories"])].copy()
    if df.empty:
        return pd.DataFrame()

    source = df["source"].dropna().iloc[0] if "source" in df.columns and not df["source"].dropna().empty else ind["source"]

    if indicator_id == "youth_share":
        latest_year = int(df["year"].max())
        latest = df[df["year"] == latest_year].copy()
        grouped = latest.groupby(["year", "territory", "sex", "age_group"], as_index=False)["population"].sum()
        totals = latest.groupby(["year", "territory", "sex"], as_index=False)["population"].sum().rename(columns={"population": "total_population"})
        rows = grouped.merge(totals, on=["year", "territory", "sex"], how="left")
        rows["value"] = rows["population"] / rows["total_population"] * 100
        rows["unit"] = "%"
        rows["source"] = source
        return rows[["year", "territory", "sex", "age_group", "value", "unit", "source"]]

    if indicator_id == "entry_cohorts":
        rows = df[df["age"].isin([19, 21, 25])].copy()
        rows["entry_age"] = rows["age"].astype(str)
        rows["value"] = rows["population"]
        rows["unit"] = "count"
        return rows[["year", "territory", "sex", "entry_age", "value", "unit", "source"]]

    if indicator_id == "youth_population_change":
        bands = {
            "15-24": (15, 24),
            "25-34": (25, 34),
            "15-34": (15, 34),
        }
        band_rows = []
        for age_group, (age_min, age_max) in bands.items():
            tmp = df[(df["age"] >= age_min) & (df["age"] <= age_max)].copy()
            tmp = tmp.groupby(["year", "territory", "sex"], as_index=False)["population"].sum()
            tmp["age_group"] = age_group
            band_rows.append(tmp)
        rows = pd.concat(band_rows, ignore_index=True)
        base_year = int(rows["year"].min())
        base = rows[rows["year"] == base_year][["territory", "sex", "age_group", "population"]].rename(columns={"population": "base_population"})
        rows = rows.merge(base, on=["territory", "sex", "age_group"], how="left")
        rows["value"] = rows["population"] / rows["base_population"] * 100
        rows["unit"] = f"index {base_year}=100"
        rows["source"] = source
        return rows[["year", "territory", "sex", "age_group", "value", "unit", "source"]]

    if indicator_id == "youth_elderly_ratio":
        rows = df[df["sex"] == "Total"].copy()
        young = rows[(rows["age"] >= 15) & (rows["age"] <= 34)].groupby(["year", "territory"], as_index=False)["population"].sum()
        old = rows[rows["age"] >= 65].groupby(["year", "territory"], as_index=False)["population"].sum()
        young = young.rename(columns={"population": "young_population"})
        old = old.rename(columns={"population": "older_population"})
        rows = young.merge(old, on=["year", "territory"], how="left")
        rows["sex"] = "Total"
        rows["value"] = rows["young_population"] / rows["older_population"]
        rows["unit"] = "ratio"
        rows["source"] = source
        return rows[["year", "territory", "sex", "value", "unit", "source"]]

    return pd.DataFrame()


def population_projection_rows(projection_df, ind):
    if projection_df.empty:
        return pd.DataFrame()

    indicator_id = ind["indicator_id"]
    if indicator_id not in {
        "working_age_entry_projection",
        "working_age_stock_change_projection",
        "young_older_workers_projection",
    }:
        return pd.DataFrame()

    df = projection_df[projection_df["territory"].isin(ind["territories"])].copy()
    if df.empty:
        return pd.DataFrame()

    if indicator_id == "working_age_entry_projection":
        rows = df[df["age"].isin([19, 21, 25])].copy()
        rows["entry_age"] = rows["age"].astype(str)
        rows["value"] = rows["population_projected"]
        rows["unit"] = "count"
        return rows[["year", "territory", "sex", "entry_age", "scenario", "value", "unit", "source"]]

    if indicator_id == "working_age_stock_change_projection":
        rows = df[(df["age"] >= 15) & (df["age"] <= 64)].copy()
        rows = rows.groupby(
            ["year", "territory", "sex", "scenario", "source"],
            as_index=False,
        )["population_projected"].sum()
        rows = rows.sort_values(["territory", "sex", "scenario", "year"])
        rows["value"] = rows.groupby(
            ["territory", "sex", "scenario"]
        )["population_projected"].diff()
        rows = rows.dropna(subset=["value"])
        rows["unit"] = "annual stock change"
        return rows[["year", "territory", "sex", "scenario", "value", "unit", "source"]]

    bands = {
        "15-29": (15, 29),
        "55-64": (55, 64),
    }
    band_rows = []
    for age_group, (age_min, age_max) in bands.items():
        rows = df[(df["age"] >= age_min) & (df["age"] <= age_max)].copy()
        rows = rows.groupby(
            ["year", "territory", "sex", "scenario", "source"],
            as_index=False,
        )["population_projected"].sum()
        rows["age_group"] = age_group
        band_rows.append(rows)
    rows = pd.concat(band_rows, ignore_index=True)
    rows["value"] = rows["population_projected"]
    rows["unit"] = "count"
    return rows[["year", "territory", "sex", "age_group", "scenario", "value", "unit", "source"]]


def rate_rows(rate_df, ind, expected_indicator_id, value_column):
    if rate_df.empty or ind["indicator_id"] != expected_indicator_id:
        return pd.DataFrame()
    df = rate_df[rate_df["territory"].isin(ind["territories"])].copy()
    df["value"] = df[value_column]
    columns = ["year", "territory", "sex", "age_group", "value", "unit", "source"]
    if "notes" in df.columns:
        columns.append("notes")
    return df[columns]


def migration_rows(migration_df, ind):
    if migration_df.empty or ind["indicator_id"] not in {"youth_migration_balance", "youth_inflow_outflow"}:
        return pd.DataFrame()

    df = migration_df[migration_df["territory"].isin(ind["territories"])].copy()
    if ind["indicator_id"] == "youth_inflow_outflow":
        return df[["year", "territory", "sex", "age_group", "citizenship", "movement_category", "flow_direction", "value", "unit", "source", "notes"]]

    index_cols = ["year", "territory", "sex", "age_group", "citizenship", "movement_category"]
    pivot = df.pivot_table(index=index_cols, columns="flow_direction", values="value", aggfunc="sum", fill_value=0).reset_index()
    if "Immigrati" not in pivot.columns:
        pivot["Immigrati"] = 0
    if "Emigrati" not in pivot.columns:
        pivot["Emigrati"] = 0
    pivot["value"] = pivot["Immigrati"] - pivot["Emigrati"]
    pivot["unit"] = "count"
    pivot["source"] = ind["source"]
    pivot["notes"] = "Saldo = Immigrati - Emigrati."
    return pivot[["year", "territory", "sex", "age_group", "citizenship", "movement_category", "value", "unit", "source", "notes"]]


def university_rows(university_df, ind):
    if university_df.empty or ind["indicator_id"] != "university_first_year_enrolments":
        return pd.DataFrame()

    df = university_df[university_df["university_area"].isin(ind["territories"])].copy()
    if df.empty:
        return pd.DataFrame()

    df["value"] = df["first_year_enrolments"]
    columns = [
        "academic_year",
        "academic_year_start",
        "academic_year_end",
        "university_area",
        "sex",
        "value",
        "unit",
        "source",
    ]
    if "notes" in df.columns:
        columns.append("notes")
    return df[columns]


def bes_best_rows(bes_df, ind):
    if bes_df.empty or ind["indicator_id"] != "bes_best_indicator":
        return pd.DataFrame()

    df = bes_df.copy()
    columns = [
        "domain_it",
        "indicator_id",
        "indicator_it",
        "year",
        "territory",
        "territory_level",
        "main_comparison",
        "value",
        "unit",
        "polarity",
        "source",
        "source_file",
        "pdf_page",
    ]
    for optional in ["italy_value", "difference_from_italy", "notes"]:
        if optional in df.columns:
            columns.append(optional)
    return df[columns]


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
            "data_status": text("integrated", lang),
            "input_dataset_ids": ", ".join(ind["input_dataset_ids"]),
        })
    return pd.DataFrame(rows)


def input_datasets_df(lang):
    rows = []
    for ds in INPUT_DATASETS:
        rows.append({
            "dataset_id": ds["dataset_id"],
            "source": ds["source"],
            "dataset": ds[f"title_{lang}"],
            "processed_file": ds["processed_file"],
            "raw_file": ds["raw_file"],
            "required_fields": ds["required_fields"],
            "used_for": ds["used_for"],
        })
    return pd.DataFrame(rows)


def dataset_files_df(states, missing_columns, lang):
    rows = []
    for dataset_name, path in DATASETS.items():
        state = states.get(dataset_name, "missing")
        if state == "ok":
            status = text("status_ok", lang)
        elif state == "empty":
            status = text("status_empty", lang)
        elif state == "bad_schema":
            status = text("status_bad_schema", lang)
        else:
            status = text("status_missing", lang)
        rows.append({
            "dataset": dataset_name,
            "path": str(path.relative_to(BASE_DIR)),
            "status": status,
            "missing_columns": ", ".join(missing_columns.get(dataset_name, [])),
        })
    return pd.DataFrame(rows)


def filter_by_sex(df, ind, lang, key_prefix):
    if not ind["sex_split"] or "sex" not in df.columns:
        return df
    options = [x for x in ["Total", "Female", "Male"] if x in set(df["sex"].dropna())]
    if not options:
        options = sorted(df["sex"].dropna().unique().tolist())
    if len(options) <= 1:
        return df
    selected = st.radio(
        text("sex", lang),
        options,
        horizontal=True,
        key=f"{key_prefix}_sex",
        format_func=lambda value: sex_label(value, lang),
    )
    return df[df["sex"] == selected]


def filter_by_select(df, column, label_key, lang, key, preferred=None, sort_values=True):
    if column not in df.columns:
        return df
    values = df[column].replace("", pd.NA).dropna().astype(str).unique().tolist()
    if len(values) <= 1:
        return df
    if column == "age_group":
        options = sort_age_groups(values)
    elif sort_values:
        options = sorted(values)
    else:
        options = values
    index = preferred_index(options, preferred) if preferred else 0
    selected = st.selectbox(text(label_key, lang), options, index=index, key=key)
    return df[df[column].astype(str) == selected]


def filter_real_data(df, ind, lang, territories):
    df = filter_by_sex(df, ind, lang, f"real_{ind['indicator_id']}")

    if ind["chart"] == "bes_best_indicator":
        domains = sorted(df["domain_it"].dropna().unique().tolist())
        domain_index = preferred_index(domains, "Innovazione, ricerca e creativita")
        domain = st.selectbox(text("domain", lang), domains, index=domain_index, key=f"real_{ind['indicator_id']}_domain")
        df = df[df["domain_it"] == domain]

        indicators = df[["indicator_id", "indicator_it"]].drop_duplicates().sort_values("indicator_it")
        indicator_labels = indicators["indicator_it"].tolist()
        default_indicator = "Mobilita dei laureati italiani (25-39 anni)"
        indicator_index = preferred_index(indicator_labels, default_indicator)
        indicator_label = st.selectbox(text("indicator", lang), indicator_labels, index=indicator_index, key=f"real_{ind['indicator_id']}_indicator")
        indicator_id = indicators.loc[indicators["indicator_it"] == indicator_label, "indicator_id"].iloc[0]
        df = df[df["indicator_id"] == indicator_id]

        scope = st.radio(
            text("territory_scope", lang),
            [text("main_territories", lang), text("all_lombardy_territories", lang)],
            horizontal=True,
            key=f"real_{ind['indicator_id']}_scope",
        )
        if scope == text("main_territories", lang):
            df = df[df["territory"].isin(territories)]
        else:
            is_lombardy_area = df["territory_level"].isin(["province", "large_municipality"])
            is_selected_reference = df["territory"].isin(territories)
            df = df[is_lombardy_area | is_selected_reference]
        return df

    if "entry_age" in df.columns and df["entry_age"].nunique() > 1:
        entry_ages = sorted(df["entry_age"].dropna().astype(str).unique().tolist(), key=lambda value: int(value))
        entry_age = st.radio(text("entry_age", lang), entry_ages, horizontal=True, key=f"real_{ind['indicator_id']}_entry_age")
        df = df[df["entry_age"].astype(str) == entry_age]

    if ind["chart"] not in {"age_structure", "generation_projection"}:
        default_age = "15-34"
        if ind["indicator_id"] in {"youth_migration_balance", "youth_inflow_outflow"}:
            default_age = "18-39"
        df = filter_by_select(df, "age_group", "age_group", lang, f"real_{ind['indicator_id']}_age_group", preferred=default_age)

    df = filter_by_select(df, "citizenship", "citizenship", lang, f"real_{ind['indicator_id']}_citizenship", preferred="Total")
    df = filter_by_select(df, "movement_category", "movement_category", lang, f"real_{ind['indicator_id']}_movement", preferred="Tutte le voci")
    return apply_standard_territory_filter(df, territories)


def chart_tooltip(df):
    preferred = [
        "year",
        "academic_year",
        "territory",
        "university_area",
        "domain_it",
        "indicator_it",
        "sex",
        "age_group",
        "citizenship",
        "movement_category",
        "flow_direction",
        "entry_age",
        "scenario",
        "value",
        "unit",
        "difference_from_italy",
        "polarity",
        "source",
        "pdf_page",
    ]
    return [col for col in preferred if col in df.columns]


def chart_panel_field(df):
    if "territory" in df.columns:
        return "territory"
    if "university_area" in df.columns:
        return "university_area"
    return None


def ordered_panels(df, panel_field):
    preferred = {
        "Bergamo": 0,
        "Lombardia": 1,
        "Altro Lombardia": 1,
        "Italia": 2,
        "Altro Italia": 2,
    }
    panels = df[panel_field].dropna().astype(str).unique().tolist()
    return sorted(panels, key=lambda value: (preferred.get(value, 10), value))


def panel_color(panel_name):
    return {
        "Bergamo": "#2AA8A1",
        "Lombardia": "#0B78B7",
        "Altro Lombardia": "#0B78B7",
        "Italia": "#082B59",
        "Altro Italia": "#082B59",
    }.get(panel_name, "#0B78B7")


def common_value_domain(df, symmetric=False):
    values = pd.to_numeric(df["value"], errors="coerce").dropna()
    if values.empty:
        return None
    if symmetric:
        limit = float(values.abs().max())
        limit = limit * 1.08 if limit else 1.0
        return [-limit, limit]
    upper = float(values.max())
    lower = float(values.min())
    if lower >= 0:
        return [0, upper * 1.08 if upper else 1.0]
    padding = (upper - lower) * 0.08
    return [lower - padding, upper + padding]


def panel_chart(panel_df, ind, lang, panel_name, value_domain):
    y_title = indicator_unit(ind, lang)
    tooltip = chart_tooltip(panel_df)
    color = panel_color(panel_name)
    y_scale = alt.Scale(domain=value_domain) if value_domain else alt.Scale()

    if ind["chart"] == "age_structure":
        return alt.Chart(panel_df).mark_bar(color=color).encode(
            x=alt.X("age_group:N", title=text("age_group", lang), sort=sort_age_groups(panel_df["age_group"].unique())),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            tooltip=tooltip,
        )

    if ind["chart"] == "migration_flows":
        return alt.Chart(panel_df).mark_line(point=True, strokeWidth=2.5).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            color=alt.Color(
                "flow_direction:N",
                title=text("flow_direction", lang),
                scale=alt.Scale(range=["#2AA8A1", "#E67E5F"]),
            ),
            tooltip=tooltip,
        )

    if ind["chart"] in {"migration_balance", "working_age_balance"}:
        line = alt.Chart(panel_df).mark_line(point=True, color=color, strokeWidth=2.5).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            tooltip=tooltip,
        )
        zero = alt.Chart(pd.DataFrame({"value": [0]})).mark_rule(
            color="#6B7280",
            opacity=0.65,
        ).encode(y=alt.Y("value:Q", scale=y_scale))
        return line + zero

    if ind["chart"] == "university_enrolments":
        return alt.Chart(panel_df).mark_line(point=True, color=color, strokeWidth=2.5).encode(
            x=alt.X(
                "academic_year:N",
                title=text("academic_year", lang),
                sort=sorted(panel_df["academic_year"].unique()),
            ),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            tooltip=tooltip,
        )

    if ind["chart"] == "bes_best_indicator":
        unit = panel_df["unit"].dropna().iloc[0] if "unit" in panel_df.columns and not panel_df["unit"].dropna().empty else y_title
        return alt.Chart(panel_df).mark_bar(color=color, size=46).encode(
            x=alt.X("value:Q", title=unit, scale=y_scale),
            y=alt.Y(f"{chart_panel_field(panel_df)}:N", title=None, axis=None),
            tooltip=tooltip,
        )

    if ind["chart"] == "generation_projection":
        return alt.Chart(panel_df).mark_line(point=True, strokeWidth=2.5).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            color=alt.Color(
                "age_group:N",
                title=text("age_group", lang),
                sort=["15-29", "55-64"],
                scale=alt.Scale(domain=["15-29", "55-64"], range=["#2AA8A1", "#082B59"]),
            ),
            tooltip=tooltip,
        )

    if "year" in panel_df.columns and panel_df["year"].nunique() > 1:
        return alt.Chart(panel_df).mark_line(point=True, color=color, strokeWidth=2.5).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            tooltip=tooltip,
        )

    if "age_group" in panel_df.columns and panel_df["age_group"].replace("", pd.NA).dropna().nunique() > 1:
        return alt.Chart(panel_df).mark_bar(color=color).encode(
            x=alt.X("age_group:N", title=text("age_group", lang), sort=sort_age_groups(panel_df["age_group"].unique())),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            tooltip=tooltip,
        )

    return alt.Chart(panel_df).mark_bar(color=color, size=48).encode(
        x=alt.X("value:Q", title=y_title, scale=y_scale),
        y=alt.Y(f"{chart_panel_field(panel_df)}:N", title=None, axis=None),
        tooltip=tooltip,
    )


SINGLE_COMPARISON_INDICATORS = {
    "youth_population_change",
    "youth_elderly_ratio",
    "youth_unemployment_rate",
    "youth_inactivity_rate",
    "bes_best_indicator",
}


def should_use_single_comparison_chart(ind):
    return ind["indicator_id"] in SINGLE_COMPARISON_INDICATORS


def comparison_color(panel_field, panels):
    return alt.Color(
        f"{panel_field}:N",
        title=None,
        scale=alt.Scale(
            domain=panels,
            range=[panel_color(panel) for panel in panels],
        ),
    )


def single_comparison_chart(df, ind, lang, panel_field):
    y_title = indicator_unit(ind, lang)
    tooltip = chart_tooltip(df)
    panels = ordered_panels(df, panel_field)
    color = comparison_color(panel_field, panels)
    value_domain = common_value_domain(df)
    y_scale = alt.Scale(domain=value_domain) if value_domain else alt.Scale()

    if ind["chart"] == "bes_best_indicator":
        unit = df["unit"].dropna().iloc[0] if "unit" in df.columns and not df["unit"].dropna().empty else y_title
        if "year" in df.columns and df["year"].nunique() > 1:
            return alt.Chart(df).mark_line(point=True, strokeWidth=2.5).encode(
                x=alt.X("year:O", title=text("year", lang)),
                y=alt.Y("value:Q", title=unit, scale=y_scale),
                color=color,
                tooltip=tooltip,
            )
        return alt.Chart(df).mark_bar(size=52).encode(
            x=alt.X(f"{panel_field}:N", title=None, sort=panels),
            y=alt.Y("value:Q", title=unit, scale=y_scale),
            color=color,
            tooltip=tooltip,
        )

    if "year" in df.columns and df["year"].nunique() > 1:
        return alt.Chart(df).mark_line(point=True, strokeWidth=2.5).encode(
            x=alt.X("year:O", title=text("year", lang)),
            y=alt.Y("value:Q", title=y_title, scale=y_scale),
            color=color,
            tooltip=tooltip,
        )

    return alt.Chart(df).mark_bar(size=52).encode(
        x=alt.X(f"{panel_field}:N", title=None, sort=panels),
        y=alt.Y("value:Q", title=y_title, scale=y_scale),
        color=color,
        tooltip=tooltip,
    )


def render_chart(df, ind, lang):
    panel_field = chart_panel_field(df)
    if panel_field is None:
        return

    if should_use_single_comparison_chart(ind):
        chart = single_comparison_chart(df, ind, lang, panel_field)
        st.altair_chart(chart.properties(height=360), width="stretch")
        return

    panels = ordered_panels(df, panel_field)
    symmetric = ind["chart"] in {"migration_balance", "working_age_balance"}

    for start in range(0, len(panels), 3):
        row_panels = panels[start:start + 3]
        columns = st.columns(len(row_panels))
        for column, panel_name in zip(columns, row_panels):
            panel_df = df[df[panel_field].astype(str) == panel_name].copy()
            value_domain = common_value_domain(panel_df, symmetric=symmetric)
            chart = panel_chart(panel_df, ind, lang, panel_name, value_domain)
            with column:
                st.altair_chart(
                    chart.properties(height=310, title=panel_name),
                    width="stretch",
                )


def rows_for_indicator(ind, population_df, projection_df, unemployment_df, inactivity_df, migration_df, university_df, bes_df):
    indicator_id = ind["indicator_id"]
    if indicator_id in {"youth_share", "entry_cohorts", "youth_population_change", "youth_elderly_ratio"}:
        return population_current_rows(population_df, ind)
    if indicator_id in {
        "working_age_entry_projection",
        "working_age_stock_change_projection",
        "young_older_workers_projection",
    }:
        return population_projection_rows(projection_df, ind)
    if indicator_id == "youth_unemployment_rate":
        return rate_rows(unemployment_df, ind, "youth_unemployment_rate", "unemployment_rate")
    if indicator_id == "youth_inactivity_rate":
        return rate_rows(inactivity_df, ind, "youth_inactivity_rate", "inactivity_rate")
    if indicator_id in {"youth_migration_balance", "youth_inflow_outflow"}:
        return migration_rows(migration_df, ind)
    if indicator_id == "university_first_year_enrolments":
        return university_rows(university_df, ind)
    if indicator_id == "bes_best_indicator":
        return bes_best_rows(bes_df, ind)
    return pd.DataFrame()


def render_indicator(ind, population_df, projection_df, unemployment_df, inactivity_df, migration_df, university_df, bes_df, lang, territories):
    st.markdown(f"### {indicator_name(ind, lang)}")
    st.write(indicator_description(ind, lang))
    st.markdown(f"**{text('source', lang)}:** {ind['source']}")

    df = rows_for_indicator(ind, population_df, projection_df, unemployment_df, inactivity_df, migration_df, university_df, bes_df)
    if df.empty:
        st.warning(text("missing_data", lang))
        return

    with st.container(border=False):
        df = filter_real_data(df, ind, lang, territories)
    if df.empty:
        st.warning(text("no_filtered_data", lang))
        return
    display_df = localize_display_values(df, lang)
    render_chart(display_df, ind, lang)
    with st.expander(text("displayed_rows", lang)):
        st.dataframe(display_df.sort_values([col for col in ["year", "territory", "sex", "age_group"] if col in display_df.columns]), width="stretch", hide_index=True)


def render_schema_page(states, missing_columns, lang):
    st.subheader(text("overview", lang))
    st.write(text("schema_intro", lang))
    st.info(text("data_quality_text", lang))

    all_ok = all(state == "ok" for state in states.values())
    if all_ok:
        st.success(text("real_data", lang))
    else:
        bad = [name for name, state in states.items() if state != "ok"]
        st.warning(f"{text('missing_data', lang)} {'; '.join(bad)}")

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
            file_name=f"heye_available_indicators_17june_{lang}.csv",
            mime="text/csv",
        )

    with tabs[1]:
        st.dataframe(datasets_df, width="stretch", hide_index=True)
        st.download_button(
            text("download_inputs", lang),
            datasets_df.to_csv(index=False).encode("utf-8"),
            file_name=f"heye_input_datasets_17june_{lang}.csv",
            mime="text/csv",
        )

    with tabs[2]:
        st.dataframe(dataset_files_df(states, missing_columns, lang), width="stretch", hide_index=True)
        st.markdown(f"**{text('required_columns', lang)} `population_current.csv`:** `{', '.join(POPULATION_CURRENT_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `population_projections.csv`:** `{', '.join(POPULATION_PROJECTIONS_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `labour_market_youth.csv`:** `{', '.join(UNEMPLOYMENT_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `inactivity_youth.csv`:** `{', '.join(INACTIVITY_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `migration_youth.csv`:** `{', '.join(MIGRATION_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `university_pipeline.csv`:** `{', '.join(UNIVERSITY_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `bes_best_indicators.csv`:** `{', '.join(BES_BEST_COLUMNS)}`")


def render_data_methods_page(states, missing_columns, lang):
    st.subheader(section_label("data_methods", lang))

    tabs = st.tabs([text("indicator_catalog", lang), text("input_datasets", lang), text("csv_contract", lang)])
    indicators_df = indicator_catalog_df(lang)
    datasets_df = input_datasets_df(lang)

    with tabs[0]:
        st.dataframe(indicators_df, width="stretch", hide_index=True)
        st.download_button(
            text("download_indicators", lang),
            indicators_df.to_csv(index=False).encode("utf-8"),
            file_name=f"heye_available_indicators_17june_{lang}.csv",
            mime="text/csv",
        )

    with tabs[1]:
        st.dataframe(datasets_df, width="stretch", hide_index=True)
        st.download_button(
            text("download_inputs", lang),
            datasets_df.to_csv(index=False).encode("utf-8"),
            file_name=f"heye_input_datasets_17june_{lang}.csv",
            mime="text/csv",
        )

    with tabs[2]:
        st.dataframe(dataset_files_df(states, missing_columns, lang), width="stretch", hide_index=True)
        st.markdown(f"**{text('required_columns', lang)} `population_current.csv`:** `{', '.join(POPULATION_CURRENT_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `population_projections.csv`:** `{', '.join(POPULATION_PROJECTIONS_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `labour_market_youth.csv`:** `{', '.join(UNEMPLOYMENT_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `inactivity_youth.csv`:** `{', '.join(INACTIVITY_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `migration_youth.csv`:** `{', '.join(MIGRATION_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `university_pipeline.csv`:** `{', '.join(UNIVERSITY_COLUMNS)}`")
        st.markdown(f"**{text('required_columns', lang)} `bes_best_indicators.csv`:** `{', '.join(BES_BEST_COLUMNS)}`")


def render_welcome_page(lang):
    left_margin, heye_column, deep_column, right_margin = st.columns([0.5, 1.4, 1.4, 0.5])
    with heye_column:
        if HEYE_LOGO_FILE.exists():
            st.image(str(HEYE_LOGO_FILE), width="stretch")
    with deep_column:
        if LOGO_FILE.exists():
            st.image(str(LOGO_FILE), width="stretch")

    area_ids = [section_id for section_id in SECTIONS_ORDER if section_id != "welcome"]
    area_labels = [section_label(section_id, lang) for section_id in area_ids]
    area_items = "".join(f"<li>{label}</li>" for label in area_labels)

    st.markdown(
        f"""
        <div style="max-width:980px; margin:1.2rem auto 0 auto;">
          <h1 style="color:#082B59; margin-bottom:0.55rem;">{text("welcome_title", lang)}</h1>
          <p style="font-size:1.22rem; color:#334155; line-height:1.55; margin-bottom:0.8rem;">
            {text("welcome_text", lang)}
          </p>
          <p style="font-size:1.16rem; color:#334155; line-height:1.5; margin-bottom:1rem;">
            {text("welcome_focus", lang)}
          </p>
          <div style="background:#EEF7F7; border-left:5px solid #2FA5A7; padding:1rem 1.2rem; margin:1.1rem 0; border-radius:8px;">
            <p style="font-size:1.1rem; font-weight:700; color:#082B59; margin:0 0 0.45rem 0;">
              {text("welcome_areas_intro", lang).format(count=len(area_labels))}
            </p>
            <ul style="columns:2; column-gap:2.5rem; font-size:1.05rem; color:#1F2A36; line-height:1.75; margin:0.2rem 0 0 1.2rem; padding:0;">
              {area_items}
            </ul>
          </div>
          <p style="font-size:1.12rem; font-weight:700; color:#0B78B7; line-height:1.45; margin-top:1rem;">
            {text("welcome_comparison", lang)}
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------
# App layout
# ----------------------------
population_df, population_state, population_missing = load_csv(
    DATASETS["population_current"],
    POPULATION_CURRENT_COLUMNS,
    numeric_columns=["population"],
    int_columns=["year", "age"],
)
projection_df, projection_state, projection_missing = load_csv(
    DATASETS["population_projections"],
    POPULATION_PROJECTIONS_COLUMNS,
    numeric_columns=["population_projected"],
    int_columns=["year", "age"],
)
unemployment_df, unemployment_state, unemployment_missing = load_csv(
    DATASETS["unemployment_youth"],
    UNEMPLOYMENT_COLUMNS,
    numeric_columns=["unemployment_rate"],
    int_columns=["year"],
)
inactivity_df, inactivity_state, inactivity_missing = load_csv(
    DATASETS["inactivity_youth"],
    INACTIVITY_COLUMNS,
    numeric_columns=["inactivity_rate"],
    int_columns=["year"],
)
migration_df, migration_state, migration_missing = load_csv(
    DATASETS["migration_youth"],
    MIGRATION_COLUMNS,
    numeric_columns=["value"],
    int_columns=["year"],
)
university_df, university_state, university_missing = load_csv(
    DATASETS["university_pipeline"],
    UNIVERSITY_COLUMNS,
    numeric_columns=["first_year_enrolments"],
    int_columns=["academic_year_start", "academic_year_end"],
)
bes_df, bes_state, bes_missing = load_csv(
    DATASETS["bes_best"],
    BES_BEST_COLUMNS,
    numeric_columns=["value"],
    int_columns=["year", "pdf_page"],
)

states = {
    "population_current": population_state,
    "population_projections": projection_state,
    "unemployment_youth": unemployment_state,
    "inactivity_youth": inactivity_state,
    "migration_youth": migration_state,
    "university_pipeline": university_state,
    "bes_best": bes_state,
}
missing_columns = {
    "population_current": population_missing,
    "population_projections": projection_missing,
    "unemployment_youth": unemployment_missing,
    "inactivity_youth": inactivity_missing,
    "migration_youth": migration_missing,
    "university_pipeline": university_missing,
    "bes_best": bes_missing,
}

with st.sidebar:
    if LOGO_FILE.exists():
        st.image(str(LOGO_FILE), width="stretch")

    language_label = st.radio("Lingua / Language", ["Italiano", "English"], horizontal=True)
    lang = "it" if language_label == "Italiano" else "en"

    st.header(text("menu", lang))
    page = st.radio(
        text("go_to", lang),
        SECTIONS_ORDER,
        format_func=lambda section_id: section_label(section_id, lang),
    )
    st.markdown("---")
    st.markdown(f"**{text('comparison', lang)}**")
    show_lombardy = st.checkbox(text("show_lombardy", lang), value=True)
    show_italy = st.checkbox(text("show_italy", lang), value=True)
    comparison_territories = selected_territories(show_lombardy, show_italy)

if page == "welcome":
    render_welcome_page(lang)
else:
    st.title(text("title", lang))
    st.caption(text("subtitle", lang))

if page == "welcome":
    pass
elif page == "data_methods":
    render_data_methods_page(states, missing_columns, lang)
else:
    st.subheader(section_label(page, lang))
    section_indicators = [ind for ind in INDICATORS if ind["section_id"] == page]
    for indicator in section_indicators:
        with st.container(border=True):
            render_indicator(indicator, population_df, projection_df, unemployment_df, inactivity_df, migration_df, university_df, bes_df, lang, comparison_territories)
