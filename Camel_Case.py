def to_camel_case(text):

    transform = text
    nueva_cadena = ""
    convertirmayus = True

    for caracter in transform:
        if convertirmayus:
            nueva_cadena += caracter.upper()
            convertirmayus = False
        elif caracter in "_-":
            nueva_cadena += caracter
            convertirmayus = True
        else:
            nueva_cadena += caracter
            transform = nueva_cadena
    if text[0] == text[0].lower():
        transform = transform[0].lower() + transform[1:]
    if transform.find("-" or "_"):
        transform = transform.replace("-", "").replace("_", "")

        return transform 
