import fitz  # PyMuPDF
import argparse

def find_word_in_pdf(pdf_path, search_word):
    page_number_with_word = None

    doc = fitz.open(pdf_path)
    for page_number in range(len(doc)):
        page = doc[page_number]
        print(f"Reading page {page_number + 1}...")
        page_text = page.get_text().replace(" ", "")  # Remove spaces from the text
        if search_word in page_text:
            page_number_with_word = page_number + 1  # Adding 1 to convert 0-based index to page number
            print(f"Word '{search_word}' found on page {page_number_with_word}.")
            break  # Stop the loop once the word is found

    doc.close()
    return page_number_with_word

def main():
    parser = argparse.ArgumentParser(description="Search for a word in a PDF using PyMuPDF and write results to a text file.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("search_word", help="Word to search for in the PDF")
    parser.add_argument("output_file", help="path to output")
    args = parser.parse_args()

    result = find_word_in_pdf(args.pdf_path, args.search_word)

    # Write result to a text file
    output_file_path = args.output_file
    with open(output_file_path, "w") as output_file:
        if result is not None:
            output_file.write(f"{result}")
        else:
            output_file.write("NOT FOUND")

    print("Result written to:", output_file_path)

if __name__ == "__main__":
    main()