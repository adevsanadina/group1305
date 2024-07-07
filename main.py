from utils import email_sender


def main():
    list_of_recipients = [
        'adevsanadina@ukr.net',
    ]
    seasons = ['Winter🏂', 'Spring🌷', 'Summer🌊', 'Autumn🍁']

    for res in list_of_recipients:
        params = {
            'letter_title': '🖐Welcome user🖐',
            'recipient_name': 'user',
            'body_content': 'Glad to see you on my first email!!!! ',
            'sender_signature': 'Mr',
            'sender_name': res,
            'footer_text': 'bottom info',
            'age': 15,
            'seasons': seasons


        }
        body = email_sender.create_welcome_letter(params)
        email_sender.send_email(
         recipients=list_of_recipients, mail_subject='Welcome', mail_body=body
     )


if __name__ == '__main__':
    main()
