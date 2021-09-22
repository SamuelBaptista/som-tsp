from unidecode import unidecode
import numpy as np

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


def euclidean_distance(a, b):
    """Return the array of distances of two numpy arrays of points."""
    return np.linalg.norm(a - b, axis=1)