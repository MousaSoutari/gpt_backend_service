# GPT Backend Service 🤖

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust backend service demonstrating RAG (Retrieval-Augmented Generation) operations, data handling, and cloud storage simulation with a focus on production-ready practices.

## 🚀 Features

- 📂 File System Data Processing
- 🗄️ Database Integration (SQLite)
- 🔄 RAG (Retrieval-Augmented Generation) File Generation
- ☁️ Cloud Storage Simulation
- 🧪 Comprehensive Unit Testing
- 📦 CI/CD Pipeline (Jenkins)

## 📁 Project Structure

```plaintext
.
├── Jenkinsfile          # CI/CD pipeline configuration
├── README.md            # Project documentation
├── backend_service.py   # Main service logic
├── cloud/               # Simulated cloud storage
├── data/                # Input data directory
│   ├── file1.txt
│   └── file2.txt
├── database.db          # SQLite database
├── output/              # Generated files
├── requirements.txt     # Python dependencies
└── test_backend_service.py  # Unit tests
```

## 🛠️ Installation

### Prerequisites

- Python 3.6+
- Git
- SQLite3

### Quick Start

1. **Clone & Navigate**
   ```bash
   git clone <repository-url>
   cd gpt_backend_service
   ```

2. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Required Directories**
   ```bash
   mkdir -p data output cloud test_data test_output
   ```

## 💻 Usage

### Running the Application

```bash
python backend_service.py
```

### Running Tests

```bash
# Run tests with verbose output
pytest test_backend_service.py -v

# Run tests with coverage
pytest --cov=backend_service test_backend_service.py
```

## 📚 API Reference

### Core Functions

| Function | Description |
|----------|-------------|
| `pull_data_from_filesystem(source_path)` | Reads and processes files from specified directory |
| `pull_data_from_database(db_path)` | Retrieves and formats data from SQLite database |
| `generate_rag_files(data, output_path)` | Generates RAG files from input data |
| `send_to_cloud(output_path, cloud_path)` | Simulates cloud storage operations |

## 🔄 CI/CD Pipeline

### Jenkins Pipeline Stages

1. **Build** 🏗️
   - Environment setup
   - Dependency installation

2. **Test** 🧪
   - Unit test execution
   - Coverage reporting

3. **Deploy** 🚀
   - Deployment automation
   - Environment configuration

## 🐛 Troubleshooting

### Common Issues & Solutions

1. **Permission Denied**
   ```bash
   chmod 755 data output cloud test_data test_output
   ```

2. **Database Issues**
   ```bash
   sqlite3 database.db
   .tables
   SELECT * FROM data;
   .quit
   ```

## 🧹 Maintenance

### Update Dependencies
```bash
pip freeze > requirements.txt
```

### Cleanup
```bash
rm -rf output/* cloud/*
rm database.db
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Project Link: [https://github.com/yourusername/gpt_backend_service](https://github.com/yourusername/gpt_backend_service)

---

⭐️ If you find this project useful, please consider giving it a star!
