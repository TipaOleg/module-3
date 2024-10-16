

def send_email(mail, recipient, sender='university.help@gmail.com'):
    check = check_mail(recipient, sender)
    if check == True:
        if sender == 'university.help@gmail.com':
            return 'Письмо успешно отправлено с адреса ' + sender + ' на адрес ' + recipient
        elif recipient == sender:
            return 'Нельзя отправить письмо самому себе!'
        else:
            return 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес ' + recipient
    else:
        return 'Нвозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient


def check_mail(recipient, sender):
    check_list = ['.com', '.ru', '.net']
    if '@' in recipient and '@' in sender:
        fl = False
        for dom in check_list:
            if recipient.endswith(dom) and sender.endswith(dom):
                fl = True
                break

        return fl

    return False











print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))

print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))

print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))

print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))