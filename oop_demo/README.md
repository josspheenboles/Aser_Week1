# OOP Masterclass

A single-file, beginner-friendly tour of the core pillars of object-oriented
programming (OOP) in Python. The shared example is a small **vehicle management
system**: cars, an electric car, a motorcycle, and a robotaxi all grow from one
`Vehicle` blueprint.

Only the Python standard library is used.

## What is demonstrated

| Section | Concept | Example in the script |
| --- | --- | --- |
| 1 | Classes, `__init__`, `__del__` | Creating and deleting a `Vehicle` |
| 2 | Instance vs. class variables | `vehicle_count` is shared; each car has its own `mileage` |
| 3 | Instance, class, and static methods | `drive()`, `from_string()`, `km_to_miles()` |
| 4 | Encapsulation and properties | `_mileage`, `__owner_id`, `@property` validation |
| 5 | Inheritance and overriding | `Car` and `ElectricCar` use `super()` |
| 6 | Polymorphism | One loop calls `start_engine()` on three subclasses |
| 7 | Abstraction | `AutonomousVehicle(ABC)` with `@abstractmethod` |

### Key terms in one sentence each

- **Class:** a blueprint for making objects.
- **Object:** one real instance built from a class.
- **`__init__`:** the constructor that prepares a new object.
- **`__del__`:** the destructor that runs when an object is cleaned up.
- **`self`:** the current object inside an instance method.
- **`cls`:** the current class inside a class method.
- **Instance variable:** unique data stored on one object.
- **Class variable:** shared data stored on the class.
- **Property:** a method that behaves like an attribute, often used to validate access.
- **`super()`:** a way for a child class to reuse its parent's code.
- **Polymorphism:** the same method name can behave differently on different classes.
- **ABC:** an abstract base class that forces subclasses to implement a blueprint.

## Requirements

- Python 3.8 or newer (the script uses only standard-library features)
- No third-party packages

Check your version:

```bash
python --version
```

## How to run

1. Open a terminal (PowerShell, Command Prompt, or a terminal on macOS/Linux).
2. Move into this folder:

   ```powershell
   cd C:\Users\M\Desktop\Aser_Demo\oop_demo
   ```

   On macOS or Linux, use the path where you saved the folder:

   ```bash
   cd /path/to/Aser_Demo/oop_demo
   ```

3. Run the script:

   ```bash
   python oop_masterclass.py
   ```

### If `python` is not found

- **Windows:** try `py oop_masterclass.py`.
- **macOS/Linux:** try `python3 oop_masterclass.py`.

## Sample output

The script prints a header for each section so the terminal output maps directly
to the code:

```text
================================================================
=== Section 1: Constructors & Destructors ===
================================================================
Creating a vehicle calls __init__ automatically:
  [created] Toyota Corolla (vehicle_count=1)
  vehicle_count after creation: 1
Deleting the object lets Python run __del__:
  [cleaned up] Corolla (vehicle_count=0)
  vehicle_count after cleanup: 0

================================================================
=== Section 6: Polymorphism ===
================================================================
One loop, three different subclasses, one shared interface:
  2022 Volvo XC60 | 18,000 miles | owner: FAM-22 | category: car | doors: 5
  Volvo XC60: engine rumbles to life.
  ...
  Tesla Model 3: electric motor hums silently.
  ...
  Royal Enfield Classic 350: BRAAAP! The engine revs loudly.
```

The final cleanup block explicitly deletes every demo object and calls
`gc.collect()`, making the `__del__` messages predictable.

## How to read the script

Each section follows the same pattern:

1. A header is printed.
2. The relevant class or method is defined with a docstring.
3. A short demo creates objects and prints the result.
4. Inline comments explain **why** the behavior happens.

Start at the top and run the file once without editing it. Then read one section
at a time beside its terminal output.

## Try it yourself

1. **Add an object:** create a second `Motorcycle` in Section 6 and add it to
   `fleet`. The polymorphism loop should handle it with no changes.
2. **Override a method:** give `Motorcycle` its own `describe()` that calls
   `super().describe()` and adds `"| type: motorcycle"`.
3. **Add validation:** make the `year` setter reject years before 1900. Store the
   year in `_year` and expose it through a property.
4. **Add a subclass:** create a `Truck(Vehicle)` with a `payload_tons` attribute
   and its own `start_engine()` sound.
5. **Extend the abstract blueprint:** add a second `@abstractmethod` such as
   `park()` to `AutonomousVehicle`, then implement it in `Robotaxi`.

## A note about `__del__`

Python does not guarantee exactly when `__del__` runs; it depends on reference
counting, the garbage collector, and interpreter shutdown. The demo uses
explicit `del` statements plus `gc.collect()` so the cleanup messages appear in
a predictable order. In real applications, prefer context managers (`with`) or
explicit `close()` methods for important resource cleanup rather than relying on
`__del__`.

## Files

| File | Purpose |
| --- | --- |
| `oop_masterclass.py` | The annotated OOP demo |
| `README.md` | This guide |
