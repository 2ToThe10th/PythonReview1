# PythonReview1
# Usage:
# There are 6 type of action:
##  encode
main.py encode --cipher {caesar,vigenere,vernam} --key KEY
               [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
## decode
main.py decode --cipher {caesar,vigenere,vernam} --key KEY
               [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
## train
main.py train [--text-file TEXT_FILE] --model-file MODEL_FILE
## hack
main.py hack --cipher {caesar,vigenere} [--input-file INPUT_FILE]
               [--output-file OUTPUT_FILE] --model-file MODEL_FILE
## train-short
main.py train-short [--text-file TEXT_FILE] --model-file MODEL_FILE -N N
## hack-short
Not implemented yet (At the seminar it was said that bonuses can be added to 2 packages)
