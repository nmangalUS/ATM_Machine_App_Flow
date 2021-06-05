password = 12345
current_balance = 60000
password = input("Enter your password: ")
if int(password) == 12345:
    withdraw_money = input("How much would you like to withdraw? ")
    remaining_balance = int(current_balance) - int(withdraw_money)
    if int(withdraw_money) > 60000:
        print("you have no sufficient balance,",
              "please discuss to the bank representative")
    elif int(withdraw_money) < 500:
        print("You cannot withdraw less than", current_balance)
    else:
        print("your current balance is", remaining_balance)
else:
    print("Your password is wrong")
