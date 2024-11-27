#       Домашняя работа по уроку "Способы вызова функции"
#       Задача "Рассылка писем"

def send_email(message, recipient, sender="university.help@gmail.com"):
   Fact = False
   if ('@' in recipient and '@' in sender):
      if (".com" in recipient[-4:] or ".net" in recipient[-4:] or ".ru" in recipient[-3:]) and (".com" in sender[-4:] or ".net" in sender[-4:] or ".ru" in sender[-3:]):
         Fact = True
   if not Fact:
      print("Невозможно отправить письмо с адреса ", sender," на адрес ", recipient)
   elif recipient == sender:
      print("Нельзя отправить письмо самому себе!")
   else:
      if sender == "university.help@gmail.com":
         print("Письмо успешно отправлено с адреса ", sender," на адрес ", recipient)
      else:
         print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender," на адрес ", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
