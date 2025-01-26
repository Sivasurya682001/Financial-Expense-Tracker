import flet as ft
import data  # Importing your modified data.py module
import matplotlib.pyplot as plt
import csv

def generate_chart(e):
    names = []
    amounts = []

    with open('saved_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if not row:  # Skip any empty rows
                continue
            if row[0] == 'Income':  # Stop processing before Income/Result
                break
            names.append(row[0])
            amounts.append(float(row[1]))

    plt.bar(names, amounts)
    plt.xlabel('Name')
    plt.ylabel('Amount')
    plt.title('Bar Chart of Names and Amounts')
    plt.show()
    
def main(page: ft.Page):
    page.window_width = 470
    page.window_height = 770
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = True
    page.title = "Nama Kanaku Pilla"
    page.fonts = {
        "Nightcore": "/fonts/Nightcore.ttf",
        "Oswald-Bold": "/fonts/Oswald-Bold.ttf",
        "Ancient": "/fonts/Ancient Ad.ttf",
        "Orange Squash": "/fonts/Orange Squash Free.ttf",
        "Sticky": "/fonts/Sticky Memos Demo Two.ttf",
        "Tamilbold": "/fonts/NotoSansTamil-Bold.ttf",
        "Tamil": "/fonts/NotoSansTamil-Medium.ttf",
        "Poppinsbold": "/fonts/Poppins-Bold.ttf",
        "Poppins": "/fonts/Poppins-Medium.ttf"
    }
    page.theme = ft.Theme(font_family="Poppins")
    page.update()
    
    appbar = ft.CupertinoAppBar(
        leading=ft.IconButton(ft.icons.KEYBOARD_BACKSPACE, on_click=lambda _: page.go("/lan")),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.MENU_BOOK_OUTLINED),
        middle=ft.Text("NAMA KANNAKU PILLA", font_family="Poppinsbold", size=24),
    )

    appbar1 = ft.CupertinoAppBar(
        leading=ft.IconButton(ft.icons.KEYBOARD_BACKSPACE, on_click=lambda _: page.go("/eng")),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.MENU_BOOK_OUTLINED),
        middle=ft.Text("NAMA KANNAKU PILLA", font_family="Poppinsbold", size=24),
    )

    def addi(e):
        new_text_field = ft.TextField(label="Enter Amount: ", width=150)
        text_fields.append(new_text_field)
        new_name_field = ft.TextField(label="Name: ", width=150)
        name_fields.append(new_name_field)
        row = ft.Row([new_name_field, new_text_field])
        additional_rows.append(row)
        content_container.controls.append(row)
        page.update()

    def calc(e):
        try:
            initial_value = float(text1_input.value)
            total_additional = sum(float(field.value) for field in text_fields)
            result = initial_value - total_additional
            result_text.value = "Result: " + str(result)
            if result_text not in content_container.controls:
                content_container.controls.append(result_text)
            page.update()
        except ValueError:
            result_text.value = "Invalid input"
            if result_text not in content_container.controls:
                content_container.controls.append(result_text)
            page.update()

    def save(e):
        data.save_data(text_fields, name_fields, text1_input, result_text)
        for name_field, text_field in zip(name_fields, text_fields):
            name = name_field.value
            amount = text_field.value
            if name and amount:
                saved_data.append(ft.ListTile(title=ft.Text(f"{name}: {amount}")))
        page.update()


    def clear(e):
        text1_input.value = ""
        for field in text_fields:
            field.value = ""
        for name_field in name_fields:
            name_field.value = ""
        result_text.value = "Result: "
        if result_text in content_container.controls:
            content_container.controls.remove(result_text)
        for row in additional_rows:
            content_container.controls.remove(row)
        text_fields.clear()
        name_fields.clear()
        additional_rows.clear()
        page.update()

    def clear_saved_data(e):
        saved_data.clear()
        page.update()

    def show_saved_data_page(e):
        page.go("/saved_data")

    text1_input = ft.TextField(label="Enter: ", width=150)
    result_text = ft.Text(value="Result: ")
    text_fields = []
    name_fields = []
    additional_rows = []
    saved_data = []

    btn_add = ft.ElevatedButton("More", on_click=addi)
    btn_calc = ft.ElevatedButton("Calc", on_click=calc)
    btn_save = ft.ElevatedButton("Save", on_click=save)
    btn_open = ft.ElevatedButton("Open", on_click=show_saved_data_page)
    btn_clear = ft.ElevatedButton("Clear", on_click=clear)

    content_container = ft.Column(
        [
            ft.Row([ft.Text(value="Income: "), text1_input]),
            ft.Row([btn_add, btn_calc, btn_save, btn_clear, btn_open]),
        ]
    )

    def route_change(route):
        page.views.clear()
        page.theme_mode = ft.ThemeMode.LIGHT
        page.theme = ft.theme.Theme(color_scheme_seed='#e87539')
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [splash_screen],
                    padding=0
                )
            )
        elif page.route == "/lan":
            page.views.append(
                ft.View(
                    "/lan",
                    [langlogo],
                    padding=0,
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )
        elif page.route == "/eng":
            page.views.append(
                ft.View(
                    "/eng",
                    [appbar, content_container],
                    padding=10,
                )
            )
        elif page.route == "/tam":
            page.views.append(
                ft.View(
                    "/tam",
                    [appbar],
                    padding=0,
                )
            )
        elif page.route == "/saved_data":
            saved_data_view = ft.View(
                "/saved_data",
                [
                    appbar1,
                    ft.ListView(
                        controls=saved_data
                    ),
                    ft.ElevatedButton("Clear Data", on_click=clear_saved_data),
                    ft.ElevatedButton("Charts", on_click=generate_chart)
                ],
                padding=10
            )
            page.views.append(saved_data_view)
        page.update()

    splash_screen_data = ft.Column(
        [
            ft.Container(height=50),
            ft.Text(value="NAMA KANNAKU PILLA", font_family="Poppins", size=30, color="white"),
            ft.Container(height=50),
            ft.Image(src="/images/booklogo.gif", width=300, scale=1.5),
            ft.Container(height=50),
            ft.ElevatedButton("START", on_click=lambda _: page.go("/lan"))
        ], horizontal_alignment='center'
    )
    splash_screen = ft.Container(
        content=splash_screen_data,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=('#e87539', '#e87539')
        ),
        width=470,
        height=800,
        padding=25
    )

    langlogo_data = ft.Column(
        [
            ft.Container(height=100),
            ft.Text(value="NAMA KANNAKU PILLA", font_family="Poppinsbold", size=30, color="white"),
            ft.Container(height=30),
            ft.Container(
                ft.Text("Hai", text_align="CENTER", size=20, color="#e87539"),
                height=100,
                bgcolor="white",
                width=300,
            ),
            ft.Container(height=50),
            ft.Text(value="Select Your Language.", font_family="Poppinsbold", size=25, color="white"),
            ft.Container(height=50),
            ft.ElevatedButton("Tamil", on_click=lambda _: page.go("/tam")),
            ft.ElevatedButton("English", on_click=lambda _: page.go("/eng")),
        ], horizontal_alignment='center'
    )

    langlogo = ft.Container(
        content=langlogo_data,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=('#e87539', '#e87539')
        ),
        width=470,
        height=800,
        padding=25
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    # Load initial saved data
    # loaded_data = data.load_data()
    # text1_input.value = loaded_data.get("initial_value", "")
    # result_text.value = loaded_data.get("result", "Result: ")
    # for field_data in loaded_data.get("fields", []):
    #     name_field = ft.TextField(label="Name: ", width=150, value=field_data.get("name", ""))
    #     amount_field = ft.TextField(label="Enter Amount: ", width=150, value=field_data.get("amount", ""))
    #     name_fields.append(name_field)
    #     text_fields.append(amount_field)
    #     additional_rows.append(ft.Row([name_field, amount_field]))
    page.update()

ft.app(target=main, assets_dir="assets")
