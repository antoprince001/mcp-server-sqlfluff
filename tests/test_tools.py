from src.mcp_server_sqlfluff.tools import lint_sql_tool, fix_sql_tool, parse_sql_tool


def test_lint_sql_tool():
    sql_query = "SELECT * FROM table WHERE column = 'value';"
    expected_result = [{'start_line_no': 1, 'start_line_pos': 1, 'code': 'AM04', 'description': 'Query produces an unknown number of result columns.', 'name': 'ambiguous.column_count', 'warning': False, 'fixes': [], 'start_file_pos': 0, 'end_line_no': 1, 'end_line_pos': 43, 'end_file_pos': 42}, {'start_line_no': 1, 'start_line_pos': 21, 'code': 'LT14', 'description': "The 'WHERE' keyword should always start a new line.", 'name': 'layout.keyword_newline', 'warning': False, 'fixes': [{'type': 'replace', 'edit': '\n', 'start_line_no': 1, 'start_line_pos': 20, 'start_file_pos': 19, 'end_line_no': 1, 'end_line_pos': 21, 'end_file_pos': 20}], 'start_file_pos': 20, 'end_line_no': 1, 'end_line_pos': 26, 'end_file_pos': 25}, {'start_line_no': 1, 'start_line_pos': 43, 'code': 'LT12', 'description': 'Files must end with a single trailing newline.', 'name': 'layout.end_of_file', 'warning': False, 'fixes': [{'type': 'create_after', 'edit': '\n', 'start_line_no': 1, 'start_line_pos': 44, 'start_file_pos': 43, 'end_line_no': 1, 'end_line_pos': 44, 'end_file_pos': 43}], 'start_file_pos': 42, 'end_line_no': 1, 'end_line_pos': 44, 'end_file_pos': 43}]

    result = lint_sql_tool(sql_query)

    assert isinstance(result, list)
    assert result == expected_result


def test_fix_sql_tool():
    bad_sql_query = "SeLEct  *, 1, blah as  fOO  from mySchema.myTable"
    expected = 'SELECT\n    *,\n    1,\n    blah AS foo\nFROM myschema.mytable\n'

    fixed_sql = fix_sql_tool(bad_sql_query)

    assert fixed_sql == expected


def test_parse_sql_tool():
    sql = "SELECT * FROM table WHERE column = 'value';"
    expected_parsed = {'file': {'statement': {'select_statement': [{'select_clause': {'keyword': 'SELECT', 'whitespace': ' ', 'select_clause_element': {'wildcard_expression': {'wildcard_identifier': {'star': '*'}}}}}, {'whitespace': ' '}, {'from_clause': {'keyword': 'FROM', 'whitespace': ' ', 'from_expression': {'from_expression_element': {'table_expression': {'table_reference': {'naked_identifier': 'table'}}}}}}, {'whitespace': ' '}, {'where_clause': {'keyword': 'WHERE', 'whitespace': ' ', 'expression': [{'column_reference': {'naked_identifier': 'column'}}, {'whitespace': ' '}, {'comparison_operator': {'raw_comparison_operator': '='}}, {'whitespace': ' '}, {'quoted_literal': "'value'"}]}}]}, 'statement_terminator': ';'}}

    parsed_result = parse_sql_tool(sql)

    assert isinstance(parsed_result, dict)
    assert parsed_result == expected_parsed
