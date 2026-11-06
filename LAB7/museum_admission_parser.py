import datetime
def format_visitor_name(name):
    """
    Formats a full name as 'Surname, Given names' for the ticket.

    Hardened behaviour:
      - None / non-string / blank input  -> "" (empty string)
      - single-word name                 -> just that word, e.g. "Rao"
      - otherwise                        -> "Surname, Given names"
    """
    if not isinstance(name, str):
        return ""
    parts = name.split()
    if not parts:
        return ""
    surname = parts[-1].title()
    given = ' '.join(parts[:-1]).title()
    if not given:
        return surname
    return surname + ', ' + given


def parse_group_ages(text):
    """
    Parses space-separated ages into a list of ints.

    Hardened behaviour:
      - None / non-string input          -> []
      - tokens that are not whole numbers (e.g. "abc", "3.5", "")
        and negative numbers are skipped instead of crashing
    """
    if not isinstance(text, str):
        return []
    ages = []
    for token in text.split():
        try:
            age = int(token)
        except (ValueError, OverflowError):
            continue 
        if age >= 0:
            ages.append(age)
    return ages


def parse_visit_date(text):
    """
    Parses a YYYY-MM-DD date into a (year, month, day) tuple.

    Hardened behaviour:
      - None / non-string input          -> None
      - wrong format, non-digit parts, or an impossible date
        (e.g. 2026-02-30, 2026-13-01)    -> None
    """
    if not isinstance(text, str):
        return None
    parts = text.strip().split('-')
    if len(parts) != 3:
        return None
    year, month, day = parts
    for part, length in ((year, 4), (month, 2), (day, 2)):
        if len(part) != length or not (part.isascii() and part.isdigit()):
            return None
    try:
        datetime.date(int(year), int(month), int(day)) 
    except ValueError:
        return None
    return int(year), int(month), int(day)


def main():
    print("==== Running format_visitor_name ====")
    value = input("Enter a visitor's full name (e.g. asha rao): ")
    result = format_visitor_name(value)
    print("Name on ticket:", result if result else "Invalid name")

    print("\n==== Running parse_group_ages ====")
    value = input("Enter the ages in the group separated by spaces (e.g. 34 12 70): ")
    print("Group ages:", parse_group_ages(value))

    print("\n==== Running parse_visit_date ====")
    value = input("Enter the visit date as YYYY-MM-DD (e.g. 2026-11-05): ")
    result = parse_visit_date(value)
    if result is None:
        print("Visit date: Invalid date")
    else:
        print("Visit date (year, month, day):", result)


if __name__ == "__main__":
    main()