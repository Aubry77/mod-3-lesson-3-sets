
def flight_route_comparison(our_routes, competitor_routes):
    """
    Compare flight routes between two airlines.
    
    Parameters:
    our_routes (set): Destinations of our airline.
    competitor_routes (set): Destinations of the competitor airline.
    
    Returns:
    dict: A dictionary with comparison results.
    """
    return {
        "common_destinations": our_routes.intersection(competitor_routes),
        "unique_to_our_airline": our_routes.difference(competitor_routes),
        "neither_shared": our_routes.symmetric_difference(competitor_routes)
    }

def main():
    our_routes = {"LAX", "JFK", "CDG", "DXB"}
    competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
    
    comparison = flight_route_comparison(our_routes, competitor_routes)
    
    print(f"Destinations both airlines fly to: {comparison['common_destinations']}")
    print(f"Destinations unique to our airline: {comparison['unique_to_our_airline']}")
    print(f"Destinations neither airline shares: {comparison['neither_shared']}")

if __name__ == "__main__":
   def remove_duplicates(customer_ids):
    """
    Remove duplicate customer IDs.
    
    Parameters:
    customer_ids (list): List of customer IDs.
    
    Returns:
    set: A set of unique customer IDs.
    """
    return set(customer_ids)

def main():
    customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
    unique_customer_ids = remove_duplicates(customer_ids)
    
    print(f"Unique customer IDs: {unique_customer_ids}")

if __name__ == "__main__":
    main()
main()


