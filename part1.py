def inputNum():
    Apple = int(input("How many apples you want to buy? "))
    Orange = int(input("How many orange you want to buy? "))
    return Apple * 20, Orange * 25
   
def displayTotal(Apple, Orange):
    print(f"\nEach apple costs ₱20.00, total = ₱{Apple:.2f}")
    print(f"Each orange costs ₱25.00, total = ₱{Orange:.2f}")
    print(f"\nThe total amount is ₱{Apple + Orange:.2f}.")

Apple, Orange = inputNum()

displayTotal(Apple, Orange)
