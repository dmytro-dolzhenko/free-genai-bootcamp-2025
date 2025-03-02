from duckduckgo_search import DDGS
from typing import List, Dict
import requests
import logging
import MeCab
from html2text import HTML2Text
import unidic

class ToolsManager:
    """
    A class that manages various tools for web search, content extraction, and text processing.
    """
    
    def __init__(self):
        """Initialize the ToolsManager with necessary components."""
        self.tagger = MeCab.Tagger()  # Use default configuration

    def search_web(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search the web using DuckDuckGo.
        
        Args:
            query (str): Search query
            max_results (int): Maximum number of results to return
            
        Returns:
            List[Dict]: List of search results with title and URL
        """
        try:
            # Ensure query is properly encoded in UTF-8
            query = query.encode('utf-8').decode('utf-8')
            results = DDGS().text(query, max_results)
            if results:
                return [
                    {
                        'title': result['title'].encode('utf-8').decode('utf-8'),
                        'url': result['href']
                    }
                    for result in results
                ]
            else:
                return []
        except Exception as e:
            logging.error(f"Search error: {str(e)}")
            return []

    def extract_content(self, url: str) -> str:
        """
        Extract content from a webpage using HTML2Text.
        
        Args:
            url (str): URL to extract content from
            
        Returns:
            str: Extracted text content
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
                'Accept-Charset': 'utf-8'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.encoding = response.apparent_encoding or 'utf-8'
            response.raise_for_status()
            
            h = HTML2Text()
            h.ignore_links = True
            h.ignore_images = True
            h.ignore_emphasis = True
            h.ignore_tables = True
            h.body_width = 0
            h.unicode_snob = True
            h.skip_internal_links = True
            h.inline_links = False
            h.protect_links = False
            
            content = h.handle(response.text)
            
            # Clean up content
            content = content.encode('utf-8').decode('utf-8')
            content = content.replace('#', '')
            content = content.replace('*', '')
            content = content.replace('_', '')
            content = content.replace('\\', '')
            content = content.replace('\r', '\n')
            content = '\n'.join(line.strip() for line in content.splitlines() if line.strip())
            
            # Return the content directly
            return content[:1000] if len(content) > 1000 else content
            
        except Exception as e:
            logging.error(f"Error extracting content from {url}: {str(e)}")
            return ''

    def tokenize_japanese(self, text: str) -> List[str]:
        """
        Tokenize Japanese text into individual words with their readings and parts of speech.
        
        Args:
            text (str): Japanese text to tokenize
            
        Returns:
            List[Dict[str, str]]: List of dictionaries containing word information
        """
        try:
            # Validate input
            if not text or not isinstance(text, str):
                logging.warning("Empty or invalid text provided for tokenization")
                return []
            
            # Clean input text
            text = text.strip()
            if not text:
                logging.warning("Text contains only whitespace")
                return []
            
            # Define characters to filter out
            filter_chars = {'、', '。', '！', '？', '．', '，', '…', '「', '」', '『', '』', '（', '）', '【', '】'}
            
            # Parse the text
            words = []
            for line in self.tagger.parse(text).split("\n"):
                if line == "EOS" or not line.strip():
                    continue

                parts = line.split("\t")
                if len(parts) < 2:
                    continue  # Skip invalid lines

                word = parts[0]
                features = parts[1].split(",")  # POS information
                pos = features[0]  # Get the part-of-speech (POS) category

                # Skip punctuation and specific characters
                if pos != "記号" and word not in filter_chars:
                    words.append(word)

            return words
            
        except Exception as e:
            logging.error(f"Error tokenizing text: {str(e)}")
            return []

    def available_tools(self):
        return {
                "search_web": self.search_web,
                "extract_content": self.extract_content,
                "tokenize_japanese": self.tokenize_japanese
                }
    # ... rest of the methods remain the same ... 

if __name__ == "__main__":
    tools = ToolsManager()
    print(tools.tokenize_japanese("こんにちは、世界"))