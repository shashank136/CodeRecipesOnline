from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/algo_ds')
def algo_ds():
	return render_template('algo_ds.html')

# all routes for algorithms: start

@app.route('/algo_ds/algorithms')
def algorithms():
	return render_template('algorithms.html')

@app.route('/algo_ds/algorithms/insertion_sort')
def insertion():
	return render_template('insertion.html')

@app.route('/algo_ds/algorithms/merge_sort')
def merge():
	return render_template('Merge.html')

@app.route('/algo_ds/algorithms/bubble_sort')
def bubble():
	return render_template('bubble.html')

@app.route('/algo_ds/algorithms/heap_sort')
def heap():
	return render_template('heap.html')

@app.route('/algo_ds/algorithms/quick_sort')
def quick():
	return render_template('quick.html')

@app.route('/algo_ds/algorithms/bucket_sort')
def bucket():
	return render_template('bucket.html')

@app.route('/algo_ds/algorithms/counting_sort')
def count():
	return render_template('count.html')

# end of routes for algorithms

@app.route('/algo_ds/data_structures')
def ds():
	return render_template('ds.html')

# start of routes for data structures

@app.route('/algo_ds/data_structures/stacks')
def stack():
	return render_template('stack.html')

@app.route('/algo_ds/data_structures/queues')
def queue():
	return render_template('queue.html')

# end of routes for data structures.

@app.route('/about', methods=['POST'])
def contact_form():
	email = request.form['email']
	comment = request.form['comment']
	print(email)
	print(comment)
	return render_template('about.html')
		
if __name__ == '__main__':
	app.run()