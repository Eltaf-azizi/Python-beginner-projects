def calculate_tip(total_bill, tip_percentage):
    """
    Calculate the tip amount based on the total bill and desired tip percentage.
    """
    tip_amount = total_bill * (tip_percentage / 100)
    return tip_amount

def main():
    print("Tip Calculator")
    print("--------------")
    total_bill = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the desired tip percentage (e.g., 15 for 15%): "))
    
    tip_amount = calculate_tip(total_bill, tip_percentage)
    print(f"Tip Amount: ${tip_amount:.2f}")

if __name__ == "__main__":
    main()
