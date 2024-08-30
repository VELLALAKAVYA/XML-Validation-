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
