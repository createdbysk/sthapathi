class Plugin(object):
    __PARAMETER_GROUP_NAME_LABEL = "parameter_group"

    class Error(Exception):
        def __init__(self, msg):
            super(Exception, self).__init__(msg)

    def __init__(self):
        pass

    def build_parameters(self, parameters, parameter_groups, active_parameter_group):
        """
        Returns the dictionary of parameters that includes inherited parameters.
        :param active_parameter_group:
        :param parameters: The parameters in the configuration. This may inherit from other parameter_groups.
        :param parameter_groups: The parameter groups.
        :return: The dictionary of parameters that include the inherited parameters.
        """

        parameters_to_return = {}
        self.__append_inherited_parameters(parameters_to_return, parameter_groups,
                                           parameters.get(Plugin.__PARAMETER_GROUP_NAME_LABEL,
                                                          active_parameter_group))

        parameters_to_return.update(parameters)
        if Plugin.__PARAMETER_GROUP_NAME_LABEL in parameters_to_return:
            del parameters_to_return[Plugin.__PARAMETER_GROUP_NAME_LABEL]

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
            def get_default_parameter_value(parameter_name):
                return "${{var.{parameter}}}".format(parameter=parameter_name)
            if type(parameter) is dict:
                name_of_parameter = parameter.keys()[0]
                parameters.update({name_of_parameter:
                                       parameter[name_of_parameter].get("value",
                                                                        get_default_parameter_value(name_of_parameter))
                                   })
            else:
                parameters.update({
                    parameter: get_default_parameter_value(parameter)
                })
