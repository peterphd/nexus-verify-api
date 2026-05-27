def levenshtein(a: str, b: str) -> int:
    a = a.lower().strip()
    b = b.lower().strip()
    rows = len(a) + 1
    cols = len(b) + 1
    table = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        table[i][0] = i
    for j in range(cols):
        table[0][j] = j

    for i in range(1, rows):
        for j in range(1,cols):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(
                        table[i - 1][j],
                        table[i][j - 1],
                        table[i - 1][j - 1]
                        )
    return table[rows - 1][cols - 1]


def name_similarity(a: str, b: str) -> float:
    distance = levenshtein(a,b)
    longest = max(len(a),len(b))
    if longest == 0:
        return 1.0
    return round(1 - (distance/longest), 2)


def dob_match(a: str, b: str) -> bool:
    return a.strip() == b.strip()


def verify(request: dict, record: dict) -> dict:
    score = name_similarity(request["name"], record["name"])

    if score >= 0.95 and dob_match(request["dob"], record["dob"]):
        result = "MATCH"
    elif score >= 0.6:
        result = "PARTIAL"
    else:
        result = "NO_MATCH"

    return {"result": result, "score": score}