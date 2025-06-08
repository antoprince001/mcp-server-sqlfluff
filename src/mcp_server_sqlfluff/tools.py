import sqlfluff


def lint_sql_tool(sql: str, dialect: str = "ansi"):
    result = sqlfluff.lint(sql, dialect=dialect)
    return result


def fix_sql_tool(sql: str, dialect: str = "ansi"):
    fixed = sqlfluff.fix(sql, dialect=dialect)
    return fixed


def parse_sql_tool(sql: str, dialect: str = "ansi"):
    parsed = sqlfluff.parse(sql, dialect=dialect)
    return parsed
