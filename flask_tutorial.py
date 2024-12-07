from flask import Flask, render_template,request
import search4letters

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'here are your results'
    results = str(search4letters.search4letters(phrase,letters))
    return render_template('reuslts.html',the_title=title,the_phrase=phrase,the_letters=letters,the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('index.html', the_title='welcome to search4letters on the web')

if __name__ == '__main__':
    app.run(debug=True)
