`touch /tmp/no_token`

`ltrace ./level10 /tmp/no_token 127.0.0.1`

Видим, что ипользуется функция access
Warning: Using access() to check if a user is authorized to, for example,
open a file before actually doing so using open(2) creates a security
hole,
because the user might exploit the short time interval
between checking and opening the file to manipulate it.
For this reason, the use of this system call should be avoided.
(In the example just described, a safer alternative would be to
temporarily
switch the process's effective user ID to the real ID and then call
open(2).)



`nc -lk 6969`

1) Запускаем ltrace для просмотра трассировки вызовов
2) Создаем  скрипт, который в бесконечном цикле создает символьную ссылку то на файл token, то на файл, к которому у нас есть доступ
3) Создаем  скрипт, который в бесконечном цикле запускает `level10`
4) Слушаем 6969 порт localhost для получения пароля