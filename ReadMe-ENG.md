A simple program for inserting translated strings from a `.locres` file with old strings into an updated `.locres` file with new strings.
<br>[Click to download a ZIP program archive file](<https://github.com/Veydzher/ReplacerLocres/archive/refs/heads/main.zip>)

<b>Usage</b>
1. Export all text to a `.csv` file from the old `.locres` file using UE4LocalisationTool (Tool -> Export all text -> CSV file).
2. Repeat as in step 1, but with a new file, and add `_New` to the file name before exporting.
3. Double-click on the file `Replacer-ENG.py` and follow the program instructions.
4. Once the program has created a new `.csv` file, open the `.locres` file with the new strings, and import new `.csv` file using UE4LocalisationTool (Tool -> Import all text).
