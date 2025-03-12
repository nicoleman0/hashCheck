import hashlib

def calculate_hash(filepath, algorithm='sha256'):
    """
    Calculate the hash of a file using the specified algorithm.

    Args:
        filepath (str): Path to the file.
        hash_algorithm (str): The algorithm to use. Default is 'sha256'.

    Returns:
        str: The hash of the file.
    """
    if algorithm.lower() == 'md5':
        hash_func = hashlib.md5()
    elif algorithm.lower() == 'sha1':
        hash_func = hashlib.sha1()
    elif algorithm.lower() == 'sha256':
        hash_func = hashlib.sha256()
    else:
        raise ValueError('Invalid hash algorithm. Please use "md5", "sha1", or "sha256".')
    
    # Read the file in binary mode
    with open(filepath, 'rb') as f:
        segment = f.read(4096)
        while segment:
            hash_func.update(segment)
            segment = f.read(4096)

    # Return the hexadecimal representation of the hash
    return hash_func.hexdigest()

def checker():
    """
    Main function to run the hash checker.
    """
    filepath = input('Enter the path to the file: ')
    algorithm = input('Enter the hash algorithm (md5, sha1, sha256): ')
    if not algorithm:
        algorithm = 'sha256'

    # Calculate the hash
    try:
        hash_value = calculate_hash(filepath, algorithm)
        print(f'The {algorithm.upper()} hash of the file is: {hash_value}')


        # Verify against a known hash
        verify = input('Do you want to verify the hash against a known value? (y/n): ')
        if verify.lower() == 'y':
            known_hash = input('Enter the known hash value: ')
            if known_hash == hash_value:
                print('The hash values match.')
            else:
                print('The hash values do not match.')

    except FileNotFoundError:
        print('File not found. Please check the file path.')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
    
if __name__ == '__main__':
    checker()