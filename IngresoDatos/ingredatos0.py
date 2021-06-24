# @autor:Misa
# 24/6/2021
#ingreso de datos por teclado con input
nombre=""
edad=0
peso=0.0

nombre=input("Ingrese su nombre ")
edad=input("ingrese su edad ")
peso=input("ingrese su peso en kg ")

print("se llama "+nombre+" su edad es "+edad+" su peso es "+peso)
print(type(nombre),type(edad),type(peso))
#los tipos ingresados son string , hay que convertir los numericos