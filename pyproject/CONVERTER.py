def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency.")
        return None
    else:
        converted_amount = amount * exchange_rates[from_currency] / exchange_rates[to_currency]
        return converted_amount

def display_exchange_rates(exchange_rates):
    print("\nCURRENT EXCHANGE RATES:")
    for currency, rate in exchange_rates.items():
        print(f"{currency}: {rate}")

def update_exchange_rate(exchange_rates):
    currency = input("Enter the currency code to update (e.g., USD): ").upper()
    if currency in exchange_rates:
        new_rate = float(input(f"Enter the new exchange rate for {currency}: "))
        exchange_rates[currency] = new_rate
        print(f"Exchange rate for {currency} updated successfully.")
    else:
        print("Currency not found.")

def main():
    exchange_rates = {
        "USD": 1.0,      # Base currency is USD
        "EUR": 0.93766,     # Example exchange rate for Euro
        "GBP": 0.78,     # Example exchange rate for British Pound
        "JPY": 154.72,   # Example exchange rate for Japanese Yen
        "INR": 83.431,    # Example exchange rate for Indian Rupee
        "CAD": 1.36,     # Example exchange rate for Canadian Dollar
        "AUD": 1.6302,     # Example exchange rate for Australian Dollar
        "CNY": 7.7787,     # Example exchange rate for Chinese Yuan
        "RUB": 98.6536,    # Example exchange rate for Russian Ruble
        "BRL": 5.47216,      # Example exchange rate for Brazilian Real
    }

    print("Welcome to the Currency Converter")

    while True:
        print("\nMENU:")
        print("1. Convert currency")
        print("2. Display current exchange rates")
        print("3. Update exchange rate")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Available currency codes:")
            for currency in exchange_rates:
                print(currency)
            from_currency = input("Enter the currency you want to convert from: ").upper()
            to_currency = input("Enter the currency you want to convert to: ").upper()
            amount = float(input("Enter the amount you want to convert: "))
            converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
            if converted_amount is not None:
                print(f"{amount} {from_currency} equals {converted_amount:.2f} {to_currency}")
        elif choice == '2':
            display_exchange_rates(exchange_rates)
        elif choice == '3':
            update_exchange_rate(exchange_rates)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
