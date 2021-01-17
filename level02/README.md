`scp -P 4242 level02@localhost:/home/user/level02/level02.pcap .
`chmod 700 level02.pcap`

1) Скачиваем файл по scp
2) Даем ему права на чтение
1) Скачиваем Wireshark
2) Заргужаем в него pcap файл
3) Вибираем пакеты с data
4) Сохраняем как json
5) Запускаем python скрипт поиска пароля
