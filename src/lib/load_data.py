import json
import pandas as pd

class DataLoader:
    def __init__(self, room_data_path, room_location_path):
        self.room_data_path = room_data_path
        self.room_location_path = room_location_path
        self.room_locations = {}
        self.room_data = None
        
    def load_room_location(self) -> None:
        """
        This function loads the relative room locations for a given JSON file for a floor.
        If the file doesn't exist or is invalid, it raises an appropriate error.
        """
        try:
            with open(self.room_location_path) as f:
                self.room_locations = json.load(f)
        except FileNotFoundError:
            print(f"Error: File '{self.room_location_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{self.room_location_path}' contains invalid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred while loading room locations: {e}")
            
    def get_room_locations(self) -> dict:
        """
        This function returns the room locations dictionary for a given floor.

        Returns:
            dict: room number -> coordinates
        """
        return self.room_locations
    
    def load_room_data(self) -> pd.DataFrame:
        """
        This function loads the room data for a given floor from a CSV file.
        If the file doesn't exist or cannot be read, it raises an appropriate error.

        Returns:
            pd.DataFrame: room data
        """
        try:
            self.room_data = pd.read_csv(self.room_data_path)
        except FileNotFoundError:
            print(f"Error: File '{self.room_data_path}' not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: File '{self.room_data_path}' is empty or corrupt.")
        except pd.errors.ParserError:
            print(f"Error: File '{self.room_data_path}' contains parsing errors.")
        except Exception as e:
            print(f"An unexpected error occurred while loading room data: {e}")
    
    def get_room_data(self) -> pd.DataFrame:
        """
        This function returns the room data for a given floor.

        Returns:
            pd.DataFrame: room data
        """
        return self.room_data
