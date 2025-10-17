import requests
from bs4 import BeautifulSoup
import re
import json
from typing import Dict, List, Optional

class BookFestAgent:
    def __init__(self, website_url: str = "https://68cf070d6f667a1e09ba881f--bookfest2025.netlify.app/"):
        """
        Initialize the BookFest AI Agent with the knowledge base URL
        """
        self.website_url = website_url
        self.knowledge_base = {}
        self._load_knowledge_base()
    
    def _load_knowledge_base(self):
        """
        Load information from the website into the knowledge base
        """
        try:
            response = requests.get(self.website_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract key information
            self.knowledge_base['title'] = soup.find('h1').get_text() if soup.find('h1') else "Pune Book Festival 2025"
            self.knowledge_base['dates'] = "May 1-9, 2025"
            self.knowledge_base['location'] = "FC, New Delhi"
            
            # Extract about section
            about_section = soup.find('div', {'id': 'about'}) or soup.find(string=re.compile("About"))
            if about_section:
                about_parent = about_section.parent if hasattr(about_section, 'parent') else about_section.find_parent()
                self.knowledge_base['about'] = about_parent.get_text()[:500] + "..." if about_parent else ""
            
            # Store the full HTML for more detailed queries
            self.knowledge_base['full_content'] = str(soup)
            
        except Exception as e:
            print(f"Error loading knowledge base: {e}")
            # Fallback to default information
            self.knowledge_base = {
                'title': 'Pune Book Festival 2025',
                'dates': 'May 1-9, 2025',
                'location': 'FC, New Delhi',
                'about': 'The Pune Book Festival is India\'s largest book festival, attracting over 10 lakh visitors annually.',
                'full_content': ''
            }
    
    def get_greeting(self) -> str:
        """
        Return the greeting message for the agent
        """
        return "Hello! How can I assist you with information from our Pune Bookfest today?"
    
    def display_main_menu(self) -> str:
        """
        Display the main menu as requested
        """
        menu = f"""
📍 MAIN MENU

1️⃣ Schedule  
 • Day-wise Schedule  

2️⃣ YouTube  

3️⃣ Facebook  

4️⃣ Instagram  

5️⃣ Website  

6️⃣ Google Location  

7️⃣ More Details  

"""
        return menu
    
    def get_schedule_info(self) -> str:
        """
        Provide schedule information
        """
        return f"""
🗓️ SCHEDULE INFORMATION

The Pune Book Festival 2025 will be held from {self.knowledge_base.get('dates', 'May 1-9, 2025')}.

The festival features:
- Author sessions with renowned writers
- Storytelling sessions
- Poetry recitations
- Cultural performances
- Book signing events
- Literary treasure hunt
- Children's corner activities
- Panel discussions on publishing and literature

For detailed day-wise schedule, please visit our website or contact our team.
"""
    
    def get_social_media_links(self, platform: str) -> str:
        """
        Provide social media information (placeholder)
        """
        links = {
            'youtube': '🔗 YouTube: https://www.youtube.com/@PuneBookFest',
            'facebook': '🔗 Facebook: https://www.facebook.com/PuneBookFest',
            'instagram': '🔗 Instagram: https://www.instagram.com/PuneBookFest',
            'website': f'🌐 Website: {self.website_url}'
        }
        
        if platform.lower() in links:
            return links[platform.lower()]
        else:
            return "Please specify a platform (YouTube, Facebook, Instagram, or Website)"
    
    def get_location_info(self) -> str:
        """
        Provide location information
        """
        location = self.knowledge_base.get('location', 'FC, New Delhi')
        return f"""
📍 LOCATION INFORMATION

Event Venue: {location}

To find us on Google Maps:
🔗 Google Location: https://maps.google.com/?q={location.replace(' ', '+')}

The venue is well-connected and easily accessible by public transport.
For detailed directions, please visit our website.
"""
    
    def get_more_details(self) -> str:
        """
        Provide additional information about the festival
        """
        return f"""
📖 MORE DETAILS ABOUT {self.knowledge_base.get('title', 'PUNE BOOK FESTIVAL 2025').upper()}

{self.knowledge_base.get('about', 'The Pune Book Festival stands as a testament to India\'s rich literary heritage and vibrant reading culture. Since its inception, we have grown to become the world\'s largest book festival, attracting over 10 lakh visitors annually.')}

Key Highlights:
- Over 10 lakh visitors expected
- ₹40+ Crores in book sales
- 10 days of literary celebration
- Content in 10+ languages
- Special activities for children
- Cultural performances
- Book shopping at special festival prices

Partners and Sponsors:
- National Book Trust India (Government Partner)
- Samarth Yuva Foundation (Strategic Partner)
- Fergusson College (Education Partner)
- Pune Municipal Corporation (Municipal Partner)
- Penguin Random House (Publishing Partner)
- The Hindu (Media Partner)

For partnership opportunities and more information, please visit our website.
"""
    
    def process_user_query(self, query: str) -> str:
        """
        Process user queries and provide relevant information
        """
        query = query.lower()
        
        if 'schedule' in query:
            return self.get_schedule_info()
        elif 'youtube' in query:
            return self.get_social_media_links('youtube')
        elif 'facebook' in query:
            return self.get_social_media_links('facebook')
        elif 'instagram' in query:
            return self.get_social_media_links('instagram')
        elif 'website' in query:
            return self.get_social_media_links('website')
        elif 'location' in query or 'google' in query:
            return self.get_location_info()
        elif 'detail' in query or 'more' in query:
            return self.get_more_details()
        else:
            return "I can help you with information about the Pune Book Festival. Please select an option from the menu or ask about schedule, social media, location, or other details."

def main():
    """
    Main function to run the BookFest AI Agent
    """
    agent = BookFestAgent()
    
    print(agent.get_greeting())
    print(agent.display_main_menu())
    
    while True:
        user_input = input("\nPlease select an option (1-7) or type 'quit' to exit: ").strip()
        
        if user_input.lower() == 'quit':
            print("Thank you for using the Pune Book Festival AI Assistant. Have a great day!")
            break
        
        if user_input == '1':
            print(agent.get_schedule_info())
        elif user_input == '2':
            print(agent.get_social_media_links('youtube'))
        elif user_input == '3':
            print(agent.get_social_media_links('facebook'))
        elif user_input == '4':
            print(agent.get_social_media_links('instagram'))
        elif user_input == '5':
            print(agent.get_social_media_links('website'))
        elif user_input == '6':
            print(agent.get_location_info())
        elif user_input == '7':
            print(agent.get_more_details())
        else:
            print("Invalid option. Please select a number between 1 and 7, or type 'quit' to exit.")

if __name__ == "__main__":
    main()