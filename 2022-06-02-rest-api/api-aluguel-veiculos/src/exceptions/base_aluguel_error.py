class BaseAluguelError(Exception):

    def __init__(self, *args: object) -> None:
        self.mensagem = args[0]
        super().__init__(*args)