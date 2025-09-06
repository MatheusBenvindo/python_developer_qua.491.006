import flet as ft

def main(page: ft.Page):
    # Campos de entrada
    preco_gasolina = ft.TextField(label="Preço da Gasolina (R$)", keyboard_type=ft.KeyboardType.NUMBER)
    preco_etanol = ft.TextField(label="Preço do Etanol (R$)", keyboard_type=ft.KeyboardType.NUMBER)

    # Texto de resultado
    resultado = ft.Text("", size=20, weight="bold")

    # Função de comparação
    def comparar_combustivel(e):
        try:
            gasolina = float(preco_gasolina.value.replace(",", "."))
            etanol = float(preco_etanol.value.replace(",", "."))

            if gasolina <= 0 or etanol <= 0:
                raise ValueError

            proporcao = etanol / gasolina

            if proporcao < 0.7:
                resultado.value = f"Etanol está mais vantajoso ({proporcao:.2f})"
                resultado.color = "green"
            else:
                resultado.value = f"Gasolina está mais vantajosa ({proporcao:.2f})"
                resultado.color = "orange"

        except ValueError:
            resultado.value = "Insira valores válidos para os preços!"
            resultado.color = "red"

        page.update()

    # Botão
    botao_comparar = ft.ElevatedButton(text="Comparar", on_click=comparar_combustivel)

    # Layout da página
    page.title = "Comparador de Combustível"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK

    page.appbar = ft.AppBar(title=ft.Text("Etanol ou Gasolina?", size=20), center_title=True)

    page.add(
        ft.Column(
            [
                ft.Text("Qual combustível vale mais a pena?", size=25, weight="bold"),
                preco_gasolina,
                preco_etanol,
                botao_comparar,
                ft.Divider(),
                resultado,
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )

ft.app(main)
