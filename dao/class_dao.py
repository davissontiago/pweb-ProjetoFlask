from dao.db_config  import get_connection 

class ClassDAO: 

    sqlSelect = 'SELECT t.id, t.semestre, c.nome_curso, p.nome FROM turma AS t JOIN professor AS p ON t.professor_id = p.id JOIN curso AS c ON t.curso_id = c.id ORDER BY id ASC'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows