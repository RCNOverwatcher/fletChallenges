import flet as ft


def main(page):
    page.title = "Reverse order printing"
    page.subtitle = "Prints numbers in an array in reverse order"

    the_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    page.add(ft.TextField(value="The array is: " + str(the_array), read_only=True))

    page.add(ft.TextField(value="The array in reverse order is: " + str(the_array[::-1]), read_only=True))

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
