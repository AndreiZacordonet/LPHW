import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()    # strips all the whitespaces if arent any params
    # raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = next_lang.decode(encoding, errors=errors)

    print(next_lang, "<===>", cooked_string)


languages = open("languages.txt", 'rb')#, encoding="utf-8")

main(languages, input_encoding, error)

languages.close()
