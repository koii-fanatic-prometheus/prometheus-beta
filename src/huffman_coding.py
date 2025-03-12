from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    """
    Represents a node in the Huffman tree.
    
    Attributes:
        char (str): The character represented by the node
        freq (int): Frequency of the character
        left (HuffmanNode): Left child node
        right (HuffmanNode): Right child node
    """
    def __init__(self, char, freq):
        """
        Initialize a Huffman tree node.
        
        Args:
            char (str): Character represented by the node
            freq (int): Frequency of the character
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        """
        Allow comparison for heapq priority queue.
        
        Args:
            other (HuffmanNode): Another Huffman node to compare
        
        Returns:
            bool: True if this node's frequency is less than the other
        """
        return self.freq < other.freq

def build_frequency_dict(data):
    """
    Build a frequency dictionary for input data.
    
    Args:
        data (str): Input string to analyze
    
    Returns:
        dict: Dictionary of character frequencies
    """
    if not data:
        return {}
    return dict(Counter(data))

def build_huffman_tree(freq_dict):
    """
    Build Huffman tree from frequency dictionary.
    
    Args:
        freq_dict (dict): Dictionary of character frequencies
    
    Returns:
        HuffmanNode: Root of the Huffman tree
    
    Raises:
        ValueError: If frequency dictionary is empty
    """
    if not freq_dict:
        raise ValueError("Frequency dictionary cannot be empty")
    
    # Create priority queue of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # Build tree by combining least frequent nodes
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node with combined frequency
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    return heap[0]

def build_huffman_codes(root):
    """
    Generate Huffman codes for each character.
    
    Args:
        root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        dict: Dictionary mapping characters to their Huffman codes
    """
    if not root:
        return {}
    
    codes = {}
    
    def traverse(node, current_code):
        """
        Recursive helper to generate Huffman codes.
        
        Args:
            node (HuffmanNode): Current node in tree
            current_code (str): Current code path
        """
        if not node:
            return
        
        # Leaf node (has a character)
        if node.char is not None:
            codes[node.char] = current_code or "0"
            return
        
        # Recursive traversal
        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")
    
    traverse(root, "")
    return codes

def huffman_encode(data):
    """
    Encode input data using Huffman coding.
    
    Args:
        data (str): Input string to encode
    
    Returns:
        tuple: (encoded_string, huffman_tree_root)
    
    Raises:
        ValueError: If input data is empty or None
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Special case for single character
    if len(data) == 1:
        return "0", HuffmanNode(data, 1)
    
    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)
    
    # Build Huffman tree
    huffman_tree = build_huffman_tree(freq_dict)
    
    # Generate Huffman codes
    huffman_codes = build_huffman_codes(huffman_tree)
    
    # Encode the input data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, huffman_tree

def huffman_decode(encoded_data, huffman_tree):
    """
    Decode Huffman encoded data.
    
    Args:
        encoded_data (str): Binary string of encoded data
        huffman_tree (HuffmanNode): Root of Huffman tree
    
    Returns:
        str: Decoded original string
    
    Raises:
        ValueError: If encoded data is empty or tree is invalid
    """
    # Validate inputs
    if huffman_tree is None:
        raise ValueError("Huffman tree cannot be None")
    
    # Special case for single character encoding
    if huffman_tree.left is None and huffman_tree.right is None:
        # For a single character, generate a full string of that character
        if encoded_data == "0":
            return huffman_tree.char * len(encoded_data)
        raise ValueError("Invalid encoded data for single character")
    
    if not encoded_data:
        raise ValueError("Encoded data cannot be empty")
    
    decoded_data = []
    current_node = huffman_tree
    
    for bit in encoded_data:
        # Traverse tree based on bit
        current_node = current_node.left if bit == '0' else current_node.right
        
        # Ensure current_node is not None
        if current_node is None:
            raise ValueError("Invalid Huffman tree structure")
        
        # If leaf node is reached
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = huffman_tree
    
    return ''.join(decoded_data)