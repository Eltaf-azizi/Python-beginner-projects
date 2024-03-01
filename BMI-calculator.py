def calculate_bmi(height, weight):
    """
    Calculate the Body Mass Index (BMI) given height (in meters) and weight (in kilograms).
    Formula: BMI = weight / (height ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("Body Mass Index (BMI) Calculator")
    print("---------------------------------")
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    
    bmi = calculate_bmi(height, weight)
    print("Your BMI is:", bmi)

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("Your weight is normal.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()
