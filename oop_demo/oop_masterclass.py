"""
oop_masterclass.py
==================

A runnable tour of Python's core object-oriented programming (OOP) pillars,
using a small vehicle-management system as the shared domain.

Sections:
    1. Classes, constructors, and destructors
    2. Instance variables vs. class variables
    3. Instance, class, and static methods
    4. Encapsulation and properties
    5. Inheritance and method overriding
    6. Polymorphism
    7. Abstraction with ABC

Run it with:

    python oop_masterclass.py

Only the Python standard library is used. Read the comments next to each
block, then compare them with the matching terminal output.
"""

import gc
from abc import ABC, abstractmethod


def print_section(title):
    """Print a clear separator so each OOP topic is easy to find."""
    print()
    print("=" * 64)
    print(title)
    print("=" * 64)


# ================================================================
# Section 1: Classes, Constructors, and Destructors
# ================================================================
# A class is a blueprint. An object (instance) is one real thing built
# from that blueprint. __init__ runs automatically when an object is
# created. __del__ runs when Python cleans the object up.
print_section("=== Section 1: Constructors & Destructors ===")


class Vehicle:
    """A general road vehicle and the base class for the fleet.

    Class variables (shared by every instance):
        vehicle_count: how many Vehicle objects currently exist
        default_wheels: the normal number of wheels
        category: a label subclasses can customize

    Instance variables (unique to each object):
        make, model, year, mileage, owner_id
    """

    # --- Class variables: stored on the class, shared by all instances ---
    vehicle_count = 0
    default_wheels = 4
    category = "vehicle"

    def __init__(self, make, model, year, mileage=0, owner_id="UNREGISTERED"):
        """Create a vehicle with its own unique data.

        Parameters:
            make: manufacturer, for example "Toyota"
            model: model name, for example "Corolla"
            year: four-digit model year
            mileage: starting mileage; must be zero or greater
            owner_id: identifier for the owner; at least four characters
        """
        # Public attributes: safe for any code to read and change.
        self.make = make
        self.model = model
        self.year = year

        # Protected attribute: the leading underscore is a convention that
        # says "internal use". Python does not block access to it.
        self._mileage = 0

        # Use the property setter to validate the starting mileage.
        self.mileage = mileage

        # Private attribute: the double underscore triggers name mangling,
        # so it is not reachable as vehicle.__owner_id from outside.
        self.__owner_id = "UNREGISTERED"

        # The public property below is the safe doorway to that private data.
        self.owner_id = owner_id

        # Update shared class state and mark this object as fully created.
        Vehicle.vehicle_count += 1
        self._counted = True
        print(f"  [created] {make} {model} (vehicle_count={Vehicle.vehicle_count})")

    def __del__(self):
        """Run when the object is cleaned up.

        Destructors are useful for diagnostics and releasing resources.
        Python does not promise an exact cleanup time, so this demo uses
        explicit `del` plus `gc.collect()` to make the output predictable.
        """
        # If __init__ failed partway through, do not change the count.
        if not getattr(self, "_counted", False):
            return

        Vehicle.vehicle_count -= 1
        model = getattr(self, "model", "unknown vehicle")
        print(
            f"  [cleaned up] {model} "
            f"(vehicle_count={Vehicle.vehicle_count})"
        )

    # -------------------- Encapsulation with properties --------------------
    @property
    def mileage(self):
        """Return the protected mileage value through a public property."""
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        """Validate mileage before storing it in _mileage."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Mileage must be a non-negative whole number.")
        self._mileage = value

    @property
    def owner_id(self):
        """Read the private owner ID through a safe public property."""
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, value):
        """Validate and normalize the private owner ID."""
        if not isinstance(value, str):
            raise ValueError("Owner ID must be text.")
        cleaned = value.strip().upper()
        if len(cleaned) < 4:
            raise ValueError("Owner ID must contain at least 4 characters.")
        self.__owner_id = cleaned

    # -------------------- Instance methods --------------------
    def describe(self):
        """Return a readable summary of this specific instance."""
        return (
            f"{self.year} {self.make} {self.model} | "
            f"{self.mileage:,} miles | owner: {self.owner_id}"
        )

    def drive(self, miles):
        """Add miles to this instance's odometer."""
        if miles <= 0:
            raise ValueError("Miles driven must be positive.")
        self.mileage = self.mileage + miles
        print(
            f"  Drove {miles:,} miles. {self.make} {self.model} now has "
            f"{self.mileage:,} miles."
        )

    def start_engine(self):
        """Default engine behavior; subclasses will override this."""
        print(f"  {self.make} {self.model}: engine starts.")

    # -------------------- Class method: alternative constructor --------------------
    @classmethod
    def from_string(cls, text):
        """Build a vehicle from text such as "Honda Accord 2021".

        cls refers to the class itself (or a subclass). A class method is
        often used as a second constructor when data arrives as text.
        """
        make, model, year_text = text.split()
        return cls(make, model, int(year_text))

    # -------------------- Static method: independent utility --------------------
    @staticmethod
    def km_to_miles(kilometers):
        """Convert kilometers to miles without using self or cls.

        A static method is simply a helper stored on the class. It does
        not need an object or any shared class data.
        """
        return kilometers * 0.621371


