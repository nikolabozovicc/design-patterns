
# Singleton Pattern

The **Singleton** ensures that a class has **only one instance** throughout the application and provides a **global access point** to it.

## 💡 Use Cases
- Logging system
- Configuration manager
- Database connections
- Caching
- Thread pools

###  Logging System
❓ Problem:
In most applications, you want all logs to be stored consistently (e.g., to the same file or console) and formatted uniformly.

⚠️ Without Singleton:
- You might accidentally create multiple logger instances.

- This could lead to different log formats, duplicated log files, or concurrency issues.

✅ With Singleton:
- One logger instance handles all logging.

- Ensures consistent format, output location, and centralized control.

- Makes it easy to change logging behavior (e.g., file path, log level) in one place.

> Real Example: Python’s built-in `logging` module is often used as a de facto singleton by configuring it globally.

### Configuration Manager
❓ Problem:
Applications often read configuration data (from files, environment variables, or databases). This config should remain consistent and globally available throughout the app.

⚠️ Without Singleton:
- Multiple objects might reload the config, increasing memory use or causing inconsistency.

- If one instance changes a setting, the others won’t know.

✅ With Singleton:
- All parts of the app access the same configuration instance.

- Guarantees consistency of config values across components.

- Useful for feature flags, environment toggles, database URLs, etc.

### Database Connections
❓ Problem:
Database connections are expensive to create and maintain.

⚠️ Without Singleton:
- Each time you access the database, a new connection might be opened.

- This is slow, wasteful, and risks hitting connection limits on the DB server.

✅ With Singleton:
- A single connection or connection pool object is reused across the app.

- Improves performance and resource efficiency.

- Centralizes error handling and connection recovery logic.

> Real Example: ORMs like SQLAlchemy or Django’s database engine use a global connection pool or connection manager.

### Caching System
❓ Problem:
To avoid repeated computation or data fetching (e.g., from DB or API), apps use caching.

⚠️ Without Singleton:
- Multiple components could build their own cache, wasting memory.

- One part of the system might not “see” what another part has cached.

✅ With Singleton:
- A global cache (like an in-memory `dict` or Redis client wrapper) ensures shared, centralized storage.

- All modules store to and read from the same memory location.

- Guarantees that cached values are reused correctly across the app.

> Example: `lru_cache` in Python or memoization decorators behave like singletons.

### Thread Pool / Task Manager
❓ Problem:
Managing threads or async tasks needs control and synchronization.

⚠️ Without Singleton:
- Multiple thread pools might be created unintentionally.

- Threads could compete, waste CPU, or lead to deadlocks.

✅ With Singleton:
- You define one `ThreadPoolExecutor` or task queue.

- All threads are managed through a single instance, with a shared task lifecycle and limit.

- Simplifies resource tracking, shutdown, and debugging.

> Real Example: Background workers, queue managers, and `asyncio` event loops often use singleton-like patterns to manage task execution.

## ❗ Aditional

In Python, modules are singletons by design:
```python
# singleton_module.py
class Config:
    ...
config = Config()
```
Anyone who does:
```python
from singleton_module import config
```
gets the same `config` object — always.

Look for the `singleton.py` file. It contains an example of how to implement a singleton class by overriding the `__new__` method.

To test it, run:
```bash
python singleton.py
```

Look for `singleton_meta.py` file. It contains an example of how to implement singleton class using metaclass, which is another popular, clean, and reusable way to implement the Singleton pattern in Python. It’s actually a more elegant solution than the `__new__` approach in many cases, especially when you want to reuse the Singleton logic across multiple unrelated classes.

To test it, run:
```bash
python singleton_meta.py
```

## ℹ️ About metaclass

In Python:

- A metaclass is like a “class of a class.”

- Just like classes create objects, metaclasses create classes.

- By customizing a metaclass, you can control how classes are created or behave at a deeper level.

So when you use:
```python
class MySingleton(metaclass=SingletonMeta):
    ...
```
it means `MySingleton`’s creation and instantiation are governed by `SingletonMeta`.

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Create the first and only instance of cls
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
```

- `SingletonMeta` inherits from `type`, which makes it a metaclass.

- `_instances` is a dictionary storing singleton instances for each class using this metaclass (keys = classes, values = their single instance).

- `__call__` is what happens when you do `MySingleton()`.

  - It overrides the normal instantiation process.

  - If no instance exists for cls (the class), it calls `super().__call__()` to create one.

  - Otherwise, it simply returns the existing instance.

Then:
```python
class MySingleton(metaclass=SingletonMeta):
    pass
```
- `MySingleton` is an ordinary class.

- But because it uses `SingletonMeta` as its metaclass, calling `MySingleton()` goes through `SingletonMeta.__call__()`.

- That guarantees only one instance of `MySingleton` will ever exist.

#### Why Is This Good?
- **Reusable**: You can use the same SingletonMeta with many classes:
```python
class Logger(metaclass=SingletonMeta):
    ...

class ConfigManager(metaclass=SingletonMeta):
    ...
```
- **Decoupled**: You don’t need to add Singleton logic in each class (unlike `__new__` approach).
- **Clean**: No need to manage `_initialized` flags or extra logic in your classes.

But it’s overkill if you only have a single class needing Singleton behavior — in that case,` __new__` approach is simpler.

