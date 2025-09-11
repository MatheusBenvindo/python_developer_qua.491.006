import flet as ft

def main(page: ft.Page):
    # Lista de registros
    registros = []

    # Função para calcular IMC
    def calcular_imc(peso, altura):
        imc = peso / (altura ** 2)
        if imc < 18.5:
            diagnostico = "Abaixo do peso"
        elif imc < 25:
            diagnostico = "Peso ideal"
        elif imc < 30:
            diagnostico = "Acima do peso"
        elif imc < 35:
            diagnostico = "Obeso"
        elif imc < 40:
            diagnostico = "Obesidade nível 2"
        else:
            diagnostico = "Obesidade mórbida"
        return imc, diagnostico

    # Campos de entrada
    nome = ft.TextField(label="Nome")
    peso = ft.TextField(label="Peso (kg)")
    altura = ft.TextField(label="Altura (m)")

    # Tabela de registros
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Nome")),
            ft.DataColumn(label=ft.Text("Peso")),
            ft.DataColumn(label=ft.Text("Altura")),
            ft.DataColumn(label=ft.Text("IMC")),
            ft.DataColumn(label=ft.Text("Diagnóstico")),
            ft.DataColumn(label=ft.Text("Ações")),
        ],
        rows=[]
    )

    # Atualizar tabela na tela
    def atualizar_tabela():
        tabela.rows.clear()
        for idx, reg in enumerate(registros):
            tabela.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(reg["nome"])),
                        ft.DataCell(ft.Text(str(reg["peso"]))),
                        ft.DataCell(ft.Text(str(reg["altura"]))),
                        ft.DataCell(ft.Text(f"{reg['imc']:.2f}")),
                        ft.DataCell(ft.Text(reg["diagnostico"])),
                        ft.DataCell(
                            ft.Row([
                                ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e, i=idx: editar_registro(i)),
                                ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, i=idx: deletar_registro(i)),
                            ])
                        ),
                    ]
                )
            )
        page.update()

    # Adicionar novo registro
    def adicionar_registro(e):
        if not nome.value or not peso.value or not altura.value:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        try:
            p = float(peso.value.replace(",", "."))
            a = float(altura.value.replace(",", "."))
            imc, diagnostico = calcular_imc(p, a)
            registros.append({
                "nome": nome.value,
                "peso": p,
                "altura": a,
                "imc": imc,
                "diagnostico": diagnostico
            })
            nome.value = ""
            peso.value = ""
            altura.value = ""
            atualizar_tabela()
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Peso e altura devem ser números!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # Editar registro
    indice_edicao = ft.Ref[int]()

    def editar_registro(index):
        registro = registros[index]
        nome.value = registro["nome"]
        peso.value = str(registro["peso"])
        altura.value = str(registro["altura"])
        btn_adicionar.text = "Salvar Alteração"
        indice_edicao.current = index
        page.update()

    # Salvar alteração
    def salvar_ou_adicionar(e):
        if btn_adicionar.text == "Salvar Alteração":
            try:
                p = float(peso.value.replace(",", "."))
                a = float(altura.value.replace(",", "."))
                imc, diagnostico = calcular_imc(p, a)
                registros[indice_edicao.current] = {
                    "nome": nome.value,
                    "peso": p,
                    "altura": a,
                    "imc": imc,
                    "diagnostico": diagnostico
                }
                nome.value = ""
                peso.value = ""
                altura.value = ""
                btn_adicionar.text = "Adicionar Registro"
                atualizar_tabela()
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.Text("Peso e altura devem ser números!"), bgcolor="red")
                page.snack_bar.open = True
                page.update()
        else:
            adicionar_registro(e)

    # Deletar registro
    def deletar_registro(index):
        registros.pop(index)
        atualizar_tabela()

    # Botão de adicionar/salvar
    btn_adicionar = ft.ElevatedButton("Adicionar Registro", on_click=salvar_ou_adicionar)

    # Layout da página
    page.title = "CRUD de IMC"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK

    page.appbar = ft.AppBar(title=ft.Text("Cadastro de IMC", size=20), center_title=True)

    page.add(
        ft.Column(
            [
                ft.Text("Registro de IMC", size=25, weight="bold"),
                nome,
                peso,
                altura,
                btn_adicionar,
                ft.Divider(),
                tabela,
            ]
        )
    )

    atualizar_tabela()

ft.app(main)
