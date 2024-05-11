# Definindo a classe Veiculo
class Veiculo:
    def __init__(self, valor, valor_entrada, qtde_parcela, taxa_juros):
        self.valor = valor
        self.valor_entrada = valor_entrada
        self.qtde_parcela = qtde_parcela
        self.taxa_juros = taxa_juros
    
    def calcular_valor_financiado(self):
        # Calculando o valor financiado
        valor_financiado = self.valor - self.valor_entrada
        return valor_financiado
    
    def calcular_valor_parcela(self):
        # Calculando a taxa de juros periódica
        taxa_periodica = self.taxa_juros / 100 / 12  # Convertendo a taxa de juros anual para mensal
        
        # Calculando o valor presente
        valor_presente = self.calcular_valor_financiado()
        
        # Calculando o valor da parcela
        valor_parcela = (valor_presente * taxa_periodica) / (1 - (1 + taxa_periodica) ** -self.qtde_parcela)
        return valor_parcela
    