from flask import Flask, render_template_string, request
import sqlite3

# Create a Flask app
app = Flask(__name__)

# Initialize the database and create a table
def init_db():
    conn = sqlite3.connect('buyers.db')  # Create or connect to a SQLite database
    cursor = conn.cursor()
    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS buyers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            buyer_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Route for the form
@app.route('/')
def form():
    return '''
        <form action="/submit" method="POST">
            Buyer: <input type="text" name="buyer_name">
            <input type="submit" value="Submit">
        </form>
    '''

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_buyer():
    buyer_name = request.form['buyer_name']  # Get the buyer's name from the form
    # Save the buyer name to the database
    conn = sqlite3.connect('buyers.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO buyers (buyer_name) VALUES (?)', (buyer_name,))
    conn.commit()
    conn.close()
    
    return f'Thank you, {buyer_name}, for your order!'

# Run the app
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
