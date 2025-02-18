# Browser Automation with LLM Agent

A powerful browser automation tool that uses Gemini AI to understand and execute complex browsing tasks through a user-friendly Streamlit interface.

## 🌟 Features

- **Natural Language Tasks**: Describe what you want the browser to do in plain English
- **Interactive UI**: Clean, modern interface built with Streamlit
- **Real-time Logging**: Watch the automation progress in real-time
- **Configurable Parameters**: Customize max steps and actions per step
- **Error Handling**: Robust error handling and user feedback
- **Light Theme**: Consistent, easy-to-read light theme interface

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Chrome/Chromium browser

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Thejas775/Browser-Agent.git
cd browser-agent
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
playwright install
```

4. Set up your environment variables:
Create a `.env` file in the project root with:
```env
GEMINI_API_KEY=your_api_key_here
```

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run agent.py
```

2. Open your browser and navigate to the provided URL (typically `http://localhost:8501`)

## 💡 Usage

1. **Enter a Task**: Describe what you want the browser to do in natural language
   - Example: "Go to Youtube and play blinding lights."

2. **Configure Parameters**:
   - Max Steps: Maximum number of steps the agent can take (default: 25)
   - Max Actions per Step: Maximum actions per step (default: 4)
## 🛠️ Project Structure

```
browser-automation/
├── agent.py           # Main Streamlit application
├── requirements.txt   # Project dependencies
├── .env              # Environment variables (create this)
└── README.md         # Project documentation
```

## 🔧 Configuration

The application can be configured through the following environment variables:
- `GEMINI_API_KEY`: Your Google Gemini API key
- Additional browser configurations can be modified in `browser_use.py`
