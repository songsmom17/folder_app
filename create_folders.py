import os

def create_folder_structure(base_path):
    folders = [
        "Case Documents/Pleadings",
        "Case Documents/Motions",
        "Case Documents/Orders",
        "Case Documents/Evidence/Photos",
        "Case Documents/Evidence/Videos",
        "Case Documents/Evidence/Documents",
        "Case Documents/Correspondence",
        "Case Documents/Court Transcripts",
        "Financial Documents/Invoices",
        "Financial Documents/Receipts",
        "Financial Documents/Bank Statements",
        "Research/Case Law",
        "Research/Statutes",
        "Research/Legal Articles",
        "Communication/Emails",
        "Communication/Letters",
        "Communication/Memos",
        "Miscellaneous/Notes",
        "Miscellaneous/Drafts",
    ]

    for folder in folders:
        # Create full path for each folder
        folder_path = os.path.join(base_path, folder)
        
        # Make directories for each path, including intermediate directories
        os.makedirs(folder_path, exist_ok=True)
        
        # Create an empty .gitignore file in each folder
        with open(os.path.join(folder_path, '.gitignore'), 'w') as f:
            f.write('# Ignore everything in this directory\n*\n# Except this file\n!.gitignore')

# Replace 'your/project/path' with the path to your local GitHub project directory
create_folder_structure('/Users/dummybunny/Desktop/folder_app-main')

print("Folder structure created successfully.")
