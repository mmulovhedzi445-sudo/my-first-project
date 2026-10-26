import unittest
from app import answer_question


class TestStudyAssistant(unittest.TestCase):

    def setUp(self):
        self.knowledge = [
            {
                "topic": "Python",
                "keywords": ["python", "programming", "code", "coding"],
                "answer": "Python is a programming language."
            }
        ]

    def test_python_question(self):
        result = answer_question("What is Python?", self.knowledge)
        self.assertEqual(result["status"], "success")

    def test_unknown_question(self):
        result = answer_question("Tell me about space travel", self.knowledge)
        self.assertEqual(result["status"], "not_found")

    def test_result_has_required_fields(self):
        result = answer_question("Python programming", self.knowledge)
        self.assertIn("answer", result)
        self.assertIn("sources", result)
        self.assertIn("question", result)


if __name__ == "__main__":
    unittest.main()
