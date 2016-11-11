import re


class JsonHelper:
    first_cap_re = re.compile('(.)([A-Z][a-z]+)')
    all_cap_re = re.compile('([a-z0-9])([A-Z])')

    @staticmethod
    def camel_to_underscore(name):
        s1 = JsonHelper.first_cap_re.sub(r'\1_\2', name)
        return JsonHelper.all_cap_re.sub(r'\1_\2', s1).lower()

