from Aluno import Aluno
from Curso import Curso

def main():
    # Criando alunos
    aluno1 = Aluno("João Silva", "2025001")
    aluno2 = Aluno("Maria Santos", "2025002")

    # Criando cursos
    curso_python = Curso("Python Básico")
    curso_java = Curso("Java Avançado")

    # Inscrever alunos em cursos
    aluno1.inscrever_curso(curso_python)
    aluno2.inscrever_curso(curso_python)
    aluno2.inscrever_curso(curso_java)

    # Listar alunos inscritos no curso de Python
    print("Alunos inscritos no curso de Python:")
    for nome in curso_python.listar_alunos():
        print("-", nome)

    # Listar cursos que a Maria está inscrita
    print("\nCursos que Maria está inscrita:")
    for nome in aluno2.listar_cursos():
        print("-", nome)

if __name__ == "__main__":
    main()
