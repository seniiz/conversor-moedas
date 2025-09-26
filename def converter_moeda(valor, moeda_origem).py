def converter_moeda(valor, moeda_origem, moeda_destino, taxa_cambio):
    if moeda_origem == moeda_destino:
        return valor
    elif moeda_origem == "BRL" and moeda_destino == "USD":
        return valor / taxa_cambio
    elif moeda_origem == "USD" and moeda_destino == "BRL":
        return valor * taxa_cambio
    else:
        raise ValueError("Conversão não suportada.")

def main():
    taxa_cambio = 5.0  # 1 USD = 5 BRL (exemplo fixo)
    
    try:
        valor = float(input("Digite o valor a ser convertido: "))
        moeda_origem = input("Digite a moeda de origem (BRL/USD): ").upper()
        moeda_destino = input("Digite a moeda de destino (BRL/USD): ").upper()
        
        resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxa_cambio)
        print(f"{valor:.2f} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino}.")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
