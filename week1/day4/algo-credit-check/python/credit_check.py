from unittest import result
from functools import reduce

def credit_check(string):

    # create a credit card list
    credit_card_num = []

    credit_card_products = []
    
    for digit in string:
        credit_card_num.append(digit)

    # print(credit_card_num)
    credit_card_num = credit_card_num[::-1]
    # print(credit_card_num)

    # in a diff list we will multiply every other acc # by 2
    # if the product is greater than 9, sum individual digits of the product
    # append the new numbers to a second list
    for index in range(0,len(credit_card_num)):
        if index % 2 != 0:
            product = int(credit_card_num[index]) * 2

            sum = 0

            if product >= 10:
                for digits in str(product):
                    sum += int(digits)
                credit_card_products.append(sum)

            else:
                credit_card_products.append(product)
        
        else:
            credit_card_products.append(int(credit_card_num[index]))

    result = reduce(lambda agg, num : agg + num, credit_card_products)

    # print(result)

    if result % 10 == 0:
        return "The number is valid!"

    return "The number is invalid!"


    

    # if the product is greater than 9, sum individual digits of the product
    # append the new numbers to a second list
    
    # third list - add all the numbers together with a reduce function

    # modulo the sum by 10, if == 0 return true, else false
    


# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

