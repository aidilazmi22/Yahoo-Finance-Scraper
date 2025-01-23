# Yahoo Finance Scraper

This repository contains a Python-based web scraper that extracts data from the Yahoo Finance website. It supports scraping data from multiple financial markets, such as World Indices, Futures, Bonds, Currencies, Stocks, Crypto, ETFs, and Mutual Funds. The extracted data is saved in an Excel file for further analysis.

## Features
- Scrapes financial data from Yahoo Finance across various markets.
- Supports different categories (e.g., Most Active, Top Gainers, Top Losers) for specific markets.
- Saves the extracted data into a timestamped Excel file with a random identifier.
- Customizable options for market and category selection.

## Prerequisites
Before running the scraper, ensure you have the following installed on your system:
- Python 3.8 or above
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/aidilazmi22/yahoo-finance-scraper.git
    cd yahoo-finance-scraper
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```
    python yf_scraper.py
    ```

2. Follow the on-screen instructions to select a market and category. For example:
    - Select a market (e.g., World Indices, Stocks, Crypto).
    - Choose a category (e.g., Most Active, Top Gainers, Top Losers).
      
3. Wait for the data scraping process to finish.

4. The script will scrape data and save it as an Excel file in the current directory. The file name will follow the format:
    ```
    YF_<Market_Type>_<Random_Number>_<Date>.xlsx
    ```

### Example Output
When you select "World Indices" and "Most Active," the script will output an Excel file containing:

| Symbol | Name           | Price | Change | Change % | Volume |
|--------|----------------|-------|--------|----------|--------|
| ...    | ...            | ...   | ...    | ...      | ...    |


## Requirements
The Python packages used in this project are listed in `requirements.txt`:

- pandas
- selenium
- openpyxl

Install them using:
    ```
    pip install -r requirements.txt
    ```

## Contribute
Contributions are welcome! If you'd like to contribute to this project, please:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## Disclaimer
This project is intended for educational and personal use only. Please note the following:

- Terms of Use: Ensure compliance with Yahoo Finance's terms of service and scraping policies.
- Rate Limits: Avoid sending excessive requests that may cause server overload.
- Data Accuracy: The extracted data may not always be accurate or up-to-date.
- Legal Liability: The author of this script assumes no liability for any misuse or damage resulting from its use.
- Personal Responsibility: It is your responsibility to use this tool ethically and lawfully.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
