import random

# Lista de preguntas y respuestas
questions_answers = {
    "How to form the first conditional'?": "if+present simple, future",
    "Transform this sentence into reported speech: She told him -come back from the party before 5 a.m'.": "She told him to come back from de party before 5 a.m",
    "Complete the sentence: She ___ to the store yesterday.": "went",
    "What is the participe of know'?": "known",
    "Form a sentence using the word 'book' as a verb.": "She will book the tickets for us.",
    # Agrega más preguntas y respuestas según sea necesario
}

def generate_question():
    """Genera una pregunta aleatoria."""
    return random.choice(list(questions_answers.keys()))

def check_answer(question, answer)
    """Verifica si la respuesta es correcta."""
    correct_answer = questions_answers.get(question)
    if correct_answer:
        return answer.strip().lower() == correct_answer
    return False

def main():
    print("¡Bienvenido al generador de ejercicios de inglés para segundo de bachillerato!")
    print("Responde las siguientes preguntas:")
    score = 0
    num_questions = 5  # Puedes ajustar el número de preguntas aquí

    for _ in range(num_questions):
        question = generate_question()
        print("\n", question)
        user_answer = input("Tu respuesta: ")
        if check_answer(question, user_answer):
            print("¡Correcto!")
            score += 1
        else:
            print("Respuesta incorrecta. La respuesta correcta es:", questions_answers[question])

    print("\nHas respondido correctamente", score, "de", num_questions, "preguntas.")

if __name__ == "__main__":
    main()
