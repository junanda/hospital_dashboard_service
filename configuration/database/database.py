from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    def __init__(self, host_db, port_db, user_db, pass_db, nama_db):
        self.host_db = host_db
        self.port_db = port_db
        self.user_db = user_db
        self.pass_db = pass_db
        self.nama_db = nama_db
        self.connection = None

    @abstractmethod
    def connect(self, app):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def get_connection(self, app):
        pass