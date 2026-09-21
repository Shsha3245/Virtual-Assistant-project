# Virtual Assistant

A simple **Virtual Assistant** built with Python that uses Natural Language Processing (NLP) to understand user queries, generate responses, speak them aloud, and log them into a SQLite database.

---

## 🚀 Features
- **NLP Processing**: Tokenization, lemmatization, intent detection, and entity extraction using NLTK.
- **Voice Output**: Text-to-speech responses powered by `pyttsx3`.
- **Database Logging**: Responses are stored in a local SQLite database.
- **Configurable**: Intents, entities, and training data are defined in JSON/CSV files for easy customization.

---

## 📂 Project Structure
Virtual Assistant
|-- src
|   |-- main.py              # Entry point
|   |-- nlp.py               # NLP utility class
|   |-- voice_assistant.py   # Voice assistant logic
|   |-- utils.py             # Database utilities
|-- data
|   |-- intents.json         # Intent definitions
|   |-- entities.json        # Entity definitions
|   |-- training_data.csv    # Training samples
|-- config
|   |-- configuration.json   # Config settings
|-- database.db              # SQLite database
|-- requirements.txt         # Dependencies

---

## ⚙️ Requirements
- Python 3.11+
- [NLTK](https://www.nltk.org/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- scikit-learn
- pandas

Install dependencies:
```bash
pip install -r requirements.txt
Usage
Run the assistant:

bash
python src/main.py
Example interaction:

Kod
User: hi
Assistant: Hello! How can I help you?
To exit, type:

Kod
User: exit
🛠 Configuration
Edit config/configuration.json to adjust API keys, database URL, or voice assistant endpoint:

json
{
  "api_key": "dummy-key",
  "database_url": "sqlite:///database.db",
  "voice_assistant_url": "http://localhost:5000/api"
}
📈 Future Improvements
Add more intents and entities (weather, jokes, time).

Continuous conversation loop until user exits.

Advanced intent classification with ML models.

Voice customization (different voices, speed, tone).

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
