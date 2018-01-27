def read_configuration(path):
    import os
    import yaml

    for dir_name, sub_dir_list, file_list in os.walk(path):
        for filename in file_list:
            name, extension = os.path.splitext(filename)
            if extension == ".yaml":
                filepath = os.path.join(dir_name, filename)
                with open(filepath, 'r') as stream:
                    document = yaml.load_all(stream)
                    for elements in document:
                        for element in elements:
                            yield element