print("Creating a vehicle calls __init__ automatically:")
first_vehicle = Vehicle(
    make="Toyota",
    model="Corolla",
    year=2018,
    mileage=15_000,
    owner_id="AB-100",
)
print(f"  vehicle_count after creation: {Vehicle.vehicle_count}")

print("Deleting the object lets Python run __del__:")
del first_vehicle
gc.collect()
print(f"  vehicle_count after cleanup: {Vehicle.vehicle_count}")


# ================================================================
# Section 2: Instance Variables vs. Class Variables
# ================================================================
# Class variables belong to the blueprint: one shared value for all
# objects. Instance variables belong to one object and can differ.
print_section("=== Section 2: Instance vs. Class Variables ===")

print(f"Shared class variable default_wheels: {Vehicle.default_wheels}")
print(f"Shared class variable vehicle_count: {Vehicle.vehicle_count}")

city_car = Vehicle(
    make="Honda",
    model="Civic",
    year=2020,
    mileage=24_000,
    owner_id="CITY-1",
)
weekend_car = Vehicle(
    make="Mazda",
    model="MX-5",
    year=2017,
    mileage=9_000,
    owner_id="FUN-99",
)

print(f"After creating two cars, vehicle_count: {Vehicle.vehicle_count}")
print("Each object has its own mileage:")
print(f"  city_car.mileage:    {city_car.mileage:,}")
print(f"  weekend_car.mileage: {weekend_car.mileage:,}")

# Changing one object's instance data does not touch the other object.
city_car.drive(500)
print(f"  city_car.mileage after driving:    {city_car.mileage:,}")
print(f"  weekend_car.mileage after driving: {weekend_car.mileage:,}")


# ================================================================
# Section 3: Instance, Class, and Static Methods
# ================================================================
# Instance methods take self and work with one object's data.
# Class methods take cls and work with the class (often as constructors).
# Static methods take neither and are plain utility functions.
print_section("=== Section 3: Instance, Class & Static Methods ===")

print("Class method: build a Vehicle from one line of text.")
sedan = Vehicle.from_string("Honda Accord 2021")
print(f"  Created: {sedan.describe()}")

print("Instance method: add miles to that specific sedan.")
sedan.drive(120)

print("Static method: convert a distance; no object is required.")
kilometers = 120
miles = Vehicle.km_to_miles(kilometers)
print(f"  {kilometers} km is about {miles:.1f} miles.")


# ================================================================
# Section 4: Encapsulation and Properties
# ================================================================
# Public attributes are open to everyone.
# Protected attributes use _name as an "internal use" convention.
# Private attributes use __name and are name-mangled by Python.
# Properties provide validated, controlled access to internal data.
print_section("=== Section 4: Encapsulation & Properties ===")

print(f"Public attribute sedan.make: {sedan.make}")
print(f"Protected attribute sedan._mileage: {sedan._mileage}")
print("  (The underscore is a convention, not a security wall.)")
print(f"Private data through the property: {sedan.owner_id}")

