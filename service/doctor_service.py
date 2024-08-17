

class DoctorService:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id):
        return self.model.get_by_id(id)

    def get_all(self):
        return self.model.get_all()
    
    def create(self, data):
        return self.model.create(data)
    
    def update(self, id, data):
        return self.model.update(id, data)
    
    def delete(self, id):
        return self.model.delete(id)