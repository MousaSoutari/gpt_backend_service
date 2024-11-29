import os
import sqlite3
import shutil
import pytest
from backend_service import (
    pull_data_from_filesystem,
    pull_data_from_database,
    generate_rag_files,
    send_to_cloud,
)


@pytest.fixture
def setup_test_data():
    # Create test directory and files
    os.makedirs("./test_data", exist_ok=True)
    with open("./test_data/test1.txt", "w") as f:
        f.write("Test content 1")
    with open("./test_data/test2.txt", "w") as f:
        f.write("Test content 2")

    # Create test database
    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, content TEXT)"
    )
    cursor.execute("INSERT INTO data (content) VALUES ('Database content 1')")
    cursor.execute("INSERT INTO data (content) VALUES ('Database content 2')")
    conn.commit()
    conn.close()

    yield

    # Cleanup
    if os.path.exists("./test_data"):
        shutil.rmtree("./test_data")
    if os.path.exists("./test_output"):
        shutil.rmtree("./test_output")
    if os.path.exists("test_database.db"):
        os.remove("test_database.db")


def test_pull_data_from_filesystem(setup_test_data):
    data = pull_data_from_filesystem("./test_data")
    assert len(data) == 2
    assert "Test content" in data[0]


def test_pull_data_from_database(setup_test_data):
    data = pull_data_from_database("test_database.db")
    assert len(data) == 2
    assert "Database content" in str(data[0])


def test_generate_rag_files(setup_test_data):
    test_data = ["Test content 1", "Test content 2"]
    generate_rag_files(test_data, "./test_output")
    assert os.path.exists("./test_output/rag_file_0.txt")
    assert os.path.exists("./test_output/rag_file_1.txt")


def test_send_to_cloud(setup_test_data):
    # Setup
    os.makedirs("./test_output", exist_ok=True)
    os.makedirs("./test_cloud", exist_ok=True)
    with open("./test_output/test.txt", "w") as f:
        f.write("Test content")

    # Test
    send_to_cloud("./test_output", "./test_cloud")
    assert os.path.exists("./test_cloud/test.txt")

    # Cleanup
    if os.path.exists("./test_cloud"):
        shutil.rmtree("./test_cloud")
