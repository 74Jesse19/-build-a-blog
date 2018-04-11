from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['DEBUG'] = True
#setup connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:vera2012@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app) #create object constructor

#using class called db.model so all objects inherit from this class
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)#id is an instance of this column
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))
   

    def __init__(self, title, body): #this is a constructor that initializes
        self.title = title
        self.body= body

@app.route('/blogPage', methods=['POST','GET'])  
def blogPage():
    btitle = Blog.query.all()
    body = Blog.query.all()
    return render_template('blogPage.html',title= " ADD BLOG ENTRY", btitle=btitle, body=body)
  



@app.route('/', methods=['POST','GET'])
def index():
    btitle=""
    body=""
    

    if request.method == 'POST':
        # set variables to retrieve and store user input for title and body
        blogtitle = request.form['btitle']   
        blogpost = request.form['body']
        
        new_title = Blog(blogtitle,blogpost)  #makes new object for title and body 
        db.session.add(new_title) #adds to database
        db.session.commit()# dont forget this you need it to commit add
   
        btitle = Blog.query.all()
        body = Blog.query.all()
        return redirect('/blogPage')

    else:
        return render_template('index.html')

    #else:
        #btitle = Blog.query.all()
        #body = Blog.query.all()
       

        #return render_template('index.html',title= " ADD BLOG ENTRY", btitle=btitle, body=body)





if __name__ == '__main__': #if you want to reference this from somewhere else this lets you import 
    app.run()


        




