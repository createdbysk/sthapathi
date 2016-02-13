# Sthapathi
Use a provider agnostic description to build and launch infrastructure.
## Why sthapathi
Sthapathi is the sanskrit word that means "Master Builder". I envision this application as the master builder for any 
data center.

# YAML Syntax
    Name_Of_The_Resource
    - Resource_Type
    - Property_Name_1: Property_Value_1
      Property_Name_2: Property_Value_2

# Development
## Transforms
Apply transforms to template parameters to generate the configuration from the templates when the templates do not 
provide some functionality required to generate the correct configuration. 

### Example
The template to generate the aws network terraform configuration is as follows

    {
        "resource": {
            "aws_vpc": {
                "{{name}}": {
                    {{! Put section begin and end on their own line. This causes the following to NOT render
                        an empty line for . }}
                    {{^enable_dns_support}}
                    "enable_dns_support": false,
                    {{/enable_dns_support}}
                    {{#enable_dns_names}}
                    "enable_dns_names": true,
                    {{/enable_dns_names}}
                    "cidr_block": "{{cidr_block}}"
                }
            }
        }
    }

enable_dns_support has a default value of true. Therefore, the following requirements apply to that scenario.

    GIVEN configuration parameters does not have enable_dns_support
    WHEN apply_transform runs on the configuration parameters
    THEN the result has enable_dns_support set to True

    GIVEN configuration parameters has enable_dns_support
    WHEN apply_transform runs on the configuration parameters
    THEN enable_dns_support is unchanged

The template defines the enable_dns_support portion of the configuration as follows.
  
    {{^enable_dns_support}}
    "enable_dns_support": false,
    {{/enable_dns_support}}
    
This means that if ```enable_dns_support``` is falsy, then it will appear in the configuration with a value of 
```false```. If enable_dns_support does not appear in the input configuration, as shown below, 
the intent is that the value of enable_dns_support should be True. 

    main_network:
      - network
      - cidr_block: 10.100.0.0/16

However, the lack of ```enable_dns_support``` in the input configuration makes that value Falsy 
and it will appear as ```false``` in the output configuration as well unless its value is set to the default ```True``` 
in the input configuration. ```transforms/aws/network.py``` defines this transform, shown below.

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

 
# References
## Template Engine
Use [mustache](http://mustache.github.io/mustache.5.html) template engine because it is logicless, similar to terraform 
templates.
