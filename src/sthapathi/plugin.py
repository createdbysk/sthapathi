class Plugin(object):
    class Error(Exception):
        def __init__(self, msg):
            super(Exception, self).__init__(msg)

    def __init__(self):
        pass

    def build_parameters(self, parameters, parameter_groups):
        """
        Returns the dictionary of parameters that includes inherited parameters.
        :param parameters: The parameters in the configuration. This may inherit from other parameter_groups.
        :param parameter_groups: The parameter groups.
        :return: The dictionary of parameters that include the inherited parameters.
        """

        parameters_to_return = {}
        self.__append_inherited_parameters(parameters_to_return, parameter_groups,
                                           parameters.get("parameter_group", "default"))

        parameters_to_return.update(parameters)
        if "group" in parameters_to_return:
            del parameters_to_return["group"]

        return parameters_to_return

    def __append_inherited_parameters(self, parameters, parameter_groups, parameter_group_name):
        """
        Updates parameters with the parameters in the specified parameter_group and the parameter groups it inherits
        from in the given collection of parameter_groups.
        :param parameters: The parameters to update
        :param parameter_groups: The collection of all parameters groups
        :param parameter_group_name: The parameter group to choose from the parameter_groups to update parameters.
        """

        if parameter_group_name not in parameter_groups:
            raise Plugin.Error("{parameter_group_name} not found in parameter groups".format(
                parameter_group_name=parameter_group_name))

        parameter_group = parameter_groups[parameter_group_name]

        if "variables" not in parameter_group:
            raise Plugin.Error("variables not found in parameter group {parameter_group_name}".format(
                parameter_group_name=parameter_group_name
            ))

        if parameter_group_name != "default":
            if "inherit" in parameter_group:
                inherited_parameter_group_name = parameter_group["inherit"]
                self.__append_inherited_parameters(parameters, parameter_groups, inherited_parameter_group_name)
            else:
                # Always inherit from default
                self.__append_inherited_parameters(parameters, parameter_groups, "default")

        for parameter in parameter_group["variables"]:
            if type(parameter) is dict:
                parameters.update(parameter)
            else:
                parameters.update({
                    parameter: "${{var.{parameter}}}".format(parameter=parameter)
                })
