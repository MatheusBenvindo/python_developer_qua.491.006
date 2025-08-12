class Curso:
    def __init__(self, nome_curso):
        self.__nome_curso = nome_curso
        self.alunos_inscritos = []

    @property
    def nome_curso(self):
        return self.__nome_curso

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            if self not in aluno.cursos_inscritos:
                aluno.cursos_inscritos.append(self)

    def listar_alunos(self):
        return [aluno.nome_aluno for aluno in self.alunos_inscritos]
