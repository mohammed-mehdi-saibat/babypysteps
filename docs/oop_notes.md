# Python OOP Notes: A PHP Dev's Perspective

Switching from Laravel/PHP to Python OOP takes a minute to get used to, but the core logic is exactly the same. Here is my quick mental translation guide.

### 1. What the heck is `self`?

TL;DR: `self` is literally just `$this` in PHP.
It refers to the current instance of the object. The only weird difference in Python is that you _have_ to explicitly write it as the first parameter in every single method definition (like `def my_method(self, name):`). It feels a bit repetitive at first because PHP just gives you `$this` magically, but they do the exact same job.

### 2. Public vs. "\_Private" Attributes

Python doesn't have strict `public`, `protected`, or `private` keywords. Technically, everything is public.
Instead, Python developers use a gentleman's agreement: if an attribute starts with a single underscore (like `self._records`), it means "Hey, this is meant to be private. Don't touch it from outside the class."
It won't actually crash the program if you break the rule, but it's bad practice. If we want outside code to read it, we should build a `@property` for it.

### 3. The Laravel / Eloquent Bridge

Building the `CsvDataset` class felt a lot like building an Eloquent Model in Laravel.

- **Laravel:** `class User extends Model` -> The `Model` parent handles all the messy database logic under the hood, so our child class can just use clean methods like `$user->save()`.
- **Python:** `class CsvDataset(Dataset)` -> `Dataset` handles the core data storage and counting, so our child class gets all those tools for free and can just focus on CSV-specific stuff.

In both languages, OOP is just about taking raw, messy data (like a database row or a CSV file) and wrapping it in an object so you can talk to it with clean, readable methods.
