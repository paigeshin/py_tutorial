def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title() # title(): abc => Abc
    return f"{formatted_f_name} {formatted_l_name}"

result = format_name("Paige", "Shin")
print(result)