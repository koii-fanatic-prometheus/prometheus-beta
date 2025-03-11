import gzip
import os

def decompress_gzip_file(input_path, output_path=None):
    """
    Decompress a gzip file to a specified output path.

    Args:
        input_path (str): Path to the input gzip file.
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, uses input filename without .gz extension.

    Returns:
        str: Path of the decompressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        IsADirectoryError: If input path is a directory.
        ValueError: If input file is not a gzip file.
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {input_path}")

    # Determine output path
    if output_path is None:
        # Remove .gz extension if present, otherwise append _decompressed
        output_path = input_path.removesuffix('.gz') if input_path.endswith('.gz') else input_path + '_decompressed'

    try:
        # Open and read the gzip file
        with gzip.open(input_path, 'rb') as gzip_file:
            # Write the contents to the output file
            with open(output_path, 'wb') as output_file:
                output_file.write(gzip_file.read())
        
        return output_path
    except gzip.BadGzipFile:
        raise ValueError(f"Input file is not a valid gzip file: {input_path}")