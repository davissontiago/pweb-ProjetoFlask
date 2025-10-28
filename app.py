from flask import Flask, render_template
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aluno') 
def listar_aluno(): 
    dao = AlunoDAO() 
    lista = dao.listar()
    return render_template('aluno/listar_aluno.html', lista=lista)

@app.route('/professor') 
def listar_professor(): 
    dao = ProfessorDAO() 
    lista = dao.listar()
    return render_template('professor/listar_professor.html', lista=lista)

@app.route('/curso') 
def listar_curso(): 
    dao = CursoDAO() 
    lista = dao.listar()
    return render_template('curso/listar_curso.html', lista=lista)

@app.route('/turma') 
def listar_turma(): 
    dao = TurmaDAO() 
    lista = dao.listar()
    return render_template('turma/listar_turma.html', lista=lista)

if __name__ == "__main__":
    app.run(debug=True)