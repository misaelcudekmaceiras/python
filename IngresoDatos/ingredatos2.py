# @autor:Misa
# 24/6/2021
#ingreso de datos por teclado con input
nombre=""
edad=0
peso=0.0

#ahora convertimos los strigs recibidos al tipo deseado
nombre=input("Ingrese su nombre ")
edad=int(input("ingrese su edad "))
peso=float(input("ingrese su peso en kg "))

#los tipos ingresados son string , se convierten  los numericos
#no se puede mezclar str con numericos con el operador +
#para eso tomo sus valores convertidos a str
print("se llama "+nombre+" su edad es "+str(edad)+" su peso es "+str(peso))
print(type(nombre),type(edad),type(peso))
