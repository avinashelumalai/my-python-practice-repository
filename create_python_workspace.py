import os

# -----------------------------------------------------------
# Dictionary that defines your folder structure.
# Keys = main folders
# Values = list of subfolders to be created inside each main folder
# -----------------------------------------------------------
structure = {
    "01_basics": [
        "variables",
        "data_types",
        "control_flow",
        "functions"
    ],
    "02_intermediate": [
        "modules_packages",
        "file_handling",
        "error_handling",
        "oop"
    ],
    "03_advanced": [
        "decorators",
        "generators",
        "multithreading",
        "multiprocessing",
        "async_programming"
    ],
    "04_data_engineering": [
        "pandas",
        "pyspark",
        "sql_queries",
        "etl_pipelines",
        "data_quality"
    ],
    "05_projects": [
        "project_1_foundation"
    ],
    "notebooks": [
        "basics",
        "intermediate",
        "advanced",
        "data_engineering",
        "experiments"
    ]
}

def create_structure():

    # Base folder that will hold the entire workspace
    base_path = "python-practice"

    # Create root folder if it does not exist
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    # -----------------------------------------------------------
    # Create all main folders and their subfolders
    # -----------------------------------------------------------
    for folder, subfolders in structure.items():
        
        # Build main folder path, example: python-practice/01_basics
        folder_path = os.path.join(base_path, folder)

        # Create the main folder; ignore error if already exists
        os.makedirs(folder_path, exist_ok=True)

        # For each subfolder under the main folder…
        for sub in subfolders:

            # Final subfolder path: python-practice/01_basics/variables
            sub_path = os.path.join(folder_path, sub)

            # Create subfolder safely
            os.makedirs(sub_path, exist_ok=True)

    # -----------------------------------------------------------
    # Create core workspace files
    # -----------------------------------------------------------

    # ---- .gitignore ----
    # Helps keep your Git repository clean
    with open(os.path.join(base_path, ".gitignore"), "w") as f:
        f.write(
            "venv/\n"
            "__pycache__/\n"
            ".ipynb_checkpoints/\n"
            "*.pyc\n"
            ".DS_Store\n"
            ".env\n"
        )

    # ---- README.md ----
    # Basic project documentation
    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write(
            "# Python Practice Workspace\n\n"
            "Auto-generated structure.\n"
        )

    # ---- requirements.txt ----
    # Placeholder for your Python dependencies
    with open(os.path.join(base_path, "requirements.txt"), "w") as f:
        f.write("# Add python packages here\n")

    print("Workspace created successfully!")


# Entry point for script execution
if __name__ == "__main__":
    create_structure()
