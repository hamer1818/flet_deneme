import flet as ft

def main(page: ft.Page):
    page.title = "Chat Uygulaması"
    
    # Mesaj listesi
    messages = ft.Column()

    # Yeni mesaj ekleme fonksiyonu
    def send_message(e):
        if message_input.value:
            messages.controls.append(ft.Text(message_input.value))
            message_input.value = ""
            page.update()

    # Mesaj girişi
    message_input = ft.TextField(hint_text="Mesajınızı yazın...", expand=True)
    
    # Gönder butonu
    send_button = ft.ElevatedButton("Gönder", on_click=send_message)

    # Sayfaya bileşenleri ekleme
    page.add(
        ft.Column([
            messages,
            ft.Row([message_input, send_button])
        ])
    )

# Uygulamayı çalıştır
ft.app(target=main)
