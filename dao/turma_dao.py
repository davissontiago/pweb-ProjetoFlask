from dao.db_config  import get_connection 

class TurmaDAO: 

    sqlSelect = 'SELECT t.id, t.semestre, c.nome_curso, p.nome FROM turma AS t JOIN professor AS p ON t.professor_id = p.id JOIN curso AS c ON t.curso_id = c.id'

    def listar(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        lista = cursor.fetchall() 
        conn.close() 
        return lista