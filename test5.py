import flet as ft


def main(page):
    page.title = "Triangle calculator"
    page.subtitle = "Enter three numbers"

    def triangle_calc(e):
        input_1 = input_box_1.value
        input_2 = input_box_2.value
        input_3 = input_box_3.value

        input_1 = int(input_1)
        input_2 = int(input_2)
        input_3 = int(input_3)

        if input_1 + input_2 > input_3 and input_1 + input_3 > input_2 and input_2 + input_3 > input_1:
            page.add(ft.Text("The inputs can form a triangle"))
            if input_1 == input_2 and input_1 == input_3:
                page.add(ft.Text("The inputs form an equilateral triangle"))
            elif input_1 == input_2 or input_1 == input_3 or input_2 == input_3:
                page.add(ft.Text("The inputs form an isosceles triangle"))
            else:
                page.add(ft.Text("The inputs form a scalene triangle"))
        else:
            page.add(ft.Text("The inputs cannot form a triangle"))

    input_box_1 = ft.TextField(label="Input 1")
    input_box_2 = ft.TextField(label="Input 2")
    input_box_3 = ft.TextField(label="Input 3")

    button = ft.ElevatedButton(text="Find largest", on_click=triangle_calc)

    page.add(ft.Row([input_box_1, input_box_2, input_box_3]))
    page.add(button)


ft.app(target=main)
