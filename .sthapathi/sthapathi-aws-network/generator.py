def generate(name, parameters, module_name):
    module = {
        "source": "./modules/{}".format(module_name),
        "name": name
    }

    module.update(parameters)
    output = {
        "module": {
            name: module
        }
    }

    return output