import pandas as pd
from sklearn.preprocessing import StandardScaler
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging


def get_sheet_data(sheet_name, credentials_file):
    logging.info("Rozpoczęcie odczytywania danych z Google Sheets.")

    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, "https://www.googleapis.com/auth/drive")
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).get_worksheet(0)
    data = sheet.get_all_values()

    df = pd.DataFrame(data[1:], columns=data[0])

    df = df.replace("", pd.NA)

    df["Wiek"] = pd.to_numeric(df["Wiek"], errors="coerce")
    df["Średnie Zarobki"] = pd.to_numeric(df["Średnie Zarobki"], errors="coerce")

    logging.info("Dane zostały pomyślnie odczytane z Google Sheets.")

    return df


def clean_data(df):
    logging.info("Rozpoczęcie czyszczenia danych.")

    init_n_rows = len(df)

    df_clean = df.dropna(thresh=5)

    n_removed_rows = init_n_rows - len(df_clean)

    n_modified_rows = 0

    n_modified_rows += df_clean["Wiek"].isna().sum()
    df_clean.loc[df_clean["Wiek"].isna(), "Wiek"] = df_clean["Wiek"].median()

    n_modified_rows += df_clean["Średnie Zarobki"].isna().sum()
    df_clean.loc[df_clean["Średnie Zarobki"].isna(), "Średnie Zarobki"] = df_clean["Średnie Zarobki"].mean()

    n_modified_rows += df_clean["Czas Początkowy Podróży"].isna().sum()
    df_clean.loc[df_clean["Czas Początkowy Podróży"].isna(), "Czas Początkowy Podróży"] = "00:00"
    n_modified_rows += df_clean["Czas Końcowy Podróży"].isna().sum()
    df_clean.loc[df_clean["Czas Końcowy Podróży"].isna(), "Czas Końcowy Podróży"] = "00:00"

    logging.info(f"Liczba usuniętych wierszy: {n_removed_rows}")
    logging.info(f"Liczba zmodyfikowanych wartości: {n_modified_rows}")

    return df_clean, n_removed_rows, n_modified_rows


def standardize_data(df):
    logging.info("Rozpoczęcie standaryzacji danych.")

    scaler = StandardScaler()

    df.loc[:, ["Wiek", "Średnie Zarobki"]] = scaler.fit_transform(df[["Wiek", "Średnie Zarobki"]])

    logging.info("Standaryzacja danych zakończona.")

    return df


def main():
    logging.info("Rozpoczęcie przetwarzania danych.")

    df = get_sheet_data("data_student_25279", "creds.json")

    df_clean, n_removed_rows, n_modified_rows = clean_data(df)

    df_standardized = standardize_data(df_clean)

    report = f"Raport:\n"
    report += f"Liczba usuniętych wierszy: {n_removed_rows}\n"
    report += f"Liczba zmodyfikowanych wartości: {n_modified_rows}\n"
    report += f"Początkowa liczba wierszy: {len(df_standardized) + n_removed_rows}\n"
    report += f"Początkowa liczba po obróbce: {len(df_standardized)}\n"

    print(report)

    with open("report.txt", "w") as f:
        f.write(report)
        print("Raport został zapisany jako report.txt")

    logging.info("Proces przetwarzania danych zakończony.")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("log.txt"),
            logging.StreamHandler()
        ]
    )

    main()
