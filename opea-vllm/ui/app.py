import streamlit as st
import requests
import json
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('ui')

# Get environment variables
MEGASERVICE_HOST_IP = os.getenv("MEGASERVICE_HOST_IP", "127.0.0.1")
MEGASERVICE_PORT = os.getenv("MEGASERVICE_PORT", 8888)
logger.info(f"Connecting to megaservice at {MEGASERVICE_HOST_IP}:{MEGASERVICE_PORT}")

# Function to make a POST request to the megaservice
def get_response_from_megaservice(prompt):
    url = f"http://{MEGASERVICE_HOST_IP}:{MEGASERVICE_PORT}/megaservice"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "Qwen/Qwen2.5-0.5B-Instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    logger.info(f"Sending request to megaservice with prompt: {prompt[:50]}...")
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise exception for HTTP errors
        logger.info("Response received successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with megaservice: {e}")
        return f"Error: {str(e)}"

# Initialize session state for input and response
if 'user_prompt' not in st.session_state:
    st.session_state.user_prompt = ''
if 'response' not in st.session_state:
    st.session_state.response = ''

# Streamlit app
st.title("OPEA Megaservice Application")
logger.info("UI application started")

# User input
st.session_state.user_prompt = st.text_input("Enter your prompt:", st.session_state.user_prompt)

# Create two columns with the first column wider to align buttons to the left
col1, col2 = st.columns([0.12, 0.88])

# Submit button in the first column
with col1:
    submit_pressed = st.button("Submit")

# Clear button in the second column
with col2:
    clear_pressed = st.button("Clear")

# Handle Submit button click
if submit_pressed:
    logger.info("Submit button pressed")
    with st.spinner("Waiting for response..."):
        try:
            # Make the request and get the response
            st.session_state.response = get_response_from_megaservice(st.session_state.user_prompt)
            # Display the response
            st.success("Response received!")
            logger.info("Response displayed to user")
        except Exception as e:
            error_msg = f"An error occurred: {e}"
            st.session_state.response = error_msg
            logger.error(error_msg)

# Handle Clear button click
if clear_pressed:
    logger.info("Clear button pressed")
    st.session_state.user_prompt = ''
    st.session_state.response = ''
    # Reset the query parameters to clear the UI
    st.query_params.clear()
    logger.info("UI state cleared")

# Display the response
if st.session_state.response:
    st.write(st.session_state.response)
