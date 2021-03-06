def LuhnAlgorithm(creditCard):
    creditCard_lowercase = creditCard.lower()
    contains_letter = creditCard_lowercase.islower()
    if not contains_letter:
        nDigits = len(creditCard)
        nSum = 0
        isSecond = False
        for i in range(len(creditCard)-1,-1,-1):
            d = int(creditCard[i])

            if isSecond:
                d *= 2
            
            nSum += d // 10
            nSum += d % 10

            isSecond = not isSecond
        return (nSum % 10 == 0)
    else:
        return False