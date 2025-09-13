def detect_delimiter(filename: str) -> str:
    """
    Detect the delimiter used in a CSV file based on its filename.
    """
    if filename.endswith(".tsv"):
        return "\t"
    return ","
