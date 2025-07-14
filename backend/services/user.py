from models.user import User as UserModel

class UserService():
  def __init__ (self, db) -> None:
    self.db = db

  def get_users(self):
    result = self.db.query(UserModel).all()
    return result
  
  def get_user_by_id(self, id):
    result = self.db.query(UserModel).filter(UserModel.id == id).first()
    return result
  
  def create_user(self, user):
    new_user = UserModel(**user.model_dump())
    self.db.add(new_user)
    self.db.commit()
    return new_user
  
  def update_user(self, id, user):
    result = self.db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
      return "User not found"
    result.username = user.username
    result.password = user.password
    self.db.commit()
    return result
  
  def delete_user(self, id):
    result = self.db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
      return "User not found"
    self.db.delete(result)
    self.db.commit()
    return "User deleted successfully"