def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    all_attributes = dir(obj)

    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in all_attributes if callable(getattr(obj, method)) and not method.startswith('__')]

    info['module'] = getattr(obj, '__module__', 'Built-in')

    info['attributes'] = attributes
    info['methods'] = methods

    return info


number_info = introspection_info(42)
print(number_info)
