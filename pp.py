import pandas as pd
import json

def extract_module_schedules(csv_file, module_list):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Initialize variables to store results
    all_schedules = {}
    current_location = None
    
    # Initialize dictionary for each module
    for module in module_list:
        all_schedules[module] = []
    
    # Iterate through the rows
    for index, row in df.iterrows():
        # Check if this is a location row
        if isinstance(row.iloc[0], str) and 'BIUST -' in row.iloc[0]:
            current_location = row.iloc[0].strip()
            continue
            
        # Check if first column contains time
        if isinstance(row.iloc[0], str) and '-' in row.iloc[0]:
            time_slot = row.iloc[0]
            
            # Check each day of the week (columns 1-5 for Mon-Fri)
            for day_index in range(1, 6):
                value = row.iloc[day_index]
                if not isinstance(value, str):
                    continue
                    
                # Check for each module
                for module in module_list:
                    if module in value.upper():
                        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                        
                        schedule_entry = {
                            'location': current_location,
                            'day': days[day_index-1],
                            'time': time_slot,
                            'class': value.strip()
                        }
                        all_schedules[module].append(schedule_entry)
    
    # Remove empty module entries
    all_schedules = {k: v for k, v in all_schedules.items() if v}
    
    return {'Module Schedules': all_schedules}

# Use the function
module_list = ['ALSS 101', 'ALSS 201', 'ALSS 301', 'BIOL 101', 'BIOL 201', 'BIOL 202', 'BIOL 203', 'BIOL 204', 'BIOL 302', 'BIOL 303', 'BIOL 304', 'BIOL 305', 'BIOL 313', 'BIOL 314', 'BIOL 401', 'BIOL 402', 'BIOL 403', 'BIOL 405', 'BIOL 406', 'BIOL 601', 'BIOL 602', 'BIOL 603', 'CETG 111', 'CHCL 101', 'CHCL 102', 'CHCL 103', 'CHCL 104', 'CHCL 105', 'CHCL 106', 'CHCL 107', 'CHEE 210', 'CHEE 310', 'CHEE 311', 'CHEE 312', 'CHEE 411', 'CHEE 412', 'CHEE 413', 'CHEE 414', 'CHEE 415', 'CHEE 510', 'CHEE 512', 'CHEE 514', 'CHEE 515', 'CHEE 516', 'CHEE 517', 'CHEM 101', 'CHEM 203', 'CHEM 205', 'CHEM 302', 'CHEM 303', 'CHEM 306', 'CHEM 307', 'CHEM 309', 'CHEM 402', 'CHEM 403', 'CHEM 405', 'CHEM 407', 'CHEM 409', 'CIVE 311', 'CIVE 312', 'CIVE 314', 'CIVE 315', 'CIVE 411', 'CIVE 412', 'CIVE 414', 'CIVE 415', 'CIVE 416', 'CIVE 514', 'CIVE 517', 'CMME 510', 'CMME 511', 'COMP 101', 'COMP 201', 'COMP 211', 'COMP 221', 'COMP 231', 'COMP 302', 'COMP 311', 'COMP 331', 'COMP 332', 'COMP 342', 'COMP 353', 'COMP 361', 'COMP 401', 'COMP 412', 'COMP 431', 'COMP 441', 'COMP 451', 'CPEN 513', 'CPEN 522', 'CTEN 415', 'CTEN 511', 'CTEN 512', 'EEEN 211', 'EEEN 221', 'EEEN 311', 'EEEN 313', 'EEEN 314', 'EEEN 411', 'EEEN 412', 'EEEN 413', 'EEEN 414', 'EEEN 510', 'EEEN 511', 'EEEN 512', 'EEEN 514', 'EEEN 516', 'EEEN 517', 'EEEN 519', 'EMTH 201', 'EMTH 301', 'ENER 411', 'ENER 412', 'ENER 415', 'ENER 511', 'ENER 513', 'ENVS 201', 'ENVS 301', 'ENVS 303', 'ENVS 305', 'ENVS 307', 'ENVS 309', 'ENVS 401', 'ENVS 403', 'ENVS 405', 'ENVS 407', 'FRSC 301', 'FRSC 401', 'FRSC 403', 'GEME 201', 'GEME 313', 'GEME 411', 'GEME 414', 'GEME 415', 'GEME 416', 'GEME 512', 'GEME 630', 'GEOL 201', 'GEOL 207', 'GEOL 301', 'GEOL 303', 'GEOL 305', 'GEOL 307', 'GEOL 401', 'GEOL 403', 'GEOL 405', 'GEOL 601', 'GEOL 611', 'GEOL 613', 'GEOL 615', 'GEOL 621', 'GEOL 623', 'GEOL 625', 'GLEN 222', 'GLEN 311', 'GLEN 313', 'GLEN 416', 'GLEN 417', 'GLEN 418', 'GLEN 514', 'INFS 222', 'INFS 312', 'INFS 361', 'INFS 401', 'INFS 411', 'INFS 441', 'INFS 451', 'INME 311', 'INME 313', 'INME 314', 'INME 411', 'INME 412', 'INME 413', 'INME 414', 'INME 511', 'INME 512', 'INME 515', 'MATH 101', 'MATH 201', 'MATH 202', 'MATH 207', 'MATH 301', 'MATH 302', 'MATH 307', 'MATH 401', 'MATH 405', 'MATH 409', 'MATH 411', 'MATH 412', 'MATH 601', 'MATH 614', 'MATH 615', 'MATH 622', 'MATH 624', 'MATH 629', 'MCTE 511', 'MCTE 521', 'MECE 211', 'MECE 311', 'MECE 312', 'MECE 313', 'MECE 412', 'MECE 511', 'MEIE 510', 'MINE 411', 'MINE 413', 'MINE 414', 'MINE 415', 'MINE 416', 'MINE 511', 'MINE 512', 'MINE 513', 'MINE 514', 'MINE 515', 'MINE 523', 'MINS 311', 'MINS 411', 'MINS 412', 'MINS 511', 'MMEE 210', 'MMEE 310', 'MMEE 313', 'MMEE 410', 'MMEE 411', 'MMEE 413', 'MMEE 415', 'MMEE 513', 'MMEE 515', 'MMEE 522', 'PHYS 101', 'PHYS 201', 'PHYS 202', 'PHYS 301', 'PHYS 305', 'PHYS 311', 'PHYS 403', 'PHYS 404', 'PHYS 411', 'PHYS 412', 'STAT 202', 'STAT 301', 'STAT 303', 'STAT 304', 'STAT 309', 'STAT 401', 'STAT 414', 'STAT 416', 'STAT 421', 'STAT 601', 'STAT 603', 'STAT 611', 'STAT 612', 'STAT 613', 'STAT 615', 'STAT 621', 'TELE 511', 'TELE 513', 'TELE 522']
    
result = extract_module_schedules('timetable.csv', module_list)

# Save to JSON file
with open('retrial.json', 'w') as f:
    json.dump(result, f, indent=2)

# Print number of modules found
print(f"Found schedules for {len(result['Module Schedules'])} modules")