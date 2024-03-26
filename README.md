#Бот выдает наибольшие, наименьшие и диапазон цен на авиабилеты из Москвы(Внуково) в Тбилиси и обратно.

1.Команда /low -> https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&limit={min_pr}&page=1&one_way=true&token=f7b597efadfaf8287ec2a27842a00b76
min_pr - требуемое количество наименьших значений
После ввода команды у пользователя запрашивается:
    - Количество авиарейсов с самыми низкими ценами, которые необходимо вывести.
2.Команда /high -> https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&limit={max_pr}&page=1&one_way=true&token=f7b597efadfaf8287ec2a27842a00b76
max_pr - требуемое количество наибольших значений
После ввода команды у пользователя запрашивается:
    - Количество авиарейсов с самыми высокими ценами, которые необходимо вывести.
3.Команда /custom -> https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&limit={start_pr}&page=1&one_way=true&token=f7b597efadfaf8287ec2a27842a00b76
https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&limit={end_pr}&page=1&one_way=true&token=f7b597efadfaf8287ec2a27842a00b76
После ввода команды у пользователя запрашивается:
    - Диапазон значений выборки (минимальное и максимальное значения).
    - Количество единиц категории, которые необходимо вывести.
4.Команда /history
После ввода команды выводится краткая история запросов пользователя (последние
десять запросов).

Описание внешнего вида и UI
Окно Телеграм-бота воспринимает команды:
    ● /help — помощь по командам бота;
    ● /low — самые дешевые авиабилеты и краткая информация о них;
    ● /high — самые дешевые авиабилеты и краткая информация о них;
    ● /custom — вывод показателей пользовательского диапазона авиабилетовтов и краткая информация о них;
    ● /history — вывод истории запросов пользователей
