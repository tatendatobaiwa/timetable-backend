import csv
import sys

def find_course_in_timetable(course_code, filename='output_file.csv'):


    course_code = course_code.upper()
    
    try:
        with open(filename, 'r') as csvfile:
          
            reader = csv.reader(csvfile)
            
            
            course_found = False
            
          
            for row in reader:
                for cell in row:
                    if course_code in cell:
                        print(f"Course found: {cell}")
                        course_found = True
                        
                    
                        try:
           
                            day_row = next(reader)
                            time_row = next(reader)
                            

                            course_col = row.index(cell)
                            
                            print(f"Day: {day_row[course_col]}")
                            print(f"Time: {time_row[0]}")
                        except (StopIteration, ValueError):
                            print("Unable to determine exact time and day.")
                        
                        break
                
          
            
            if not course_found:
                print(f"No information found for course {course_code}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():

 

    course_code = "CHEM 101"
    find_course_in_timetable(course_code)

if __name__ == "__main__":
    main()