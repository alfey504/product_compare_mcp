from fastmcp import FastMCP
from mcp_app.product_mcp import register_product_mcp
from repositories.product_repo import ProductRepo

mcp = FastMCP(
    name="ProductMCP"
)

product_repo = ProductRepo()
register_product_mcp(mcp, product_repo) 


