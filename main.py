import requests

def convert_currency(amount, from_curr, to_curr):
    url = f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}"

    response = requests.get(url).json()

    if response.get("result") is None:
        raise ValueError("Currency not supported")

    return response["result"]

def main():
    print("=== Currency Converter ===")
    amount = float(input("Amount: "))
    from_curr = input("From (e.g. USD): ").upper()
    to_curr = input("To (e.g. EUR): ").upper()

    try:
        result = convert_currency(amount, from_curr, to_curr)
        print(f"\n{amount} {from_curr} = {result} {to_curr}")
    except Exception as e:
        print("\nError:", e)

if __name__ == "__main__":
    main()
