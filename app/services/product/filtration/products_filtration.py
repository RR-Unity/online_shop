from app.database.entities.productEntity import ProductEntity
from app.database.utils.filtration.filters.simpleFilters import AccurateFilter
from app.database.utils.filtration.filtrationBuilder import FiltrationBuilder

from app.services.product.filtration.ProductsFiltration import ProductsFiltration


def products_filtration(
    params: ProductsFiltration,
):
    builder = FiltrationBuilder()

    # name
    builder.add_filter(AccurateFilter(
        params.name,
        ProductEntity.name,
    ))

    # price
    builder.add_filter(AccurateFilter(
        params.price,
        ProductEntity.price,
    ))

    return builder
