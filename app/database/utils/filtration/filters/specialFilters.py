from app.database.utils.filtration.absFilters import Filter, SubqueryFilter
from sqlalchemy import or_, cast, String
from sqlalchemy.sql.elements import BooleanClauseList


class AssignedFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            if self.filter_value.value == 'assigned':
                where.append(self.model_field.is_not(None))

            if self.filter_value.value == 'unassigned':
                where.append(self.model_field.is_(None))

        return where


class BoolUnassignedFilter(Filter):
    def execute(self, where: list):
        if self:
            if self.filter_value:
                where.append(self.model_field.is_(None))
            else:
                where.append(self.model_field.is_not(None))

        return where


class ShowSoftDeleteFilter(Filter):
    def execute(self, where: list):
        if self.filter_value is not None \
                and not self.filter_value:  # noqa: WPS318, WPS337

            where.append(self.model_field.is_(None))

        return where


class InFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field.in_(self.filter_value))

        return where


class NotInFilter(Filter):
    def execute(self, where: list):
        if self:
            where.append(self.model_field.not_in(self.filter_value))

        return where


class SubqueryInBoolFilter(SubqueryFilter):
    def execute(self, where: list):
        if self:
            if self.filter_value:
                where.append(self.entity_field.in_(self.subquery))
            else:
                where.append(self.entity_field.not_in(self.subquery))

        return where
