#currency value (multiplied by 1 GBP) as of 12/05/2024. 7:11pm
EUR = 1.16
USD = 1.25
JPY = 195.53
AUD = 1.88

#used a function to convert currency
def convert(amount, currency):
  if currency == "eur":
    return amount * EUR
  elif currency == "usd":
    return amount * USD
  elif currency == "jpy":
    return amount * JPY
  elif currency == "aud":
    return amount * AUD
  elif currency == "gbp":
    return amount * GBP
  else:
    print("Invalid Currency!")
  

#i declared the data types using float() and to make sure the user inputs valid data types
amount = float(input("Enter the amount to convert:   "))
print()
currency = input("Enter the currency to convert to EUR, USD, JPY, AUD:   ")
result = convert(amount, currency.lower())

#rounding the output of the conversion to 2 decimal places
result = round(result, 2)
print()

#final output of the currency conversion
print(amount, "GBP converted into", currency, "is", result, currency)
print()