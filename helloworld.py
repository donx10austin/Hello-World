import datetime
import platform

# Your BYU-I Developer Profile
name = "Tech Lover @ BYU-Idaho"
language = "Python"
system = platform.system()

print("========================================")
print("             HELLO WORLD!               ")
print("========================================")
print(f"Developer: {name}")
print(f"Language:  {language}")
print(f"OS:        {system}")
print(f"Status:    Ready for Data Analysis & SQL")
print(f"Timestamp: {datetime.datetime.now().strftime('%c')}")
print("========================================")