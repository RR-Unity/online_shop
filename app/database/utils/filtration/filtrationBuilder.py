from app.database.utils.filtration.absFilters import FilterAbstract


class FiltrationBuilder(object):
    def __init__(self, where_conditions: list = None):
        self.filters_list: list[FilterAbstract] = []
        self.pre_conditions = where_conditions if where_conditions else []

    def get_conditions(self):
        where_conditions = self.pre_conditions
        for sql_filter in self.filters_list:
            sql_filter.execute(where_conditions)

        return where_conditions

    def add_filter(self, element: FilterAbstract):
        self.filters_list.append(element)

    def get_str_executed_conditions(self):
        str_where = []
        for sql_filter in self.filters_list:
            if sql_filter:
                str_where.append(str(sql_filter))
        return str_where

    def __bool__(self):
        return bool(self.filters_list)

    def __str__(self):
        return f'<FiltrationBuilder with {len(self.pre_conditions) + len(self.filters_list)} elements of list ' \
            f'and {len(self.get_str_executed_conditions())} of them executed>'  # noqa: WPS326
