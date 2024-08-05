## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    if len(valores) == 0:
        return 0  # Evita divisão por zero se a lista estiver vazia
    soma = sum(valores)
    tamanho = len(valores)
    media = soma / tamanho
    return media

continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    else:
        try:
            numero = float(valor)  # Converte a entrada para um número
            valores.append(numero)  # Adiciona o número à lista
        except ValueError:
            print('Entrada inválida. Por favor, digite um número ou "ok" para calcular.')

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))
