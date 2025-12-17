def get_full_name(first_name: str, last_name: str) -> str:
    if not first_name or not last_name:
        raise ValueError("First name and last name are required")
    return f"Hello {first_name} {last_name} 👋"


if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    try:
        result = get_full_name(first_name, last_name)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

