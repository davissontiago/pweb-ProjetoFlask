from flask import Flask, render_template
from dao.student_dao import StudentDAO
from dao.teacher_dao import TeacherDAO
from dao.course_dao import CourseDAO
from dao.class_dao import ClassDAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/students') 
def list_students(): 
    dao = StudentDAO() 
    data = dao.get_all()
    return render_template('students/students.html', data=data)

@app.route('/teachers') 
def list_teachers(): 
    dao = TeacherDAO() 
    data = dao.get_all()
    return render_template('teachers/teachers.html', data=data)

@app.route('/courses') 
def list_courses(): 
    dao = CourseDAO() 
    data = dao.get_all()
    return render_template('courses/courses.html', data=data)

@app.route('/classes') 
def list_classes(): 
    dao = ClassDAO() 
    data = dao.get_all()
    return render_template('classes/classes.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)