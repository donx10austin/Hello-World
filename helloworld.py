import datetime

# --- Number 4: BYU-I Developer Profile Data ---
developer_info = {
    "Name": "donx10austin",
    "University": "BYU-Idaho",
    "Major": "Software Development",
    "Focus": "SQL, Web Apps, & Data Analysis",
    "Mission": "Turning complex datasets into actionable insights."
}

def run_system_check():
    print("==========================================")
    print("       SYSTEM BOOT: HELLO WORLD           ")
    print("==========================================")
    
    # Printing the classic message
    print("Message: Hello World!")
    print(f"Status:  System active on {datetime.datetime.now().strftime('%Y-%m-%d')}")
    print("-" * 42)
    
    # Printing the Developer Profile (Number 4)
    print("DEVELOPER PROFILE:")
    for key, value in developer_info.items():
        print(f" > {key}: {value}")
        
    print("==========================================")
    print("    READY TO BUILD DATA-DRIVEN APPS       ")
    print("==========================================")

if __name__ == "__main__":
    run_system_check()