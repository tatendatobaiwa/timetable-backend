
import pandas as pd
import re

class TimetableParser:
    def __init__(self, csv_file):
        """
        Initialize the timetable parser with a CSV file
        
        :param csv_file: Path to the CSV file containing the timetable
        """
        # Read the CSV file manually to handle complex structure
        self.locations = []
        self.df = self._load_and_clean_csv(csv_file)
    
    def _load_and_clean_csv(self, csv_file):
        """
        Load and clean the CSV file
        
        :param csv_file: Path to the CSV file
        :return: Cleaned DataFrame
        """
        # Read the entire file to extract locations
        with open(csv_file, 'r') as file:
            content = file.readlines()
        
        # Extract locations (looking for lines with 'BIUST - ')
        self.locations = [
            line.strip() for line in content 
            if 'BIUST -' in line and 'Semester' not in line
        ]
        
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Remove columns with all NaN values
        df = df.dropna(axis=1, how='all')
        
        # Set the first column (time slots) as the index
        df.set_index(df.columns[0], inplace=True)
        
        # Rename the columns to days
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        if len(df.columns) == len(days):
            df.columns = days
        
        return df
    
    def find_module_details(self, module_code):
        """
        Find all occurrences of a specific module with location details
        
        :param module_code: Module code to search for (e.g., 'MATH 101')
        :return: List of dictionaries with module details including location
        """
        results = []
        
        # Use locations extracted during initialization
        default_location = "BIUST - Unknown Location"
        current_location = default_location
        
        # Iterate through days and time slots
        for day in self.df.columns:
            for time, modules in self.df[day].items():
                # Check if the current line is a location
                location_matches = [
                    loc for loc in self.locations 
                    if 'BIUST -' in loc
                ]
                if location_matches:
                    current_location = location_matches[0]
                
                # Check for module
                if isinstance(modules, str) and module_code.upper() in modules.upper():
                    results.append({
                        'location': current_location,
                        'day': day,
                        'time': time,
                        'details': modules
                    })
        
        return results

# Example usage function
def main():
    # Replace with the path to your CSV file
    csv_file_path = 'output_file.csv'
    
    # Create parser
    parser = TimetableParser(csv_file_path)
    
    # Find all occurrences of a specific module
    module_code = 'MATH 101'
    module_details = parser.find_module_details(module_code)
    
    # Print details
    for details in module_details:
        print(f"Module: {module_code}")
        print(f"Location: {details['location']}")
        print(f"Day: {details['day']}")
        print(f"Time: {details['time']}")
        print(f"Details: {details['details']}")
        print("---")

if __name__ == "__main__":
    main()
