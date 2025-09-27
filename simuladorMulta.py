# Solicita ao usuário a velocidade atual do carro
velocidade = float(input("Qual a velocidade atual do carro? "))

# Verifica se a velocidade ultrapassa o limite permitido (80 km/h)
if velocidade > 80:
    # Informa que o motorista foi multado
    print("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    
    # Calcula e exibe o valor da multa (R$7,00 por cada km acima do limite)
    print("O valor da multa é de: R${:.2f}".format((velocidade - 80) * 7))

# Exibe uma mensagem de encerramento
print("Tenha um bom dia! Dirija com segurança!")
