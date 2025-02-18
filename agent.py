import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import Agent

# Page config
st.set_page_config(
    page_title="Browser Automation Control",
    page_icon="🌐",
    layout="wide"
)

# Custom CSS to match the React styling
st.markdown("""
    <style>
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
    }
    .css-1y4p8pa {
        max-width: 100%;
    }
    .stTextInput > div > div {
    background-color: white;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    padding: 8px 12px;
    color: #000000;
    }
    .stTextInput input {
        color: #000000 !important;
    }
    .stButton > button {
        border-radius: 6px;
        padding: 8px 16px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }
    .log-container {
        background-color: #f8fafc;
        border-radius: 8px;
        padding: 16px;
        height: 300px;
        overflow-y: auto;
        font-family: monospace;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'is_running' not in st.session_state:
    st.session_state.is_running = False

def initialize_agent(task):
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        st.error('GEMINI_API_KEY is not set')
        return None
    
    llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash-exp',
        api_key=SecretStr(api_key)
    )
    return Agent(task=task, llm=llm)

async def run_automation(task, max_steps, max_actions_per_step):
    agent = initialize_agent(task)  # Pass the task here
    if not agent:
        return
    
    # Remove this line since we already set the task in initialization
    # agent.task = task
    agent.max_actions_per_step = max_actions_per_step
    
    try:
        st.session_state.logs.append(f"Starting automation task: {task}")
        await agent.run(max_steps=max_steps)
    except Exception as e:
        st.session_state.logs.append(f"Error: {str(e)}")
    finally:
        st.session_state.is_running = False

def main():
    st.title("Browser Automation Control")
    
    # Main control card
    with st.container():
        st.markdown("### Configuration")
        
        # Task input
        task = st.text_input(
            "Task Description",
            placeholder="Enter your automation task...",
            disabled=st.session_state.is_running
        )
        
        # Parameters
        col1, col2 = st.columns(2)
        with col1:
            max_steps = st.number_input(
                "Max Steps",
                min_value=1,
                max_value=100,
                value=25,
                disabled=st.session_state.is_running
            )
        with col2:
            max_actions = st.number_input(
                "Max Actions per Step",
                min_value=1,
                max_value=10,
                value=4,
                disabled=st.session_state.is_running
            )
        
        # Control buttons
        col1, col2 = st.columns([1, 5])
        with col1:
            if not st.session_state.is_running:
                if st.button("▶️ Start Automation", disabled=not task):
                    st.session_state.is_running = True
                    st.session_state.logs = []
                    asyncio.run(run_automation(task, max_steps, max_actions))
            else:
                if st.button("⏹️ Stop", type="primary"):
                    st.session_state.is_running = False
                    st.session_state.logs.append("Automation stopped by user")
    
    # Logs card
    # st.markdown("### Automation Logs")
    # log_placeholder = st.empty()
    # with log_placeholder.container():
    #     st.markdown('<div class="log-container">', unsafe_allow_html=True)
    #     for log in st.session_state.logs:
    #         st.text(log)
    #     if not st.session_state.logs:
    #         st.text("No logs available. Start the automation to see progress.")
    #     st.markdown('</div>', unsafe_allow_html=True)
    
    # Auto-refresh logs while running
    if st.session_state.is_running:
        st.rerun()

if __name__ == "__main__":
    main()