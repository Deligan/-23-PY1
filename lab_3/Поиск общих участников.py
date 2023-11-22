participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
list_1 = participants_first_group.split("|")
list_2 = participants_second_group.split("|")
# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result
print(sorted(find_common_elements(list_1,list_2)))
