# First-Year AI & DS Project: Simple Unit Converter
print("--- Welcome to the Metric Converter ---")

def convert_cm_to_inches(cm):
    return cm / 2.54

# Taking user input for measurements
user_cm = float(input("Enter length in centimeters (cm): "))
result_inches = convert_cm_to_inches(user_cm)

# Displaying the calculated output
print(f"{user_cm} cm is equal to {result_inches:.2f} inches.")
print("Code execution successful. Foundation block completed!")
