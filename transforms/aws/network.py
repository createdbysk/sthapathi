def apply_transform(configuration_parameters):
    """
    GIVEN configuration parameters does not have enable_dns_support
    WHEN apply_transform runs on the configuration parameters
    THEN the result has enable_dns_support set to True
    :param configuration_parameters: The configuration parameters
    """
    if not configuration_parameters.has_key('enable_dns_support'):
        result = configuration_parameters.copy()
        result['enable_dns_support'] = True
    else:
        result = configuration_parameters
    return result

