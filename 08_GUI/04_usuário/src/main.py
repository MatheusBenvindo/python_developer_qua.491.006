import flet as ft
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    cpf: str
    idade: int
    altura: float
    email: str

def main(page: ft.Page):
    # Configurações da página
    page.title = "Dados do usuário"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada (TextFields)
    nome_input = ft.TextField(label="NOME")
    cpf_input = ft.TextField(label="CPF")
    idade_input = ft.TextField(label="IDADE", suffix_text="anos")
    altura_input = ft.TextField(label="ALTURA", suffix_text="m")
    email_input = ft.TextField(label="EMAIL")

    resultado = ft.Text()

    # Função para capturar os dados e exibir
    def salvar_dados(e):
        try:
            usuario = Pessoa(
                nome=nome_input.value,
                cpf=cpf_input.value,
                idade=int(idade_input.value),
                altura= float(altura_input.value),
                email=email_input.value
            )

            resultado.value = (
                f"Nome: {usuario.nome}\n"
                f"CPF: {usuario.cpf}\n"
                f"Idade: {usuario.idade} anos\n"
                f"Altura: {usuario.altura:.2f} m\n"
                f"Email: {usuario.email}"
            )
        except ValueError:
            resultado.value = "Erro: Verifique se idade e altura são números válidos."

        resultado.update()

    # Adicionando os componentes à página
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do usuário", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        nome_input,
        cpf_input,
        idade_input,
        altura_input,
        email_input,
        ft.ElevatedButton("Salvar", on_click=salvar_dados),
        resultado
    )

ft.app(main)
