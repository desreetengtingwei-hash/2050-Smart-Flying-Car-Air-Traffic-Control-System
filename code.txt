print ("=== FURNITURE ORDER SYSTEM ===")
chair = input ("Product (C/D) : ").upper()

if chair == "C" or chair == "D":
  quantity = int (input("Quantity : "))
  if chair == "C":
    name = "Office Chair"
    price = 250
    cost = price*quantity
    if quantity > 10:
      if quantity > 30:
        discount = cost*0.12
      else:
        discount = cost*0.05
  else:
    name = "Study Desk"
    price = 400
    cost = price*quantity
    if quantity > 8:
      if quantity > 20:
        discount = cost*0.15
      else:
        discount = cost*0.08

  assembly = input ("Assembly (Y/N) : ").upper()

  if assembly == "Y" or assembly == "N":
    if assembly == "Y":
      additional = 20*quantity
    else:
      additional = 0

  adjusted_cost = cost - discount + additional

  if adjusted_cost < 5000:
    delivery = 100
  else:
    delivery = 0

  final_payment = adjusted_cost + delivery

  print ("-"*30)
  print ("Product       : ", name)
  print ("Original Cost :  RM", f"{cost:.2f}")
  print ("Discount      :  RM", f"{discount:.2f}")
  print ("Assembly Fee  :  RM", f"{additional:.2f}")
  print ("Delivery      :  RM", f"{delivery:.2f}")
  print ("Final Payment :  RM", f"{final_payment:.2f}")
