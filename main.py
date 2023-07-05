import csv
import re


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def list_correction(list_: list):
    phone_pattern = r"(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})\s*\(*(доб\.{1})?\s*(\d{4})?\)*"
    phone_pattern_correct = r"+7(\2)\3-\4-\5 \6\7"

    name_pattern = r"^(\w+)\s*(\,?)(\w+)\s*(\,?)(\w*)(\,?)(\,?)(\,?)"
    name_pattern_correct = r"\1\2\8\3\4\7\5\6"

    for n, i in enumerate(list_):
        list_join = ','.join(i)
        fixed_phone = re.sub(phone_pattern, phone_pattern_correct, list_join)
        fixed_phone_name = re.sub(name_pattern, name_pattern_correct, fixed_phone)
        correct = fixed_phone_name.split(',')
        list_[n] = correct

    return list_


def remove_duplicates(list_: list):
    list_ = sorted(list_)
    i = 0
    while i < len(list_) - 1:
        a = list_[i + 1]
        b = list_[i]
        if a[0] == b[0] and a[1] == b[1]:
            d = dict.fromkeys(a)
            d.update(dict.fromkeys(b))
            correct_list = list(d.keys())
            list_.remove(a)
            list_.remove(b)
            list_.append(correct_list)
        i += 1
    return list_


contacts_list = list_correction(contacts_list)
contacts_list = remove_duplicates(contacts_list)


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