print("The owner_id setter cleans and uppercases its input:")
sedan.owner_id = "own-2021"
print(f"  sedan.owner_id is now: {sedan.owner_id}")

print("The mileage setter accepts valid values and rejects bad ones:")
sedan.mileage = 5_000
print(f"  sedan.mileage is now: {sedan.mileage:,}")

try:
    sedan.mileage = -100
except ValueError as error:
    print(f"  Rejected mileage -> {error}")

try:
    sedan.owner_id = "abc"
except ValueError as error:
    print(f"  Rejected owner ID -> {error}")

print("Direct access to the private name is blocked from outside:")
try:
    print(sedan.__owner_id)
except AttributeError:
    print("  AttributeError: use the public owner_id property instead.")


# ================================================================
# Section 5: Inheritance and Method Overriding
# ================================================================
# A child class inherits parent attributes and methods. super() lets the
# child reuse the parent's work, then add or replace behavior.
print_section("=== Section 5: Inheritance & Method Overriding ===")


class Car(Vehicle):
    """A passenger car that specializes the Vehicle blueprint."""

    category = "car"

    def __init__(
        self,
        make,
        model,
        year,
        doors=4,
        mileage=0,
        owner_id="UNREGISTERED",
    ):
        """Initialize the Vehicle part first, then add car-specific data."""
        super().__init__(
            make=make,
            model=model,
            year=year,
            mileage=mileage,
            owner_id=owner_id,
        )
        self.doors = doors

    def describe(self):
        """Override describe(), extending the parent version with super()."""
        parent_text = super().describe()
        return f"{parent_text} | category: {self.category} | doors: {self.doors}"

    def start_engine(self):
        """Override the parent's generic engine sound."""
        print(f"  {self.make} {self.model}: engine rumbles to life.")


class ElectricCar(Car):
    """An electric car: inherits from Car and specializes it further."""

    category = "electric car"

    def __init__(self, make, model, year, battery_kwh, mileage=0, owner_id="UNREGISTERED"):
        """Reuse Car's constructor through super(), then add the battery."""
        super().__init__(
            make=make,
            model=model,
            year=year,
            doors=4,
            mileage=mileage,
            owner_id=owner_id,
        )
        self.battery_kwh = battery_kwh

    def describe(self):
        """Extend the car description with battery information."""
        parent_text = super().describe()
        return f"{parent_text} | battery: {self.battery_kwh} kWh"

    def start_engine(self):
        """A quiet override: electric cars do not rumble."""
        print(f"  {self.make} {self.model}: electric motor hums silently.")


family_car = Car(
    make="Volvo",
    model="XC60",
    year=2022,
    doors=5,
    mileage=18_000,
    owner_id="FAM-22",
)
print("Car inherits from Vehicle and calls super().__init__():")
print(f"  {family_car.describe()}")
print("Car overrides start_engine():")
family_car.start_engine()

electric_car = ElectricCar(
    make="Tesla",
    model="Model 3",
    year=2023,
    battery_kwh=75,
    mileage=6_000,
    owner_id="EV-2023",
)
print("ElectricCar reuses Car through super() and adds its own details:")
print(f"  {electric_car.describe()}")
electric_car.start_engine()


# ================================================================
# Section 6: Polymorphism
# ================================================================
# Polymorphism means one method name can produce different behavior.
# The loop below treats every object the same way: it calls describe()
# and start_engine() without checking the exact subclass first.
print_section("=== Section 6: Polymorphism ===")


class Motorcycle(Vehicle):
    """Another Vehicle subclass with its own engine behavior."""

    category = "motorcycle"
    wheels = 2  # a class variable that overrides Vehicle.default_wheels

    def __init__(self, make, model, year, mileage=0, owner_id="UNREGISTERED"):
        """Reuse the parent constructor; no extra instance data is needed."""
        super().__init__(
            make=make,
            model=model,
            year=year,
            mileage=mileage,
            owner_id=owner_id,
        )

    def start_engine(self):
        """Override the parent with motorcycle-specific behavior."""
        print(f"  {self.make} {self.model}: BRAAAP! The engine revs loudly.")


