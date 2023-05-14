
from abc import ABC, abstractmethod


class AbstractAnimal(ABC):
  @property
  @abstractmethod
  def nome(self)-> str:
    pass

  @property
  @abstractmethod
  def raca(self) -> str:
    pass

  @property
  @abstractmethod
  def chip(self)-> int:
    pass

 
    