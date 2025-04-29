class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.rules = {}

    def add_fact(self, fact, value=False):
        self.facts[fact] = value

    def add_rule(self, result, required_facts):
        self.rules[result] = required_facts

    def ask_questions(self):
        questions = {
            "completed_projects": "Has the employee completed their projects? (yes/no): ",
            "good_attendance": "Does the employee have good attendance? (yes/no): ",
            "positive_feedback": "Is client feedback positive? (yes/no): ",
            "missed_deadlines": "Has the employee missed deadlines? (yes/no): ",
            "teamwork": "Does the employee show good teamwork? (yes/no): "
        }
        for fact, question in questions.items():
            ans = input(question).strip().lower()
            self.facts[fact] = ans == "yes"

    def infer(self):
        for result, conditions in self.rules.items():
            if all(self.facts.get(fact) == value for fact, value in conditions.items()):
                return result
        return "No matching evaluation found"

# Create system
expert = ExpertSystem()

# Define all facts
fact_list = ["completed_projects", "good_attendance", "positive_feedback", "missed_deadlines", "teamwork"]
for fact in fact_list:
    expert.add_fact(fact)

# Define rules
expert.add_rule("Outstanding Performer", {
    "completed_projects": True,
    "good_attendance": True,
    "positive_feedback": True,
    "missed_deadlines": False,
    "teamwork": True
})

expert.add_rule("Good Performer", {
    "completed_projects": True,
    "good_attendance": True,
    "missed_deadlines": False
})

expert.add_rule("Needs Improvement", {
    "completed_projects": False,
    "good_attendance": False,
    "missed_deadlines": True
})

# Ask questions and infer
expert.ask_questions()
evaluation = expert.infer()
print("\nEmployee Evaluation:", evaluation)
