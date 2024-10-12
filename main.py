import flet as ft
from Utils.helper import send_email
from Utils.Constants import (SMTP_SERVER_ADDRESS, SENDER_ADDRESS, SENDER_PASSWORD, PORT)


def main(page):

    # Define o corpo do botao
    def btn_clicked(e): 
        if not message_body.value and not subject_field.value:

            message_body.value = "Please entre a message"
            subject_field.value = "Please entre a subject"
        else:
            extra_info = """
            
            -----------------------------------------------
            Email Address of sender {} \n

            Sender Full Name {} \n
            """.format(SENDER_ADDRESS, full_name.value)


            message = extra_info + message_body.value

            email_sent = send_email(
                SENDER_ADDRESS, SENDER_PASSWORD, receiver_address.value, SMTP_SERVER_ADDRESS, PORT, message, subject_field.value, attachment= None
            )

            if email_sent:
                email_sent_message.value = "Email is sent"
                page.add(email_sent_message)
                page.update()



    subject_field = ft.TextField(label="Assunto")
    full_name = ft.TextField(label="Nome")
    receiver_address = ft.TextField(label="Email")
    message_body = ft.TextField(label="Messagem ", multiline=True)
    send_button = ft.ElevatedButton("Enviar", on_click= btn_clicked)
    email_sent_message = ft.Text("")

    page.add(
        ft.Container(content= ft.Column(

            [ft.Container(content = subject_field, width= 500, alignment=ft.alignment.center),
            ft.Container(content = full_name, width= 500, alignment=ft.alignment.center),
            ft.Container(content = receiver_address, width= 500, alignment=ft.alignment.center),
            ft.Container(content = message_body, width= 500, alignment=ft.alignment.center),
            ft.Container(content = send_button, width= 500, alignment=ft.alignment.center)],
        ), alignment= ft.alignment.center) 
                              
    )

    page.update()

ft.app(target=main)