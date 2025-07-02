class SingletonMeta(type):
    """
    A metaclass that creates a Singleton by overriding __call__.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"[SingletonMeta] Creating new instance of {cls.__name__}")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            print(f"[SingletonMeta] Reusing existing instance of {cls.__name__}")
        return cls._instances[cls]


class MySingleton(metaclass=SingletonMeta):
    def __init__(self):
        print("MySingleton __init__ called")
        self.data = "Some important shared data"

    def do_something(self):
        print(f"Doing something with {self.data}")


def test_singleton():
    print("\n--- Testing Singleton ---")
    s1 = MySingleton()
    s2 = MySingleton()

    s1.do_something()
    s2.do_something()

    print(f"s1 id: {id(s1)}")
    print(f"s2 id: {id(s2)}")
    assert s1 is s2, "Singleton failed: Different instances exist!"
    print("✅ Singleton test passed: s1 and s2 are the same instance.")


if __name__ == "__main__":
    test_singleton()
