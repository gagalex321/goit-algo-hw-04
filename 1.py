# Завдання 1:
# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, 
# переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.

import argparse
import shutil
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів за розширенням."
    )
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням: dist)"
    )
    return parser.parse_args()


def copy_file(file_path, source, destination):
    try:
        extension = file_path.suffix.lower().lstrip(".")

        if not extension:
            extension = "no_extension"

        target_dir = destination / extension
        target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / file_path.name

        # Уникаємо перезапису файлів з однаковими назвами
        if target_file.exists():
            print(f"Файл вже існує, пропускаємо: {target_file}")
            return

        shutil.copy2(file_path, target_file)
        print(f"Скопійовано: {file_path} -> {target_file}")

    except (OSError, shutil.Error) as error:
        print(f"Помилка копіювання {file_path}: {error}")


def read_directory(directory, source, destination):
    try:
        for item in directory.iterdir():
            try:
                if item.is_dir():
                    read_directory(item, source, destination)
                elif item.is_file():
                    copy_file(item, source, destination)

            except OSError as error:
                print(f"Помилка обробки {item}: {error}")

    except OSError as error:
        print(f"Помилка читання директорії {directory}: {error}")


def main():
    args = parse_arguments()

    source = Path(args.source).resolve()
    destination = Path(args.destination).resolve()

    if not source.is_dir():
        print(f"Помилка: вихідна директорія не існує: {source}")
        return

    # Не дозволяємо копіювати директорію призначення саму в себе
    # або створювати нескінченний рекурсивний обхід.
    if destination == source or source in destination.parents:
        print("Помилка: директорія призначення не повинна бути всередині вихідної директорії або збігатися з нею.")
        return

    try:
        destination.mkdir(parents=True, exist_ok=True)
        read_directory(source, source, destination)
        print("Копіювання завершено.")

    except OSError as error:
        print(f"Помилка роботи з директоріями: {error}")


if __name__ == "__main__":
    main()


# Запуск програми:

# Вказати лише вихідну директорію
# python 1.py ./files

# Вказати вихідну директорію та директорію призначення
# python 1.py ./files ./dist