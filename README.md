# sthapathi
Use a provider agnostic description to build and launch infrastructure.

# configuration syntax
Yaml file with the following format

- variable: variable_name
- type: element_type
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
