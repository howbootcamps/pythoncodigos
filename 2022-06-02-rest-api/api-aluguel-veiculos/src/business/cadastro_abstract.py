from abc import ABC
from typing import List
from src.entities.entity import Entity
from src.exceptions.not_found_error import NotFoundError

class CadastroAbtract(ABC):

    def __init__(self):
        self.__lista = []

    def inserir(self, entidade: Entity) -> None:
        self.__lista.append(entidade)

    def consultar(self, id: str) -> Entity:
        entidade = list(filter(lambda x: x.id == id, self.__lista))

        if entidade == []:
            raise NotFoundError("Entidade não encontrada.")

        return entidade[0]

    def remover_por_id(self, id: str) -> None:
        entidade = self.consultar(id)
        self.__lista.remove(entidade)

    def remover_por_entidade(self, entidade: Entity) -> None:
        self.__lista.remove(entidade)

    def listar_todos(self) -> List[Entity]:
        return self.__lista
