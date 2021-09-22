from unidecode import unidecode

def clean_column_names(columns):
    clean_columns = []
    for col in columns:
        clean_columns.append(
            unidecode(col)\
               .strip()\
               .lower()\
               .replace('.', '')\
               .replace(' - ', '_')\
               .replace('/', '_')\
               .replace(' ', '_')
        )
    
    return clean_columns