# Supermarket Sales Summary Script

sales_records = [
    ["Apples", "Produce", 1.50, 200],
    ["Milk", "Dairy", 2.49, 120],
    ["Bread", "Bakery", 2.10, 95],
    ["Chicken", "Meat", 6.50, 60],
    ["Eggs", "Dairy", 3.20, 110],
    ["Bananas", "Produce", 0.99, 250]
]

def analyze_sales(records):
    print("=== SUPERMARKET SALES REPORT ===")
    print(f"Total Unique Items: {len(records)}")
    
    total_revenue = 0
    item_sales = []

    for item, category, price, quantity in records:
        revenue = price * quantity
        total_revenue += revenue
        item_sales.append((item, revenue))
        print(f"- {item} ({category}): Sold {quantity} units | Revenue: ${revenue:.2f}")

    print("-" * 35)
    print(f"Total Store Revenue: ${total_revenue:.2f}")
    
    top_item = max(item_sales, key=lambda x: x[1])
    print(f"Top Performing Item: {top_item[0]} (${top_item[1]:.2f})")

if __name__ == "__main__":
    analyze_sales(sales_records)