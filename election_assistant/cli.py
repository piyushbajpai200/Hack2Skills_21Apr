from election_assistant.faq import answer_question


def main() -> None:
    print("Hi — ask me anything about voting and I’ll do my best to answer.")
    print("Try questions like: registration, ID requirements, mail ballots, polling place, or issue help.")

    while True:
        question = input("\nAsk a question (or type 'quit' to exit): ").strip()
        if not question:
            print("Type a question about voting, or enter 'quit' to exit.")
            continue

        if question.lower() in {"quit", "exit", "bye"}:
            print("Goodbye! Vote safely.")
            break

        print("\n" + answer_question(question))


if __name__ == "__main__":
    main()
