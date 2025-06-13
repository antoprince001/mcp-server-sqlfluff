import sqlfluff
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from tools import fix_sql_tool, lint_sql_tool, parse_sql_tool

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
        List of linting results, each containing:
            - start_line_no: Line number where the issue starts
            - start_line_pos: Position in the line where the issue starts
            - code: Error code
            - description: Description of the issue
            - name: Name of the linting rule
            - warning: Whether it's a warning or an error
            - fixes: List of possible fixes
            - start_file_pos: Start position in the file
            - end_line_no: Line number where the issue ends
            - end_line_pos: Position in the line where the issue ends
            - end_file_pos: End position in the file
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


def main():
    mcp.run()


if __name__ == "__main__":
    main()
