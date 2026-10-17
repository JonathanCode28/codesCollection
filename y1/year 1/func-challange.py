total_price_orders = 0

def ordering_ver(costumer, item, price, quantity):
    global total_price_orders # הגדרה זו אומרת לפונקציה כי משתנה זה הינו גלובלי
    total_price_for_item = price * quantity
    total_price_orders += total_price_for_item
    print(f"{costumer} ordered {quantity} X {item}")
    print(f"total price: {total_price_for_item:.2f}")
    print("-"*30)

ordering_ver("Magnus Karlsen", "chess board", 500.90, 3)
ordering_ver("Hikaru Nakamura", "Iphone", 1200.90, 5)
ordering_ver("Harry Kasparov", "headphones", 150.90, 7)

print(f"Total revenue: {total_price_orders:.1f}")