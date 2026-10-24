from datetime import date, datetime

from src.models.pessoa import Pessoa


class PessoaService:
    def criar_pessoa(self):
        nome = input("Digite o nome da pessoa: ")

        data_texto = input(
            "Digite a data de nascimento (DD/MM/AAAA): "
        )

        data_nascimento = datetime.strptime(
            data_texto, "%d/%m/%Y"
        ).date()

        data_atual = date.today()

        pessoa = Pessoa(
            nome,
            data_nascimento,
            data_atual
        )

        return pessoa