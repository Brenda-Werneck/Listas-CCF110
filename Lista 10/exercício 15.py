#Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, "Iracema" é um anagrama para "America". Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, "a" = "A".

s1, s2 = [input(f"{x + 1}ª string: ").strip() for x in range(2)]
isAnagrama = True
if len(s1) == len(s2):
    for x in s1:
        if x.lower() not in s2.lower():
            isAnagrama = False
else:
    isAnagrama = False
if isAnagrama:
    print("São anagramas")
else:
    print("Não são anagramas")