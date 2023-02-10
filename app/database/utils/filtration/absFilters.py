from abc import ABC, abstractmethod


class FilterAbstract(ABC):
    @abstractmethod
    def __init__(self, filter_value, model_field):
        self.model_field = model_field
        self.filter_value = filter_value

    @abstractmethod
    def execute(self, where: list):
        if self.filter_value:
            where.append('condition')
        return where

    @abstractmethod
    def __str__(self):
        pass  # noqa: WPS100

    def __bool__(self):
        return self.filter_value is not None


class Filter(FilterAbstract):
    def __init__(self, filter_value, model_field):
        self.filter_value = filter_value
        self.model_field = model_field

    @abstractmethod
    def execute(self, where: list):
        if self.filter_value:
            where.append('condition')
        return where

    def __str__(self):
        return f'{self.model_field} filtering by {self.filter_value}'


class SubqueryFilter(FilterAbstract):
    def __init__(self, filter_value, entity_field, subquery):
        self.filter_value = filter_value
        self.entity_field = entity_field
        self.subquery = subquery

    @abstractmethod
    def execute(self, where: list):
        if self.filter_value:
            where.append('condition')
        return where

    def __str__(self):
        return f'{self.model_field} filtering by {self.filter_value}'


class FilterWithTwoFields(FilterAbstract):
    def __init__(self, filter_value, model_field, extra_value):
        self.model_field = model_field
        self.extra_value = extra_value
        self.filter_value = filter_value

    @abstractmethod
    def execute(self, where: list):
        if self.filter_value:
            where.append('condition')
        return where

    def __str__(self):
        return f'{self.first_model_field}.{self.second_model_field} filtering by {self.filter_value}'


class FilterWithTwoValues(FilterAbstract):
    def __init__(self, filter_value_to, filter_value_from, model_field):
        self.model_field = model_field
        self.filter_value_to = filter_value_to
        self.filter_value_from = filter_value_from
        self.filter_value = True

    @abstractmethod
    def execute(self, where: list):
        if self.filter_value:
            where.append('condition')
        return where

    def __str__(self):
        return f'{self.first_model_field}.{self.second_model_field} filtering by {self.filter_value}'
