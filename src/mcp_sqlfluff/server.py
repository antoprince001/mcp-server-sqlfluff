from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from tools import lint_sql_tool, fix_sql_tool, parse_sql_tool
import sqlfluff

mcp = FastMCP("SQLFluff MCP")


class SQLRequest(BaseModel):
    sql: str
    dialect: str = "ansi"


@mcp.tool()
def lint_sql(request: SQLRequest):
    """
    Lint SQL query and return syntax errors

    Some syntax errors are not detected by the parser like trailing commas

    Args:
        sql: SQL query to analyze
        dialect: Optional SQL dialect (e.g., 'mysql', 'postgresql')

    Returns:
        error message or "No syntax errors" if parsing succeeds
    """
    try:
        results = lint_sql_tool(request.sql, dialect=request.dialect)
        return results
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def fix_sql(request: SQLRequest):
    """
    Fix SQL query and return the fixed version.

    Args:
        sql: SQL query to fix.
        dialect: Optional SQL dialect (e.g., 'mysql', 'postgresql').

    Returns:
        Fixed SQL query string.
    """
    try:
        fixed_sql = fix_sql_tool(request.sql, dialect=request.dialect)
        return fixed_sql
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def parse_sql(request: SQLRequest):
    """
    Parse SQL query and return the parsed tree.
    Args:
        sql: SQL query to parse.
        dialect: Optional SQL dialect (e.g., 'mysql', 'postgresql').
    Returns:
        Parsed tree as a string.
    """
    try:
        parsed_result = parse_sql_tool(request.sql, dialect=request.dialect)
        return parsed_result
    except Exception as e:
        return {"error": str(e)}


@mcp.resource("dialects://all")
def get_all_dialects():
    """
    Get all supported SQL dialects.

    Returns:
        List of supported SQL dialects.
    """
    dialects = [dialect.name for dialect in sqlfluff.list_dialects()]
    return dialects
