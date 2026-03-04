import datetime

# --- Developer Profile Data ---
# This dictionary stores metadata for the diagnostic report
developer_info = {
    "Name": "donx10austin",
    "Affiliation": "BYU-Idaho",
    "Specialization": "Software Development",
    "Core Focus": "SQL, Web Apps, & Data Analysis",
    "Mission": "Turning complex datasets into actionable insights."
}

def run_system_check():
    """
    Executes a system diagnostic to verify the development environment.
    """
    print("==========================================")
    print("       SYSTEM BOOT: HELLO WORLD           ")
    print("==========================================")
    
    # Core Output
    print("Message: Hello World!")
    print(f"Status:  Environment active on {datetime.datetime.now().strftime('%Y-%m-%d')}")
    print("-" * 42)
    
    # Iterating through the Developer Profile
    print("DEVELOPER PROFILE:")
    for key, value in developer_info.items():
        # Using f-string padding for clean alignment
        print(f" > {key:15}: {value}")
        
    print("==========================================")
    print("    READY TO BUILD DATA-DRIVEN APPS       ")
    print("==========================================")

if __name__ == "__main__":
    run_system_check()