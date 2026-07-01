"""Goal: Build a simple stock tracker that calculates total investment based on manually defined stock
prices.
● Simplified Scope:
○ User inputs stock names and quantity.
○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
○ Display total investment value and optionally save the result in a .txt or .csv file.
● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling
(optional)
"""
stock_price={"AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400}
total_investment=0
report=""
n=int(input("How many different stocks do you want to enter? : "))
for i in range(n):
    stock=input("Enter the  key: ").upper()
    price=int(input("Enter the values: "))
    stock_price[stock]=price
print(stock_price)
if stock in stock_price:
    # print("Stock exist")
    quantity=int(input("Enter the quantity: "))
    price=stock_price[stock]
    investment=price*quantity
    total_investment+=investment
     # Display stock details
    print("\nStock:", stock)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Investment:", investment)
    print("Total Investment:", total_investment)
    report += (
            f"Stock: {stock}\n"
            f"Price: {price}\n"
            f"Quantity: {quantity}\n"
            f"Investment: {investment}\n\n"
        )
    
else:
    print("Stock not found.")
print("\nTotal Investment =", total_investment)
choice = input("\nDo you want to save the report? (yes/no): ").lower()

if choice == "yes":
    file = open("Investment.txt", "w")

    file.write(report)

    file.close()

    print("Report saved successfully in investment.txt")

else:
    print("Program Ended.")

