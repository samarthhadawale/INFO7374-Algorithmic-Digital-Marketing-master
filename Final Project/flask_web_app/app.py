import json
import flask
from api import BookSimilarity

app = flask.Flask(__name__)
booksim = BookSimilarity()

@app.route('/')
def index():
	return flask.render_template('main.html')

@app.route('/recommendindex')
def recindex():
        return flask.render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	search = flask.request.args.get('q')
	filtered_books = list(booksim.search(search)['title'].values)
	return flask.jsonify(matching_results=filtered_books)

@app.route('/recommend')
def recommend():
	searchText = flask.request.args.get('jsdata')

	output = ''
	if searchText:
		print(f'Search text: {searchText}')
		results = booksim.recommend(searchText)
		if results is not None:
			output = json.loads(results[['title', 'url']].to_json(orient='records'))#results.title.values

	print(output)
	return flask.render_template('results.html', recommendations=output)

@app.route('/clv')
def clv():
        return flask.render_template('clv.html')

 
@app.route('/rfm')
def rfm():
        return flask.render_template('rfm.html')

@app.route('/predictsales')
def predictsales():
        return flask.render_template('predictsales.html')

@app.route('/analytics')
def analytics():
        return flask.render_template('goodreads.html')

@app.route('/predictiveanalytics')
def predictanalysis():
        return flask.render_template('shiny.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

