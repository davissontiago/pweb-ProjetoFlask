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
    
    def save(self, name, age, city, id=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:            
            if id:
                cursor.execute('UPDATE aluno SET nome = %s, idade =%s, cidade = %s WHERE id =%s', (name, age, city, id))
            else:
                cursor.execute('INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)', (name, age, city))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
            
    def get_by_id(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute('SELECT id, nome, idade, cidade FROM aluno WHERE id = %s', (id,))
        record = cursor.fetchone()
        conn.close()
        return record