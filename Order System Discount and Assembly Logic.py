print(f"{"FURNITURE ORDER SYSTEM":=^40}")
product=input("Product (C/D):").upper()
quant=int(input("Quantity:"))
assembly=input("Assembly (Y/N):").upper()

if product=="C":
  name="Office Chair"
  ori_cost=250*quant
  if quant>=30:
    dis=250*quant*0.12
  elif quant>=10:
     dis=250*quant*0.05
  else:
    dis=0

if product=="D":
  name="Study Desk"
  ori_cost=400*quant
  if quant>=20:
    dis=400*quant*0.15
  elif quant>=8:
     dis=400*quant*0.08
  else:
    dis=0

if assembly=="Y":
  ass_fee= quant*20
elif assembly =="N":
  ass_fee=0

total_after_disandass= ori_cost-dis+ass_fee

if total_after_disandass >= 5000:
  delivery=0
else:
  delivery=100

final=total_after_disandass+delivery

print("-"*40)
print(f"Product: {name}")
print(f"Original Cost: RM{ori_cost:.2f}")
print(f"Discount: RM{dis:.2f}")1
print(f"Assembly Fee: RM{ass_fee:.2f}")
print(f"Delivery: RM{delivery:.2f}")
print(f"Final Payment: RM{final:.2f}")
