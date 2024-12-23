import csv
import time
import os

def replace_strings_in_csv(input_csv_file, output_csv_file, data_csv_file):
    """
    Args:
    input_csv_file (str): Файл .csv з новими ключами та рядками.
    output_csv_file (str): Файл .csv, куди будуть вставлені перекладені рядки.
    data_csv_file (str): Файл .csv, з якого будуть взяті перекладені рядки для заміни.
    """
    
    try:
        replacement_data = {}
        with open(data_csv_file, 'r', newline='', encoding='utf-8') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                key = row['key']
                replacement_string = row['source']
                replacement_data[key] = replacement_string

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
    
    except FileNotFoundError as e:
        print(f"Файл не знайдено: {e.filename}")
    except Exception as e:
        print(f"Сталася помилка: {str(e)}")

def main():
    print(f'Програма для оновлення рядків під нові файли від veydzh3r.\nПеред початком використання, рекомендується прочитати інструкції у файлі «ReadMe»\n')
    try:
        input_csv_file = input('1. Введіть файл .csv з новими рядками (до прикладу Foxhole-CodeStrings_New.csv): ')
        output_csv_file = input('2. Введіть назву нового файлу .csv, куди будуть вставлені перекладені рядки (до прикладу Foxhole-CodeStrings-Output): ')
        data_csv_file = input('3. Введіть файл .csv, з якого будуть взяті перекладені рядки (до прикладу Foxhole-CodeStrings.csv): ')
    except ValueError as e:
        print(f'Файл не знайдено: {e}')
        print('Перезапуск програми...')
        time.sleep(1.5)
        main()
    if os.path.exists(input_csv_file) and os.path.exists(data_csv_file):
        replace_strings_in_csv(input_csv_file, output_csv_file+'.csv', data_csv_file)
    else:
        main()

if __name__ == '__main__':
    main()