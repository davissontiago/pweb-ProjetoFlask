from dao.db_config  import get_connection 

class TeacherDAO: 

    sqlSelect = 'SELECT id, nome, disciplina FROM professor'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows