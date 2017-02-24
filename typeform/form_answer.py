class FormAnswer(object):
    """TypeForm response answer object"""
    __slots__ = ['_question', '_question_id', '_answer']

    def __init__(self, answer=None, question=None, question_id=None):
        """Constructor for TypeForm response answer"""
        self._answer = answer
        self._question = question
        self._question_id = question_id

    @property
    def question(self):
        """The question that was asked"""
        return self._question

    @property
    def question_id(self):
        """The id of the question asked"""
        return self._question_id

    @property
    def answer(self):
        """The user's answer to the question"""
        return self._answer

    def __repr__(self):
        return (
            'FormAnswer(answer={answer!r}, question={question!r}, question_id={question_id!r})'
            .format(answer=self.answer, question=self.question, question_id=self.question_id)
        )
