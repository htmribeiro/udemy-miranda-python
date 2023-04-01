from calc_birth import date_of_birth

nome = 'Hamilton'
sobrenome = 'Ribeiro'
data_nascimento = date_of_birth(1980, 3, 21)
idade = data_nascimento[1]
maior_de_idade = idade >= 18
altura_metros = 1.88

print('Name:', nome)
print("Last Name:", sobrenome)
print("Age:", idade)
print("Year was born:", data_nascimento[0])
print("Adult:", maior_de_idade)
print("Width:", altura_metros)
