# Stock Portfolio Tracker

def stock_portfolio_tracker():
    # Step 1: Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,   # Apple
        "TSLA": 250,   # Tesla
        "GOOG": 2700,  # Google
        "MSFT": 320,   # Microsoft
        "AMZN": 140    # Amazon
    }

    portfolio = {}   # To store user input (stock: quantity)
    total_investment = 0

    print("📊 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    # Step 2: Take user input
    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("⚠️ Stock not available. Try again.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        # Add to portfolio
        portfolio[stock] = portfolio.get(stock, 0) + qty

    # Step 3: Calculate investment
    print("\n🧾 Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_investment += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

    print(f"\n💰 Total Investment Value = ${total_investment}")

    # Step 4: Save to file
    choice = input("\nDo you want to save results to a file? (yes/no): ").lower()
    if choice == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
            f.write(f"\nTotal Investment = ${total_investment}\n")
        print("✅ Portfolio saved to 'portfolio.txt'")

# Run the tracker
stock_portfolio_tracker()
