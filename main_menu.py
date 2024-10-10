
def main_menu():
    options = ["Шифр Цезаря", "Шифр Атбаш",
               "Пропорциональный шифр", "Шифр Вернама", "Шифр Вижинера",
               "Шифр Плейфейера", "Гаммирование", "Шифр с фиксированным периодом",
               "Шифр перестановкой по таблице", "Выход"]

    choice = 1

    while True:
        if choice == len(options):
            print("Выход")
            break

        print("Выберите опцию:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        choice = input("Ваш выбор: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        if choice > len(options) or choice <= 0:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        match choice:
            case 1:
                run_caesar_cipher()
            case 2:
                run_atbash_cipher()
            case 3:
                run_proportional_cipher()
            case 4:
                run_vernam_cipher()
            case 5:
                run_vigener_cipher()
            case 6:
                run_playfair_cipher()
            case 7:
                run_gamming()
            case 8:
                run_fixed_period_cipher()
            case 9:
                run_table_permutation_cipher()


def run_caesar_cipher():
    print()


def run_atbash_cipher():
    print()


def run_proportional_cipher():
    print()


def run_vernam_cipher():
    print()


def run_vigener_cipher():
    print()


def run_playfair_cipher():
    print()


def run_gamming():
    print()


def run_fixed_period_cipher():
    print()


def run_table_permutation_cipher():
    print()


if __name__ == "__main__":
    main_menu()
