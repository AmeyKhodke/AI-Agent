from flask import Flask, render_template, request, jsonify
import os

# Import our BookFestAgent
from bookfest_agent import BookFestAgent

app = Flask(__name__)

# Initialize the agent
agent = BookFestAgent()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/greeting')
def greeting():
    """API endpoint to get the greeting message"""
    return jsonify({'message': agent.get_greeting()})

@app.route('/api/menu')
def menu():
    """API endpoint to get the main menu"""
    return jsonify({'menu': agent.display_main_menu()})

@app.route('/api/info', methods=['POST'])
def get_info():
    """API endpoint to get information based on user selection"""
    data = request.json
    option = data.get('option')
    
    if option == 1:
        return jsonify({'response': agent.get_schedule_info()})
    elif option == 2:
        return jsonify({'response': agent.get_social_media_links('youtube')})
    elif option == 3:
        return jsonify({'response': agent.get_social_media_links('facebook')})
    elif option == 4:
        return jsonify({'response': agent.get_social_media_links('instagram')})
    elif option == 5:
        return jsonify({'response': agent.get_social_media_links('website')})
    elif option == 6:
        return jsonify({'response': agent.get_location_info()})
    elif option == 7:
        return jsonify({'response': agent.get_more_details()})
    else:
        return jsonify({'response': 'Invalid option. Please select a number between 1 and 7.'})

@app.route('/api/query', methods=['POST'])
def process_query():
    """API endpoint to process custom queries"""
    data = request.json
    query = data.get('query', '')
    response = agent.process_user_query(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Move index.html to templates directory
    if os.path.exists('index.html'):
        os.rename('index.html', 'templates/index.html')
    
    app.run(debug=True, host='0.0.0.0', port=5000)