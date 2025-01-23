import time
import pandas as pd
import re
import random
import sys
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start_time = time.time()  # Start timer

# Setup Selenium WebDriver with headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no UI)
options.add_argument('--disable-gpu')  # Performance improvement
options.add_argument('--window-size=1920,1080')  # Ensure proper resolution in headless mode
options.add_argument('--disable-notifications')  # Disable notification request prompt
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

print("--- Yahoo Finance [Web Scraper] by aidilazmi22 ---")

while True:
    text = """
List of Markets:
1 = World Indices
2 = Futures
3 = Bonds
4 = Currencies
5 = Options
6 = Stocks
7 = Crypto
8 = ETFs
9 = Mutual Funds
"""
    print(text)

    market_types = {
        1: ["world-indices", "World Indices"],  # World Indices
        2: ["commodities", "Futures"],  # Futures
        3: ["bonds", "Bonds"],  # Bonds
        4: ["currencies", "Currencies"],  # Currencies
        5: ["options", "Options"],  # Options ------
        6: ["stocks", "Stocks"],  # Stocks ------
        7: ["crypto", "Crypto"],  # Crypto ------
        8: ["etfs", "ETFs"],  # ETFs ------
        9: ["mutualfunds", "Mutual Funds"]  # Mutual Funds ------
    }

    option = int(input("Please choose an option (1-9): ").strip())
    if not option:
        print("Input cannot be blank or just spaces. Please try again.\n")

    elif option in range (1, 5):  # (From 1 to 4)
        market = market_types[option][0]
        print(f"Market: [{option}] - {market_types[option][1]}")
        break

    elif option == 5:  # Options ------
        print(f"Market: {market_types[option][1]}")

        extension_text = """
Categories:
A = Most Active
B = Top Gainers
C = Top Losers
D = Highest Implied Volatility
E = Highest Open Interest
"""
        while True:
            print(extension_text)

            extension_types = {
                "A": ["/most-active", "Most Active"],
                "B": ["/gainers", "Top Gainers"],
                "C": ["/losers", "Top Losers"],
                "D": ["/highest-implied-volatility", "Highest Implied Volatility"],
                "E": ["/highest-open-interest", "Highest Open Interest"]
            }

            extension = input("Please select a category (A-E, a-e): ").strip().upper()
            if not extension:
                print("Input cannot be blank or just spaces. Please try again.\n")
            elif extension in extension_types:
                market = market_types[option][0] + extension_types[extension][0]
                break
            else:
                print("Invalid input. Only single character is accepted!\n")
        break

    elif option == 6:  # Stocks ------
        print(f"Market: {market_types[option][1]}")

        extension_text = """
Categories:
A = Most Active
B = Trending Now
C = Top Gainers
D = Top Losers
E = 52 Week Gainers
F = 52 Week Losers
"""
        while True:
            print(extension_text)

            extension_types = {
                "A": ["/most-active", "Most Active"],
                "B": ["/trending", "Trending Now"],
                "C": ["/gainers", "Top Gainers"],
                "D": ["/losers", "Top Losers"],
                "E": ["/52-week-gainers", "52 Week Gainers"],
                "F": ["/52-week-losers", "52 Week Losers"]
            }

            extension = input("Please select a category (A-F, a-f): ").strip().upper()
            if not extension:
                print("Input cannot be blank or just spaces. Please try again.\n")
            elif extension in extension_types:
                market = market_types[option][0] + extension_types[extension][0]
                break
            else:
                print("Invalid input. Only single character is accepted!\n")
        break

    elif option == 7:  # Crypto ------
        print(f"Market: {market_types[option][1]}")

        extension_text = """
Categories:
A = All
B = Most Active
C = Top Gainers
D = Top Losers
E = Trending Now
"""
        while True:
            print(extension_text)

            extension_types = {
                "A": ["/all", "All"],
                "B": ["/most-active", "Most Active"],
                "C": ["/gainers", "Top Gainers"],
                "D": ["/losers", "Top Losers"],
                "E": ["/trending", "Trending Now"]
            }
            extension = input("Please select a category (A-E, a-e): ").strip().upper()
            if not extension:
                print("Input cannot be blank or just spaces. Please try again.\n")
            elif extension in extension_types:
                market = market_types[option][0] + extension_types[extension][0]
                break
            else:
                print("Invalid input. Only single character is accepted!\n")
        break

    elif option == 8:  # ETFs ------
        print(f"Market: {market_types[option][1]}")

        extension_text = """
Categories:
A = Most Active
B = Top Gainers
C = Top Losers
D = Top Performing
E = Trending Now
F = Best Historical Performance
G = Top ETFs
"""
        while True:
            print(extension_text)

            extension_types = {
                "A": ["/most-active", "Most Active"],
                "B": ["/gainers", "Top Gainers"],
                "C": ["/losers", "Top Losers"],
                "D": ["/top-performing", "Top Performing"],
                "E": ["/trending", "Trending Now"],
                "F": ["/best-historical-performance", "Best Historical Performance"],
                "G": ["/top", "Top ETFs"]
            }
            extension = input("Please select a category (A-G, a-g): ").strip().upper()
            if not extension:
                print("Input cannot be blank or just spaces. Please try again.\n")
            elif extension in extension_types:
                market = market_types[option][0] + extension_types[extension][0]
                break
            else:
                print("Invalid input. Only single character is accepted!\n")
        break

    elif option == 9:  # Mutual Funds ------
        print(f"Market: {market_types[option][1]}")

        extension_text = """
Categories:
A = Top Gainers
B = Top Losers
C = Top Performing
D = Best Historical Performance
E = Top Mutual Funds
"""
        while True:
            print(extension_text)

            extension_types = {
                "A": ["/gainers", "Top Gainers"],
                "B": ["/losers", "Top Losers"],
                "C": ["/top-performing", "Top Performing"],
                "D": ["/best-historical-performance", "Best Historical Performance"],
                "E": ["/top", "Top Mutual Funds"],
            }
            extension = input("Please select a category (A-F, a-f): ").strip().upper()
            if not extension:
                print("Input cannot be blank or just spaces. Please try again.\n")
            elif extension in extension_types:
                market = market_types[option][0] + extension_types[extension][0]
                break
            else:
                print("Invalid input. Only single character is accepted!\n")
        break

    else:
        print("Invalid input. Only single digit number is accepted!\n")