motorcycle = Motorcycle(
    make="Royal Enfield",
    model="Classic 350",
    year=2021,
    mileage=4_200,
    owner_id="MC-350",
)

fleet = [family_car, electric_car, motorcycle]

print("One loop, three different subclasses, one shared interface:")
for vehicle in fleet:
    print(f"  {vehicle.describe()}")
    vehicle.start_engine()

print(f"Motorcycle class variable wheels: {motorcycle.wheels}")
print(f"Vehicle class variable default_wheels: {Vehicle.default_wheels}")


# ================================================================
# Section 7: Abstraction with ABC
# ================================================================
# An abstract base class defines a blueprint that child classes must
# follow. You cannot instantiate the blueprint itself, and any child
# must implement every @abstractmethod before it can be created.
print_section("=== Section 7: Abstraction with ABC ===")


class AutonomousVehicle(Vehicle, ABC):
    """Blueprint for vehicles that must be able to navigate themselves."""

    @abstractmethod
    def navigate(self, destination):
        """Plan and follow a route to destination.

        Every concrete autonomous vehicle MUST implement this method.
        """


print("Trying to instantiate the abstract blueprint directly:")
try:
    blueprint = AutonomousVehicle("Acme", "Prototype", 2026)
except TypeError as error:
    print(f"  Blocked as expected -> {error}")


class Robotaxi(AutonomousVehicle):
    """A concrete autonomous vehicle that implements the blueprint."""

    category = "robotaxi"

    def __init__(self, make, model, year, mileage=0, owner_id="UNREGISTERED"):
        """Reuse Vehicle's constructor through the abstract class."""
        super().__init__(
            make=make,
            model=model,
            year=year,
            mileage=mileage,
            owner_id=owner_id,
        )
        self.autopilot_on = False

    def navigate(self, destination):
        """Fulfill the abstract requirement with a concrete implementation."""
        self.autopilot_on = True
        print(
            f"  {self.make} {self.model}: route to {destination} calculated. "
            "Autopilot engaged."
        )

    def start_engine(self):
        """Override the parent engine behavior for a quiet robotaxi."""
        print(f"  {self.make} {self.model}: electric motors spin up quietly.")


robotaxi = Robotaxi(
    make="Waymo",
    model="Zeekr",
    year=2025,
    mileage=1_200,
    owner_id="ROBO-1",
)

print("Robotaxi implements the required navigate() method:")
robotaxi.navigate("Central Station")
robotaxi.start_engine()
print(f"  robotaxi.autopilot_on: {robotaxi.autopilot_on}")
print(f"  Is a Robotaxi also a Vehicle? {isinstance(robotaxi, Vehicle)}")


# ================================================================
# Summary and explicit cleanup
# ================================================================
print_section("=== Summary: The Seven Pillars ===")
print("1. Class / object    -> a blueprint and the real instances built from it")
print("2. Constructor       -> __init__ prepares a new object")
print("3. Destructor        -> __del__ runs during cleanup")
print("4. Instance data     -> unique values stored on self")
print("5. Class data        -> shared values stored on the class")
print("6. Instance method   -> uses self")
print("7. Class method      -> uses cls; handy as an alternative constructor")
print("8. Static method     -> a utility that needs neither self nor cls")
print("9. Encapsulation     -> public / protected / private + validated properties")
print("10. Inheritance      -> a child reuses a parent through super()")
print("11. Overriding       -> a child replaces or extends inherited behavior")
print("12. Polymorphism     -> one method name, many behaviors")
print("13. Abstraction      -> ABC + @abstractmethod enforce a blueprint")

print()
print(f"Vehicles registered before cleanup: {Vehicle.vehicle_count}")
print("Releasing every demo object so __del__ can be observed:")
del fleet, vehicle
del city_car, weekend_car, sedan, family_car, electric_car, motorcycle, robotaxi
gc.collect()
print(f"Vehicles registered after cleanup: {Vehicle.vehicle_count}")
