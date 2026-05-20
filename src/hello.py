def greet_store_owner(store_name: str) -> str:
    return f"Welcome, {store_name}! This project helps stores build better websites."


def create_website_idea(store_type: str) -> str:
    return f"A cinematic scroll website concept for a {store_type} store."


if __name__ == "__main__":
    print(greet_store_owner("Local Store"))
    print(create_website_idea("clothing"))