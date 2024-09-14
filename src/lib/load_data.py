import json
import pandas as pd

class DataLoader:
    def __init__(self, room_data_path, room_location_path):
        self.room_data_path = room_data_path
        self.room_location_path = room_location_path
        self.room_locations = {}
        self.room_data = None
        
        self.acuity_list = []
        self.room_list = []
        self.discharge_list = []
        
    def load_JSON(self) -> None:
        """
        This function loads the relative room locations for a given JSON file for a floor.
        If the file doesn't exist or is invalid, it raises an appropriate error.
        """
        try:
            with open(self.room_location_path) as f:
                self.room_locations = json.loads(f)
        except FileNotFoundError:
            print(f"Error: File '{self.room_location_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{self.room_location_path}' contains invalid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred while loading room locations: {e}")
            
    def get_JSON(self) -> dict:
        """
        This function returns the room locations dictionary for a given floor.

        Returns:
            dict: room number -> coordinates
        """
        return self.room_locations
    
    def load_CSV(self) -> pd.DataFrame:
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
    
    def get_CSV(self) -> pd.DataFrame:
        """
        This function returns the room data for a given floor.

        Returns:
            pd.DataFrame: room data
        """
        return self.room_data
    
    def make_acuity_list(self) -> None:
        """
        This function creates a list of acuity values from the room data.
        """
        try:
            self.acuity_list = self.room_data['Acuity'].tolist()
        except KeyError:
            print("Error: 'Acuity' column not found in room data.")
        except AttributeError:
            print("Error: 'room_data' is not properly loaded or is None.")
        except Exception as e:
            print(f"An unexpected error occurred while creating the acuity list: {e}")
            
    def get_acuity_list(self) -> list:
        """
        This function returns the list of acuity values.
        """
        return self.acuity_list
        
    def make_room_list(self) -> None:
        """
        This function creates a list of room numbers from the room data.
        """
        try:
            self.room_list = self.room_data['Room'].tolist()
        except KeyError:
            print("Error: 'Room' column not found in room data.")
        except AttributeError:
            print("Error: 'room_data' is not properly loaded or is None.")
        except Exception as e:
            print(f"An unexpected error occurred while creating the room numbers list: {e}")
            
    def get_room_list(self) -> list:
        """
        This function returns the list of room numbers.
        """
        return self.room_list
        
    def make_discharge_list(self) -> None:
        """
        This function creates a list of discharge values from the room data.
        """
        try:
            self.discharge_list = self.room_data['Discharge'].tolist()
        except KeyError:
            print("Error: 'Discharge' column not found in room data.")
        except AttributeError:
            print("Error: 'room_data' is not properly loaded or is None.")
        except Exception as e:
            print(f"An unexpected error occurred while creating the discharge list: {e}")
            
    def get_discharge_list(self) -> list:
        """ 
        This function returns the list of discharge values.
        """
        return self.discharge_list
