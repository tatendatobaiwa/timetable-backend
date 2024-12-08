import json
from datetime import datetime

def parse_time(time_str):
    """Convert time string (e.g., '0800-0850') to tuple of start and end times"""
    start, end = time_str.split('-')
    return (
        datetime.strptime(start, '%H%M').time(),
        datetime.strptime(end, '%H%M').time()
    )

def format_time_range(start_time, end_time):
    """Convert time objects back to string format"""
    return f"{start_time.strftime('%H%M')}-{end_time.strftime('%H%M')}"

def combine_schedules(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    combined_schedules = {}
    
    # Process each module
    for module, schedules in data['Module Schedules'].items():
        combined_schedules[module] = []
        
        # Group events by location, class name, and day
        event_groups = {}
        for event in schedules:
            key = (event['location'], event['class'], event['day'])
            if key not in event_groups:
                event_groups[key] = []
            event_groups[key].append(event)
        
        # Combine times for each group
        for (location, class_name, day), events in event_groups.items():
            # Get all start and end times
            all_times = [parse_time(event['time']) for event in events]
            start_times, end_times = zip(*all_times)
            
            # Find earliest start and latest end
            earliest_start = min(start_times)
            latest_end = max(end_times)
            
            # Create combined event
            combined_event = {
                'location': location,
                'day': day,
                'time': format_time_range(earliest_start, latest_end),
                'class': class_name
            }
            combined_schedules[module].append(combined_event)
    
    # Create output structure
    output_data = {'Module Schedules': combined_schedules}
    
    # Write to output file
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    # Print summary
    total_modules = len(combined_schedules)
    total_events = sum(len(events) for events in combined_schedules.values())
    print(f"Combined schedules for {total_modules} modules ({total_events} total events)")

if __name__ == "__main__":
    combine_schedules('uncombined-timetable.json', 'final-timetable.json')
