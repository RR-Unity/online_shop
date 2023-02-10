from app.services.product.productService import ProductService
from app.services.product.productRepository import ProductRepository


def get_product_service(providers, session):
    repository = providers.Factory(
        ProductRepository,
        db_session=session,
    )

    return providers.Factory(
        ProductService,
        repository=repository,
    )
