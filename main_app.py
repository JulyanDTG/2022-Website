from flask import Flask, render_template


app = Flask(__name__)



posts = [
    
    {
      'author': 'Julyan Balicao',
      'title': 'Blog Post 1',
      'content': 'First post content',
      'date_posted': 'February 2, 2022'
    },
    
    {
      'author': 'Mark Price',
      'title': 'Blog Post 2',
      'content': 'Second post content',
      'date_posted': 'February 4, 2022'
    },
    
    {
      'author': 'Hannah Williams',
      'title': 'Blog Post 3',
      'content': 'Third post content',
      'date_posted': 'February 6, 2022'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
  
  
if __name__=='__main__':
    app.run(debug=True)