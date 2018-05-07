# Решатель квадратных уравнений

Данный модуль позволяет решать квадратные уравнения (статья о квадратных уравнениях на [Википедии](https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82%D0%BD%D0%BE%D0%B5_%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5))

# Как использовать

Программный интерфейс модуля представлен функцией get_roots. Получение справочной информации о функции производится следующим образом:

```
>>> import quadratic_equation
>>> help(quadratic_equation.get_roots)

Help on function get_roots in module quadratic_equation:

get_roots(a, b, c)
    Решает квадратное уравнение.

    Данная функция решает квадратные уравнения, имеющие вид
    a*x*x + b*x + c = 0

    Аргументы функции:
    a -- старший коэффициент уравнения
    b -- средний коэффициент уравнения
    c -- свободный член

    Функция возвращает кортеж из 2-х элементов.

    При этом содержимое кортежа зависит от значения дискриминанта:
    (None, None) - если дискриминант меньше нуля
    (корень1, None) - если дискриминант равен нулю
    (корень1, корень2) - если дискриминант больше нуля
```

Примеры использования модуля для решения квадратных уравнений:

```
>>> import quadratic_equation
>>>
>>> two_roots = quadratic_equation.get_roots(1, 2, -24)
>>> print(two_roots)
(-6.0, 4.0)
>>>
>>> one_root = quadratic_equation.get_roots(1, 4, 4)
>>> print(one_root)
(-2.0, None)
>>>
>>> none_roots = quadratic_equation.get_roots(4, 1, 3)
>>> print(none_roots)
(None, None)
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
