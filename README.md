<<<<<<< HEAD
# naonime
=======
# Anichin API

🎌 **Anichin API** adalah sebuah API RESTful yang dikembangkan untuk memudahkan developer dalam mengakses data anime dan donghua. Proyek ini telah direfactor dengan type annotations, logging komprehensif, dan error handling yang robust untuk production-ready deployment.

## ✨ Features

-   🔍 **Search Anime/Donghua** - Pencarian berdasarkan query
-   📚 **Anime Information** - Detail lengkap anime/donghua
-   🎬 **Episode Details** - Informasi episode dan video sources
-   🏷️ **Genre Filtering** - Filter berdasarkan genre
-   📖 **Home Page Content** - Konten halaman utama dengan section
-   🎥 **Video Sources** - Ekstraksi link video streaming
-   📊 **Comprehensive Logging** - Logging sistem untuk monitoring
-   🛡️ **Type Safety** - Full type annotations untuk better development experience
-   🔒 **Error Handling** - Robust error handling untuk stabilitas

## 🛠️ Technology Stack

-   **Framework**: Flask with CORS support
-   **Web Scraping**: BeautifulSoup4 + Requests
-   **Type Safety**: Python typing module
-   **Logging**: Python logging with file and console output
-   **Environment**: python-dotenv for configuration

## 📋 API Reference

### Base URL

```
http://localhost:5000
```

### Endpoints

| Endpoint               | Method | Description             | Parameters                                            | Response                            |
| ---------------------- | ------ | ----------------------- | ----------------------------------------------------- | ----------------------------------- |
| `/`                    | GET    | Get home page content   | `page` (optional) - int                               | JSON dengan data halaman utama      |
| `/search/<query>`      | GET    | Search anime by query   | `query` - string (required)                           | JSON dengan hasil pencarian         |
| `/<slug>`              | GET    | Get anime details       | `slug` - string (required)                            | JSON dengan detail anime            |
| `/genres`              | GET    | List all genres         | None                                                  | JSON dengan daftar genre            |
| `/genre/<slug>`        | GET    | Get anime by genre      | `slug` - string (required)<br>`page` (optional) - int | JSON dengan anime berdasarkan genre |
| `/episode/<slug>`      | GET    | Get episode details     | `slug` - string (required)                            | JSON dengan detail episode          |
| `/video-source/<slug>` | GET    | Get video sources       | `slug` - string (required)                            | JSON dengan sumber video            |
| `/anime`               | GET    | List anime with filters | Query parameters optional                             | JSON dengan daftar anime            |

### Response Format

#### Success Response

```json
{
  "result": {...},
  "source": "https://anichin.club/...",
  "total": 10
}
```

#### Error Response

```json
{
    "message": "Error description",
    "error": "Detailed error information"
}
```

## 🚀 Installation & Setup

### Prerequisites

-   Python 3.8+
-   pip package manager

### Clone Repository

```bash
git clone https://github.com/asmindev/anichin-api
cd anichin-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file in the root directory:

```env
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3
```

### Run the Application

```bash
# Development mode
python main.py

# Production mode
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

The API will be available at `http://localhost:5000`

## 📊 Logging

Aplikasi menggunakan comprehensive logging system:

-   **File Logging**: Logs disimpan di `anichin_api.log`
-   **Console Logging**: Output ke terminal untuk development
-   **Log Levels**: DEBUG, INFO, WARNING, ERROR
-   **Structured Format**: Timestamp, module, level, dan message

### Log Configuration

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('anichin_api.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
```

## 🛡️ Error Handling

| HTTP Status | Description           | Example                  |
| ----------- | --------------------- | ------------------------ |
| `200`       | Success               | Request berhasil         |
| `400`       | Bad Request           | Parameter tidak valid    |
| `404`       | Not Found             | Resource tidak ditemukan |
| `500`       | Internal Server Error | Error server internal    |

## 🏗️ Architecture

```
anichin-api/
├── main.py                 # Flask application entry point
├── api/
│   ├── __init__.py        # Main API handler class
│   └── utils/             # Utility modules
│       ├── parsing.py     # Base scraping class
│       ├── info.py        # Anime information scraper
│       ├── search.py      # Search functionality
│       ├── episode.py     # Episode details scraper
│       ├── home.py        # Home page content scraper
│       ├── genre.py       # Genre listing and filtering
│       ├── anime.py       # Anime listing scraper
│       └── video.py       # Video source extraction
├── requirements.txt       # Python dependencies
├── anichin_api.log       # Application logs
└── README.md             # Documentation
```

## 🔧 Development

### Type Safety

Proyek ini menggunakan type annotations untuk better development experience:

```python
def get_info(self, slug: str) -> Dict[str, Any]:
    """Get anime information by slug."""
    try:
        logger.info(f"Getting info for slug: {slug}")
        return Info(slug).to_json()
    except Exception as e:
        logger.error(f"Error getting info for {slug}: {e}")
        return {"result": None, "error": str(e)}
```

### Adding New Scrapers

1. Inherit dari `Parsing` base class
2. Implement required methods dengan type hints
3. Add comprehensive error handling
4. Include proper logging
5. Update main API handler

## 📝 Example Usage

### Search Anime

```bash
curl "http://localhost:5000/search/one%20piece"
```

### Get Anime Details

```bash
curl "http://localhost:5000/battle-through-the-heavens-season-5"
```

### Get Video Sources

```bash
curl "http://localhost:5000/video-source/perfect-world-episode-03-subtitle-indonesia"
```

### Get Genres

```bash
curl "http://localhost:5000/genres"
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

-   Follow type annotations
-   Add comprehensive logging
-   Include error handling
-   Write descriptive commit messages
-   Test endpoints thoroughly

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

-   **[@iniasmin\_](https://instagram.com/iniasmin_)** - Original Developer
-   **[@asmindev](https://github.com/asmindev)** - Maintainer

## 🙏 Acknowledgments

-   [Anichin.club](https://anichin.club) untuk sumber data
-   Flask community untuk framework yang amazing
-   BeautifulSoup untuk web scraping capabilities

## 📞 Support

Jika ada pertanyaan atau masalah, silakan:

-   Open an issue di GitHub repository
-   Contact via Instagram [@iniasmin\_](https://instagram.com/iniasmin_)

---

**Made with ❤️ for the anime community**
>>>>>>> 4f420459690b3c24bdd4f1ef049bc8a135c488ab
