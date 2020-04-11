import argparse
from distutils.util import strtobool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script is going to create an employee profile. 
    """)
    parser.add_argument("name", help="Name of Employee")
    parser.add_argument("title", help="Job Title of Employee")
    parser.add_argument("--address", help="Address of Employee")
    parser.add_argument("--country",choices=["Singapore", "United States", "Malaysia"], help="Country/Region of Employee")
    parser.add_argument("--isFullTime", default=True, type=strtobool, help="Is this Employee Full Time? (default: %(default)s)")

    args = parser.parse_args()

    NAME = args.name
    TITLE = args.title
    ADDRESS = args.address
    COUNTRY = args.country
    FULLTIME = args.isFullTime

    print("Name : " + NAME)
    print("Job Title : " + TITLE)
    print("Address : " + str(ADDRESS))
    print("Country : " + str(COUNTRY))

    if FULLTIME:
        print(NAME + " is a full time employee.") 
    else: 
        print(NAME + " is not a full time employee.") 

