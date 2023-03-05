### Autor: João Ricardo de Souza Gomes

str = ""
str_inv = ""

str = input("informe uma string: ")

# índice do último elemento da string informada
i = len(str) - 1

# iterar a string informada a partir de seu fim, populando a string invertida a partir de seu início
while ( i >= 0 ):
    str_inv += str[i]
    i -= 1

print(str_inv)
