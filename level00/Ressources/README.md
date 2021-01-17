`ssh level00@localhost -p 4242`

`find / -user flag00 2>/dev/null`

`python script.py {pwd} > pwds.txt`

`hydra -l flag00 -P pwds.txt -t 4 ssh://127.0.0.1:4242`

1) Ищем файлы-подсказки
2) Запускаем скрипт расшифровки с помощью шифра Цезаря
3) Запускаем hydra для взлома пароля