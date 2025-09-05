import flet as ft


def main(page: ft.Page):
    # Função de evento
    def calcular_imc(e):
        if not peso.value:
            peso.error_text = "Insira o peso"
            page.update()
        else:
            peso.error = ""
            page.update()   

        if not altura.value:
            altura.error_text = "Insira a altura"
            page.update()
        else:
            altura.error_text = ""

            # Recebe o valor do input
            peso.value = float(peso.value.replace(",","."))
            altura.value = float(altura.value.replace(",","."))

            # Calcula o IMC
            imc = peso.value/(altura.value**2)
            
            # Exibe o valor do IMC
            dlg_modal.title.value = f"Seu IMC é {imc:.2f}"

            # Diagnóstico
            if imc < 18.5:
                dlg_modal.content.value = "Abaixo do peso."
            elif imc < 25:
                dlg_modal.content.value = "Peso ideal."
            elif imc < 30:
                dlg_modal.content.value = "Acima do peso."
            elif imc < 35:
                dlg_modal.content.value = "Obeso."
            elif imc < 40:
                dlg_modal.content.value = "Obsidade nível 2."
            else:
                dlg_modal.content.value = "Obsidade mórbida."

            # Abre o modal
            page.open(dlg_modal)

            # Limpa e prepara os campos
            peso.value = ""
            altura.value = ""

            page.update()  
            
    # Propriedades da janela
    page.title = "Índice de Massa Corporal"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK

    # Variáveis
    peso = ft.TextField(label="Peso", suffix_text="kg", border_color="white")
    altura = ft.TextField(label="Altura", suffix_text="metros", on_submit=calcular_imc, border_color="white")

    # Caixa de diálago
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    # Barra superior
    page.appbar = ft.AppBar(title=ft.Text("IMC", size=16))

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Índice de Massa Corporal", size=30, weight="bold"),
                alignment=ft.alignment.center
            ),
            expand=True,
        ),
        ft.ResponsiveRow(   
            [
                ft.Container(peso, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(altura , col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Calcular IMC", on_click=calcular_imc, bgcolor="white", color="black"),
                    padding=30,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)