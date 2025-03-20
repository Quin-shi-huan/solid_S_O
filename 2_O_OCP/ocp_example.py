from abc import ABC, abstractmethod


# Versão com OCP
class AprovaExame(ABC):
    @abstractmethod
    def aprovar_exame(self, exame): pass

    @abstractmethod
    def verificar_condicoes(self, exame): pass


class Exame:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def aprovar(self, aprovador):
        aprovador.aprovar_exame(self)


class AprovadorExameDeSangue(AprovaExame):
    def aprovar_exame(self, exame):
        if exame.tipo == "sangue" and self.verificar_condicoes(exame):
            print("Exame sanguíneo aprovado!")

    def verificar_condicoes(self, exame):
        return True


class AprovadorExameDeRaioX(AprovaExame):
    def aprovar_exame(self, exame):
        if exame.tipo == "raio-x" and self.verificar_condicoes(exame):
            print("Raio-X aprovado!")

    def verificar_condicoes(self, exame):
        return True


exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador_sangue = AprovadorExameDeSangue()
aprovador_raio_x = AprovadorExameDeRaioX()

exame_sangue.aprovar(aprovador_sangue)
exame_raio_x.aprovar(aprovador_raio_x)
