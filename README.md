# PythonReview1

Это проект для кодирования информации с помощью шифра Цезаря, Виженера и Вернама

Также с помощью команды hack проект умеет взламывать шифры Цезаря и Виженера при помощи частотного анализа.
Для этого нужно обучить систему с помощью команд train, если у вас большой текст или с помощью
команды train-short для дешифровки небольших текстов закодированных шифром Цезаря (в этом случае шанс дешифровки сильно понижается)

### Usage:

**encode** - закодировать с помощью выбраного шифра и ключа

main.py encode --cipher {caesar,vigenere,vernam} --key KEY
               [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
               
**decode** - раскодировать с помощью выбраного шифра и ключа

main.py decode --cipher {caesar,vigenere,vernam} --key KEY
               [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
               
**train** - подготовить систему к взлому файла с помощью hack
 
main.py train [--text-file TEXT_FILE] --model-file MODEL_FILE

**hack** - взломать текст зашифрованный шифром Цезаря или Виженера 

main.py hack --cipher {caesar,vigenere} [--input-file INPUT_FILE]
               [--output-file OUTPUT_FILE] --model-file MODEL_FILE

**train-short** - подготовить систему к взлому небольшого файла с помощью hack-short

main.py train-short [--text-file TEXT_FILE] --model-file MODEL_FILE -N N

**hack-short** - взломать маленький текст зашифрованный шифром Цезаря 

main.py hack-short [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
               --model-file MODEL_FILE
