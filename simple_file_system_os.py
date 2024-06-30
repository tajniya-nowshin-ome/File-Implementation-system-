import os

class SimpleFileSystem:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)
        print(f"File system initialized at {root_dir}")

    def create_file(self, filename, content=""):
        file_path = os.path.join(self.root_dir, filename)
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{filename}' created.")

    def delete_file(self, filename):
        file_path = os.path.join(self.root_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' not found.")

    def read_file(self, filename):
        file_path = os.path.join(self.root_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
            print(f"Content of '{filename}':\n{content}")
            return content
        else:
            print(f"File '{filename}' not found.")
            return None

    def write_file(self, filename, content):
        file_path = os.path.join(self.root_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{filename}' updated.")
        else:
            print(f"File '{filename}' not found.")

    def list_files(self):
        files = os.listdir(self.root_dir)
        print("Files in file system:")
        for file in files:
            print(f"- {file}")
        return files

# Example usage
if __name__ == "__main__":
    fs = SimpleFileSystem("my_file_system")

    # Creating files
    fs.create_file("file1.txt", "Hello, World!")
    fs.create_file("file2.txt", "This is another file.")


  # Reading files
    fs.read_file("file1.txt")



   
    