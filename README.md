# Virtual Assistant

A lightweight Python virtual assistant that uses natural language processing (NLP) to interpret user input, generate a response, speak it aloud, and save the response to a SQLite database.

## ✨ Features

- **Natural language processing** with NLTK for tokenization, lemmatization, intent detection, and entity extraction.
- **Text-to-speech responses** powered by [`pyttsx3`](https://pypi.org/project/pyttsx3/).
- **Response logging** using SQLite.
- **Data-driven configuration** through JSON and CSV files.
- **Machine-learning support** through scikit-learn.

## 🗂️ Project Structure

```text
Virtual-Assistant-project/
├── src/
│   ├── main.py              # Application entry point
│   ├── nlp.py               # NLP processing utilities
│   ├── voice_assistant.py   # Assistant response and speech logic
│   └── utils.py             # Database and utility functions
├── data/
│   ├── intents.json         # Intent definitions
│   ├── entities.json        # Entity definitions
│   └── training_data.csv    # Training examples
├── config/
│   └── configuration.json   # Application settings
├── requirements.txt         # Python dependencies
└── database.db              # Local SQLite database, created or updated at runtime
```

## ✅ Requirements

- Python 3.11 or newer
- The dependencies listed in `requirements.txt`
- An audio output device for text-to-speech features

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shsha3245/Virtual-Assistant-project.git
   cd Virtual-Assistant-project
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   **Windows PowerShell:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## ▶️ Usage

Run the assistant from the project root:

```bash
python src/main.py
```

Example interaction:

```text
User: hi
Assistant: Hello! How can I help you?
```

The assistant processes one input, prints the response, speaks it using `pyttsx3`, and saves the response to the database.

> **Note:** Depending on your operating system, `pyttsx3` may require an additional speech engine or system audio package.

## ⚙️ Configuration

Application settings are stored in `config/configuration.json`:

```json
{
  "api_key": "dummy-key-123",
  "database_url": "sqlite:///database.db",
  "voice_assistant_url": "http://localhost:5000/api"
}
```

Update these values as needed for your local setup. Do not commit real API keys or other secrets to the repository.

## 🧪 Development Ideas

- Add more intents and entities, such as weather, jokes, and time.
- Support continuous conversations until the user exits.
- Improve intent classification with trained machine-learning models.
- Add configurable voices, speech rates, and volume.
- Add automated tests for NLP processing, responses, and database logging.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Create a feature branch.
2. Make and test your changes.
3. Open a pull request with a clear description of the change.

For larger changes, please open an issue first to discuss the proposal.

## 📄 License

No license has been specified for this project yet. Add a `LICENSE` file if you want others to use, modify, or distribute the project under defined terms.
