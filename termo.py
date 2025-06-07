import random
import colorama
colorama.init()

palavras = ['carro', 'celular', 'futebol', 'computador', 'sapato', 'melancia']
palavra_sorteada = random.choice(palavras).lower() 
tamanho = len(palavra_sorteada)

tentativas = 6  

print("Bem-vindo ao TERMO!")
print(f"A palavra tem {tamanho} letras. Você tem {tentativas} tentativas.")

while tentativas > 0:
    tentativa = input(f"\nDigite uma palavra de {tamanho} letras: ").lower()

    if len(tentativa) != tamanho:
        print("Número incorreto de letras. Tente novamente.")
        continue

    resultado = ''
    for i in range(tamanho):
        letra = tentativa[i].upper()
        if tentativa[i] == palavra_sorteada[i]:
            resultado += colorama.Fore.GREEN + letra + colorama.Fore.RESET
        elif tentativa[i] in palavra_sorteada:
            resultado += colorama.Fore.YELLOW + letra + colorama.Fore.RESET
        else:
            # Letra errada (cinza)
            resultado += colorama.Fore.WHITE + letra + colorama.Fore.RESET

    print(f"Resultado: {resultado}")

    if tentativa == palavra_sorteada:
        print("Parabéns! Você acertou a palavra!")
        break

    tentativas -= 1

if tentativa != palavra_sorteada:
    print(f"Suas tentativas acabaram. A palavra era: {palavra_sorteada.upper()}")
