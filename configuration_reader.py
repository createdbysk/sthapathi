class ConfigurationReader(object):
    __TYPE_INDEX = 0
    __NAME_INDEX = 1
    __PARAMETERS_INDEX = 2

    @staticmethod
    def read_type(configuration_parameters):
        return configuration_parameters[ConfigurationReader.__TYPE_INDEX]

    @staticmethod
    def read_name(configuration_parameters):
        return configuration_parameters[ConfigurationReader.__NAME_INDEX]

    @staticmethod
    def read_parameters(configuration_parameters):
        return configuration_parameters[ConfigurationReader.__PARAMETERS_INDEX]
