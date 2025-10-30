from dao.db_config  import get_connection 

class StudentDAO: 

    sqlSelect = 'SELECT id, nome, idade, cidade FROM aluno'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows