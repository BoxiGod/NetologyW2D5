from pprint import pprint
import re

import csv
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

pattern = re.compile(r"\s([А-я]*)?[\s|,]?([А-я]*)?[\s|,]?([А-я]*)?,*([А-я]{3,6})?,"
                     r"?([^,+8@I]*)?,?(\+?7?8?)\s?\(?([0-9]{3})?"
                     r"\)?\s?-?([0-9]{3})?-?([0-9]{2})?-?([0-9]{2})?,? ?\(?(доб. ?([0-9]{4}))?\)?,?(\w*.?\w*@\w*.ru)?")

text = pattern.sub(r'')


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
