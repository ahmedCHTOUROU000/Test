import os
import json
import sqlite3
import networkx as nx

def run_example(example_path):
    with open(os.path.join(example_path, 'millennium-falcon.json')) as f:
        falcon_data = json.load(f)

    with open(os.path.join(example_path, 'empire.json')) as f:
        empire_data = json.load(f)

    # Parameters
    departure = falcon_data["departure"]
    arrival = falcon_data["arrival"]
    autonomy = falcon_data["autonomy"]
    countdown = empire_data["countdown"]
    bounty_hunters = empire_data["bounty_hunters"]

    # Step 1: Load the universe.db data and construct the graph
    conn = sqlite3.connect(os.path.join(example_path, falcon_data["routes_db"]))
    cursor = conn.cursor()
    G = nx.DiGraph()
    cursor.execute("SELECT ORIGIN, DESTINATION, TRAVEL_TIME FROM ROUTES")
    for origin, destination, travel_time in cursor.fetchall():
        G.add_edge(origin, destination, weight=travel_time)
    conn.close()

    # Step 2: Calculate shortest path (minimum distance)
    try:
        min_days = nx.shortest_path_length(G, source=departure, target=arrival, weight="weight")
    except nx.NetworkXNoPath:
        min_days = float('inf')

    if min_days <= countdown:
        def calculate_capture_probability(encounters):
            total_prob = 0.0
            capture_prob = 0.1
            for _ in range(encounters):
                total_prob += capture_prob
                capture_prob *= 0.9
            return total_prob

        safest_path, min_capture_prob, successful_plan = None, float('inf'), None

        for path in nx.all_simple_paths(G, source=departure, target=arrival):
            for wait_start in range(countdown):
                days, fuel, encounters = wait_start, autonomy, 0
                plan = [f"Wait {wait_start} days on {departure}"] if wait_start > 0 else []
                for i in range(len(path) - 1):
                    travel_time = G[path[i]][path[i+1]]['weight']
                    if fuel < travel_time:
                        days += 1
                        fuel = autonomy
                        plan.append(f"Refuel on {path[i]} on day {days}")
                        if any(bh["planet"] == path[i] and bh["day"] == days for bh in bounty_hunters):
                            encounters += 1
                    days += travel_time
                    fuel -= travel_time
                    plan.append(f"Travel from {path[i]} to {path[i+1]} on day {days}")
                    if any(bh["planet"] == path[i+1] and bh["day"] == days for bh in bounty_hunters):
                        encounters += 1

                if days <= countdown:
                    capture_prob = calculate_capture_probability(encounters)
                    if capture_prob == 0:
                        successful_plan = plan
                        break
                    if capture_prob < min_capture_prob:
                        min_capture_prob, safest_path, safest_plan = capture_prob, path, plan
            if successful_plan:
                break

        if successful_plan:
            print(f"100% Safe Plan: {' -> '.join(successful_plan)}")
            print("Probability of capture: 0% - The Millennium Falcon can avoid all bounty hunters.")
        elif safest_path:
            print(f"Safest path: {' -> '.join(safest_path)}")
            print(f"Plan: {' -> '.join(safest_plan)}")
            print(f"Probability of capture: {100 - min_capture_prob * 100:.2f}%")
        else:
            print("Probability of capture: 0% - The Millennium Falcon can avoid all bounty hunters.")
    else:
        print("Probability of capture: 0% - The Millennium Falcon cannot reach Endor in time.")

# Run all examples
base_path = "examples"
for example in ["example1", "example2", "example3", "example4"]:
    print(f"\nRunning {example}...\n")
    run_example(os.path.join(base_path, example))







