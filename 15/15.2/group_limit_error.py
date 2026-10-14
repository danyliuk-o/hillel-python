class GroupLimitError(Exception):

    def __init__(self, limit):
        super().__init__(f'Група не може містити більше {limit} студентів')
        self.limit = limit
