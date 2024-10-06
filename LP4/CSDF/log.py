import logging
import datetime
import re

class LogCaptureAndEventCorrelation:
    def __init__(self, log_files):
        self.log_files = log_files
        self.log_events = []
        self.correlation_rules = []

    def capture_logs(self):
        for log_file in self.log_files:
            try:
                with open(log_file, "r") as f:
                    for line in f:
                        self.log_events.append(self.parse_log_line(line))
            except FileNotFoundError:
                print(f"Error: File '{log_file}' not found.")
                continue  # Skip this file and continue with others
            except Exception as e:
                print(f"An error occurred while processing '{log_file}': {e}")
                continue

    def parse_log_line(self, line):
        # Split the log line into fields
        fields = re.split(r"\s+", line)
        # Extract the timestamp and message from the log line
        timestamp = datetime.datetime.strptime(fields[0] + ' ' + fields[1], "%Y-%m-%d %H:%M:%S")
        message = " ".join(fields[2:])  # Adjusted to handle the split
        # Create a log event object
        log_event = {
            "timestamp": timestamp,
            "message": message
        }
        return log_event

    def add_correlation_rule(self, rule):
        self.correlation_rules.append(rule)

    def correlate_events(self):
        for rule in self.correlation_rules:
            # Match the correlation rule against the log events
            matching_events = [event for event in self.log_events if rule["conditions"][0]["value"] in event["message"]]
            # If the rule matches two or more log events, then generate a correlation alert
            if len(matching_events) >= 2:
                alert = {
                    "rule": rule,
                    "matching_events": matching_events
                }
                print("\nCorrelation alert:")
                print("Rule:", rule["name"])
                print("Matching events:")
                for event in matching_events:
                    print(event)

    def start(self):
        self.capture_logs()
        self.correlate_events()

if __name__ == "__main__":
    # Prompt for user-defined input for log files
    user_input = input("Enter the paths of the log files (comma-separated): ")
    log_file_paths = [path.strip() for path in user_input.split(",")]

    # Create a LogCaptureAndEventCorrelation object
    log_capture_and_event_correlation = LogCaptureAndEventCorrelation(log_file_paths)
    
    # Add a correlation rule
    log_capture_and_event_correlation.add_correlation_rule({
        "name": "Failed login attempts",
        "conditions": [
            {
                "field": "message",
                "operator": "contains",
                "value": "Failed login"
            }
        ]
    })

    # Start the log capture and event correlation process
    log_capture_and_event_correlation.start()
