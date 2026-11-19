"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    # Create an empty dictionary to store restaurant reservations.
    reservations = {}

    # Add five reservation records using unique reservation IDs.
    reservations["R101"] = {"guest": "Jordan Lee", "time": "6:00 PM", "party_size": 2}
    reservations["R102"] = {"guest": "Morgan Patel", "time": "6:15 PM", "party_size": 4}
    reservations["R103"] = {"guest": "Taylor Smith", "time": "6:30 PM", "party_size": 3}
    reservations["R104"] = {"guest": "Casey Brown", "time": "7:00 PM", "party_size": 5}
    reservations["R105"] = {"guest": "Riley Chen", "time": "7:15 PM", "party_size": 2}

    # Python dictionaries use hashing to locate values associated with keys.
    # Display all reservation records.
    print("\n=== INSERT OPERATIONS ===")
    for reservation_id, details in reservations.items():
        print(f"{reservation_id}: {details}")


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.


    # Dictionary lookup uses the reservation ID to find its value.
    # The get() method safely retrieves a value associated with a key.
    print("Looking up reservation R101:")
    print(reservations.get("R101"))

    print("\nLooking up reservation R104:")
    print(reservations.get("R104"))


    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.


    # Display the reservation before updating it.
    print("Before update:")
    print(reservations["R102"])

    # Assigning a new value to an existing key updates its value.
    reservations["R102"] = {
        "guest": "Morgan Patel",
        "time": "6:30 PM",
        "party_size": 4
    }

    # Display the reservation after updating it.
    print("After update:")
    print(reservations["R102"])


    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.


    # Display the dictionary before deletion.
    print("Before deletion:")
    print(reservations)

    # Delete reservation R105 from the dictionary.
    # The del statement removes the key and its associated value.
    del reservations["R105"]

    # Display the dictionary after deletion.
    print("\nAfter deletion:")
    print(reservations)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.


    # Edge case 1: Look up a reservation that does not exist.
    # get() returns None instead of raising a KeyError.
    print("Edge Case 1: Looking up missing reservation R999")
    print(reservations.get("R999"))

    # Edge case 2: Attempt to delete a missing reservation safely.
    # pop() returns None because a default value was provided.
    print("\nEdge Case 2: Deleting missing reservation R999")
    print(reservations.pop("R999", None))

    # Edge case 3: Look up a value in an empty dictionary.
    empty_reservations = {}
    print("\nEdge Case 3: Looking up an empty dictionary")
    print(empty_reservations.get("R000"))
    # Edge case 4: Adding an existing reservation ID.
    print("\nEdge Case 4: Adding an existing reservation ID R103")

    reservations["R103"] = {
        "guest": "Taylor Smith",
        "time": "6:45 PM",
        "party_size": 3
    }

    print("Updated R103:", reservations["R103"])
    print("Total reservations:", len(reservations))


if __name__ == "__main__":
    main()