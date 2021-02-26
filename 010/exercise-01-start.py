def format_name(f_name, l_name):
    if f_name == "" or  l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return formated_f_name + " " + formated_l_name

name1 = "edith"
last_name1 = "puclla"

name2 = "EDiTh"
last_name2 = "PUCLLA"

print(format_name(f_name = name1, l_name = last_name2))
print(format_name(f_name = name2, l_name = last_name2))

output = len(format_name(f_name = name2, l_name = last_name2))
print(output)

print(format_name(input("What is your first name? "), input("What is your last name? ")))
