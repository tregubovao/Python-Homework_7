def import_mod(surname):
    res_list = []
    with open('catalog.txt', 'r', encoding='utf-8') as file:        
        while True:                         
            line = file.readline()
            if not line:
                if not file.readline():                
                    break
            if line.rstrip() == surname:
                res_list.append(surname)
                for i in range(1, 4):
                    res_list.append(file.readline().rstrip()                    )
                res_list.append('')
    if len(res_list) > 0:
        return res_list
    return 'Таких людей не найдено'

def export_mod(data_list):        
    with open('catalog.txt', 'a', encoding='utf-8') as file:
        file.write(f' \n')
        for el in data_list:            
            file.write(el + '\n')    
