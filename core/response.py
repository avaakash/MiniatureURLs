class StandardResponseStructure:
    def __init__(self) -> None:
        self.data = []
        self.message = ''
        self.status = False
    
    def object(self) -> dict:
        return {
            'data': self.data,
            'message': self.message,
            'status': self.status
        }