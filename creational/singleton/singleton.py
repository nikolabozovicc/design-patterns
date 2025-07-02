class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the Singleton instance (only once)...")
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False  # add flag to track initialization
        return cls._instance

    def __init__(self):
        if not self._initialized:
            print("Initializing the Singleton instance (only once)...")
            # Put your one-time initialization logic here:
            self.some_data = "Important data"
            self._initialized = True

    def some_business_logic(self):
        print("Doing something important...")


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    s1.some_business_logic()
    s2.some_business_logic()

    print(f"Are s1 and s2 the same instance? {s1 is s2}")
