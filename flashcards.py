import json
import os
import random
import string

class QnA:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.progress = Progress()

    def modify_score(self, score):
        self.progress.corrects += score.corrects
        self.progress.incorrects += score.incorrects

    def reset_score(self):
        self.progress.corrects = 0
        self.progress.incorrects = 0

class Progress:
    def __init__(self, corrects=0, incorrects=0):
        self.corrects = corrects
        self.incorrects = incorrects

class Flashcards:
    def __init__(self, filename="default.json"):
        self.filename = filename
        self.flashcards = self.load_flashcards()

    def load_flashcards(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                flashcards = []
                for flashcard in data:
                    fc_obj = QnA(flashcard["question"], flashcard["answer"])
                    progress_data = flashcard.get("progress", {})
                    fc_obj.progress = Progress(**progress_data)
                    flashcards.append(fc_obj)
                return flashcards
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_flashcards(self):
        try:
            with open(self.filename, "w") as file:
                json.dump([
                    {
                        "question": flashcard.question,
                        "answer": flashcard.answer,
                        "progress": {
                            "corrects": flashcard.progress.corrects,
                            "incorrects": flashcard.progress.incorrects
                        }
                    }
                    for flashcard in self.flashcards
                ], file, indent=4)
        except Exception as e:
            print("Error Saving!", e)

    def modify_score(self, question, score):
        for flashcard in self.flashcards:
            if flashcard.question.lower() == question.lower():
                flashcard.modify_score(score)
                self.save_flashcards()
                return

    def enhanced_active_learn_mode(self):
        session_questions = set()  # Track seen questions
        question_counter = 0  # Count questions asked
        reinforcement_index = 0  # Track which reinforcement question to use

        while True:
            # Refresh categorized lists every 5 questions or at the start
            if question_counter % 5 == 0 or question_counter == 0:
                new_questions = [fc for fc in self.flashcards if fc.progress.corrects == 0]
                struggling_questions = [fc for fc in self.flashcards if fc.progress.incorrects >= 2]
                mastered_questions = [
                    fc for fc in self.flashcards if fc.progress.corrects >= 2 and fc.progress.incorrects < fc.progress.corrects
                ]
                random.shuffle(mastered_questions)  # Shuffle reinforcement questions

            # Ensure a fresh question pool
            question_pool = new_questions + struggling_questions

            # If no new or struggling questions, reinforce with mastered ones
            if not question_pool and mastered_questions:
                question_pool.append(mastered_questions[reinforcement_index])
                reinforcement_index = (reinforcement_index + 1) % len(mastered_questions)

            # If still empty, restart session
            if not question_pool:
                print("No available questions. Resetting session...")
                session_questions.clear()
                continue

            # Pick a random question (ensure no immediate repetition)
            flashcard = random.choice(question_pool)
            while flashcard.question in session_questions and len(question_pool) > 1:
                flashcard = random.choice(question_pool)
            session_questions.add(flashcard.question)
            question_counter += 1

            # Display progress status
            status = (
                "📌 New Question" if flashcard in new_questions else
                "🔁 Re-learning" if flashcard in struggling_questions else
                "✅ Reinforcement"
            )
            print(f"\n{status} | ✅ {flashcard.progress.corrects} | ❌ {flashcard.progress.incorrects}")
            print(flashcard.question)

            # Create multiple-choice answers
            choices = [flashcard.answer]
            incorrect_answers = list(set(fc.answer for fc in self.flashcards if fc.answer != flashcard.answer))
            random.shuffle(incorrect_answers)
            choices.extend(incorrect_answers[:3])
            random.shuffle(choices)

            correct_ans = ""
            for index, choice in zip(string.ascii_uppercase, choices):
                print(f"{index}. {choice}")
                if choice == flashcard.answer:
                    correct_ans = index

            # Get user input
            answer = input("Enter your answer: ").strip().upper()
            if answer == correct_ans:
                print("✅ Correct!")
                score = Progress(1, 0)
            else:
                print(f"❌ Wrong! The correct answer was {correct_ans}. {flashcard.answer}")
                score = Progress(0, 1)

            self.modify_score(flashcard.question, score)

            # Option to continue or exit
            cont = input("\nContinue? (Y/N): ").strip().lower()
            if cont != 'y':
                break

# Run Flashcard Learning Mode
fc = Flashcards()
fc.enhanced_active_learn_mode()
