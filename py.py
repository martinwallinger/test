import random

# Define the vocabulary and questions
vocabulary = {
    "Wages": "b",
    "Austerity": "b",
    "To ground to a halt": "b",
    "To scrap": "c",
    "To scrape": "b",
    "Inheritance tax": "c",
    "To level up": "b",
    "Widespread": "c",
    "Cronyism": "c",
    "Wishful thinking": "c",
    "Poll tax": "c",
    "To be under strain": "c"
}

questions = {
    "What is the term for the regular payment received by a worker for their services?\n a) Salary\n b) Wages\n c) Allowance\n d) Bonus\n": "b",
    "Which term describes a policy of reducing public spending to cut government debt?\n a) Inflation\n b) Austerity\n c) Subsidy\n d) Expansion\n": "b",
    "What phrase means to stop completely, especially suddenly?\n a) To speed up\n b) To ground to a halt\n c) To take off\n d) To keep pace\n": "b",
    "Which term means to abandon or discard something no longer needed?\n a) To scrape\n b) To scarp\n c) To scrap\n d) To scrounge\n": "c",
    "What verb means to remove something from a surface by rubbing or brushing?\n a) To scarp\n b) To scrape\n c) To scratch\n d) To scold\n": "b",
    "What is the term for the tax imposed on individuals who inherit assets from deceased persons?\n a) Income tax\n b) Capital gains tax\n c) Inheritance tax\n d) Value-added tax\n": "c",
    "Which phrase means to increase something to a higher standard or to equalize opportunities?\n a) To step down\n b) To level up\n c) To tone down\n d) To bring down\n": "b",
    "What word describes something that is found or distributed over a large area or among many people?\n a) Narrow\n b) Localized\n c) Widespread\n d) Contained\n": "c",
    "Which term describes the practice of favoring friends, especially in political appointments?\n a) Meritocracy\n b) Nepotism\n c) Cronyism\n d) Bureaucracy\n": "c",
    "What phrase means believing something is true or will happen because you want it to, even if it is unlikely?\n a) Realism\n b) Pragmatism\n c) Wishful thinking\n d) Skepticism\n": "c",
    "What is the term for a tax levied on individuals as a fixed amount per person?\n a) Income tax\n b) Property tax\n c) Poll tax\n d) Corporate tax\n": "c",
    "Which phrase means experiencing pressure or stress due to difficult circumstances?\n a) To be under control\n b) To be under pressure\n c) To be under strain\n d) To be underwhelmed\n": "c"
}

def quiz_user(questions, answers):
    score = 0
    questions_list = list(questions.keys())
    random.shuffle(questions_list)

    for i, question in enumerate(questions_list):
        print(question)
        answer = answers[i].strip().lower()  # Use pre-defined answers for testing
        if answer == questions[question]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {questions[question]}.\n")
    
    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    # Pre-defined answers for testing
    test_answers = ["b", "b", "b", "c", "b", "c", "b", "c", "c", "c", "c", "c"]
    quiz_user(questions, test_answers)
