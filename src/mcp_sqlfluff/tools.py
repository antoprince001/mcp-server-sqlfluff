from sqlfluff.core import Linter


def lint_sql_tool(sql: str, dialect: str = "ansi"):
    linter = Linter(dialect=dialect)
    result = linter.lint_string(sql, dialect=dialect)
    return [
        {
            "line": v.line_no,
            "position": v.line_pos,
            "code": v.rule_code,
            "description": v.description
        }
        for v in result.get_violations()
    ]


def fix_sql_tool(sql: str, dialect: str = "ansi"):
    linter = Linter(dialect=dialect)
    fixed = linter.fix_string(sql, dialect=dialect)
    return fixed


def parse_sql_tool(sql: str, dialect: str = "ansi"):
    linter = Linter(dialect=dialect)
    parsed = linter.parse_string(sql, dialect=dialect)
    return {
        "parsed_tree": parsed.tree.stringify(),
    }
