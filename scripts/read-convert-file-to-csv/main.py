# File path
file_path = '/path/to/file.txt'

import csv
from datetime import datetime

# Define the order
order = {'New': 1, 'Pending': 2, 'Canceled': 3}

# Define the count of each status to be counted
status_count = {'New': 0, 'Pending': 0, 'Canceled': 0}


# Function to insert date and name
def date_and_name():
    date = None  # Initialize date as None
    name = ""  # Initialize name as an empty string
    while True:
        if date is None:
            # Validate the date
            date_input = input("Enter today's date (dd/mm/yyyy): ")
            try:
                datetime.strptime(date_input, "%d/%m/%Y")
                date = date_input  # Save the valid date
            except ValueError:
                print("Invalid date format. Use the format dd/mm/yyyy.")
                continue  # If the date is invalid, continue the loop to ask for the date again

        # Validate the name
        name = input("Enter your name: ").strip()
        if name == "":
            print("Name cannot be empty. Please enter your name.")
        else:
            break  # If the name is valid, exit the loop

    return date, name


def validate_confirmation():
    while True:
        confirmation = input("Do you want to proceed? (y/n): ").strip().lower()
        if confirmation == 'y':
            return True
        elif confirmation == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def remove_empty_lines(file_path):
    try:
        # Read the file and filter out empty lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Filter out empty lines (lines that are just whitespace are considered empty)
        non_empty_lines = [line for line in lines if line.strip()]

        # Write the non-empty lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(non_empty_lines)

        print(f"Empty lines removed from {file_path}")

    except FileNotFoundError:
        print(f"The file {file_path} was not found. Please check the file path.")
    except IOError as e:
        print(f"Error reading or writing the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Function to get the status from a line
def get_status(line):
    return line.split()[1]


# Function to read a text file and return a list of space-separated information
def read_ordered_file(ordered_file):
    try:
        with open(ordered_file, 'r') as file:
            # Read all lines and split each line into components
            lines = [line.strip().split() for line in file.readlines()]
        return lines

    except FileNotFoundError:
        # Capture the error if the file is not found
        print("The file was not found. Check the file name and path.")
    except IOError as e:
        # Capture and display errors related to file reading or writing
        print(f"Error reading the file: {e}")
    except Exception as e:
        # Capture and display any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Function to write data to a CSV file, including the provided date and name
def write_to_csv(ordered_file, output_csv, date, name):
    try:
        with open(output_csv, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for entry in ordered_file:
                if len(entry) >= 2:  # Check if the line has at least two elements
                    code, status = entry
                    csv_writer.writerow([date, code, name, status])

    except FileNotFoundError:
        # Capture the error if the file is not found
        print("The file was not found. Check the file name and path.")
    except IOError as e:
        # Capture and display errors related to file reading or writing
        print(f"Error reading the file: {e}")
    except Exception as e:
        # Capture and display any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Function to read the text file and display the information
def file_info():
    remove_empty_lines(file_path)
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Initialize the line counter
            total_lines = len(lines)

            # Counter for each status
            for line in lines:
                # Remove whitespace around and split the line
                parts = line.strip().split()

                # Check if the line has at least two elements
                if len(parts) >= 2:
                    status = get_status(line)
                    if status in status_count:
                        status_count[status] += 1

        # Display the results
        print(f"File name: {file_path.split('/')[-1]}\nTotal lines: {total_lines}")
        for status, count in status_count.items():
            print(f"Total '{status}': {count}")
    # Capture exception
    except FileNotFoundError:
        # Capture the error if the file is not found
        print("The file was not found. Check the file name and path.")
    except IOError as e:
        # Capture and display errors related to file reading or writing
        print(f"Error reading the file: {e}")
    except Exception as e:
        # Capture and display any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Sorting function
def sort_file():
    try:
        # Open the file for sorting
        with open(file_path, 'r') as file:
            # Read all lines from the file, removing whitespace around
            lines = [line.strip() for line in file.readlines()]

        # Sort the lines based on the value defined in 'order'
        # 'key=lambda line: order.get(get_status(line), float('inf'))' defines the sorting logic
        # The value returned by get_status is used to look up the order in the 'order' dictionary
        # If the status is not in the dictionary, use float('inf') to ensure it's sorted last
        ordered_lines = sorted(lines, key=lambda line: order.get(get_status(line), float('inf')))

        # Display the ordered lines in the console
        for line in ordered_lines:
            print(line)

        # Open a new file for writing
        # Write the ordered lines to the new file
        with open('/path/to/ordered-file.txt', 'w') as ordered_file:
            for line in ordered_lines:
                ordered_file.write(f"{line}\n")

    except FileNotFoundError:
        # Capture the error if the file is not found
        print("The file was not found. Check the file name and path.")
    except IOError as e:
        # Capture and display errors related to file reading or writing
        print(f"Error reading the file: {e}")
    except Exception as e:
        # Capture and display any other unexpected errors
        print(f"An unexpected error occurred: {e}")


def main():
    try:
        print("Script started!")

        date, name = date_and_name()
        print(f"Date: {date}\nName: {name}")
        print("File information:")
        file_info()
        if not validate_confirmation():
            exit("Operation canceled")

        sort_file()
        print("Ordered file created!")
        if not validate_confirmation():
            exit("Operation canceled")

        ordered_file_path = '/path/to/ordered-file.txt'
        ordered_file = read_ordered_file(ordered_file_path)
        output_csv = '/path/to/file.csv'

        # Write the data to the CSV file
        write_to_csv(ordered_file, output_csv, date, name)
        print(f"Data has been written to {output_csv}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
