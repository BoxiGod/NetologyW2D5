from pprint import pprint
import re
import csv


def find_and_replace_same(name, surname, reged_list, start):
    for count, line in enumerate(reged_list[start + 1:], start + 1):
        if line[0] == name and line[1] == surname:
            for i, value in enumerate(line, 0):
                if len(value) > len(reged_list[start][i]):
                    reged_list[start][i] = value
            return count


def main():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        before_reg = ""
        for line in f:
            before_reg += line

    pattern = re.compile(r"\s([А-я]*)?[\s|,]?([А-я]*)?[\s|,]?([А-я]*)?,*([А-я]{3,6})?,"
                         r"?([^,+8@I]*)?,?(\+?7?8?)\s?\(?([0-9]{3})?"
                         r"\)?\s?-?([0-9]{3})?-?([0-9]{2})?-?([0-9]{2})?,? ?\(?((доб.) ?([0-9]{4})\)?)?,?(\w*.?\w*@\w*.ru)?")
    text = pattern.sub('\n' + r'\1,\2,\3,\4,\5,\6(\7)\8\9\10 \12 \13,\14', before_reg)
    split_text = text.split('\n')
    reged_list = [x.split(',') for x in split_text]
    delete_indexes = []
    for i, line in enumerate(reged_list[1:], 1):
        index = find_and_replace_same(line[0], line[1], reged_list, i)
        if index:
            delete_indexes.append(index - len(delete_indexes))
    for index in delete_indexes:
        if index:
            reged_list.pop(index)

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(reged_list)


if __name__ == '__main__':
    main()
