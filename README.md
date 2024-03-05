# Holberton School - AirBnB Clone

## Description

This project is an implementation of a simple version of the AirBnB clone. It includes a command-line interpreter (CLI) that allows users to create, update, destroy, and display Airbnb-like objects. The objects include amenities, cities, places, reviews, and users.

## Command Interpreter

### How to Start

To start the command interpreter, run the following command:

```bash
./console.py
```

### How to Use

Once the interpreter is running, you can use the following commands:

- `help`: List available commands.
- `create <class_name>`: Create a new instance of the given class.
- `show <class_name> <id>`: Show details of a specific instance.
- `destroy <class_name> <id>`: Delete an instance.
- `all [class_name]`: Show all instances or all instances of a specific class.
- `update <class_name> <id> <attribute_name> "<attribute_value>"`: Update attributes of an instance.

### Examples

Here are some examples of using the command interpreter:

```bash
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) all
(hbnb) destroy BaseModel 1234-1234-1234
(hbnb) update BaseModel 1234-1234-1234 name "New Name"
```

## Requirements

- Python 3.7.4 or later
- PEP8 style
- Unittest module for testing

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tync0/holbertonschool-AirBnB_clone.git
   ```
2. Change into the project directory:
   ```bash
   cd holbertonschool-AirBnB_clone
   ```
3. Run the command interpreter:
   ```bash
   ./console.py
   ```

## Authors

- [Elnur](https://github.com/elnurra)
- [Tuncay](https://github.com/tync0)

## Learning Objectives

- Serialization / Deserialization flow (object <-> Dict <-> Json <-> file)
- Packages / Modules / Cyclical imports / How to import / Prevent execution / Etc.
- Layered architecture
- Interfaces (storage)
- Abstract Classes (BaseClass)

## Team Collaboration

### Knowledge of the Main Program Flow

We used various packages and modules throughout the project to ensure a smooth program flow. The main packages include:
- `os`: For working with the operating system.
- `json`: For JSON serialization and deserialization.
- `unittest`: For testing.
- `datetime`: For working with dates and times.

### Distribution of Work

We divided the project into manageable tasks and each team member took responsibility for specific modules. Pull requests were used for code review and merging into the main branch.

---
