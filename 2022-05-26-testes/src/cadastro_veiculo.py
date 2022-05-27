
class CadastroVeiculo():

    def __init__(self) -> None:
        self.__lista = []

    def inserir(self, entity):        
        try:
            self.__lista.append(entity)
        except Exception as ex:
            raise ex
        else:
            return True

    def consultar(self, id):
        lista = list(filter(lambda x: x.id == id, self.__lista))
        if len(lista) > 0:
            return lista[0]

    def remover_por_id(self, id):
        try:
            veiculo = self.consultar(id)
            self.__lista.remove(veiculo)
        except Exception as ex:
            raise ex
        else:
            return True

    def listar_todos(self):
        return self.__lista