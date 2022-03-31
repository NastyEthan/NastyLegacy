from flask import Blueprint, jsonify


api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates/pages/')

questions = []
question_list = [
    ["Where is Forbidden Rice from?", ['Vietnam','China','India','America'], '2'],
    ["What rice is part of the Great Wall of China?", ['Sticky Rice','Basmati Rice','Brown Rice','Parboiled Rice'], '1'],
    ["What rice is the most common in the world?", ['Forbidden Rice', 'White Rice', 'Jasmine Rice', 'Sushi Rice'], '2'],
    ["Which rice is healthiest?", ['Parboiled Rice','Brown Rice','Basmati Rice','Jasmine Rice'], '3'],
    ["Which rice tastes nutty?", ['Jasmine Rice','Sticky Rice','Brown Rice','Red Cargo Rice'], '4']
]

def _find_next_id():
    return max(questions["id"] for question in questions) + 1


def _init_questions():
    id = 1
    # Creating the questions list which will store all the data to be converted to json
    for question in question_list:
        questions.append({"id": id, "question": question_list[id-1][0], "answer1": question_list[id-1][1][0], "answer2": question_list[id-1][1][1], "answer3": question_list[id-1][1][2], "answer4": question_list[id-1][1][3], "correctAnswer": question_list[id-1][2]})
        id += 1


# Converts questions to json
@api_bp.route('/questions/')
def get_questions():
    if len(questions) == 0:
        _init_questions()
    return jsonify(questions)


if __name__ == "__main__":
    get_questions()
    print(questions)