# Open the Yahoo Finance website
url = f"https://finance.yahoo.com/markets/{market}/?start=0&count=100"
print(url)
driver.get(url)
print("\nInitializing...")
print("\n" + "Current URL: " + url + "\n")

# Wait for the table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'table.markets-table'))
)

def extract_header():
    try:
        column = driver.find_elements(By.CSS_SELECTOR, "tr > th")
        if option == 1:  # World Indices
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[3].text,  # Price | nth-child(4)
                column[4].text,  # Change | nth-child(5)
                column[5].text,  # Change % | nth-child(6)
                column[6].text,  # Volume | nth-child(7)
            ]
            # print(customized_column)
            return customized_column

        elif option == 2:  # Futures
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[3].text,  # Price | nth-child(4)
                column[4].text,  # Market Time | nth-child(5)
                column[5].text,  # Change | nth-child(6)
                column[6].text,  # Change % | nth-child(7)
                column[7].text,  # Volume | nth-child(8)
                column[8].text,  # Open Interest | nth-child(9)
            ]
            # print(customized_column)
            return customized_column

        elif option == 3:  # Bonds
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[3].text,  # Price | nth-child(4)
                column[4].text,  # Change | nth-child(5)
                column[5].text,  # Change % | nth-child(6)
            ]
            # print(customized_column)
            return customized_column

        elif option == 4:  # Currencies
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[3].text,  # Price | nth-child(4)
                column[4].text,  # Change | nth-child(5)
                column[5].text,  # Change % | nth-child(6)
            ]
            # print(customized_column)
            return customized_column

        elif option == 5:  # Options
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[2].text,  # Underlying Symbol | nth-child(3)
                column[3].text,  # Strike | nth-child(4)
                column[4].text,  # Expiration Data | nth-child(5)
                column[5].text,  # Price | nth-child(6)
                column[6].text,  # Change | nth-child(7)
                column[7].text,  # Change % | nth-child(8)
                column[8].text,  # Bid | nth-child(9)
                column[9].text,  # Ask | nth-child(10)
                column[10].text,  # Volume | nth-child(11)
                column[11].text,  # Open Interest | nth-child(12)
            ]
            # print(customized_column)
            return customized_column

        elif option == 6:  # Stocks
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[3].text,  # Price | nth-child(4)
                column[4].text,  # Change | nth-child(5)
                column[5].text,  # Change % | nth-child(6)
                column[6].text,  # Volume | nth-child(7)
                column[7].text,  # Avg Vol (3m) | nth-child(8)
                column[8].text,  # Market Cap | nth-child(9)
                column[9].text,  # P/E Ratio (TTM) | nth-child(10)
                column[10].text,  # 52 Wk Change % | nth-child(11)
            ]
            # print(customized_column)
            return customized_column

        elif option == 7:  # Crypto
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[3].text,  # Price | nth-child(4)
                column[4].text,  # Change | nth-child(5)
                column[5].text,  # Change % | nth-child(6)
                column[6].text,  # Market Cap | nth-child(7)
                column[7].text,  # Volume | nth-child(8)
                column[8].text,  # Volume In Currency (24hr) | nth-child(9)
                column[9].text,  # Total Volume All Currencies (24hr) | nth-child(10)
                column[10].text,  # Circulating Supply | nth-child(11)
                column[11].text,  # 52 Wk Change % | nth-child(12)
            ]
            # print(customized_column)
            return customized_column

        elif option == 8:  # ETFs
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[3].text,  # Price | nth-child(4)
                column[4].text,  # Change | nth-child(5)
                column[5].text,  # Change % | nth-child(6)
                column[6].text,  # Volume | nth-child(7)
                column[7].text,  # 50-Day Average | nth-child(8)
                column[8].text,  # 200-Day Average | nth-child(9)
                column[9].text,  # 3-Month Return | nth-child(10)
                column[10].text,  # YTD Return | nth-child(11)
                column[11].text,  # 52-Wk Change % | nth-child(12)
            ]
            # print(customized_column)
            return customized_column

        elif option == 9:  # Mutual Funds
            customized_column = [
                column[0].text,  # Symbol | nth-child(1)
                column[1].text,  # Name | nth-child(2)
                column[2].text,  # Price | nth-child(3)
                column[3].text,  # Change | nth-child(4)
                column[4].text,  # Change % | nth-child(5)
                column[5].text,  # Volume | nth-child(6)
                column[6].text,  # 50-Day Average | nth-child(7)
                column[7].text,  # 200-Day Average | nth-child(8)
                column[8].text,  # 3-Month Return | nth-child(9)
                column[9].text,  # YTD Return | nth-child(10)
                column[10].text,  # 52-Wk Change % | nth-child(11)
            ]
            # print(customized_column)
            return customized_column

    except Exception:
        print(f"Error while getting header values...")
        sys.exit()

