from dao.db_config  import get_connection 

class CourseDAO: 

    sqlSelect = 'SELECT id, nome_curso, duracao FROM curso ORDER BY id ASC'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows
    
    def save(self, name_course, duration, id=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:            
            cursor.execute('INSERT INTO curso (nome_curso, duracao ) VALUES (%s, %s)', (name_course, duration))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()