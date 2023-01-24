def add_score(subject_score, student, subject, score):
  if student in subject_score:
    subject_score[student].update({subject: score})
    return subject_score
  subject_score.update({student: {subject: score}})
  return subject_score


def calc_average_score(subject_score):
  return {student: "{:.2f}".format(sum(subject_score[student].values()) / len(subject_score[student])) for student in subject_score}
  