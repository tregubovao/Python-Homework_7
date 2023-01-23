import view
import operation_im_ex
import mod_process
import log

def button_click():
    mod = view.inp_mod()
    choose_mod = mod_process.processing(mod)
    if choose_mod.lower() == 'им':
        surname = view.inp_import()
        result_search = operation_im_ex.import_mod(surname)
        if isinstance(result_search, str):
            view.view_import_no()
        else:
            view.view_import(result_search)
            log.log_cash(result_search, choose_mod)


    elif choose_mod == 'эк':
        data_list = view.inp_export()
        operation_im_ex.export_mod(data_list)
        data_list.append(' ')
        log.log_cash(data_list, choose_mod)
        view.view_export()

    else: print('Введен некорректный режим. Перезапустите программу и повторите ввод')
        
