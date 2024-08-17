from dotenv import load_dotenv
import os

load_dotenv()

class ConfigEnvironment:

    def __init__(self) -> None:
        self._host_db=os.getenv('HOST_POSTGRE', 'localhost')
        self._port_db=os.getenv('PORT_POSTGRE', '5432')
        self._user_db=os.getenv('USER_POSTGRE', 'root')
        self._pass_db=os.getenv('PASS_POSTGRE', '')
        self._nama_db=os.getenv('DB_POSTGRE', 'hospital')
    
    def getHostDB(self):
        return self._host_db
    
    def getPortDB(self):
        return self._port_db
    
    def getUserDB(self):
        return self._user_db
    
    def getPassDB(self):
        return self._pass_db
    
    def getNamaDB(self):
        return self._nama_db