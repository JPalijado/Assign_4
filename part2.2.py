import math
def getInput():
    money = float(input("Enter the amount of money you have: ₱"))
    applePrice = float(input("What is the price of an apple? ₱"))
    numApple = money / applePrice
    wNumApple = math.trunc(numApple)
    change = money % applePrice
    short = applePrice - money
    return wNumApple, change, short

def displayOutput(wNumApple, change, short):
    if wNumApple > 1:
        print(f"You can buy {wNumApple} apples and your change is ₱{change:.2f}.")
    elif wNumApple == 1:
        print(f"You can buy {wNumApple} apple and your change is ₱{change:.2f}.")
    else:
        print(f"Sorry, you cannot afford to buy an apple. You need ₱{short:.2f} more for you to buy one.")

wNumApple, change, short = getInput()

displayOutput(wNumApple, change, short)