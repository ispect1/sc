`scp -P 4242 level02@localhost:/home/user/level02/level02.pcap .`

`chmod +r level02.pcap`

`python script.py level02.json`

1) Скачиваем файл по scp
2) Даем ему права на чтение
3) Скачиваем Wireshark
4) Заргужаем в него pcap файл
5) Вибираем пакеты с data
6) Сохраняем как json
7) Запускаем python скрипт поиска пароля
