
from abc import ABC, abstractmethod


class AbstractUsuario(ABC):
  @property
  @abstractmethod
  def nome(self)-> str:
    pass

  @property
  @abstractmethod
  def dt_nasc(self) -> str:
    pass

  @property
  @abstractmethod
  def cpf(self)-> int:
    pass

  @property
  @abstractmethod
  def endereco(self)-> int:
    pass
    