def format_names(names):
    formatted = []

    for name in names:
        first, last = (part.strip() for part in name.split(",", 1))
        formatted.append(f"{last},{first}")

    return sorted(formatted, key=lambda name: name.split(",", 1)[0].casefold())


print(format_names(["John,Doe", "Alice,Smith"]))
# ["Doe,John", "Smith,Alice"]
