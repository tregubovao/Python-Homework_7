import datetime

def log_cash(result_search, choose_mod):
    rs = result_search
    n = int(len(rs) / 5)    # 5 в данном случае минимальная длина списка, в случае однофамильцев длина списка будет кратна 5
    cm = choose_mod
    with open('log.txt', 'a', encoding='utf-8') as file:
        k = 0
        for i in range (1, n + 1):            
            file.write(f'{datetime.datetime.now()} Режим: {cm} Субъект: {rs[0 + k]} {rs[1 + k]} Телефон: {rs[2 + k]} Тип: {rs[3 + k]} \n')
            k += 5