# Extract the data
def extract_data():
    data_rows = []  # To store row data

    try:
        # Scrape data on the current page
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")

        if option == 1:  # World Indices
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketVolume"]').text,  # Volume
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 2:  # Futures
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'td:nth-child(5) > span').text,  # Market Time
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketVolume"]').text,  # Volume
                    row.find_element(By.CSS_SELECTOR, 'td:nth-child(9) > span').text,  # Open Interest
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 3:  # Bonds
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 4:  # Currencies
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 5:  # Options
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) > span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, ".loud-link.fin-size-medium.yf-1xqzjha").text,  # Underlying Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(4) > span").text,  # Strike
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(5) > span").text,  # Expiration Date
                    row.find_element(By.CSS_SELECTOR, '[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="bid"]').text,  # Bid
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="ask"]').text,  # Ask
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketVolume"]').text,  # Volume
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(12) > span").text,  # Open Interest
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 6:  # Stocks
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketVolume"]').text,  # Volume
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(8) span").text,  # Avg Vol (3M)
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="marketCap"]').text,  # Market Cap
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(10) span").text,  # P/E Ratio (TTM)
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(11) span").text,  # 52 Wk Change %
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 7:  # Crypto
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) > span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketVolume"]').text,  # Market Cap
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(8) span").text,  # Volume
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="marketCap"]').text,  # Volume In Currency (24hr)
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(10) span").text,  # Total Volume All Currencies (24hr)
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(11) span").text,  # Circulating Supply
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(12) span").text,  # 52 Wk Change %
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 8:  # ETFs
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketVolume"]').text,  # Volume
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(8) span").text,  # 50-Day Average
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(9) span").text,  # 200-Day Average
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(10) span").text,  # 3-Month Return
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="ytdReturn"] span').text,  # YTD Return
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(12) span").text,  # 52-Wk Change %
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

        elif option == 9:  # Mutual Funds
            for row in rows:
                customized_row_data = [
                    row.find_element(By.CSS_SELECTOR, ".name.yf-1m808gl.stacked").text,  # Symbol
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(2) span").text,  # Name
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text,  # Price
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChange"] span').text,  # Change
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketChangePercent"] span').text,  # Change %
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(6) span").text,  # 50-Day Average
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(7) span").text,  # 200-Day Average
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(8) span").text,  # 3-Month Return
                    row.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="ytdReturn"] span').text,  # YTD Return
                    row.find_element(By.CSS_SELECTOR, "td:nth-child(10) span").text,  # 52-Wk Change %
                ]
                data_rows.append(customized_row_data)
                print(customized_row_data)
            return data_rows

    except Exception:
        print("Data extraction error! Please check the URL.")
        sys.exit()

    print()  # For neatness during program execution

