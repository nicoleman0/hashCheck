import hashlib

def calculate_hash(filepath, hash_algorithm='sha256'):
    """
    Calculate the hash of a file using the specified algorithm.

    Args:
        filepath (str): The path to the file.
        hash_algorithm (str): The algorithm to use. Default is 'sha256'.

    Returns:
        str: The hash of the file.
    """
    if hash_algorithm.lower() == 'md5':
        hash_func = hashlib.md5()
    elif hash_algorithm.lower() == 'sha1':
        hash_func = hashlib.sha1()
    elif hash_algorithm.lower() == 'sha256':
        hash_func = hashlib.sha256()
    else:
        raise ValueError('Invalid hash algorithm.')
    
    # Read the file in binary mode
    with open(filepath, 'rb') as f:
        segment = f.read(4096)
        while segment:
            hash_func.update(segment)
            segment = f.read(4096)

    # Return the hexadecimal representation of the hash
    return hash_func.hexdigest()