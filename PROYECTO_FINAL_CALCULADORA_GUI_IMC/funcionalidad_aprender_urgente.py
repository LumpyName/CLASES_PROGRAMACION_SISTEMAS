import os

if __name__ == "__main__":
    from fontTools.ttLib import TTFont

    directorio = "fuentes_ttf"  # ajusta si lo ejecutas desde otro lugar

    for archivo in os.listdir(directorio):
        if archivo.lower().endswith(".ttf"):
            ruta = os.path.join(directorio, archivo)
            font = TTFont(ruta)
            name = font['name']
            for record in name.names:
                if record.nameID == 1:  # 1 = Font Family name
                    try:
                        nombre = record.string.decode(record.getEncoding())
                        print(f"{archivo} => '{nombre}'")
                    except:
                        pass
