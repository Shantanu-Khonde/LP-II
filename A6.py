# Define the rules for performance evaluation
rules = {
    {'work_quality': {
        'Excellent': 'work_quality >= 90',
        'Good': 'work_quality >= 80 and work_quality < 90',
        'Needs improvement': 'work_quality < 80'
    }
    },
    {'attendance': {
        'Excellent': 'attendance >= 95',
        'Good': 'attendance >= 90 and attendance < 95',
        'Needs improvement': 'attendance < 90'
    }
    },
    {'teamwork': {
        'Excellent': 'teamwork >= 90',
        'Good': 'teamwork >= 80 and teamwork < 90',
        'Needs improvement': 'teamwork < 80'
    }
    },
    {'initiative': {
        'Excellent': 'initiative >= 90',
        'Good': 'initiative >= 80 and initiative < 90',
        'Needs improvement': 'initiative < 80'
    }
    }
}

# Define the questions to ask
questions = {
    'work_quality': 'What is the employee\'s work quality (0-100)? ',
    'attendance': 'What is the employee\'s attendance rate (0-100)? ',
    'teamwork': 'How would you rate the employee\'s teamwork (0-100)? ',
    'initiative': 'How would you rate the employee\'s initiative (0-100)? '
}

# Define the function to evaluate performance
def evaluate_performance(answers):
    score = 0
    for key, value in answers.items():
        for grade, rule in rules[key].items():
            if eval(rule):
                score += int(value) * (int(grade[0]) / 10)
                break
    return score

# Ask the questions and get the answers
answers = {}
for key, question in questions.items():
    answer = input(question)
    answers[key] = answer

# Evaluate the performance and print the score
score = evaluate_performance(answers)
print('The employee\'s performance score is:', score)
