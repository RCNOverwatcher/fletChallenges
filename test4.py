import flet as ft

def format_array(array):
    return ", ".join(array)




def main(page):
    page.title = "Reverse order printing"
    page.subtitle = "Prints numbers in an array in reverse order"

    the_array = ["apple", "banana", "cherry", "durian", "elderberry"]

    page.add(ft.TextField(value="The array is: " + format_array(the_array), read_only=True))

    page.add(ft.TextField(value="The array in reverse order is: " + format_array(the_array[::-1]), read_only=True))

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
