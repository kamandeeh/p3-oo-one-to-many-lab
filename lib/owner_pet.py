class Owner:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Owner name must be a non-empty string.")
        self.name = name
        self._pets = []  # Stores the pets owned by this owner

    def pets(self):
        """Returns a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's list of pets, setting the pet's owner if not already set."""
        if not isinstance(pet, Pet):
            raise Exception("add_pet requires a Pet instance.")

        if pet.owner and pet.owner != self:
            raise Exception(f"This pet is already owned by {pet.owner.name}.")

        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Class variable to store all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Pet name must be a non-empty string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type. Must be one of: {', '.join(Pet.PET_TYPES)}.")
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the pet to the owner's list if an owner is provided
        if owner:
            owner.add_pet(self)

        # Add this instance to the class-level list of pets
        Pet.all.append(self)


# Example Usage
# Create Owners
owner1 = Owner("Alice")
owner2 = Owner("Bob")

# Create Pets
pet1 = Pet("Fluffy", "dog", owner1)
pet2 = Pet("Whiskers", "cat", owner1)
pet3 = Pet("Tweety", "bird")

# Add a pet to an owner
owner2.add_pet(pet3)

# List of all pets
print([pet.name for pet in Pet.all])

# Owner's pets
print([pet.name for pet in owner1.pets()])

# Sorted pets by name for an owner
print([pet.name for pet in owner1.get_sorted_pets()])
