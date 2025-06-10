import random # This will help create the fake log entries like the IPs, filenames, and event types
import datetime # Here it will generate a realistic timestamp for each log entry that is shown to the user
import ipaddress # This will simulate the source of events like the attackers IP address and this will ensure the IPs look valid

def generate_system_logs(num_entries=20): #This defines the function generate_system_logs and creates the fake log entries now by default it will create 20 of them
    logs = [] # This will create an empty list to store when each log is generated
    event_types = ['login', 'file_access', 'process_start', 'network_connection', 'ransomware_activity'] # Creating a list of all the possible system event types
    countries = ['US', 'CN', 'RU', 'BR', 'IN', 'DE', 'FR', 'NG', 'KR', 'IR'] # I am setting a list here of country codes to get randomly assigned to each of the log entries
    for _ in range(num_entries): # This begins a for loop to run the num_entries 20 times by default to create a fake system log entry each time
        event = random.choice(event_types) # This randomly picks an event type that I defined earlier for the log entries
        timestamp = datetime.datetime.now() - datetime.timedelta(minutes=random.randint(1, 10000)) # This will take the current time and subtract a random number of minutes from it to simulate the past event times
        ip = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1))) # It will randomly pick a number between 0 and the max possible IPv4 address, and it will make it look like a real IP address then converts it into a string for the log dictionary
        country = random.choice(countries) # picks a random country origin I specified earlier for the log entry
        log_entry = {   # Here I created a dictionary to hold these key value pairs to represent a full log entry
            'timestamp': timestamp,
            'ip': ip,
            'country': country,
            'event': event
        }
        logs.append(log_entry)  # This adds the current log entry to the logs list
    return logs # This will return the complete list of generated lof entries

def detect_ransomware_and_alert(logs): # Here I created a new function to take the logs as the input and check each entry for any ransomware the handle and log the alerts are they appear
    ransomware_logs = [log for log in logs if log['event'] == 'ransomware_activity']  # Added this missing line to define ransomware_logs
    if ransomware_logs: # Checks if the list ransomware_logs is not empty meaning no ransomware detected
        print("ALERT! Ransomware activity detected! Please review the log file immediately!!") # This will be shown to the user if there is ransomware detected
        with open('ransomware_logs.txt', 'w') as file: # This creates and opens a file in write mode  to save the ransomware event details
            for log in ransomware_logs: # This starts a for loop to get through every ransomware log entry
                file.write(f"{log['timestamp']} | {log['ip']} | {log['country']} | {log['event']}\n") # This writes a single ransomware log line into the file to show the timestamp, IP, country and event type
        view = input("Would you like to view the ransomware log file now? (yes/no): ").strip().lower() # This here will allow the user to decide if they would like to open the log file now or wait
        if view == 'yes': # Checks if the user said yes then decides to run the next part
            with open('ransomware_logs.txt', 'r') as file: # Opens the file for the user in read mode only
                for line in file:
                    print(line.strip()) # This for loop goes through each line of the file and prints it to the screen for the user to view the strip() helps remove any whitespace or newline characters

if __name__ == "__main__":
    logs = generate_system_logs()  # Generates 20 fake system logs
    detect_ransomware_and_alert(logs)  # Checks for ransomware and any alerts
