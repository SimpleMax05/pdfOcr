import flet as ft
import tkinter.filedialog as fd

def main(page: ft.Page):
    page.title = "pdf в pdfocr"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "white"
    
        
    def pick_files_result(e: ft.FilePickerResultEvent):
        txt_number.value = e.path
        txt_number.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    txt_number = ft.TextField(label="Место расположение файлов", bgcolor="grey", value="", text_align=ft.TextAlign.RIGHT, width=600)

    page.overlay.append(pick_files_dialog)
        
    page.add(
        ft.Row(
            [
                txt_number,
                ft.ElevatedButton(
                    "Путь",
                    icon=ft.icons.FOLDER_OPEN_ROUNDED,
                    on_click=lambda _: pick_files_dialog.get_directory_path(
                        dialog_title="Выберите папку с pdf файлами"
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )

ft.app(main)