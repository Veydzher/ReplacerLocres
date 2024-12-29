import csv
import os

def load_replacement_data(data_csv_file):
    try:
        replacement_data = {}
        with open(data_csv_file, 'r', newline='', encoding='utf-8') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                key = row['key']
                replacement_string = row['source']
                replacement_data[key] = replacement_string
        return replacement_data
    except FileNotFoundError:
        print(f"Файл {data_csv_file} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка під час завантаження даних: {str(e)}")
        return None

def replace_strings_in_csv(input_csv_file, output_csv_file, replacement_data):
    try:
        with open(input_csv_file, 'r', newline='', encoding='utf-8') as input_file, \
                open(output_csv_file, 'w', newline='', encoding='utf-8') as output_file:
            reader = csv.DictReader(input_file)
            fieldnames = reader.fieldnames

            if 'Translation' not in fieldnames:
                fieldnames.append('Translation')

            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            replaced_count = 0
            total_count = 0

            for row in reader:
                total_count += 1
                key = row['key']
                if key in replacement_data:
                    row['Translation'] = replacement_data[key]
                    replaced_count += 1
                else:
                    row['Translation'] = ""

                writer.writerow(row)

        print(f"Заміна завершена. Оновлений вміст збережено в {output_csv_file}.")
        print(f"Заміна була здійснена для {replaced_count} з {total_count} рядків.")
    except FileNotFoundError:
        print(f"Файл {input_csv_file} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {str(e)}")

def get_file_input(prompt):
    while True:
        file_path = input(prompt).strip()
        if os.path.isfile(file_path):
            return file_path
        print(f"Файл {file_path} не знайдено. Спробуйте ще раз.")

def main():
    print(f'Програма для оновлення рядків під нові файли від veydzh3r.\nПеред початком використання, рекомендується прочитати інструкції у файлі «ReadMe»\n')
    
    input_csv_file = get_file_input('1. Введіть файл .csv з новими рядками (наприклад, Game_New.csv): ')
    output_csv_file = input('2. Введіть назву нового файлу .csv (наприклад, Game_Output.csv): ').strip()
    data_csv_file = get_file_input('3. Введіть файл .csv, з якого будуть взяті перекладені рядки (наприклад, Game.csv): ')

    replacement_data = load_replacement_data(data_csv_file)
    if replacement_data is not None:
        replace_strings_in_csv(input_csv_file, output_csv_file, replacement_data)

if __name__ == '__main__':
    main()
