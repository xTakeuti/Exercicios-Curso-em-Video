import random

print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")

opcoes = ["pedra", "papel", "tesoura"]

escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

escolha_computador = random.choice(opcoes)

print(f"Você escolheu {escolha_usuario}")
print(f"O computador escolheu {escolha_computador}")

if escolha_usuario == escolha_computador:
    print("Empate!")
elif escolha_usuario == "pedra" and escolha_computador == "tesoura":
    print("Você ganhou! Pedra quebra tesoura.")
elif escolha_usuario == "papel" and escolha_computador == "pedra":
    print("Você ganhou! Papel cobre pedra.")
elif escolha_usuario == "tesoura" and escolha_computador == "papel":
    print("Você ganhou! Tesoura corta papel.")
else:
    print("Você perdeu! Tente novamente.")
