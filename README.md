# sthapathi
Use a provider agnostic description to build and launch infrastructure.

# Usage Guide
## Catalog
The catalog is a yaml file that provides a mapping between the elements in the configuration and the terraform modules that they translate 
to for different providers.

    providers:
        provider_name:
            element_one: 
                source: ./modules/element_one
                argument_groups: 
                - argument_group_name1
                - argument_group_name2
                arguments:
                - argument_name11
                - argument_name12
            element_two: 
                source: git::ssh://git.url/path/to/module/in/git
                arguments:
                - argument_name21
                - argument_name22
                - argument_name23                
    argument_groups:
        argument_group_name1: 
            arguments:
            - argument_name31
            - argument_name32
            inherits:
            - argument_group_name3
        argument_group_name2:
            - argument_name41
            - argument_name42
            - argument_name43
        argument_group_name3:
        - argument_name51

# For Developers
## Testing
Uses [tox](https://tox.readthedocs.io/en/latest/index.html) to seamlessly test installation rather than source. Install tox as follows.

    virtualenv venv
    . venv/bin/activate
    pip install tox
    
## Testing from Pycharm IDE
Follow instructions [here](https://www.jetbrains.com/help/pycharm/tox-support.html).
    
    

