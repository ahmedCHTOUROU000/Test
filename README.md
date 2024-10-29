# Millennium Falcon Escape Plan

This project provides a solution for calculating the safest and fastest route for the Millennium Falcon to reach **Endor** within a restricted time frame while avoiding bounty hunters. The solution incorporates shortest-path analysis, fuel management, and risk assessment with encounter probabilities.

## Project Structure

```plaintext
.
├── examples/
│   ├── example1/
│   │   ├── millennium-falcon.json
│   │   ├── empire.json
│   │   └── universe.db
│   ├── example2/
│   ├── example3/
│   └── example4/
├── graph_image.png                # Optional: Graph visualization of the universe routes
├── App.py                 # Main script to run the solution for each example
└── README.md                      # Project documentation
```

- **examples/**: Each example directory (e.g., `example1`, `example2`) contains files with unique scenario data:
  - `millennium-falcon.json`: Falcon’s departure, arrival, fuel autonomy, and routes database path.
  - `empire.json`: Countdown timer and bounty hunters’ information.
  - `universe.db`: SQLite database of the universe routes, including origin, destination, and travel time for each route.
- **graph_image.png**: Visualization of the routes in `universe.db`. This image illustrates the travel routes between planets with corresponding travel times.
- **App.py**: Main Python script that calculates the safest path for each example and outputs the results.

## Setup Instructions

### Step 1: Create a Virtual Environment

1. In your project root, create a virtual environment:

   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:

   - **On Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

### Step 2: Install Required Libraries

Install dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` file should contain:

```plaintext
db-sqlite3
networkx
```

### Step 3: Run the Solution

1. **Prepare Example Data**: Place all files for each scenario (e.g., `example1`, `example2`) in the `examples/` directory as shown in the project structure.
2. **Execute the Script**: Run `main_script.py` to compute the safest path for each example scenario:

   ```bash
   python App.py
   ```

3. **Results**: For each scenario, the script will display:
   - The safest path from the departure planet to the arrival planet.
   - Detailed travel plan including waiting or refueling days as needed.
   - Probability of capture, based on the number of encounters with bounty hunters along the path.

## Solution Overview

The solution calculates the optimal path by considering three key constraints:

1. **Shortest Path**: Determines the minimum days required to travel from the departure planet to the arrival planet, considering the countdown limit.
2. **Fuel Autonomy and Refueling**: Each journey leg is constrained by the Falcon's autonomy (fuel capacity). If fuel is insufficient for a leg, a refuel stop is added to the plan.
3. **Bounty Hunter Encounters**: Tracks encounters with bounty hunters, calculating capture probability along each path to find the safest route.

## Graph Visualization

The file `graph_image.png` provides a visualization of the universe’s routes and travel times between planets. This graph is generated using `networkx` and `matplotlib` for reference and helps illustrate route options visually.

## Example Output

For each example, `main_script.py` provides output similar to:

```plaintext
Running example1...

Safest path: Tatooine -> Dagobah -> Endor
Plan: Wait 1 day on Tatooine -> Travel from Tatooine to Dagobah on day 2 -> Refuel on Dagobah on day 4 -> Travel from Dagobah to Endor on day 5
Probability of capture: 10.0%

Running example2...

100% Safe Plan: Wait 2 days on Tatooine -> Travel from Tatooine to Endor on day 3
Probability of capture: 0% - The Millennium Falcon can avoid all bounty hunters.
```

## License

This project is open-source and available for modification and distribution.