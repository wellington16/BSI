salario=float (input ("digite o salário para calculodo imposto:"))
base=salario
imposto=0
if base>3000:
    imposto=imposto+((base-300)*0.35)
    base =3000
if base >1000:
    imposto=((base- 1000)*0.20)
print ("Salário :R$%6.2f imposto a pagar:R$%6.2f"%(salario,imposto))
