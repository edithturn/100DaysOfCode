def format_name(f_name, l_name):
    """Take the firts and last name and format it to return 
    the title of the complete name """
    if f_name == "" or  l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return formated_f_name + " " + formated_l_name


print(format_name("edi", "asdsa"))


