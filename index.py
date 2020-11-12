print ("bienvenido supersalud Lauger") #se agrego bienvenida
userId=input ("ingresa tu nombre ")
print(userId)
birthDate=input("ingresa tu fecha de nacimiento ")
print(birthDate)
temperature= int(input("ingresa tu temperatura ")) #se adiciona boleean basico para división de triage
if temperature >= 34:
    if temperature < 37:
        print(f"Su temperatura es {temperature}")
        print("Triage 3")
    elif temperature >= 37:
        print(f"Su temperatura es {temperature}")
        print("Triage 1")
else:
    print("por favor ingrese nuevamente los datos")