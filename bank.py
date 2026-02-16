# Loan Eligibility Checker

# Taking user inputs
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))
existing_loans = input("Do you have existing loans? (Yes/No): ").strip().lower()

# Basic eligibility check
if age < 21 or age > 60:
    print("Loan Rejected: Age must be between 21 and 60.")
elif salary < 25000:
    print("Loan Rejected: Salary must be at least 25,000.")
else:
    # Determine credit score category
    if credit_score >= 750:
        category = "Excellent"
    elif 650 <= credit_score <= 749:
        category = "Good"
    elif 550 <= credit_score <= 649:
        category = "Average"
    else:
        category = "Poor"
    
    print(f"Credit Score Category: {category}")
    
    # Nested loan approval logic
    if category == "Excellent" and existing_loans == "no":
        print("Loan Status: Approved (Immediate Approval)")
    elif category == "Good" and salary > 50000:
        print("Loan Status: Approved")
    elif category == "Average" and existing_loans == "no":
        print("Loan Status: Conditional Approval")
    elif category == "Poor":
        print("Loan Status: Rejected")
    else:
        print("Loan Status: Rejected")
# Electricity Bill Calculator

# Input
units = float(input("Enter units consumed: "))
senior = input("Are you a senior citizen? (Yes/No): ").strip().lower()

# Check for invalid input
if units < 0:
    print("Invalid input: Units cannot be negative.")
else:
    bill = 0

    # Slab Calculation
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 8)
    else:
        bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)

    print(f"Bill after slab calculation: ₹{bill:.2f}")

    # Apply surcharge if applicable
    if bill > 5000:
        surcharge = bill * 0.10
        bill += surcharge
        print(f"10% Surcharge Applied: ₹{surcharge:.2f}")
        print(f"Bill after surcharge: ₹{bill:.2f}")

    # Apply senior citizen discount after surcharge
    if senior == "yes":
        discount = bill * 0.05
        bill -= discount
        print(f"5% Senior Citizen Discount: ₹{discount:.2f}")

    # Final Bill
    print(f"Final Electricity Bill: ₹{bill:.2f}")
amount = float(input("Enter total purchase amount: "))
member = input("Membership type (Gold/Silver/None): ").lower()
festival = input("Festival season? (Yes/No): ").lower()

if amount < 0:
    print("Invalid input")
else:
    original = amount  # store original amount

    # Membership discount
    if member == "gold":
        amount -= amount * 0.20
    elif member == "silver":
        amount -= amount * 0.10

    # Festival discount (after membership discount)
    if festival == "yes":
        amount -= amount * 0.10

    # Extra 5% if purchase > 10000
    if original > 10000:
        amount -= amount * 0.05


    print("Final Payable Amount:", round(amount, 2))

    # Free shipping message
    if original > 10000 and festival == "yes":
        print("Free Shipping Applied!")



