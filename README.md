### Тех. Задание - календарь на стеке Django + vue
#### Итерация №1:
Базовая сборка vue и django.
Поиск и установка [компонента календаря](https://github.com/richardtallent/vue-simple-calendar) для Vue.

##### Идея реализации:

2 сервера для фронта и бэка. Коммуникация между сервисами через rest-api.
Сохранение состояни календаря в JSON.
Восстановление состояние каллендаря из JSON.

##### P.S.
Попробовал сделать билд приложения Vue и интегрировать с Django средствами встроенного шаблонизатора, удобного решения на поверхности не обнаружил, нужна тонкая настройка WebPack.
Думаю самый корректный путь - 2 сервиса для бэка и фронта с возможностью запуска на одном инстансе.