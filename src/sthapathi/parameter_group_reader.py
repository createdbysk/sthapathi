def read(path):
    """
    Returns a dictionary of parameter groups
    :param path: The root of the path.
    """
    import os
    import yaml

    all_parameter_groups = {}
    for dir_name, sub_dir_list, file_list in os.walk(path):
        for filename in file_list:
            name, extension = os.path.splitext(filename)
            if extension == ".yaml":
                filepath = os.path.join(dir_name, filename)
                with open(filepath, 'r') as stream:
                    document = yaml.load_all(stream)
                    for parameter_groups in document:
                        all_parameter_groups.update(parameter_groups)

    return all_parameter_groups
