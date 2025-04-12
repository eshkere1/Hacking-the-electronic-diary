# Hacking the electronic diary

## Содержание

- [Описание](#описание)
- [Установка](#установка)
- [Использование](#использование)

## Описание

Меняет оценки, убирает замечания, создает похвалу

## Установка


```bash
# Клонируйте репозиторий
git clone https://github.com/eshkere1/Hacking the electronic diary.git

# Перейдите в каталог проекта
cd ваш_репозиторий

# Установите зависимости
npm install
```

## Использование

В ```scripts.py``` хронятся функции:
```fix_marks()``` меняет оценки
```remove_chastisements()``` убирает замечания
```create_commendation()``` создает похвалу

В переменной ```SCHOOLKID``` можете поменять имя ученика, для этого создайте файл .env там нужно написать KID_NAME="" (в ковычках должно быть ФИО ученика)



