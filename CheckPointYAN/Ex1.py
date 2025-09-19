


print ("\nCheckpoint 1 - python - prof. Leo - Yan B.")

# Cadastro
x = int (input ("\nDigite um número principal:  "))
x2 = int (input ("Escolhe um outro número:  "))
y = int (input ("Escreva uma Nota (0 a 10):  "))
valor_produto = int ( input ("Dê um valor para o produto x:  "))
desconto_produto = int ( input ("Dê um desconto para o produto x (10% = 10):  "))
valor_mínimo_desconto = int ( input ("Esse desconto é aplicado a partir de qual valor?:  "))
 
 # 1. Número positivo ou negativo
if x > 0:
    print ("\n1. Número Positivo")
elif x == 0:
    print ("\n1. O Número é Zero")
else:
    print ("\n1. Número Negativo")

# 2. Par ou ímpar
if x % 2 == 0:
    print ("2. Número Par")
else:
    print ("2. Número Ímpar")

# 3. Maioridade
if x >= 18:
    print ("3. Maior de Idade")
else:
    print ("3. Menor de Idade")

# 4. Nota de aprovação
if y < 0 or y > 10:
    print ("4. Nota Inválida - Somente de 0 a 10")
elif y >= 6:
    print ("4. Aprovado")
else:
    print ("4. Reprovado")

# 5.Comparação de dois números
if x > x2:
    print (f"O número {x} é maior do que o {x2}")
elif x2 > x:
    print (f"O número {x2} é maior do que o {x}")
else:
    print ("Os números são iguais")

# 6. Desconto em produto
if valor_produto >= valor_mínimo_desconto:
    print (f"O valor original do produto é {valor_produto}, como esse valor excede {valor_mínimo_desconto}, você recebe um desconto de {desconto_produto}%. O novo valor fica em {valor_produto * (1 - (desconto_produto / 100))}")
# 7. Login simples

# 8. Par ou múltiplo de 5

# 9. Conversão de temperatura

# 10. Calculadora simples