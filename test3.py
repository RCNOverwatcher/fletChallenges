import flet as ft


def main(page):
    page.title = "Take 3 inputs and determine the largest"
    page.subtitle = "Enter three numbers"

    def find_largest(e):
        input_1 = input_box_1.value
        input_2 = input_box_2.value
        input_3 = input_box_3.value

        input_1 = int(input_1)
        input_2 = int(input_2)
        input_3 = int(input_3)

        if input_1 > input_2 and input_1 > input_3:
            largest = input_1
            page.add(ft.Text(f"The largest value is {largest}, in the input box number 1"))
        elif input_2 > input_1 and input_2 > input_3:
            largest = input_2
            page.add(ft.Text(f"The largest value is {largest}, in the input box number 2"))
        elif input_3 > input_1 and input_3 > input_2:
            largest = input_3
            page.add(ft.Text(f"The largest value is {largest}, in the input box number 3"))
        else:
            page.add(ft.Text("Two or more inputs are equal"))

    input_box_1 = ft.TextField(label="Input 1")
    input_box_2 = ft.TextField(label="Input 2")
    input_box_3 = ft.TextField(label="Input 3")

    button = ft.ElevatedButton(text="Find largest", on_click=find_largest)

    page.add(ft.Row([input_box_1, input_box_2, input_box_3]))
    page.add(button)

ft.app(target=main)