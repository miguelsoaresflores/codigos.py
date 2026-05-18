# Média do Aluno com Exame
# Disciplina: Lógica de Programação — Engenharia de Software — CEUB
# Autor: Miguel Soares Flores
 
nome = input("Digite o nome do aluno: ")
 
nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))
 
media = (nota1 + nota2) / 2
 
print(f"\n===== RESULTADO DE {nome.upper()} =====")
print(f"Média: {media:.1f}")
 
if media >= 7.0:
    print("Situação: APROVADO ✓")
elif media >= 5.0:
    print("Situação: EXAME FINAL")
    exame = float(input("Digite a nota do exame final: "))
    media_final = (media + exame) / 2
    print(f"Média Final: {media_final:.1f}")
    if media_final >= 5.0:
        print("Situação Final: APROVADO ✓")
    else:
        print("Situação Final: REPROVADO ✗")
else:
    print("Situação: REPROVADO ✗")
 
