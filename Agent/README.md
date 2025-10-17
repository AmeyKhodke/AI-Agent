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
   git clone <repository-url>
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
├── netlify.toml          # Netlify deployment configuration
│
└── templates/
    └── index.html        # Main web interface
```

## Deployment to Netlify

This application can be deployed to Netlify using the following steps:

1. Create a Netlify account at [netlify.com](https://netlify.com)
2. Install the Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```
3. Login to Netlify:
   ```bash
   netlify login
   ```
4. Initialize your project:
   ```bash
   netlify init
   ```
5. Deploy your site:
   ```bash
   netlify deploy
   ```
6. For production deployment:
   ```bash
   netlify deploy --prod
   ```

Alternatively, you can deploy by:
1. Going to [netlify.com](https://netlify.com)
2. Clicking "New site from Git"
3. Connecting your Git provider (GitHub, GitLab, or Bitbucket)
4. Selecting your repository
5. Configuring the build settings:
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `templates`
6. Clicking "Deploy site"

## Customization

You can customize the assistant by modifying:

- `bookfest_agent.py` - Update the knowledge base and responses
- `templates/index.html` - Modify the UI/UX design
- `app.py` - Change API endpoints or add new features

## License

This project is for educational purposes.

## Contact

Your Name - your.email@example.com