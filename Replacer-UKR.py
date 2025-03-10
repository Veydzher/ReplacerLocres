import time
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

def file_input(prompt, extension):
    file_path = input(f'\n{prompt}\n').strip()
    if os.path.isfile(file_path) and file_path.endswith(extension):
        return file_path
    print(f"Файл не знайдено або недійсний формат файлу. Спробуйте ще раз.")
    time.sleep(1)
    return file_input(prompt, extension)

def main():
    print(f'Програма для оновлення рядків під нові файли від veydzh3r.\nПеред початком використання, рекомендується прочитати інструкції у файлі «ReadMe»\n')
    
    data_csv_file = file_input('1. Введіть файл .csv, з якого будуть взяті перекладені рядки (наприклад, Game.csv): ', '.csv')
    input_csv_file = file_input('2. Введіть файл .csv з новими рядками (наприклад, Game_New.csv): ', '.csv')
    output_csv_file = input('3. Введіть назву нового файлу .csv (наприклад, Game_Output.csv): ').strip()

    replacement_data = load_replacement_data(data_csv_file)
    if replacement_data is not None:
        replace_strings_in_csv(input_csv_file, output_csv_file, replacement_data)

if __name__ == '__main__':
    main()
