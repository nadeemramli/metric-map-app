import os

# Path to the directory where Prophet is installed
prophet_path = "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages"  # Replace with the actual path

# Function to replace np.float_ with np.float64
def replace_np_float(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    new_content = content.replace("np.float_", "np.float64")
                    if new_content != content:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        print(f"Updated {file_path}")
                except Exception as e:
                    print(f"Failed to update {file_path}: {e}")

# Run the replacement function
replace_np_float(prophet_path)
