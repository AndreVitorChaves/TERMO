import random

# Lista de palavras possíveis
palavras = ['carro', 'celular', 'futebol', 'computador', 'sapato', 'melancia']
palavra_sorteada = random.choice(palavras).lower()  # Escolhe uma palavra aleatória
tamanho = len(palavra_sorteada)

tentativas = 6  # Número máximo de tentativas

print("Bem-vindo ao TERMO!")
print(f"A palavra tem {tamanho} letras. Você tem {tentativas} tentativas.")

while tentativas > 0:
    tentativa = input(f"\nDigite uma palavra de {tamanho} letras: ").lower()

    if len(tentativa) != tamanho:
        print("Número incorreto de letras. Tente novamente.")
        continue

    resultado = ''
    for i in range(tamanho):
        if tentativa[i] == palavra_sorteada[i]:
            # Letra correta no lugar certo (verde)
            resultado += f'🟩{tentativa[i].upper()}'
        elif tentativa[i] in palavra_sorteada:
            # Letra correta no lugar errado (amarelo)
            resultado += f'🟨{tentativa[i].upper()}'
        else:
            # Letra errada (cinza)
            resultado += f'⬜{tentativa[i].upper()}'

    print(f"Resultado: {resultado}")

    if tentativa == palavra_sorteada:
        print("Parabéns! Você acertou a palavra!")
        break

    tentativas -= 1

if tentativa != palavra_sorteada:
    print(f"Suas tentativas acabaram. A palavra era: {palavra_sorteada.upper()}")
