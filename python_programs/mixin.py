"""

A mixin is a class that provides method implementations for reuse by multiple related child classes. However, the inheritance is not implying an is-a relationship.
A mixin doesn’t define a new type. Therefore, it is not intended for direction instantiation.
A mixin bundles a set of methods for reuse. Each mixin should have a single specific behavior, implementing closely related methods.

"""

import json
from pprint import pprint


class DictMixin:

    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes):
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict())


class Person:
    def __init__(self, name):
        self.name = name


class Employee(DictMixin, JSONMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


if __name__ == '__main__':
    e = Employee(
        name='John',
        skills=['Python Programming''Project Management'],
        dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']}
    )

    #pprint(e.to_dict())
    print(e.to_json())
