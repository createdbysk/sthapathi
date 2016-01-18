import pystache

template = """Before Key
{{#key}}
key was {{key}}.
{{/key}}
Before not defined key
{{^key}}key was not defined.{{/key}}"""

# If key is defined then the result will be "key was defined"
print pystache.render(template, {"key": "defined"})

# If key is not defined, the result will be ''key as not defined."
print pystache.render(template, {})
