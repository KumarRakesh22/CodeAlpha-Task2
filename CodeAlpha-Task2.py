def stock_portfolio_tracker():
    # Predefined stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 135,
        "AMZN": 140,
        "INFY": 1500
    }

    portfolio = {}
    total_value = 0

    print("📈 Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("⚠ Invalid stock symbol. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

    print("\n🧾 Portfolio Summary:")
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            total_value += value
            line = f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{value}"
            print(line)
            file.write(line + "\n")

        print(f"\n💰 Total Investment Value: ₹{total_value}")
        file.write(f"\nTotal Investment Value: ₹{total_value}")

    print("📄 Summary saved to 'portfolio_summary.txt'")

stock_portfolio_tracker()