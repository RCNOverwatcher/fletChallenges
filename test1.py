import flet as ft


def main(page):
    page.title = "Positive, Negative or Zero"
    page.subtitle = "Enter a number to find out if it is positive, negative or zero"

    def number_click(e):
        if not number_input.value:
            number_input.error_text = "Please enter a valid value"
            page.update()
        else:
            number_input.error_text = ""
            number = float(number_input.value)
            if number > 0:
                page.add(ft.Text(f"{number} is a positive number"))
            elif number < 0:
                page.add(ft.Text(f"{number} is a negative number"))
            else:
                page.add(ft.Text(f"{number} is zero"))

    number_input = ft.TextField(label="Number", width=500)
    number_input.content_padding = 100
    check_button = ft.ElevatedButton("Check", on_click=number_click, width=300)
    page.add(number_input)
    page.add(check_button)

    page.update()


ft.app(target=main)
