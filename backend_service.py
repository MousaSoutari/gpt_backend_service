import os
import shutil
import sqlite3


def pull_data_from_filesystem(source_path):
    # Pull data from the file system
    files = os.listdir(source_path)
    data = []
    for file in files:
        with open(os.path.join(source_path, file), "r") as f:
            data.append(f.read())
    return data


def pull_data_from_database(db_path):
    # Pull data from a database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    conn.close()
    return data


def generate_rag_files(data, output_path):
    # Generate RAG files
    os.makedirs(output_path, exist_ok=True)
    for i, item in enumerate(data):
        with open(os.path.join(output_path, f"rag_file_{i}.txt"), "w") as f:
            f.write(str(item))


def send_to_cloud(output_path, cloud_path):
    # Simulate sending files to the cloud
    if os.path.exists(cloud_path):
        shutil.rmtree(cloud_path)
    shutil.copytree(output_path, cloud_path)


def main():
    source_path = "./data"
    db_path = "./database.db"
    output_path = "./output"
    cloud_path = "./cloud"

    data_from_fs = pull_data_from_filesystem(source_path)
    data_from_db = pull_data_from_database(db_path)
    all_data = data_from_fs + data_from_db

    generate_rag_files(all_data, output_path)
    send_to_cloud(output_path, cloud_path)


if __name__ == "__main__":
    main()
