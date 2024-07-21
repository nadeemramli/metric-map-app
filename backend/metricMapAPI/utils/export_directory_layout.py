import os

def export_directory_layout(directory, output_file):
    """Export the directory layout to a text file."""
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f"{indent}{os.path.basename(root)}/\n")
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f"{sub_indent}{file}\n")

if __name__ == "__main__":
    app_directory = "."  # Replace with your app directory name
    output_file = "directory_layout_all.txt"  # Replace with your desired output file name

    export_directory_layout(app_directory, output_file)
    print(f"Directory layout of {app_directory} has been successfully exported to {output_file}")
