# @autor:Misa
# 24/6/2021
#ingreso de datos por teclado con input
#este programa tiene una disparidad de tipos en el operador + en linea 16
nombre=""
edad=0
peso=0.0

#ahora convertimos los strigs recibidos al tipo deseado
nombre=input("Ingrese su nombre ")
edad=int(input("ingrese su edad "))
peso=float(input("ingrese su peso en kg "))

#los tipos ingresados son string , se convierten  los numericos
#no se puede mezclar str con numericos con el operador +
print("se llama "+nombre+" su edad es "+edad+" su peso es "+peso)
print(type(nombre),type(edad),type(peso))
