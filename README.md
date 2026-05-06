# The Techno Property Nepal - Land Management System

A robust Python-based terminal application designed to manage land rentals and returns for **The Techno Property Nepal**. This system allows users to view available lands, process rental transactions with automated billing, and manage land returns with automatic fine calculation for overdue rentals.

---

## ## Features

*   **Display Land Records**: View a formatted table of all land plots including Kitta number, district, size (in Aana), price, and availability status.
*   **Rent Land**: 
    *   Validation of Land ID and availability.
    *   Capture customer details (Name, Address, Email).
    *   Calculation of total rent based on duration.
    *   Generation of a text-based invoice.
*   **Return Land**:
    *   Update land status back to "Available".
    *   **Automatic Fine Calculation**: Applies a 10% fine if the rental duration exceeds the agreed period.
    *   Generation of a return bill.
*   **Data Persistence**: All changes are updated in real-time within the `land.txt` database file.

---

## ## File Structure

| File | Description |
| :--- | :--- |
| `main.py` | The entry point of the application containing the primary menu loop. |
| `operation.py` | Contains core logic for renting, returning, and bill generation. |
| `read.py` | Handles reading data from `land.txt` and displaying it to the console. |
| `write.py` | Handles updating and writing data back to the `land.txt` file. |
| `land.txt` | The text-based database storing land records. |

---

## ## Data Format (`land.txt`)

The system stores data in a comma-separated format:
`KittaID, District, Direction, Aana, Price, Status`

**Example:**
`101,Kathmandu,North,2,50000,Available`

---

## ## Getting Started

### ### Prerequisites
*   Python 3.x installed on your machine.

### ### Installation & Execution
1.  Clone this repository to your local machine.
2.  Ensure `land.txt`, `main.py`, `operation.py`, `read.py`, and `write.py` are in the same directory.
3.  Run the application using:
    ```bash
    python main.py
    ```

---

## ## Usage Guide

1.  **Greeting**: Upon startup, enter your name to access the dashboard.
2.  **Navigation**:
    *   **Press 1**: To see the list of all lands.
    *   **Press 2**: To rent a land (Requires a valid Land ID and duration in months).
    *   **Press 3**: To return a land (Calculates fines if applicable).
    *   **Press 4**: To safely exit the system.

---

## ## System Logic Highlights

### ### Fine Calculation
The system utilizes the `datetime` module to track rental periods. If the return date exceeds the allocated duration, a fine is calculated as:
$$\text{Fine} = \text{Extra Days} \times \text{Daily Rate} \times 0.10$$

### ### Invoice Generation
Invoices are generated as unique `.txt` files named with the customer's name and the current timestamp to prevent overwriting.
```
