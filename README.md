# IP Network Tags Lookup

This is a Python application that utilizes an interval tree to efficiently manage and search for tags associated with IP addresses.

## Functionalities

*   **Build Interval Tree:** Creates an interval tree data structure from a list of (IP network, tag) pairs.
*   **IP Tag List Lookup:** Given an IP address, it searches the knowledge base and retrieves all associated tags from overlapping networks.
*   **IP Tag Report**: Given an IP address, it searches the knowledge base and returns all associated tags in a form of a HTML report.

## Usage

1.  **Setup:**

    In order for the service to work properly, you need to:
    * **Provide a JSON data file**: the file has to be put inside of the /data folder
    Example JSON file:
    ```json
    [
      {"tag": "foo", "ip_network": "192.0.2.0/24"},
      {"tag": "bar", "ip_network": "192.0.2.8/29"},
      {"tag": "bar", "ip_network": "10.20.0.0/16"},
      {"tag": "SPAM", "ip_network": "10.20.30.40/32"},
    ]
    ```
    If no data file is provided, activating the service will fail.

    * **Setup the .env file**: copy the .env file using
    ```bash
    cp .env.example .env 
    ```
    and set its environmental variables accordingly:

    KNOWLEDGE_BASE_FILENAME - file name of the JSON file inside of /data folder
    NUM_WORKERS - number of Uvicorn workers to be used by the service
    HOST - address the service will be served at
    PORT - port the service will be available at

2.  **Running the service:**

    The service is best run using docker compose with the following:
    ```bash
    docker compose up
    ```

3.  **Usage:**

    After starting, the service allows its users to send HTTP requests at the specified host and port.
    The available endpoints are:
    * **GET /ip-tags/{ip}**: returns a JSON document containing the tags corresponding to the passed IP address.
    * **GET /ip-tags-report/{ip}**: return a HTML document containing a table with tags corresponding to the passed IP address.

    The service's OpenAPI documentation is available at the */docs* endpoint.

4.  **[Optional] Testing:**

    To run the application's tests you need the pytest framework to be installed in your environment and run the *run_tests.sh* script.
