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
            if id:
                cursor.execute('UPDATE curso SET nome_curso = %s, duracao =%s WHERE id =%s', (name_course, duration, id))
            else:          
                cursor.execute('INSERT INTO curso (nome_curso, duracao ) VALUES (%s, %s)', (name_course, duration))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
            
    def get_by_id(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute('SELECT id, nome_curso, duracao FROM curso WHERE id = %s', (id,))
        record = cursor.fetchone()
        conn.close()
        return record
    
    def delete(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        try:
            cursor.execute('DELETE FROM curso WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()