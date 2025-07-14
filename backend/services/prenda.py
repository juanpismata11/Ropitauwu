from models.prenda import Prenda as PrendaModel

class PrendaService():
  def __init__ (self, db) -> None:
    self.db = db

  def get_prendas(self):
    result = self.db.query(PrendaModel).all()
    return result
  
  def get_prenda_by_id(self, id):
    result = self.db.query(PrendaModel).filter(PrendaModel.id == id).first()
    return result
  
  def create_prenda(self, prenda):
    new_prenda = PrendaModel(**prenda.model_dump())
    self.db.add(new_prenda)
    self.db.commit()
    return new_prenda
  
  def update_prenda(self, id, prenda):
    result = self.db.query(PrendaModel).filter(PrendaModel.id == id).first()
    if not result:
      return "Prenda not foundssss"
    result.nombre = prenda.nombre
    result.img = prenda.img
    result.tipo = prenda.tipo
    self.db.commit()
    return result
  
  def delete_prenda(self, id):
    result = self.db.query(PrendaModel).filter(PrendaModel.id == id).first()
    if not result:
      return "Prenda not found"
    self.db.delete(result)
    self.db.commit()
    return "Prenda deleted successfully"