import argparse

def add_https_to_file(input_file_path, output_file_path):
    """
    Reads subdomains from an input file, prepends 'https://' to each, and writes the resulting URLs to an output file.
    """
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                subdomain = line.strip()
                if subdomain:  # Ensure the line is not empty
                    url = 'https://' + subdomain
                    output_file.write(url + '\n')
        print(f"URLs have been successfully written to {output_file_path}")
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Prepend 'https://' to subdomains from a file.")
    parser.add_argument('-s', '--source', required=True, help="Input file containing subdomains")
    parser.add_argument('-o', '--output', required=True, help="Output file to write URLs with 'https://'")

    args = parser.parse_args()

    add_https_to_file(args.source, args.output)

if __name__ == "__main__":
    main()
