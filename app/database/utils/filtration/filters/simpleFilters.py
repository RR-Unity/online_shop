from sqlalchemy import and_, not_

from app.database.utils.filtration.absFilters import Filter, FilterWithTwoFields, FilterWithTwoValues


class AccurateFilter(Filter):
    def execute(self, where: list):
        if self:
            where.append(self.model_field == self.filter_value)
        return where


class BoolAccurateFilter(FilterWithTwoFields):
    def execute(self, where: list):
        match self.filter_value:
            case True:
                where.append(self.model_field == self.extra_value)
            case False:
                where.append(self.model_field != self.extra_value)
        return where


class IntegerFromFilter(Filter):
    def execute(self, where: list):
        if self:
            where.append(self.model_field >= self.filter_value)
        return where


class IsAnyFilter(Filter):
    def execute(self, where: list):
        if self.filter_value is True:
            where.append(self.model_field.any())
        if self.filter_value is False:
            where.append(not_(self.model_field.any()))
        return where


class IntegerToFilter(Filter):
    def execute(self, where: list):
        if self:
            where.append(self.model_field <= self.filter_value)
        return where


class IntegerInPeriodFilter(FilterWithTwoFields):
    def execute(self, where: list):
        if self:
            where.append(and_(
                self.model_field <= self.filter_value,
                self.extra_value >= self.filter_value,
            ))
        return where


class DateInPeriodFilter(FilterWithTwoValues):
    def execute(self, where: list):
        if self.filter_value_from and self.filter_value_to:
            where.append(and_(
                self.model_field >= self.filter_value_from,
                self.model_field <= self.filter_value_to,
            ))
        return where


class BoolFilter(Filter):
    def execute(self, where: list):
        if self.filter_value is not None:
            if self.filter_value:
                where.append(self.model_field.is_(True))
            else:
                where.append(self.model_field.is_(False))
        return where


class HasFilter(Filter):
    def execute(self, where: list):
        if self.filter_value is not None:
            if self.filter_value:
                where.append(self.model_field.is_not(None))
            else:
                where.append(self.model_field.is_(None))
        return where


class LikeFilter(Filter):
    def execute(self, where: list):
        if self:
            where.append(
                self.model_field.ilike(
                    f'%{self.filter_value}%',
                ),
            )
        return where
