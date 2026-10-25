from fastmcp import FastMCP
from schemas.product import Product,  UseCase
from repositories.product_repo import ProductRepo

def register_product_mcp(mcp: FastMCP, product_repo: ProductRepo) -> None:
    
    @mcp.tool
    def get_product_by_id(id: int) -> Product | None:
        """
        function to get a product by its id
        """
        return product_repo.get_product_by_id(id)

    @mcp.tool
    def get_product_by_name(name: str) -> Product | None:
        """
        function to get a product by its name
        """
        return product_repo.get_product_by_name(name)

    @mcp.tool
    def get_products_by_use_case(use_case: UseCase) -> list[Product]:
        """
        function to get a list of products
        """
        return product_repo.get_products_by_use_case(use_case)
    