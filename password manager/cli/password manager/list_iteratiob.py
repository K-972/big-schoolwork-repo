password_list = []

def GetAndDecryptDictionaryFile(password_list):
    try:
        with open('dictionary.txt', 'r') as dictionary:
            dimension_list_counter = -1
            int(dimension_list_counter)
            lines = dictionary.readlines()
            for line in lines:
                dimension_list_counter += 1
                line = (line.strip().split('|'))
                password_list.append(line[0])
                for value in line[1: ]:

                    print(value)
        print(password_list)







    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
        return None

GetAndDecryptDictionaryFile(password_list)