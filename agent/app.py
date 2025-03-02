import requests
import json
from typing import Dict, Any, List
from tools_manager import ToolsManager
from tools_config_loader import load_tool_configs
from models import TutorResponse

class LanguageTutorAgent:
    """An AI language tutor agent that helps learn Japanese through songs"""
    
    def __init__(self, model: str, max_messages: int = 10):
        """
        Initialize the language tutor agent
        
        Args:
            model: Name of the Ollama model to use
            max_messages: Maximum number of messages in conversation
        """
        self.model = model
        self.tools = ToolsManager()
        self.tool_configs = load_tool_configs()
        self.base_url = "http://localhost:8008/api/chat"  # Fixed port number
        self.max_messages = max_messages
        self.current_song_info = {"title": "", "artist": ""}
        
        # Updated system prompt to emphasize complete vocabulary information
        self.system_prompt = """You are a Japanese tutor. You must follow these steps in order:

STEP 1: Search for song lyrics provided by the user
Use: search_web({"query": "<song_title> 歌詞"})
IMPORTANT: Do not modify the song title.

STEP 2: Extract song lyrics content only from the whole text
Use: extract_content({"url": "<first_search_result_url>"})
IMPORTANT: 
- Look for the actual song lyrics section in the extracted content
- The lyrics start after "シェア" in this case
- Example lyrics from the content:
  幼い微熱を下げられないまま 神様の影を恐れて
  隠したナイフが似合わない僕を おどけた歌でなぐさめた
  ...
- Use ONLY these actual lyrics for the next step

STEP 3: Analyze vocabulary
Use: tokenize_japanese({"text": "<ONLY THE ACTUAL LYRICS TEXT>"})
IMPORTANT:
- Pass ONLY the actual song lyrics to tokenize_japanese
- Example of what to pass:
  幼い微熱を下げられないまま 神様の影を恐れて
  隠したナイフが似合わない僕を おどけた歌でなぐさめた
  ...
- After getting tokens, you MUST create a vocabulary entry for EACH token
- The vocabulary list should have the same number of entries as tokens returned

IMPORTANT FOR VOCABULARY ANALYSIS:
- Create a vocabulary entry for EVERY token returned by tokenize_japanese
- The vocabulary list length should match the number of tokens
- For each token, you MUST provide:
  * word (the exact token from tokenize_japanese)
  * reading (in hiragana)
  * meaning (accurate English translation)
  * part of speech (noun, verb, adjective, etc.)
  * example (a sentence from lyrics containing this word)
  * English translation of the example

Example vocabulary entry format:
{
    "word": "幼い",  // Exact token from tokenize_japanese
    "reading": "おさない",
    "meaning": "young, childish",
    "type": "adjective",
    "example": {
        "japanese": "幼い微熱を下げられないまま",
        "english": "Unable to lower the slight fever from childhood"
    }
}

Rules:
1. Must complete all 3 steps in order
2. Must use next tool after each response
3. Keep examples short and educational
4. Do not reproduce full lyrics
5. Make sure provided translations are correct and accurate
6. Always preserve Japanese characters in their original form
7. NEVER leave reading, meaning, or example fields empty
8. Process ALL tokens from tokenize_japanese - do not skip any words
9. The vocabulary list must contain ALL tokens"""

    def _call_ollama(self, messages: List[Dict[str, str]], format_schema: dict = None) -> Dict[str, Any]:
        """Make a call to Ollama API"""
        try:            
            data = {
                "model": self.model,
                "messages": messages,
                "stream": False,
                "tools": self.tool_configs,
                "options": {
                    "num_ctx": 8192,
                    "temperature": 0.1,
                    "raw": True    # Preserve raw text without modifications
                }
            }
            
            if format_schema is not None:
                data["format"] = format_schema

            # Convert to JSON with proper UTF-8 handling
            json_data = json.dumps(data, ensure_ascii=False)
            
            response = requests.post(
                self.base_url, 
                data=json_data.encode('utf-8'),  # Explicitly encode as UTF-8
                timeout=1200,
                headers={
                    'Content-Type': 'application/json; charset=utf-8',
                    'Accept': 'application/json; charset=utf-8'
                }
            )
            response.raise_for_status()
            
            # Ensure proper UTF-8 decoding of the response
            return json.loads(response.content.decode('utf-8'), strict=False)
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to Ollama: {str(e)}")

    def process_song_request(self, song_title: str) -> str:
        """Process a song request and return vocabulary analysis"""
        try:           
            # Create a more explicit instruction to preserve the song title exactly
            system_prompt = self.system_prompt + f"\n\nIMPORTANT: For this request, use EXACTLY this search query: search_web({{\"query\": \"{song_title} 歌詞\"}})"
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Analyze this song: {song_title}"}
            ]

            print(f"Messages: {json.dumps(messages, ensure_ascii=False)}")
            
            # Add debug logging
            print(f"\nProcessing song request: {song_title}")
            print(f"Expected search query: search_web({{\"query\": \"{song_title} 歌詞\"}})")
            
            goal_reached = False
            
            while not goal_reached and len(messages) < self.max_messages:
                response = self._call_ollama(messages)
                
                # Handle tool calls
                if response.get("message", {}).get("tool_calls"):
                    tool_calls = response["message"]["tool_calls"]
                    for tool_call in tool_calls:
                        function = tool_call.get("function", {})                    
                        tool_name = function.get("name")
                        if tool_name in self.tools.available_tools():
                            tool_args = function.get("arguments", {})
                        
                            print(f"\n→ Tool Call:")
                            print(f"  Name: {tool_name}")
                            print(f"  Arguments: {json.dumps(tool_args, ensure_ascii=False)}")
                        
                            try:
                                print("  Executing tool...")
                                result = self._execute_tool(tool_name, tool_args)
                            
                                # Ensure proper UTF-8 handling when logging
                                result_preview = result
                                print(f"  Result: {json.dumps(result_preview, ensure_ascii=False)}")
                                print("  ✓ Tool execution successful\n")
                                                            
                                messages.append(response.get("message"))
                                
                                # Convert result to string with proper UTF-8 handling
                                if isinstance(result, dict) or isinstance(result, list):
                                    result_str = json.dumps(result, ensure_ascii=False)
                                else:
                                    result_str = str(result)
                                
                                messages.append({'role': 'tool', 'content': result_str, 'name': tool_name})
                                                            
                            except Exception as e:
                                print(f"  ✗ Tool execution failed: {str(e)}")
                                messages.append({
                                    "role": "system", 
                                    "content": f"Tool execution failed: {str(e)}. Please try again with the next tool."
                                })            
                else:
                    goal_reached = True

            final_response = self._call_ollama(messages, format_schema=TutorResponse.model_json_schema())
            # Decode the JSON response to ensure proper UTF-8 handling
            final_content = final_response.get("message", {}).get("content", "")
            
            # First parse the content if it's a string
            if isinstance(final_content, str):
                try:
                    final_content = json.loads(final_content)
                except json.JSONDecodeError:
                    pass

            # Return properly formatted JSON with Japanese characters preserved
            return json.dumps(
                final_content,
                ensure_ascii=False,  # This ensures Japanese characters are not escaped
                indent=2,
                default=str
            )

        except Exception as e:
            return json.dumps({"error": str(e)}, ensure_ascii=False, indent=2)

    def _execute_tool(self, tool_name: str, tool_args: Dict[str, Any]) -> Any:
        """Execute a tool based on its name and arguments"""
        try:
            # Ensure tool_args values are properly encoded strings
            if tool_name == "search_web" and "query" in tool_args:
                tool_args["query"] = str(tool_args["query"])
                print(f"Search query: {tool_args['query']}")
            
            if tool_name == "search_web":
                result = self.tools.search_web(**tool_args)
            elif tool_name == "extract_content":
                result = self.tools.extract_content(**tool_args)
                # Add debug logging for extracted content
                print("\nExtracted Content:")
                print(result[:500] + "..." if len(result) > 500 else result)  # Show first 500 chars
            elif tool_name == "tokenize_japanese":
                # Verify the input text
                print("\nText to tokenize:")
                print(tool_args.get("text", "")[:500] + "..." if len(tool_args.get("text", "")) > 500 else tool_args.get("text", ""))
                
                result = self.tools.tokenize_japanese(**tool_args)
                print("\nTokenization Results:")
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
            
            return result
            
        except Exception as e:
            raise RuntimeError(f"Tool execution failed - {tool_name}: {str(e)}")

    def interactive_session(self):
        """Start an interactive tutoring session"""
        print("Welcome to Japanese Song Language Tutor!")
        print("Enter a Japanese song title to learn vocabulary (or 'quit' to exit)")
        
        while True:
            try:
                song_title = input("\nSong title: ").strip()
                if song_title.lower() == 'quit':
                    break
                    
                if not song_title:
                    print("Please enter a song title")
                    continue
                
                # Process the song request with proper UTF-8 handling
                result = self.process_song_request(song_title)
                
                # Display the results with a clear header
                print("\n=== Analysis Results ===")
                
                # Parse and format the JSON with proper character handling
                try:
                    parsed_json = json.loads(result)
                    formatted_result = json.dumps(
                        parsed_json,
                        ensure_ascii=False,  # Ensures Japanese characters are preserved
                        indent=4,
                        sort_keys=False
                    )
                    print(formatted_result)
                except json.JSONDecodeError:
                    print(result)
                    
            except KeyboardInterrupt:
                print("\nSession terminated by user")
                break
            except Exception as e:
                print(f"\nUnexpected error: {e}")
                print("Please try again")

if __name__ == "__main__":
    # Create and run the language tutor agent
    tutor = LanguageTutorAgent(model="llama3.2:3b", max_messages=20)
    tutor.interactive_session()