all_data = []

# Pagination
try:
    pagination_element = driver.find_element(By.CSS_SELECTOR, "div.total").text
    raw_result = int(pagination_element.split(' ')[2])
    total_result = round(raw_result, -2)
    print(f"Total result: {raw_result}")

    for row in range(100, total_result + 100, 100):
        print(f"Scraping page {row // 100 if row != 0 else 1} of {total_result // 100}...\n")

        # Extract data from current page
        print(extract_header())
        all_data.extend(extract_data())

        # If not on the last page, go to the next page
        if row < total_result:
            try:
                # Construct the URL for the next page
                next_page_url = f"https://finance.yahoo.com/markets/{market}/?start={row}&count=100"
                print("\nCurrent URL: " + next_page_url)
                driver.get(next_page_url)
                driver.refresh()

                # Wait for the new page to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'table.markets-table'))
                )
            except Exception:
                print(f"Error in page {row + 1}. Possible end of search result.\n")
                break
            except:
                print("\nNext page button not found or is disabled.\n")
                break
        else:
            continue
except Exception:
    # Extract data from current page
    print(extract_header())
    all_data.extend(extract_data())
    print("\nInfo: Pagination element is not found. Only 1 page can be scraped.")


finally:
    current_date = date.today()  # Get the current date
    serial_number = random.randint(100000, 999999)  # Add random number to file name
    markettype = re.sub(r'\s', '+', market_types[option][1])
    filename = f"YF_{markettype}_{serial_number}_{current_date}"

    header = extract_header()

    # Save data to an Excel file using pandas
    df = pd.DataFrame(all_data)
    df.to_excel(f"{filename}.xlsx", index=False, header=header, engine='openpyxl')

    print(f"\nData has been extracted, and saved to '{filename}.xlsx'\n")

    end_time = time.time()  # End timer
    elapsed_time = end_time - start_time
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")  # Print elapsed time

    # Close the browser
    driver.quit()
###########################################################################
