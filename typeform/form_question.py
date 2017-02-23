class FormQuestion(object):
    """TypeForm form question object"""
    __slots__ = ['_field_id', '_id', '_question']

    def __init__(self, field_id=None, id=None, question=None):
        """Constructor for TypeForm form question"""
        self._field_id = field_id
        self._id = id
        self._question = question

    @property
    def field_id(self):
        """The field_id of the question"""
        return self._field_id

    @property
    def id(self):
        """The id of the question"""
        return self._id

    @property
    def question(self):
        """The question asked by this question"""
        return self._question

    def __repr__(self):
        return (
            'FormQuestion(field_id={field_id!r}, id={id!r}, question={question!r})'
            .format(field_id=self.field_id, id=self.id, question=self.question)
        )
