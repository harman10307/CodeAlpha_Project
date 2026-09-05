# TASK 2: STOCK PORTFOLIO TRACKER

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 175
}

# Store user's portfolio
portfolio = {}

print("=" * 50)
print("          STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "-> $", price)

print("\nEnter 'done' when you have finished adding stocks.")

# Take stock information from user
while True:

    stock = input("\nEnter stock name: ").upper()

    # Stop entering stocks
    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print("❌ Stock not available.")
        print("Please choose from the available stocks.")
        continue

    # Take quantity
    quantity = input("Enter quantity: ")

    # Check if quantity is a number
    if not quantity.isdigit():
        print("❌ Please enter a valid quantity.")
        continue

    quantity = int(quantity)

    # Store stock and quantity
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print("✅ Stock added successfully!")

# Calculate total investment
total_investment = 0

print("\n" + "=" * 50)
print("             YOUR PORTFOLIO")
print("=" * 50)

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Value: $", investment
    )

# Display total
print("=" * 50)
print("TOTAL INVESTMENT: $", total_investment)
print("=" * 50)


# Optional: Save portfolio to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 40 + "\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${investment}\n"
            )

        file.write("=" * 40 + "\n")
        file.write(f"TOTAL INVESTMENT: ${total_investment}\n")

    print("✅ Portfolio saved successfully in portfolio.txt")

else:
    print("Portfolio was not saved.")

print("\nThank you for using Stock Portfolio Tracker!")