import unittest
from bookfest_agent import BookFestAgent

class TestBookFestAgent(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.agent = BookFestAgent()
    
    def test_get_greeting(self):
        """Test that greeting message is returned."""
        greeting = self.agent.get_greeting()
        self.assertIsInstance(greeting, str)
        self.assertGreater(len(greeting), 0)
    
    def test_display_main_menu(self):
        """Test that main menu is returned."""
        menu = self.agent.display_main_menu()
        self.assertIsInstance(menu, str)
        self.assertGreater(len(menu), 0)
    
    def test_get_schedule_info(self):
        """Test that schedule information is returned."""
        schedule = self.agent.get_schedule_info()
        self.assertIsInstance(schedule, str)
        self.assertGreater(len(schedule), 0)
    
    def test_get_social_media_links(self):
        """Test that social media links are returned."""
        youtube_link = self.agent.get_social_media_links('youtube')
        self.assertIsInstance(youtube_link, str)
        self.assertIn('youtube.com', youtube_link.lower())
    
    def test_get_location_info(self):
        """Test that location information is returned."""
        location = self.agent.get_location_info()
        self.assertIsInstance(location, str)
        self.assertGreater(len(location), 0)
    
    def test_get_more_details(self):
        """Test that more details are returned."""
        details = self.agent.get_more_details()
        self.assertIsInstance(details, str)
        self.assertGreater(len(details), 0)
    
    def test_process_user_query(self):
        """Test that user queries are processed."""
        query_result = self.agent.process_user_query('schedule')
        self.assertIsInstance(query_result, str)
        self.assertGreater(len(query_result), 0)

if __name__ == '__main__':
    unittest.main()