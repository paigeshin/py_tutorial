def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title() # title(): abc => Abc
    return f"{formatted_f_name} {formatted_l_name}"

result = format_name(input("What is your first name?"), input("What is your last name?"))
print(result)