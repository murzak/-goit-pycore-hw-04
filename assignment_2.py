def get_cats_info(path: str) -> list:
    # Initiate an array for all cats available in file passed
    cats = []
    try:
        # Open file in read mode
        with open(path, 'r') as f:
            # Get all lines from the file
            lines = f.readlines()
            # Loop through all the lines
            for line in lines:
                # Get id, name, age splitted by ',' delimiter
                id_, name, age = line.split(',')

                # Append a dictionary to cats array. 
                # Since each line but the last one ends with '\n', we'd need to incorporate removing those signs
                cats.append({'id': id_, 'name': name, 'age': age.replace('\n', '')})
        return cats
    except FileNotFoundError:
        print(f'There is no such file as {path}')

    except UnicodeDecodeError:
        print(f"Cannot read {path} due to encoding issue")
        return None

    except OSError as e:
        print(f"There has been another issue {e} while working with {path}")

print(get_cats_info('text_2.txt'))
