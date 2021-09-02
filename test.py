def make(category_name, file_name, file_path):
    cat = 0
    name = 0
    path = 0
    for c in category_name:
        cat += ord(c)
    for c in file_name:
        name += ord(c)
    for c in file_path:
        path += ord(c)

    id = str(cat) + str(name) + str(path)
    id = int(id)
    
    print(type(id))

make("test", "file", "C://user/whatever")