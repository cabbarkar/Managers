import os
from abc import ABC, abstractmethod
from datetime import datetime

class FileManager(ABC):
    """
    Abstract base class for file operations.
    """
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def open_file(self, file_path: str, mode: str):
        """
        Abstract method to open a file.

        Args:
        - file_path (str): Path to the file.
        - mode (str): File opening mode ('r', 'w', 'a', etc.).
        """
        pass
    
    @abstractmethod
    def close_file(self):
        """
        Abstract method to close the currently opened file.
        """
        pass
    
    @abstractmethod
    def read_entire_file(self, file_path: str) -> str:
        """
        Abstract method to read entire content from a file.

        Args:
        - file_path (str): Path to the file.

        Returns:
        - str: Content of the file as a string.
        """
        pass
    
    @abstractmethod
    def read_line_from_file(self, file_path: str) -> str:
        """
        Abstract method to read a single line from a file.

        Args:
        - file_path (str): Path to the file.

        Returns:
        - str: A single line from the file as a string.
        """
        pass
    
    @abstractmethod
    def write_to_file(self, file_path: str, data: str):
        """
        Abstract method to write data to a file.

        Args:
        - file_path (str): Path to the file.
        - data (str): Data to write to the file.
        """
        pass
    
    @abstractmethod
    def append_to_file(self, file_path: str, data: str):
        """
        Abstract method to append data to a file.

        Args:
        - file_path (str): Path to the file.
        - data (str): Data to append to the file.
        """
        pass

    def delete_file(self, file_path: str):
        """
        Deletes a file specified by the file path.
        """
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error: {e.strerror} - {e.filename}")

    def get_file_size(self, file_path: str) -> int:
        """
        Gets the size of a file.

        Args:
        - file_path (str): Path to the file.

        Returns:
        - int: Size of the file in bytes.
        """
        return os.path.getsize(file_path)

    def get_file_creation_time(self, file_path: str) -> datetime:
        """
        Gets the creation time of a file.

        Args:
        - file_path (str): Path to the file.

        Returns:
        - datetime: Creation time of the file.
        """
        return datetime.fromtimestamp(os.path.getctime(file_path))

    def get_file_modification_time(self, file_path: str) -> datetime:
        """
        Gets the modification time of a file.

        Args:
        - file_path (str): Path to the file.

        Returns:
        - datetime: Modification time of the file.
        """
        return datetime.fromtimestamp(os.path.getmtime(file_path))

# Example usage
if __name__ == "__main__":
    raise RuntimeError("Abstract classes cannot be instantiated directly.")
