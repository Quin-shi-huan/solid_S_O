from abc import ABC, abstractmethod


# Versão com OCP

class Exame:
    def __init__(self, tipo: str):
        self.tipo = tipo


class AprovaExame(ABC):
    @abstractmethod
    def aprovar_exame(self, exame): pass


class VerificarTipoExame(ABC):
    @abstractmethod
    def verificar(self, exame: Exame) -> bool: pass


class VerificarExameDeSangue(VerificarTipoExame):
    def verificar(self, exame: Exame) -> bool:
        return exame.tipo == 'sangue'


class VerificarExameDeRaioX(VerificarTipoExame):
    def verificar(self, exame: Exame) -> bool:
        return exame.tipo == 'raio-x'


class AprovadorExameDeSangue(AprovaExame):
    def __init__(self, verifica: VerificarExameDeSangue):
        self.verifica = verifica

    def aprovar_exame(self, exame):
        if self.verifica.verificar(exame):
            print(f"Exame de {exame.tipo} aprovado!")
        else:
            print(f"Exame de {exame.tipo} não aprovado!")


class AprovadorExameDeRaioX(AprovaExame):
    def __init__(self, verifica: VerificarExameDeRaioX):
        self.verifica = verifica

    def aprovar_exame(self, exame):
        if self.verifica.verificar(exame):
            print(f"Exame de {exame.tipo} aprovado!")
        else:
            print(f"Exame de {exame.tipo} não aprovado!")


exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

verificar_sangue = VerificarExameDeSangue()
verificar_raio_x = VerificarExameDeRaioX()

aprovar_sangue = AprovadorExameDeSangue(verificar_sangue)
aprovar_raio_x = AprovadorExameDeRaioX(verificar_raio_x)

aprovar_sangue.aprovar_exame(exame_sangue)
aprovar_raio_x.aprovar_exame(exame_raio_x)
