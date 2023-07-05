# Редактирование телефонной книги
## В рамках домашнего задания «Regular expressions»

Необходимо редактировать адресную книгу, используя регулярные выражения.  
Структура данных будет всегда:   
`lastname,firstname,surname,organization,position,phone,email`  
Предполагается, что телефон и e-mail у человека может быть только один.  

Реализовано:

1. Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
2. Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
3. Объединить все дублирующиеся записи о человеке в одну.  

Функции на Python для управления данными:
- list_correction() - с помощью регулярных выражений приводит к нужному виду ФИО и телефон.
- remove_duplicates() - объединяет записи если совпадает фамилия и имя.