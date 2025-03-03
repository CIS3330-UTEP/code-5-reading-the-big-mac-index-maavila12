import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df= pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]
    df= df[df['iso_a3'].str.lower() == country_code.lower()]
    if df.empty:
        return None
    return round(df['dollar_price'].mean(),2)


def get_big_mac_price_by_country(country_code):
    df= pd.read_csv(big_mac_file)
    df = df[df['iso_a3'].str.lower() == country_code.lower()]
    if df.empty:
        return None
    return round(df['dollar_price'].mean(), 2)


def get_the_cheapest_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]
    if df.empty:
        return None
    cheapest = df.nsmallest(1, 'dollar_price').iloc[0]
    return f"{cheapest['name']}({cheapest['iso_a3'].upper()}): ${round(cheapest['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]
    if df.empty:
        return None
    most_expensive = df.nlargest(1, 'dollar_price').iloc[0]
    return f"{most_expensive['name']}({most_expensive['iso_a3'].upper()}): ${round(most_expensive['dollar_price'], 2)}"


if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Get Big Mac price by year and country")
        print("2. Get average Big Mac price by country")
        print("3. Get the cheapest Big Mac price by year")
        print("4. Get the most expensive Big Mac price by year")
        print("5. Exit")
       
        choice = input("Enter choice (1-5): ")
       
        if choice == "1":
            year = input("Enter year: ")
            country_code = input("Enter country code: ")
            result = get_big_mac_price_by_year(year, country_code)
            print(f"Average price: ${result}" if result is not None else "No data available.")
       
        elif choice == "2":
            country_code = input("Enter country code: ")
            result = get_big_mac_price_by_country(country_code)
            print(f"Average price: ${result}" if result is not None else "No data available.")
       
        elif choice == "3":
            year = input("Enter year: ")
            print(get_the_cheapest_big_mac_price_by_year(year))
       
        elif choice == "4":
            year = input("Enter year: ")
            print(get_the_most_expensive_big_mac_price_by_year(year))
       
        elif choice == "5":
            print("Exiting program.")
            break
       
        else:
            print("Invalid choice. Please select again.")

