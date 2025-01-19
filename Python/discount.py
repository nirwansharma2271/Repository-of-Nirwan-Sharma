customer_name=input("Enter Your Name:")
membership_code=int(input("Enter The membership code:"))
meal_plan=input("Choose Meal Plan(A/B):")
no_of_days=int(input("No of days:"))
if membership_code==1:
    if meal_plan=="A":
        amount=250*no_of_days
        discount=amount*10/100
        bill=amount-discount
        print(" ")
        print("Customer's Name:",customer_name)
        print("meal plan:",meal_plan)
        print("no of days:",no_of_days)
        print("amount:",amount)
        print("discount:",discount)
        print("Payable Bill:",bill)
    elif meal_plan=="B":
        amount=350*no_of_days
        discount=amount*15/100
        bill=amount-discount
        print(" ")
        print("Customer's Name:",customer_name)
        print("meal plan:",meal_plan)
        print("no of days:",no_of_days)
        print("amount:",amount)
        print("discount:",discount)
        print("Payable Bill:",bill)
    else:
        print("wrong meal plan.")
elif membership_code==2:
    if meal_plan=="A":
        amount=250*no_of_days
        discount=amount*15/100
        bill=amount-discount
        print(" ")
        print("Customer's Name:",customer_name)
        print("meal plan:",meal_plan)
        print("no of days:",no_of_days)
        print("amount:",amount)
        print("discount:",discount)
        print("Payable Bill:",bill)
    elif meal_plan=="B":
        amount=350*no_of_days
        discount=amount*20/100
        bill=amount-discount
        print(" ")
        print("Customer's Name:",customer_name)
        print("meal plan:",meal_plan)
        print("no of days:",no_of_days)
        print("amount:",amount)
        print("discount:",discount)
        print("Payable Bill:",bill)
    else:
        print("wrong meal plan.")
elif membership_code==3:
    if meal_plan=="A":
        amount=250*no_of_days
        discount=amount*20/100
        bill=amount-discount
        print(" ")
        print("Customer's Name:",customer_name)
        print("meal plan:",meal_plan)
        print("no of days:",no_of_days)
        print("amount:",amount)
        print("discount:",discount)
        print("Payable Bill:",bill)
    elif meal_plan=="B":
        amount=350*no_of_days
        discount=amount*25/100
        bill=amount-discount
        print(" ")
        print("Customer's Name:",customer_name)
        print("meal plan:",meal_plan)
        print("no of days:",no_of_days)
        print("amount:",amount)
        print("discount:",discount)
        print("Payable Bill:",bill)
    else:
        print("wrong meal plan.")
else:
    print("wrong membership code.")
