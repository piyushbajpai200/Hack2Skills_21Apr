from election_assistant.assistant import generate_guidance


def main() -> None:
    print("Hi — I can help you vote with a simple plan.")
    state = input("What state are you voting in? ").strip()
    first_time = input("Is this your first time voting? (Yes/No) ").strip()
    method = input(
        "How do you plan to vote? (In-person early / Election Day / Mail or absentee / Not sure) "
    ).strip()

    print("\nWould you like details on: registration, ID requirements, mail ballot rules, polling place, issue help?")
    topic = input("Optional topic (press Enter to skip): ").strip()

    output = generate_guidance(state, first_time, method, topic if topic else None)
    print("\n" + output)


if __name__ == "__main__":
    main()
