class DatabaseConnectionManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnectionManager, cls).__new__(cls)
            # Initialize database connection here
            cls._instance.connection = None
        return cls._instance

    def connect(self, database_url):
        if not self.connection:
            # Simulate establishing a database connection
            print(f"Connecting to {database_url}")
            self.connection = f"Connection to {database_url} established."
        else:
            print("Already connected.")

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            return "Not connected. Call connect() first."

# Client code
if __name__ == "__main__":
    # Creating instances
    db_manager1 = DatabaseConnectionManager()
    db_manager2 = DatabaseConnectionManager()

    # Both instances should be the same
    print(db_manager1 is db_manager2)  # Output: True

    # Connecting to the database
    db_manager1.connect("example_database_url")

    # Attempting to connect again
    db_manager2.connect("another_database_url")

    # Both instances share the same connection
    print(db_manager1.get_connection())  # Output: Connection to example_database_url established.
    print(db_manager2.get_connection())  # Output: Connection to example_database_url established.
