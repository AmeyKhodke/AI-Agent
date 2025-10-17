# Pune Book Festival AI Agent

An AI assistant that provides information about the Pune Book Festival 2025 using the official website as a knowledge base.

## Features

- Displays a user-friendly menu with festival information
- Provides schedule details
- Shares social media links (YouTube, Facebook, Instagram)
- Shows website and location information
- Offers detailed information about the festival
- Both command-line and web interfaces

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Command Line Interface

Run the AI agent in command-line mode:

```bash
python bookfest_agent.py
```

The agent will greet you and display the main menu. Select an option by entering the corresponding number (1-7).

To exit the program, type 'quit' when prompted for input.

### Option 2: Web Interface

Run the Flask web application:

```bash
python app.py
```

Then open your browser and go to http://127.0.0.1:5000 to access the web interface.

Alternatively, you can run the start_agent.bat file on Windows.

To stop the server, press Ctrl+C in the terminal.

## How It Works

The AI agent fetches information from the Pune Book Festival website (https://68cf070d6f667a1e09ba881f--bookfest2025.netlify.app/) and stores it in a knowledge base. When users select menu options, the agent provides relevant information extracted from this knowledge base.

## Project Structure

- `bookfest_agent.py`: Main AI agent implementation
- `app.py`: Flask web application
- `requirements.txt`: Python dependencies
- `templates/index.html`: Web interface
- `start_agent.bat`: Windows batch file to start the web interface
- `USAGE.txt`: Usage instructions

## Customization

You can modify the `BookFestAgent` class in `bookfest_agent.py` to:
- Add new menu options
- Enhance information extraction
- Improve response formatting
- Add new features

## Support

For issues or feature requests, please open an issue in this repository.