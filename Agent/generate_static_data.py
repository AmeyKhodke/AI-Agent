#!/usr/bin/env python3
"""
Script to generate static JSON data for the BookFest AI Assistant
This allows the app to work on static hosting platforms like Netlify
"""

import json
import os
import sys

# Add the current directory to the path so we can import bookfest_agent
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bookfest_agent import BookFestAgent

def generate_static_data():
    """Generate static JSON data from the BookFestAgent"""
    # Initialize the agent
    agent = BookFestAgent()
    
    # Generate all the data
    data = {
        "greeting": agent.get_greeting(),
        "menu": agent.display_main_menu(),
        "schedule": agent.get_schedule_info(),
        "social_media": {
            "youtube": agent.get_social_media_links('youtube'),
            "facebook": agent.get_social_media_links('facebook'),
            "instagram": agent.get_social_media_links('instagram'),
            "website": agent.get_social_media_links('website')
        },
        "location": agent.get_location_info(),
        "more_details": agent.get_more_details()
    }
    
    # Save to static directory
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    data_file = os.path.join(static_dir, 'bookfest_data.json')
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Static data generated and saved to {data_file}")
    return data

if __name__ == "__main__":
    generate_static_data()