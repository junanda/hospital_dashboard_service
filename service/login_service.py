from ..entity.user import RequestLogin
from ..repository.user_repository import UserRepository
from ..utils.utilities import check_password, generate_token

class LoginService:
    def __init__(self):
        pass

    def login(self, data:RequestLogin):
        result = UserRepository().get_by_username(data.username)
        if not result:
            return False, None, 'not_found'
        
        if not check_password(data.password, result.password):
            return False, None, 'in_correct'
        
        token = generate_token(result.id, result.role)
        return True, token, None
    
    def logout(self):
        return True