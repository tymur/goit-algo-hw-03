import os
import shutil
import argparse


def copy_and_sort_files(source_dir, dest_dir="dist"):
    try:
        # Створюємо директорію призначення, якщо вона не існує
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Обробка всіх елементів у директорії
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)

            if os.path.isdir(item_path):
                # Рекурсивний виклик для вкладених директорій
                copy_and_sort_files(item_path, dest_dir)
            else:
                # Отримуємо розширення файлу
                file_extension = os.path.splitext(item)[-1][1:].lower() or "unknown"
                ext_dir = os.path.join(dest_dir, file_extension)

                # Створюємо піддиректорію для розширення, якщо вона не існує
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(item_path, ext_dir)
                print(f"Скопійовано: {item_path} -> {ext_dir}")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів за розширенням."
    )
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням 'dist')",
    )
    args = parser.parse_args()

    copy_and_sort_files(args.source, args.destination)
