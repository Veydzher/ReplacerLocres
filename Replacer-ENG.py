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
        print(f"File '{data_csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error while loading the data: {str(e)}")
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

        print(f"Replacement complete. Updated content is stored in file '{output_csv_file}'.")
        print(f"Replacement has been done for {replaced_count} of {total_count} strings.")
    except FileNotFoundError:
        print(f"File '{input_csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def file_input(prompt, extension):
    file_path = input(f'\n{prompt}\n').strip()
    if os.path.isfile(file_path) and file_path.endswith(extension):
        return file_path
    print(f"Either file not found or invalid file extension. Try again.")
    time.sleep(1)
    return file_input(prompt, extension)

def main():
    print(f'A program for updating strings for new files by veydzh3r.\nBefore using, it is recommended to read the instructions in the "ReadMe" file\n')
    
    data_csv_file = file_input('1. Enter a .csv file from which the translated strings will be taken (e.g, Game.csv): ', '.csv')
    input_csv_file = file_input('2. Enter a .csv file with new added strings (e.g. Game_New.csv): ', '.csv')
    output_csv_file = input('3. Enter a name for the new .csv file (e.g, Game_Output.csv): ').strip()

    replacement_data = load_replacement_data(data_csv_file)
    if replacement_data is not None:
        replace_strings_in_csv(input_csv_file, output_csv_file, replacement_data)

if __name__ == '__main__':
    main()
