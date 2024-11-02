import os

def get_file_analysis(path):
    if os.path.exists(path):  # Verify file existence
        size_in_bytes = os.path.getsize(path)  # Get size of the file in bytes
        with open(path, 'r', encoding='utf-8') as doc:
            content = doc.read()
        
        # Separate paragraphs by double newlines and count
        sections = content.split('\n\n')  
        num_paragraphs = len(sections)

        # Initialize counters for words and sentences
        words_total = 0
        sentences_total = 0
        
        for sec in sections:
            sec = sec.strip()  # Remove unwanted whitespaces
            if sec:
                # Sentences are determined by splitting on periods followed by space
                sentences_in_sec = sec.split('. ')
                sentences_total += len(sentences_in_sec)
                
                # Count words by splitting by whitespace
                words_in_sec = sec.split()
                words_total += len(words_in_sec)
        
        # Returning the analysis results as a dictionary
        return {
            'Total Paragraphs': num_paragraphs,
            'Total Words': words_total,
            'Total Sentences': sentences_total,
            'File Size (Bytes)': size_in_bytes
        }
    else:
        print(f"File {path} does not exist.")
        return None

# Main execution point
if __name__ == "__main__":
    doc_path = 'document.txt'  # Replace with the actual file path if necessary
    results = get_file_analysis(doc_path)
    
    if results:
        print("Document Analysis:")
        for key, value in results.items():
            print(f"{key}: {value}")
