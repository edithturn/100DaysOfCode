def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

name1 = "edith"
last_name1 = "puclla"

name2 = "EDiTh"
last_name2 = "PUCLLA"

format_name(f_name = name1, l_name = last_name2)
format_name(f_name = name2, l_name = last_name2)
