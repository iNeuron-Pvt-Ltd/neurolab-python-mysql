def get_data(file_path):
    with open(file_path) as file_in:
        data = []
    
        for line in file_in:
             data.append(line.rstrip("\n"))
    return data    