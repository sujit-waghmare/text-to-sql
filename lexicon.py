import re

# simple english > SQL
LEXICON = {
    "select": "SELECT",
    "show": "SELECT",
    "get": "SELECT",
    "find": "SELECT",
    "list": "SELECT",
    "everything": "*",
    "all": "*",
    "unique": "DISTINCT",
    "distinct": "DISTINCT",
  
    "from": "FROM",
    "table": "",
  
    "where": "WHERE",
    "with": "WHERE",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "between": "BETWEEN",
    "like": "LIKE",
    "containing": "LIKE",
  
    "greater than": ">",
    "more than": ">",
    "less than": "<",
    "fewer than": "<",
    "at least": ">=",
    "at most": "<=",
    "equals": "=",
    "is": "=",
  
    "count of": "COUNT(*)",
    "number of": "COUNT(*)",
    "average": "AVG",
    "total": "SUM",
    "sum": "SUM",
    "highest": "MAX",
    "lowest": "MIN",
  
    "sorted by": "ORDER BY",
    "ordered by": "ORDER BY",
    "grouped by": "GROUP BY",
    "per": "GROUP BY",
    "ascending": "ASC",
    "descending": "DESC",
    "top": "LIMIT",
    "first": "LIMIT",
    "limit": "LIMIT",
}

_PHRASES = sorted(LEXICON, key=len, reverse=True)
_PATTERN = re.compile(r"\b(" + "|".join(map(re.escape, _PHRASES)) + r")\b", re.I)


def translate(text: str) -> str:
    sql = _PATTERN.sub(lambda m: LEXICON[m.group(1).lower()], text.strip())
    sql = re.sub(r"\s+", " ", sql).strip()
    return sql.rstrip(";") + ";"


if __name__ == "__main__":
    print(translate(input("Input English wording: ")))