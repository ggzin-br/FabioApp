# This Python file uses the following encoding: utf-8


class FabioTurtle:

    # Declarações
    turma: tuple = ("André", "Fernanda", "Luiz")
    def __init__(self, nome):
        self.nome = nome

    # Função de verificar o item na tupla
    def checkar(self):
        if self.turma.__contains__(self.nome):
            return True
        return False
