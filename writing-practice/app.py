import streamlit as st
from streamlit_drawable_canvas import st_canvas
from sentence_generator import generate_random_sentence, compare_kanji
from utils.logging_config import setup_logger
import requests
import time
import os

# Get Ollama connection details from environment variables
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'ollama-server')
OLLAMA_PORT = os.getenv('OLLAMA_PORT', '11434')
OLLAMA_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"

# Initialize logger and model only once using Streamlit's session state
if 'logger' not in st.session_state:
    st.session_state.logger = setup_logger('app')
    st.session_state.logger.info("Starting application")

    # Initialize model loading
    st.session_state.logger.info("Starting model initialization")
    try:
        # Pull the model using Ollama API
        response = requests.post(
            f"{OLLAMA_URL}/api/pull",
            json={"model": "llama2:3b"},
            timeout=600  # 10 minute timeout for model pulling
        )
        
        if response.status_code == 200:
            st.session_state.logger.info("Model pulled successfully")
            
            # Verify model is loaded by trying a simple generation
            verify_response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": "llama2:3b",
                    "prompt": "Hi",
                    "stream": False
                }
            )
            
            if verify_response.status_code == 200:
                st.session_state.logger.info("Model verified and ready")
                st.session_state.model_ready = True
            else:
                st.session_state.logger.error("Model verification failed")
                st.session_state.model_ready = False
        else:
            st.session_state.logger.error("Failed to pull model")
            st.session_state.model_ready = False
            
    except Exception as e:
        st.session_state.logger.error(f"Error during model initialization: {str(e)}")
        st.session_state.model_ready = False

def reset_canvas_state():
    """Reset all canvas-related state"""
    st.session_state.canvas_key += 1
    if 'current_sentence' in st.session_state:
        del st.session_state.current_sentence
    if 'target_text' in st.session_state:
        del st.session_state.target_text
    # Clear any previous results/messages
    if 'last_detection' in st.session_state:
        del st.session_state.last_detection
    if 'last_result' in st.session_state:
        del st.session_state.last_result

def main():
    st.title("Japanese Word Practice")
    
    # Show model status
    if not st.session_state.get('model_ready', False):
        st.error("LLM model is not ready. Please wait for initialization or check logs.")
        if st.button("Retry Model Initialization"):
            st.session_state.clear()
            st.rerun()
        return
    
    # Initialize canvas state if not exists
    if 'canvas_key' not in st.session_state:
        st.session_state.canvas_key = 0
    
    # Adjust column ratio to give more space for the drawing area
    col1, col2 = st.columns([1, 2])  # Make drawing column twice as wide
    
    with col1:
        if 'current_sentence' not in st.session_state:
            st.session_state.current_sentence = None
            
        if st.button("Generate Sentence"):
            st.session_state.logger.info("Generate sentence button clicked")
            # Reset everything first
            reset_canvas_state()
            # Then generate new sentence
            result = generate_random_sentence(group_id=1)
            if result:
                st.session_state.current_sentence = result
                st.session_state.target_text = result['sentence']['japanese']
                st.session_state.logger.info(f"Generated new sentence: {result['sentence']['japanese']}")
        
        # Show current sentence if it exists
        if 'current_sentence' in st.session_state and st.session_state.current_sentence:
            st.write("Japanese:")
            st.write(st.session_state.current_sentence['sentence']['japanese'])
            st.write("English:")
            st.write(st.session_state.current_sentence['sentence']['english'])
    
    with col2:
        st.subheader("Practice Drawing")
        
        # Calculate canvas width based on column width
        canvas_width = 600  # Increased width to show right border
        
        # Container for canvas to ensure consistent width
        canvas_container = st.container()
        with canvas_container:
            # Add padding to ensure right border is visible
            st.markdown(
                """
                <style>
                    .canvas-container { margin-right: 20px; }
                </style>
                """,
                unsafe_allow_html=True
            )
            
            # Adjust canvas size to better fit the column
            canvas_result = st_canvas(
                stroke_width=3,
                stroke_color='#000',
                background_color='#fff',
                height=300,
                width=canvas_width,
                drawing_mode="freedraw",
                key=f"canvas_{st.session_state.canvas_key}",
            )
        
        # Container for buttons to match canvas width
        button_container = st.container()
        with button_container:
            # Create two columns for buttons with exact same width as canvas
            btn_col1, btn_col2 = st.columns(2)
            
            with btn_col1:
                if st.button("Clear Canvas", use_container_width=True):
                    st.session_state.logger.debug("Clearing canvas")
                    st.session_state.canvas_key += 1
                    st.rerun()
            
            with btn_col2:
                if st.button("Submit Drawing", use_container_width=True):
                    st.session_state.logger.info("Drawing submitted for comparison")
                    if (canvas_result.image_data is not None and 
                        'target_text' in st.session_state and 
                        canvas_result.image_data.any()):  # Check if anything is drawn
                        
                        result = compare_kanji(
                            canvas_result.image_data, 
                            st.session_state.target_text
                        )
                        st.write(f"Detected text: {result['detected_text']}")
                        if result['is_match']:
                            st.session_state.logger.info("Drawing matched target text")
                            st.success("Correct! The text matches!")
                        else:
                            st.session_state.logger.info("Drawing did not match target text")
                            st.error("Try again! The text doesn't match.")
                    else:
                        st.session_state.logger.warning("Drawing submitted without target text or empty canvas")
                        st.warning("Please draw something first and generate a sentence.")
        
        # Always show the target text if one is generated
        if 'target_text' in st.session_state:
            st.markdown("### Target Text:")
            st.markdown(f"### {st.session_state.target_text}")

if __name__ == "__main__":
    main() 