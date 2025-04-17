import random
import json
import os

def make_quiz(lesson,start_time,qbank,new_quiz,current_user,file_path):
    list_of_before_questions = []
    list_of_question = []
    list_of_option = []
    list_of_answer = []
    i = 0
    if not os.path.exists(file_path):
         open(file_path, 'w')
    else:
        with open(file_path, 'r') as f2:
            recive_before_context = f2.readlines()
            if recive_before_context is not None:
                for line in recive_before_context:
                    change_to_dict = json.loads(line)
                    list_of_before_questions.append(change_to_dict['question1'])
                    list_of_before_questions.append(change_to_dict['question2'])
                    list_of_before_questions.append(change_to_dict['question3'])
                print('list_of_before_questions is : ', list_of_before_questions)

    while i < 100:
        random_number = random.randint(0, len(qbank) - 1)
        random_question = qbank[random_number]
        option1 = random_question.option1
        option2 = random_question.option2
        option3 = random_question.option3
        option4 = random_question.option4
        answer = random_question.answer

        if random_question not in list_of_question:
            print('random_question is: ', random_question,'type random: ',type(str(random_question)))
            if str(random_question) not in list_of_before_questions:
                print('list_of_before_questions is : ', list_of_before_questions)
                list_of_question.append(random_question)
                options = [option1, option2, option3, option4]
                if options not in list_of_option:
                    list_of_option.append(options)
                    list_of_answer.append(answer)

        if len(list_of_question) == 3:
            break
        i += 1

    q1 = list_of_question[0];q2 = list_of_question[1];q3 = list_of_question[2]
    op1 = list_of_option[0];op2 = list_of_option[1];op3 = list_of_option[2]
    an1 = list_of_answer[0];an2 = list_of_answer[1];an3 = list_of_answer[2]
    context = {
        'lesson': lesson,
        'start_time':start_time,
        'is_context_empty': 't',
        # 'current_user': current_user.__dict__,
        'question1': q1.__dict__['question'], 'question2': q2.__dict__['question'],
        'question3': q3.__dict__['question'],
        'options1a': op1[0], 'options1b': op1[1], 'options1c': op1[2], 'options1d': op1[3],
        'options2a': op2[0], 'options2b': op2[1], 'options2c': op2[2], 'options2d': op2[3],
        'options3a': op3[0], 'options3b': op3[1], 'options3c': op3[2], 'options3d': op3[3],
        # 'options4a': op4[0], 'options4b': op4[1], 'options4c': op4[2], 'options4d': op4[3],
        'answer1': an1, 'answer2': an2, 'answer3': an3
    }
    print('start_time: ', context['start_time'], 'question1: ', context['question1'])

    with open(file_path, 'a') as f1:
        change_dict_to_json_string = json.dumps(context)
        print(change_dict_to_json_string, type(change_dict_to_json_string))
        f1.write(change_dict_to_json_string + '\n')

    # print('list_of_before_questions is: ', list_of_before_questions)

    return context
