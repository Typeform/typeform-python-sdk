from .form_answer import FormAnswer
from .form_question import FormQuestion


class FormResponse(object):
    """TypeForm form response object"""
    __slots__ = ['_token', '_completed', '_answers', '_hidden', '_metadata', '_questions']

    def __init__(self, token=None, completed=None, answers=None, hidden=None, metadata=None, questions=None):
        """Constructor for TypeForm form response object"""
        self._token = token
        self._completed = bool(completed)
        self._hidden = hidden
        self._metadata = metadata
        self._questions = questions

        self._answers = []
        # Generate a list of FormAnswer's from the answers provided
        # DEV: Answers are provided in the form dict(<question_id>=<answer>)
        for question_id, answer in answers.items():
            question = self.get_question(question_id)
            self._answers.append(
                FormAnswer(answer=answer, question=question.question, question_id=question.id)
            )

    @property
    def questions(self):
        """The list of questions asked by the form"""
        return self._questions

    def get_question(self, id):
        """Get a specific question by id from the list of questions"""
        if not self.questions:
            return None

        for question in self.questions:
            if question.id == id:
                return question

    @property
    def completed(self):
        """Whether or not this form was completed"""
        return self._completed

    @property
    def answers(self):
        """The answers provided to this form"""
        return self._answers

    @property
    def hidden(self):
        """Any hidden fields for this response"""
        return self._hidden

    @property
    def metadata(self):
        """Any metadata for this response"""
        return self._metadata

    @property
    def token(self):
        """This response token"""
        return self._token

    def __repr__(self):
        return 'FormResponse(token={token!r})'.format(token=self.token)


class FormResponses(object):
    """TypeForm form responses collection object"""
    __slots__ = ['_stats', '_responses', '_questions']

    def __init__(self, stats=None, responses=None, questions=None):
        """Constructor for TypeForm for responses collection object"""
        self._stats = stats

        # Convert our questions input into a list of FormQuestion objects
        self._questions = []
        if questions:
            self._questions = [
                FormQuestion(**question) for question in questions
            ]

        # Convert our responses input into a list of FormResponse objects
        self._responses = []
        if responses:
            self._responses = [
                FormResponse(
                    token=resp.get('token'),
                    completed=resp.get('completed'),
                    hidden=resp.get('hidden'),
                    metadata=resp.get('metadata'),
                    answers=resp.get('answers'),
                    questions=self._questions,
                )
                for resp in responses
            ]

    def get_question(self, id):
        """Get a specific question by id"""
        if not self.questions:
            return None

        for question in self.questions:
            if question.id == id:
                return question

    @property
    def responses(self):
        """The responses to the form"""
        return self._responses

    def get_response(self, token):
        """Get a specific response by it's token"""
        if not self.responses:
            return None

        for response in self.responses:
            if response.token == token:
                return response

    @property
    def stats(self):
        """Get the stats for the results"""
        return self._stats

    @property
    def questions(self):
        """The questions asked by this form"""
        return self._questions

    def __getitem__(self, idx):
        """Get a specific response by index"""
        return self.responses[idx]

    def __len__(self):
        """The number of responses"""
        return len(self.responses)

    def __iter__(self):
        """Iterator over the responses"""
        return iter(self.responses)

    def __repr__(self):
        return (
            'FormResponses(questions={questions!r}, responses={responses!r})'
            .format(questions=len(self.questions), responses=len(self.responses))
        )
