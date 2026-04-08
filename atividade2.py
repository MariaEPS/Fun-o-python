def soma_imposto(taxa_imposto, custo):
    valor_do_imposto = custo * (taxa_imposto/ 100)

    valor_final = custo + valor_do_imposto

    return valor_final

custo_digitado = float(input("Digite o custo do item: "))
taxa_digitada = float(input("Digite a taxa de imposto (em %): "))

resultado = soma_imposto(taxa_digitada, custo_digitado)

print(f"O valor final com imposto é: R$ {resultado:.2f}")
