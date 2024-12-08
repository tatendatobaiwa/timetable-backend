import json
from datetime import datetime, timedelta

def combine_entries(data):
    """
    Combine schedule entries with overlapping or adjacent times for the same module, location, day, and details.
    
    Args:
        data (dict): Dictionary containing module schedules
    
    Returns:
        dict: Consolidated schedule with combined time ranges
    """
    combined = {}
    
    for module, entries in data.items():
        # Sort entries by day and start time for more predictable processing
        sorted_entries = sorted(entries, key=lambda x: (x["day"], datetime.strptime(x["time"].split('-')[0], "%H%M")))
        
        for entry in sorted_entries:
            key = (module, entry["location"], entry["day"], entry["details"])
            time_range = entry["time"].split('-')
            start_time = datetime.strptime(time_range[0], "%H%M")
            end_time = datetime.strptime(time_range[1], "%H%M")
            
            # Handle times crossing midnight by adding a day if end time is before start time
            if end_time < start_time:
                end_time += timedelta(days=1)
            
            # Check for existing entries that can be merged
            merged = False
            for existing_key, existing_times in list(combined.items()):
                if existing_key == key:
                    # Merge time ranges if they overlap or are adjacent
                    if (start_time <= existing_times["end_time"] + timedelta(minutes=1) and 
                        end_time >= existing_times["start_time"] - timedelta(minutes=1)):
                        combined[existing_key]["start_time"] = min(existing_times["start_time"], start_time)
                        combined[existing_key]["end_time"] = max(existing_times["end_time"], end_time)
                        merged = True
                        break
            
            # If no merge occurred, add as a new entry
            if not merged:
                combined[key] = {"start_time": start_time, "end_time": end_time}
    
    # Format results
    formatted_data = {}
    for (module, location, day, details), times in combined.items():
        if module not in formatted_data:
            formatted_data[module] = []
        formatted_data[module].append({
            "location": location,
            "day": day,
            "details": details,
            "time": f"{times['start_time'].strftime('%H%M')}-{times['end_time'].strftime('%H%M')}"
        })
    
    return formatted_data

# Sample data
data = {
  "ALSS 101": [
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Monday",
      "time": "0900-0950",
      "details": "ALSS 101 Lecture Group D"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Monday",
      "time": "1700-1750",
      "details": "ALSS 101 Lecture Group F"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Monday",
      "time": "0800-0850",
      "details": "ALSS 101 Tutorial Group A"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Monday",
      "time": "1000-1050",
      "details": "ALSS 101 Tutorial Group K"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Monday",
      "time": "1000-1050",
      "details": "ALSS 101 Lecture Group A"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Tuesday",
      "time": "1400-1450",
      "details": "ALSS 101 Lecture Group H"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Tuesday",
      "time": "1000-1050",
      "details": "ALSS 101 Lecture Group B"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Tuesday",
      "time": "1500-1550",
      "details": "ALSS 101 Tutorial Group F"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Tuesday",
      "time": "0800-0850",
      "details": "ALSS 101 Tutorial Group H"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Wednesday",
      "time": "1200-1250",
      "details": "ALSS 101 Lecture Group J"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Wednesday",
      "time": "1300-1350",
      "details": "ALSS 101 Lecture Group K"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Thursday",
      "time": "1100-1150",
      "details": "ALSS 101 Tutorial Group J"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Thursday",
      "time": "1700-1750",
      "details": "ALSS 101 Tutorial Group G"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Thursday",
      "time": "1300-1350",
      "details": "ALSS 101 Tutorial Group D"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Thursday",
      "time": "1200-1250",
      "details": "ALSS 101 Lecture Group C"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Thursday",
      "time": "1700-1750",
      "details": "ALSS 101 Lecture Group I"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Friday",
      "time": "1100-1150",
      "details": "ALSS 101 Lecture Group E"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Friday",
      "time": "0800-0850",
      "details": "ALSS 101 Tutorial Group C"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Friday",
      "time": "1300-1350",
      "details": "ALSS 101 Lecture Group G"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Friday",
      "time": "1600-1650",
      "details": "ALSS 101 Tutorial Group E"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Friday",
      "time": "1600-1650",
      "details": "ALSS 101 Tutorial Group I"
    },
    {
      "location": "BIUST - AUDITORIUM,,,,,",
      "day": "Friday",
      "time": "1600-1650",
      "details": "ALSS 101 Tutorial Group B"
    }
  ]
}

# Process the data
result = combine_entries(data)

# Print the combined data
print(json.dumps(result, indent=4))