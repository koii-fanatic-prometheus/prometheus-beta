import os
import zipfile


def extract_zip_archive(zip_path, extract_path=None):
    """
    Extract all files from a given zip archive.

    Args:
        zip_path (str): Path to the zip file to be extracted.
        extract_path (str, optional): Destination directory for extracted files. 
                                      If None, extracts to the same directory as the zip file.

    Returns:
        list: A list of paths to the extracted files.

    Raises:
        FileNotFoundError: If the zip file does not exist.
        ValueError: If the zip_path is not a valid zip file.
        PermissionError: If there are insufficient permissions to extract files.
    """
    # Validate input
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(zip_path))
    
    # Ensure extraction path exists
    os.makedirs(extract_path, exist_ok=True)

    # Validate zip file
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Check if it's a valid zip file
            zip_ref.testzip()
            
            # Extract all files
            extracted_files = []
            for file in zip_ref.namelist():
                # Avoid potential directory traversal attacks
                safe_path = os.path.normpath(os.path.join(extract_path, file))
                if not safe_path.startswith(extract_path):
                    raise ValueError(f"Unsafe file path in zip: {file}")
                
                # Extract the file
                zip_ref.extract(file, extract_path)
                extracted_files.append(os.path.join(extract_path, file))
            
            return extracted_files
    except zipfile.BadZipFile:
        raise ValueError(f"Invalid zip file: {zip_path}")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to extract files to {extract_path}")