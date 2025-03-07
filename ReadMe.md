Простенька програма для вставлення перекладених рядків з файлу `.locres` із старими рядками, в оновлений файл `.locres` з новими рядками.
<br>[Натисніть для завантаження ZIP файлу програми](<https://github.com/Veydzher/ReplacerLocres/archive/refs/heads/main.zip>)

<b>Інструкції з використання</b>
1. Експортуйте весь текст у файл `.csv` зі старого файлу `.locres` за допомогою UE4LocalizationTool (Tool -> Export all text -> CSV file).
2. Так само повторіть як у пункті 1, тільки вже з новим файлом, і додайте до назви `_New` перед експортом.
3. Двічі клацніть на файл `Replacer.py`, і слідуйте за вказівками програми.
4. Після того, як програма створила новий файл `.csv`, ви відкриваєте файл `.locres` з новими рядками, та імпортовуєте той новий файл `.csv` за допомогою UE4LocalizationTool (Tool -> Import all text).
