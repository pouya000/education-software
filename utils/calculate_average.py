def calc_avg(quiz_farsi, quiz_riazi):
    farsi_scores = []
    riazi_scores = []
    for quiz in quiz_riazi:
        for q in quiz.quizdetail_set.all():
            riazi_scores.append(q.score)

    if len(riazi_scores) != 0:
        riazi_average = sum(riazi_scores) / len(riazi_scores)
        riazi_average_mark = float("%6.2f" % riazi_average)
    else:
        riazi_average_mark = 0
        riazi_average = 0

    for quiz in quiz_farsi:
        for q in quiz.quizdetail_set.all():
            # print('score in quiz_farsi is: ', q.score)
            farsi_scores.append(q.score)

    if len(farsi_scores) != 0:
        farsi_average = sum(farsi_scores) / len(farsi_scores)
        farsi_average_mark = float("%6.2f" % farsi_average)
    else:
        farsi_average_mark = 0
        farsi_average = 0

    return riazi_average_mark , farsi_average_mark, riazi_scores , farsi_scores
    # return riazi_average , farsi_average , riazi_scores , farsi_scores







# print('farsi_average_mark: ', farsi_average_mark, 'riazi_average_mark: ', riazi_average_mark)
# quiz_farsi_len = len(farsi_scores)
# quiz_riazi_len = len(quiz_riazi)