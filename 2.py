# Завдання 2:
# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
# що користувач повинен мати можливість вказати рівень рекурсії.

import turtle


def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length = length / 3.0

        koch_curve(t, length, level - 1)
        t.left(60)

        koch_curve(t, length, level - 1)
        t.right(120)

        koch_curve(t, length, level - 1)
        t.left(60)

        koch_curve(t, length, level - 1)


def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main():
    try:
        level = int(input("Введіть рівень рекурсії (0–6): "))

        if not 0 <= level <= 6:
            print("Помилка: рівень рекурсії має бути від 0 до 6.")
            return

    except ValueError:
        print("Помилка: введіть ціле число.")
        return

    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.pensize(2)

    # Початкові налаштування малювання
    t.penup()
    t.goto(-200, 115)
    t.pendown()

    koch_snowflake(t, 400, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()