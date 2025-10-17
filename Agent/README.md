# Pune Book Festival 2025 AI Assistant

An intelligent AI assistant for the Pune Book Festival 2025 that retrieves and presents information from the official website. This web-based assistant provides festival-goers with quick access to schedules, locations, social media links, and other important information.

## Features

- 📅 **Festival Schedule** - Get detailed information about daily events
- 📍 **Location Information** - Find venue details and directions
- 🔗 **Social Media Links** - Direct access to YouTube, Facebook, Instagram
- 🌐 **Official Website** - Quick link to the festival website
- 📖 **Detailed Information** - Learn more about the festival highlights
- 💬 **Interactive Chat Interface** - User-friendly chatbot experience

## Technologies Used

- **Python** - Core programming language
- **Flask** - Web framework for the backend
- **HTML/CSS/JavaScript** - Frontend interface
- **BeautifulSoup** - Web scraping for data extraction
- **Requests** - HTTP library for API calls

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bookfest-agent.git
   cd bookfest-agent
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Access the web interface at `http://localhost:5000`
2. Type "hi", "hello", or "hey" to see the main menu
3. Click on any menu option to get detailed information
4. For options 1 (Schedule) and 7 (More Details), information will be displayed in the chat
5. For options 2-6 (social media links), external websites will open in new tabs

## Project Structure

```
bookfest-agent/
│
├── app.py                 # Flask web application
├── bookfest_agent.py      # Core AI agent logic
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── USAGE.txt             # Usage instructions
├── start_agent.bat       # Windows batch script to start the server
├── Procfile              # Heroku deployment configuration
├── runtime.txt           # Python runtime version for Heroku
├── setup.py              # Package setup file
├── LICENSE               # License file
├── .gitignore            # Git ignore file
│
├── templates/
│   └── index.html        # Main web interface
│
├── docs/
│   └── deployment.md     # Deployment guide
│
└── tests/
    └── test_bookfest_agent.py  # Unit tests
```

## Customization

You can customize the assistant by modifying:

- `bookfest_agent.py` - Update the knowledge base and responses
- `templates/index.html` - Modify the UI/UX design
- `app.py` - Change API endpoints or add new features

## Deployment

This application can be deployed to various platforms:

- **Heroku** - Using Procfile and requirements.txt
- **PythonAnywhere** - Direct upload and configuration
- **AWS Elastic Beanstalk** - Using the EB CLI
- **Google Cloud Platform** - Using App Engine

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - your.email@example.com

Project Link: [https://github.com/yourusername/bookfest-agent](https://github.com/yourusername/bookfest-agent)