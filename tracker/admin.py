import inspect, sys
from django.contrib import admin

def register_all_models(module):
    for name, obj in inspect.getmembers(sys.modules[module]):
        if inspect.isclass(obj) and obj.__name__ is not "User":
            if hasattr(obj, "_meta") and not obj._meta.abstract:
                admin.site.register(obj)

register_all_models("tracker.models")
