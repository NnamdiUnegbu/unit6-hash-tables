# unit6-hash-tables
CMSC 315 Unit 6 Discussion: Python Dictionaries as Hash Tables
# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Implementation Summary

### Application Scenario

I developed a restaurant reservation management system using a Python dictionary. Each reservation ID served as a unique key, while the guest's name, reservation time, and party size were stored as the associated value.

### Operations Implemented

1. **Creation and insertion:** I created an empty dictionary and inserted five reservation records.
2. **Lookup:** I retrieved reservation details using reservation IDs R101 and R104.
3. **Update:** I updated Morgan Patel's reservation from 6:15 PM to 6:30 PM.
4. **Deletion:** I deleted reservation R105 and displayed the dictionary before and after deletion.
5. **Edge cases:** I tested missing-key lookup, deletion of a missing key, and lookup in an empty dictionary.

### Hash Table Concepts

Python dictionaries use hashing to locate values associated with keys. A collision occurs when different keys produce the same hash value. Python handles collisions internally and uses key equality to identify the correct entry. Hash tables generally provide average constant-time lookup, insertion, and deletion.

### Testing Results

The program executed successfully. All five operations were demonstrated, and the edge-case tests completed without runtime errors.
I also tested duplicate reservation IDs and confirmed that assigning a new value to an existing key updated the record without increasing the dictionary size.
