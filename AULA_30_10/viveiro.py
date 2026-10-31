class Viveiro:
    planta = "Viveiro verde"
    def __init__(self, nome, preco, qualidade):
        self.nome =nome
        self.preco =preco
        self.qualidade = qualidade
    def valor_total(self):
        return self.preco*self.qualidade
    def exibir (self):  
        total =self.valor_total()
        print (f"{self.nome}-R$ {self.preco} {self.qualidade} = R$ {total:.2f}" )

sambambaia = Viveiro ( "sambabaia" , 22.90, 5 )  
sambambaia.exibir()   

def calcular_total (plantas): 
    total = 0
    for planta in plantas: 
        valor_planta = planta.valor_total()
        total += valor_planta
    return total    
        
