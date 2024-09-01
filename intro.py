import inspect
import pprint


def introspection_info(obj):
    info = {'тип':type(obj),
            'атрибуты':[a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj,a))],
            'методы':[m for m in dir(obj) if m.startswith('__')],
            'модуль':inspect.getmodule(introspection_info)}
    return info


number_info = introspection_info(42)
pprint.pprint(number_info)
