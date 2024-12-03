import shutil

# Define the number of copies you want
num_files = 500

# Loop to create the files
for i in range(1, num_files + 1):
    # Construct the new filename
    new_filename = f"pipeline{i}.orch.yaml"
    # Copy the existing file to the new filename
    shutil.copy("pipeline.orch.yaml", new_filename)

print(f"{num_files} files created successfully.")
