import csv
import sys

# Read the csv file
def read_csv(path: str) -> list:
    try:
        with open(path) as data:
            reader = csv.reader(data)
            next(reader) # Skip header row
            return list(reader)
    except IOError as e:
        print(e)
        sys.exit()

# Get all the returns
def get_returns() -> list:
    return [float(returns[1]) for returns in read_csv("data.csv")]

def process_the_returns() -> float:
    # Get the sum of the returns and divide the sum by the number of returns
    returns = get_returns()
    return sum(returns) / len(returns)

print("%.2f" % process_the_returns() + "%")