import datetime

from app.database.utils.filtration.absFilters import Filter


class DateFromFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field >= self.filter_value)
        return where


class DateToDateFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field <= self.filter_value)
        return where


class DateToDatetimeFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field <= self.filter_value + datetime.timedelta(days=1))
        return where


class CertainDateFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field == self.filter_value)
        return where


class DatetimeFromFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field >= self.filter_value)
        return where


class DatetimeToFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field <= self.filter_value)
        return where
