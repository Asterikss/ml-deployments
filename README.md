# Data Cleaning Script

This GitHub Actions workflow automates the process of data cleaning using a script that retrieves data from a Google Sheet, cleans it, and generates a report. The script performs the following operations:

1. **Data Retrieval**: Fetches data from a Google Sheet.
2. **Data Cleaning**: Removes rows with excessive missing data and fills missing values in key columns.
3. **Data Standardization**: Standardizes numeric columns like age and average income.
4. **Report Generation**: Produces a report detailing the data cleaning process.

### Workflow Steps
1. **Checkout repository**: Pulls the main repository.
2. **Set up Python**: Installs Python 3.x.
3. **Checkout foreign repository**: Pulls a second repository with required dependencies.
4. **Install foreign dependencies**: Installs dependencies from the external repository.
5. **Generate Data**: Runs a script to generate data.
6. **Install dependencies**: Installs dependencies for the main project.
7. **Download and clean data**: Downloads the Google Sheet data and runs the cleaning script.
8. **Display report**: Outputs the cleaning report.

## Local Development

To run the script locally:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your Google Sheets credentials in `creds.json`.
3. Run the cleaning script:
   ```bash
   python main.py
   ```
4. View the report in `report.txt` after the script completes.

## Secrets

- `GH_TOKEN`: GitHub token for accessing private repositories.
- `SHEETS_CREDS`: Credentials for accessing Google Sheets.
