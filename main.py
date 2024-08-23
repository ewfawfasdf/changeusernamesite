import flet as ft
import time


def main(page: ft.Page):
    # Установка заголовка страницы
    page.title = "bemosoft 0.29.3 no root"

    # Создание текстового поля для ввода ключа
    key_input = ft.TextField(label="Введите ключ", width=300)
    def errmessage():
        error_message = ft.Text("Неверный ключ", color=ft.colors.RED)
        page.add(error_message)
        time.sleep(1)
        page.remove(error_message)
        page.update()
    # Функция для обработки нажатия кнопки
    def on_button_click(e):
        # Показать сообщение о неверном ключе
        error_message = ft.Text("Неверный ключ", color=ft.colors.RED)
        page.add(error_message)



    # Создание кнопки
    submit_button = ft.ElevatedButton(text="Проверить ключ", on_click=on_button_click)

    # Добавление элементов на страницу
    page.add(
        ft.Column(
            controls=[
                key_input,
                submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Выравнивание по центру
        )
    )


# Запуск приложения
if __name__ == "__main__":
    ft.app(target=main)
