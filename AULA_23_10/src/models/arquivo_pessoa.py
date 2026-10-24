from pathlib import Path
from datetime import datetime

from src.models.erros_arquivo_pessoa import (
    ErroCriacaoArquivoPessoa
)


class ArquivoPessoa:
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def salvar(self):
        try:
            agora = datetime.now()
            nome_pasta = agora.strftime("%Y%m%d_%H-%M-%S")

            raiz_projeto = Path(__file__).resolve().parents[2]

            pasta = (
                raiz_projeto
                / "arquivos_criados"
                / nome_pasta
            )

            pasta.mkdir(parents=True, exist_ok=True)

            arquivo = pasta / "pessoa.txt"

            conteudo = (
                f"Nome: {self.pessoa.nome}\n"
                f"Data de nascimento: {self.pessoa.data_nascimento}\n"
                f"Data atual: {self.pessoa.data_atual}\n"
                f"Idade: {self.pessoa.idade}\n"
            )

            arquivo.write_text(conteudo, encoding="utf-8")

            return arquivo

        except OSError as erro:
            raise ErroCriacaoArquivoPessoa(
                f"Erro ao salvar os dados: {erro}"
            ) from erro