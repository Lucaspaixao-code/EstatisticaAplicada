class Veiculo:
    def __init__(self, valor, valor_entrada, qtde_parcela, taxa_juros):
        self.valor = valor
        self.valor_entrada = valor_entrada
        self.qtde_parcela = qtde_parcela
        self.taxa_juros = taxa_juros
    
    def calcular_valor_financiado(self):
        valor_financiado = self.valor - self.valor_entrada
        return valor_financiado
    
    def ValorParcelaSemJuros(self):
        valorFinanciado = self.calcular_valor_financiado()
        return valorFinanciado / self.qtde_parcela
    
    def calcular_valor_parcela(self):
        taxa_periodica = self.taxa_juros / 100 
            
        valor_presente = self.calcular_valor_financiado()
        valor_parcela = (valor_presente * taxa_periodica) / (1 - (1 + taxa_periodica) ** -self.qtde_parcela)
        return valor_parcela
    
class Imovel:
    def __init__(self, divida, periodo, taxa, entrada):
        self.divida = divida
        self.periodo = periodo
        self.taxa = taxa
        self.entrada = entrada
    
    def calcular_valor_financiado(self):
        return self.divida - self.entrada

    def calcular_valor_parcela(self):
        saldo_devedor = self.calcular_valor_financiado()
        valor_amortizacao = saldo_devedor / self.periodo

        prestacao_mensal = []

        for x in range(1, self.periodo +1):
            juros_mensal = ((saldo_devedor * self.taxa) / 100)
            prestacao_mensal.append(valor_amortizacao + juros_mensal)
            saldo_devedor -= valor_amortizacao
  
        return prestacao_mensal
    
    def juros_por_parcela(self):
        saldo_devedor = self.calcular_valor_financiado()
        valor_amortizacao = saldo_devedor/ self.periodo

        jurosMensal = []

        for x in range(1, self.periodo + 1):
            juros_mensal = ((saldo_devedor * self.taxa) / 100)
            jurosMensal.append(juros_mensal)
            saldo_devedor -= valor_amortizacao

        return jurosMensal
    
    def ValorParcelaSemJurosFixa(self):
        valorFinanciado = self.calcular_valor_financiado()
        return valorFinanciado / self.periodo
    
    def CalcularValorParcelaFixa(self):
        taxa_periodica = self.taxa / 100 

        valor_presente = self.calcular_valor_financiado()
        valor_parcela = (valor_presente * taxa_periodica) / (1 - (1 + taxa_periodica) ** -self.periodo)
        return valor_parcela