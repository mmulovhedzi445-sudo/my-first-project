import json

def load_knowledge():
    with open("knowledge_base.json", "r", encoding="utf-8") as file:
        return json.load(file)

def answer_question(question, knowledge):
    question_lower = question.lower()

    for note in knowledge:
        keywords = note["keywords"]

        if any(word in question_lower for word in keywords):
            return {
                "status": "success",
                "question": question,
                "answer": note["answer"],
                "sources": [note["topic"]]
            }

    return {
        "status": "not_found",
        "question": question,
        "answer": "I don't have enough information to answer that yet.",
        "sources": []
    }

def main():
    knowledge = load_knowledge()

    print("AI Study Assistant")
    print("Ask a question, or type 'bye' to exit.")

    while True:
        question = input("\nYou: ")

        if question.lower() == "bye":
            print("Goodbye!")
            break

        if question.lower() == "help":
            print("Ask about Python, APIs, AI agents, RAG, or AI safety.")
            continue

        result = answer_question(question, knowledge)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
