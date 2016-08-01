from PyQt5.QtCore import QObject, pyqtSignal
from pylogix.eip import PLC
import sqlite3

class DB_Interface(QObject):
  ''' Database interface, which uses a default sqlite database for testing purposes

      Handles client and server connections between the various PLC and parses the
      information between them and the database

  '''

  new_tracking_item = pyqtSignal()

  def __init__(self, parent=None):
    super(DB_Interface, self).__init__(parent)

    self.conn = sqlite3.connect('CS_Main.db')

    self.recipe_cursor = self.conn.cursor()
    self.tracking_cursor = self.conn.cursor()

  def __del__(self):
    self.conn.close()


  def build_recipe_table(self):
    self.recipe_cursor.execute('''CREATE TABLE recipe
                                  (Temperature.Max REAL, Hole.Left BOOL, Hole.Right BOOL, Model STRING, Group DINT, Version INT)''')
    self.conn.commit()

  def build_tracking_table(self):
    self.tracking_cursor.execute('''CREATE TABLE tracking
                                    (Alarm.Activated DINT, User.Actual INT, Position.Left BOOL, Position.Right BOOL, Temperature.Actual REAL, Timer.Production.Begin TIME, Timer.Production.End TIME)''')
    self.conn.commit()

  def recipe_table_addline(self):
    self.new_tracking_item.emit()


