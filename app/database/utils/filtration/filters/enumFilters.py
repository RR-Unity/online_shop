from app.database.utils.filtration.absFilters import Filter


class EnumFilter(Filter):
    def execute(self, where: list):
        if self.filter_value is not None:
            where.append(self.model_field == self.filter_value.value)
        return where


class ExcludeEnumTypesFilter(Filter):
    def execute(self, where: list):
        if self.filter_value:
            where.append(self.model_field.not_in(self.filter_value))

        return where
