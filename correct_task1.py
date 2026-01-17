# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0.0
    valid_count = 0

    for order in orders:
        if order.get("status") != "cancelled":
            try:
                amount = float(order.get("amount", 0))
                total += amount
                valid_count += 1
            except (TypeError, ValueError):
                continue

    if valid_count == 0:
        return 0.0

    return total / valid_count
