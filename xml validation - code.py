import xmlschema
import sys

def validate_xml(xml_file, xsd_file):
    try:
        # Load the XML Schema (XSD)
        schema = xmlschema.XMLSchema(xsd_file)
        
        # Validate the XML file against the schema
        schema.validate(xml_file)
        
        print(f"The XML file '{xml_file}' is valid according to the schema '{xsd_file}'.")
    except xmlschema.XMLSchemaValidationError as e:
        print(f"Validation error: {e}")
    except xmlschema.XMLSchemaParseError as e:
        print(f"Schema parsing error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_xml.py <input_xml_file> <xsd_schema_file>")
    else:
        xml_file = sys.argv[1]
        xsd_file = sys.argv[2]
        validate_xml(xml_file, xsd_file)


# How the Script Works
# Load Schema: The script uses xmlschema.XMLSchema to load the XSD schema file.
# Validate XML: It then validates the XML file against the schema using the validate method.
# Error Handling: If validation fails, the script catches exceptions and provides detailed error messages.
# Instructions to Use the Script
# Place the script in the same directory as your XML and XSD files, or provide the full path to these files.
# Run the script using Python, specifying the input XML file and XSD schema file as arguments.
# Customization Tips
# Custom Error Handling: Adjust the error handling in the script to fit your needs, such as writing errors to a log file or integrating with a user interface.
# Schema Types: Modify the schema and XML structure according to your specific requirements and data models.
