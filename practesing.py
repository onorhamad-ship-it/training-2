Set-Content -Path "sales_data_processor.py" -Value '# Supermarket Data Processing Script

data = [
    {"item": "Laptop", "category": "Electronics", "price": 850.00, "qty": 4},
    {"item": "Coffee Maker", "category": "Home Appliances", "price": 45.50, "qty": 12},
    {"item": "Desk Chair", "category": "Furniture", "price": 120.00, "qty": 6},
    {"item": "Wireless Mouse", "category": "Electronics", "price": 25.00, "qty": 20},
    {"item": "Blender", "category": "Home Appliances", "price": 60.00, "qty": 8}
]

def process_sales(records):
    print("===========================================")
    print("=== DATA ANALYSIS & REVENUE REPORT ===")
    print("===========================================\n")
    
    total_revenue = 0
    high_value_items = []

    for entry in records:
        item = entry["item"]
        category = entry["category"]
        price = entry["price"]
        qty = entry["qty"]
        revenue = price * qty
        total_revenue += revenue

        if revenue > 300:
            high_value_items.append((item, revenue))

        print(f"Product: {item:<15} | Cat: {category:<15} | Revenue: ${revenue:>8.2f}")

    print("\n" + "-" * 45)
    print(f"Total Portfolio Revenue : ${total_revenue:.2f}")
    print(f"High-Value Transactions : {len(high_value_items)} products generating > $300")
    print("===========================================")

if __name__ == "__main__":
    process_sales(data)'