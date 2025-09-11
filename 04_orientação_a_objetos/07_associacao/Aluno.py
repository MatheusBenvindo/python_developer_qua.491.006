class Aluno:
    def __init__(self, nome_aluno, matricula):
        self.__nome_aluno = nome_aluno
        self.__matricula = matricula
        self.cursos_inscritos = []

    @property
    def nome_aluno(self):
        return self.__nome_aluno

    @nome_aluno.setter
    def nome_aluno(self, nome_aluno):
        self.__nome_aluno = nome_aluno

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)

    def listar_cursos(self):
        return [curso.nome_curso for curso in self.cursos_inscritos]
