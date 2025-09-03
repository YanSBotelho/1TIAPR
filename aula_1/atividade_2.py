nome = input ("Qual seu nome?: ")

print(f"\n Olá, {nome}! Como você está? ")

input ("\nseu sentimento: ")

print ("\nque bom! vamos começar calculando a área do seu círculo! \nme diga qual o raio dele...")

raio_circ = input("\nraio do seu círculo: ")
PI = 3.14159
area_circ = PI * float(raio_circ) ** 2

print("\nsexy! a área do seu círculo é: ", area_circ)
