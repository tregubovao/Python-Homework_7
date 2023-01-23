def inp_mod():
    mod = input('Введите режим работы: импорт(ИМ) или экспорт(ЭК): \n')
    return mod


def inp_import():
    surname = input('Введите фамилия для поиска: ')
    return surname


def inp_export():
    surname = input('Введите фамилию для загрузки в справочник: ')
    name = input('Введите имя для загрузки в справочник: ')
    phone_number = input('Введите № телефона для загрузки в справочник: ')
    number_type = input('Введите тип телефона для загрузки в справочник: ')
    data_list = []
    # data_list.append(surname)
    # data_list.append(name)
    # data_list.append(phone_number)
    # data_list.append(number_type)
    data_list = [surname, name, phone_number, number_type]
    return data_list

def view_import(result):
    print(*result, sep='\n')


def view_export():
    print(f'Введенные данные успешно сохранены')
    
def view_import_no():
    print(f'Данные не найдены')