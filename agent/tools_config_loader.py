import yaml
from typing import List, Dict, Any
from pathlib import Path
import os

class ToolsConfigLoader:
    """Loader for tool configurations to be used with Ollama API"""
    
    def __init__(self, config_path: str = "agent/tools.yaml"):
        """
        Initialize the tools config loader
        
        Args:
            config_path: Path to the YAML config file
        """
        # Try multiple possible locations for the config file
        possible_paths = [
            Path(config_path),  # Try direct path
            Path("agent") / "tools.yaml",  # Try relative to workspace root
            Path(__file__).parent / "tools.yaml"  # Try relative to this script
        ]
        
        # Use the first path that exists
        for path in possible_paths:
            if path.exists():
                self.config_path = path
                break
        else:
            # If no path exists, use the first one for error reporting
            self.config_path = possible_paths[0]
    
    def load_configs(self) -> List[Dict[str, Any]]:
        """
        Load and validate tool configurations from YAML
        
        Returns:
            List of tool configurations in Ollama API format
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config file is invalid
        """
        if not self.config_path.exists():
            raise FileNotFoundError(f"Tools config file not found: {self.config_path}")
            
        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                config = yaml.safe_load(file)
                
            if not isinstance(config, dict) or 'tools' not in config:
                raise ValueError("Invalid config: 'tools' section not found")
                
            if not isinstance(config['tools'], list):
                raise ValueError("Invalid config: 'tools' must be a list")
                
            return [self._format_tool(tool) for tool in config['tools']]
                
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format in config file: {e}")
    
    def _format_tool(self, tool: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format a tool configuration for Ollama API
        
        Args:
            tool: Raw tool configuration from YAML
            
        Returns:
            Formatted tool configuration
            
        Raises:
            ValueError: If tool configuration is invalid
        """
        required_fields = {'name', 'description', 'parameters'}
        if not all(field in tool for field in required_fields):
            raise ValueError(f"Tool config missing required fields: {required_fields}")
            
        return {
            "type": "function",
            "function": tool
        }


def load_tool_configs() -> List[Dict[str, Any]]:
    """
    Convenience function to load tool configurations
    
    Returns:
        List of tool configurations in Ollama API format
    """
    loader = ToolsConfigLoader()
    return loader.load_configs()


if __name__ == "__main__":
    # Example usage and testing
    try:
        configs = load_tool_configs()
        import json
        print(json.dumps(configs, indent=2))
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading tool configs: {e}")
