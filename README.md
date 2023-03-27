# Описание программы cheker.exe

Данная программа предназначена для сравнения двух файлов с текстом и выявления различий между ними. 

### Использование

Для работы программы необходимо подготовить два файла с текстом: `data.txt` и `old.txt`. Файл `data.txt` должен содержать последнюю версию текста, а файл `old.txt` - предыдущую версию. 

Для подготовки файлов локализации игры можно воспользоваться утилитой [EasyTranslateCraftopia](https://github.com/asidsx/EasyTranslateCraftopia), которая автоматически выгружает текст из игры.

Затем необходимо скопировать исполняемый файл `cheker.exe` в папку с файлами `data.txt` и `old.txt` и запустить его. После выполнения программы будет создан файл `error.txt`, в котором будут указаны новые строки и измененные строки из файла `data.txt`.

### Пример использования

1. Выгрузить последнюю версию локализации игры orig.txt с помощью утилиты EasyTranslateCraftopia и переименуйте ее в файл `data.txt`.
2. Скопировать старый файл `orig.txt` с прошлого патча Craftopia в туже папку, переименовать его в `old.txt`.
3. Скопировать исполняемый файл `cheker.exe` в эту же папку.
4. Запустить программу `cheker.exe`.
5. В файле `error.txt` будут указаны новые строки и измененные строки из файла `data.txt`.


<hr>

# Description of the cheker.exe program

This program is designed to compare two text files and identify differences between them.

### Usage

To use the program, you need to prepare two text files: `data.txt` and `old.txt`. The `data.txt` file should contain the latest version of the text, and the `old.txt` file should contain the previous version.

To prepare localization files for the game, you can use the [EasyTranslateCraftopia](https://github.com/asidsx/EasyTranslateCraftopia) utility, which automatically extracts text from the game.

Then copy the executable file `cheker.exe` to the folder with the `data.txt` and `old.txt` files and run it. After the program is executed, a `error.txt` file will be created, which will indicate new and modified lines from the `data.txt` file.

### Usage example

1. Extract the latest version of the game localization orig.txt using the EasyTranslateCraftopia utility and rename it to `data.txt`.
2. Copy the old `orig.txt` file from the previous Craftopia patch to the same folder, rename it to `old.txt`.
3. Copy the executable file `cheker.exe` to the same folder.
4. Run the `cheker.exe` program.
5. The `error.txt` file will indicate new and modified lines from the `data.txt` file.
