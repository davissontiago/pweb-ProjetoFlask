from dao.db_config  import get_connection 

class CourseDAO: 

    sqlSelect = 'SELECT id, nome_curso, duracao FROM curso'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows