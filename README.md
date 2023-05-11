# Serial Number Generator

## Description

- The generator shall be controlled either via console or GUI.
- It should be possible to choose between different serial number types (e.g. only numbers, letters, length).
- With a button (GUI) or number (console) serial numbers can be generated.
- These are stored in a `.csv` file (`valid_numbers.csv`) line by line.
- The program offers the possibility to enter a serial number. Afterwards the program checks
by means of the file `valide_number.csv` whether the serial number is present there. If yes, `"Valid"` is output as text is displayed. If not, `"not Valid"` is displayed.
- If a serial number was classified as valid, the serial number is marked as used in the file.
in the file.
- If you try to enter an already used serial number, the message "already used" appears.

## The CSV

| Serial Number | Used |
| ------------- | ---- |
| 123456        | true |
| 123457        | false|
