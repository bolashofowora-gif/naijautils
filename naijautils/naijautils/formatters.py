def format_naira(amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    return f"₦{amount:,.0f}"
