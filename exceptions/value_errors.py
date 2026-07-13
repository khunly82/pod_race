class InvalidSortError(ValueError):
    def __repr__(self):
        return 'Invalid sort'
    
class AttachToPodError(ValueError):

    def __init__(self, message: str, *args):
        super().__init__(*args)
        self.message = message

    def __repr__(self):
        return f'Cannot attach this part to this pod ({self.message})'
    
class DetachFromPodError(ValueError):

    def __init__(self, message: str, *args):
        super().__init__(*args)
        self.message = message

    def __repr__(self):
        return f'Cannot detach this part to this pod ({self.message})'