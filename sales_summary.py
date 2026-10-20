# Aldi Supermarket Sales Summary Script

sales_records = [
    ["Apples", "Produce", 1.50, 200],
    ["Milk", "Dairy", 2.49, 120],
    ["Bread", "Bakery", 2.10, 95],
    ["Chicken", "Meat", 6.50, 60],
    ["Eggs", "Dairy", 3.20, 110],
    ["Bananas", "Produce", 0.99, 250],
    ["Orange Juice", "Beverages", 3.49, 85],
    ["Cheddar Cheese", "Dairy", 4.10, 70]
]

def analyze_sales(records):
    print("===================================")
    print("=== ALDI SALES & REVENUE REPORT ===")
    print("===================================")
    print(f"Total Unique Items Tracked: {len(records)}\n")
    
    total_revenue = 0
    total_items_sold = 0
    item_sales = []

    for item, category, price, quantity in records:
        revenue = price * quantity
        total_revenue += revenue
        total_items_sold += quantity
        item_sales.append((item, revenue))
        print(f"- {item:<15} ({category:<9}): Sold {quantity:>3} units | Revenue: ${revenue:>7.2f}")

    print("-" * 50)
    print(f"Total Units Sold : {total_items_sold}")
    print(f"Total Store Revenue: ${total_revenue:.2f}")
    
    top_item = max(item_sales, key=lambda x: x[1])
    print(f"Top Performing Item: {top_item[0]} (${top_item[1]:.2f})")
    print("===================================")

if __name__ == "__main__":
    analyze_sales(sales_records)