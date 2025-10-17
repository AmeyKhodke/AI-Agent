# Deployment Guide

This guide will help you deploy the Pune Book Festival AI Assistant to various platforms.

## Table of Contents
- [Heroku Deployment](#heroku-deployment)
- [PythonAnywhere Deployment](#pythonanywhere-deployment)
- [AWS Elastic Beanstalk](#aws-elastic-beanstalk)
- [Google Cloud Platform](#google-cloud-platform)
- [Local Development](#local-development)

## Heroku Deployment

1. Create a Heroku account at [heroku.com](https://heroku.com)
2. Install the Heroku CLI
3. Login to Heroku CLI:
   ```bash
   heroku login
   ```
4. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
5. Set the stack to container:
   ```bash
   heroku stack:set container
   ```
6. Deploy the app:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```
7. Open the app:
   ```bash
   heroku open
   ```

## PythonAnywhere Deployment

1. Create a PythonAnywhere account at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your project files using the file browser or Git
3. Open a bash console and navigate to your project directory
4. Create a virtual environment:
   ```bash
   mkvirtualenv bookfest-agent --python=/usr/bin/python3.9
   pip install -r requirements.txt
   ```
5. Configure the web app:
   - Go to the Web tab
   - Add a new web app
   - Choose Manual configuration
   - Select Python 3.9
   - Edit the WSGI configuration file:
     ```python
     import sys
     path = '/home/yourusername/bookfest-agent'
     if path not in sys.path:
         sys.path.append(path)
     
     from app import app as application
     ```
6. Reload the web app

## AWS Elastic Beanstalk

1. Install the EB CLI
2. Initialize your EB application:
   ```bash
   eb init
   ```
3. Create an environment and deploy:
   ```bash
   eb create bookfest-agent-env
   eb deploy
   ```
4. Open the app:
   ```bash
   eb open
   ```

## Google Cloud Platform

1. Install the Google Cloud SDK
2. Create a new project in the GCP Console
3. Enable the App Engine API
4. Deploy the app:
   ```bash
   gcloud app deploy
   ```
5. View your app:
   ```bash
   gcloud app browse
   ```

## Local Development

To run the application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bookfest-agent.git
   cd bookfest-agent
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

## Environment Variables

The application uses the following environment variables:

- `PORT` - Port number for the web server (default: 5000)

## Troubleshooting

If you encounter issues during deployment:

1. Check that all dependencies are listed in `requirements.txt`
2. Ensure the `Procfile` is correctly configured
3. Verify the Python runtime version in `runtime.txt`
4. Check application logs for error messages