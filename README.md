# AI Study Assistant

## Project Overview
The AI Study Assistant is a beginner Python project designed to answer study questions using a local knowledge base. It demonstrates basic programming, information retrieval, structured JSON responses, and testing.

## Features
- Answers questions about Python, APIs, AI agents, RAG, and AI safety.
- Searches a knowledge base using keywords.
- Returns structured responses containing a status, question, answer, and sources.
- Handles questions it cannot answer.
- Includes automated tests using Python's unittest framework.

## Technologies Used
- Python
- JSON
- GitHub
- Python unittest

## Project Files
- `app.py` — main application.
- `knowledge_base.json` — study topics and answers.
- `test_app.py` — automated tests.
- `hello.py` — beginner Python practice.
- `chatbot.py` — a simple rule-based chatbot.

## How It Works
The user enters a question. The application compares words in the question with keywords in its knowledge base and returns a matching answer when available. If no match is found, it explains that it does not have enough information.

## Current Limitations
This is an early prototype. It uses keyword matching and does not yet connect to a live large language model or external APIs.

## Future Improvements
- Integrate a large language model through an API.
- Add more study material.
- Improve search and retrieval.
- Expand testing and error handling.

## Learning Goals
This project helps me develop my Python programming, AI application development, structured data handling, testing, and GitHub skills.


