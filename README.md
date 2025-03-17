# Restaurant Name & Menu Generator

An AI-powered web application that generates creative restaurant names and menu items based on selected cuisines. Built using **Python, Streamlit, LangChain, and Mistral AI**, this project helps restaurant owners, entrepreneurs, and food startups quickly brainstorm unique branding ideas.

## Features

- Generate **restaurant names** and **menu items** based on selected cuisines.
- Refresh results to explore multiple suggestions.
- Simple and interactive **Streamlit web app** interface.
- Powered by **LangChain** for AI-driven text generation.

## Tech Stack

- **Python** - Backend logic
- **Streamlit** - Web app framework
- **LangChain** - AI integration
- **Mistral AI API** - AI model for text generation

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/restaurant-name-menu-generator.git
   cd restaurant-name-menu-generator
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the **Mistral AI API key**:
   - Create a `.env` file in the root directory.
   - Add your API key:
     ```
     MISTRAL_API_KEY=your_api_key_here
     ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

### How It Works

1. Select a cuisine (e.g., Italian, Mexican, Chinese, etc.).
2. Click **Generate** to receive a list of AI-generated restaurant names and menu items.
3. Click **Refresh** to explore different options.


