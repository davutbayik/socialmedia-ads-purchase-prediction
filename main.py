import subprocess
import time

# Function to run FastAPI using uvicorn
def run_fastapi():
    print("Starting FastAPI...\n")
    subprocess.Popen(["uvicorn", "fastapi_app:app", "--reload"])

# Function to run Streamlit
def run_streamlit():
    print("Starting Streamlit...\n")
    subprocess.Popen(["streamlit", "run", "streamlit_app.py"])

# Main function to run both
def main():
    run_fastapi()
    run_streamlit()

    # Keep the script running to allow both processes to continue
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()