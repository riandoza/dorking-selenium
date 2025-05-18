import csv
import time
from urllib.parse import urlparse


def wait_for_string(string_variable, timeout=60):
    start_time = time.time()
    while True:
        if string_variable:  # Checks if the string is not None or empty
            return string_variable
        if time.time() - start_time > timeout:
            raise TimeoutError("Timeout waiting for string to be not null")
        time.sleep(1)


def get_schema_and_domain(url):
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme.strip()
    domain = parsed_url.netloc.strip()
    return f"{scheme}://{domain}"


def append_dict_to_csv(file_path, field_names, data_dict):
    # writing to csv file
    with open(file_path, "a", newline="") as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        # writing headers (field names)
        if csvfile.tell() == 0:
            writer.writeheader()
        # writing data rows
        writer.writerows(data_dict)
    csvfile.close()
    return True
