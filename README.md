# mcp-server-sql-analyzer

A Model Context Protocol (MCP) server that provides SQL analysis, linting, and fixing capabilities using [SQLFluff](https://sqlfluff.com/).

## Overview

The sqlfluff MCP server provides tools for analyzing and working with SQL queries. It helps with:

- Lint SQL query and return syntax errors
- Fix SQL query and return the fixed version.
- Parse SQL query and return the parsed tree.

## Tools

1. lint_sql
  - Lint SQL query and return syntax errors. Some syntax errors are not detected by the parser like trailing commas.
  - Inputs:
    - sql (string): SQL query to analyze.
    - dialect (string, optional): SQL dialect (e.g., 'mysql', 'postgresql').
  - Returns: 
    - List of linting results, each containing:
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


2. fix_sql
   - Fix SQL query and return the fixed version.
   - Inputs:
     - sql (string): SQL query to fix.
     - dialect (string, optional): SQL dialect (e.g., 'mysql', 'postgresql').
   - Returns:
     - Fixed SQL query string.

3. parse_sql
   - Parse SQL query and return the parsed tree.
   - Inputs:
     - sql (string): SQL query to parse.
     - dialect (string, optional): SQL dialect (e.g., 'mysql', 'postgresql').
   - Returns:
     - Parsed tree as a string.

## Resources

### SQL Dialect Discovery

```
dialects://all
```

Returns a list of all supported SQL dialects for use in all tools.

## Configuration

### Using uvx

Add this to your `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
      "sql-analyzer": {
          "command": "uvx",
          "args": [
              "--from",
              "git+https://github.com/j4c0bs/mcp-server-sqlfluff.git",
              "mcp-server-sqlfluff"
          ]
      }
  }
}
```

### Using uv

After cloning this repo, add this to your MCP client config file::

```json
{
  "mcpServers": {
      "sql-fluff": {
          "command": "uvx",
          "args": [
              "--from",
              "git+https://github.com/antoprince001/mcp-server-sqlfluff.git",
              "mcp-server-sqlfluff"
          ]
      }
  }
}
```

## Development

To run the server in development mode:

```bash
# Clone the repository
git clone git@github.com:antoprince001/mcp-server-sqlfluff.git

# Run the server
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-server-sqlfluff run mcp-server-sqlfluff
```

To run unit tests:

```bash
uv run pytest .
```

## License

Released under the MIT License. See the LICENSE file for details.

