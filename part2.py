import math
def getInput():
    money = float(input("Enter the amount of money you have: ₱"))
    applePrice = float(input("What is the price of an apple? ₱"))
    numApple = (money) / (applePrice)
    wNumApple = math.trunc(numApple)
    return wNumApple, applePrice, money

def displayOutput(wNumApple, applePrice, money):
    if wNumApple >> 1:
        print(f"You can buy {wNumApple} apples and your change is ₱{money % applePrice:.2f}.")
    if wNumApple == 1:
        print(f"You can buy {wNumApple} apple and your change is ₱{money % applePrice:.2f}.")
    if wNumApple == 0:
        print(f"Sorry, you cannot afford to buy an apple. You need ₱{applePrice - money:.2f} more for you to buy one.")

wNumApple, applePrice, money = getInput()

displayOutput(wNumApple, applePrice, money)