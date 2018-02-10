# sthapathi
Use a provider agnostic description to build and launch infrastructure.

# Parameter group syntax

parameter_group_name:
	variables:
	- variable1
	- variable2: ${var.variable2_value}
	- variable3
	inherits:
	- base_parameter_group_name
	
* default is a special parameter_group_name and is available even when not specified.
* if base_parameter_group_name is not specified, then the parameter group inherits from default. The exception to 
  this rule is the default parameter group.

# configuration syntax
Yaml file with the following format

- variable: variable_name
- module: module_name1
  name: name for the element in the target configuration
  parameters:
    parameter_name: paramater_value
    # Optional
    group: parameter_group_name 
  # If group is specified, then all the elements below automatically inherit the parameters from that the parameter
  # group
- group: 
  parameter_group_name: parameter-group-name
  elements:
  - module: module_name2
    name: name for the element in the target configuration
    parameters:
      parameter_name: paramater_value
      # Optional
      group: parameter_group_name 
  	
* you can create custom parameter groups.
* If group is specified under parameters, then parameters automatically includes variables defined by that group.
	* any parameters specified explicitly will override the value of the parameters specified through the group.
* If no group is specified, the group name is assumed to be default.
* Variables that are part of parameter groups are automatically declared.
* use variable to declare variables that are NOT part of the parameter groups.
