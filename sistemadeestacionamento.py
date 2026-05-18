# Sistema de Estacionamento
# Disciplina: Lógica de Programação — Engenharia de Software — CEUB
# Autor: Miguel Soares Flores

preco_hora = 5.00
preco_fracao = 2.50  # a cada 30 minutos

print("===== SISTEMA DE ESTACIONAMENTO =====\n")

placa = input("Digite a placa do veículo: ")
horas = int(input("Horas estacionadas: "))
minutos = int(input("Minutos adicionais (0, 30): "))

total = horas * preco_hora

if minutos >= 30:
    total += preco_fracao

print(f"\n===== COMPROVANTE =====")
print(f"Placa: {placa.upper()}")
print(f"Tempo: {horas}h {minutos}min")
print(f"Valor a pagar: R$ {total:.2f}")
