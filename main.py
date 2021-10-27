def format_css(path) -> None:
    """
    Format a CSS file with consistent indentation, spacing and alphabetize CSS rules for each selector.
    Not working with media queries and similar structures with multiples levels of "{}".
        @param path: Specify the file path you want to format.
        @type path: str
    """
    # Split filename and extension
    filename = path.split(".")[0]
    file_ext = path.split(".")[1]

    # Read file content and store it
    with open(path, "r") as f:
        base_css = f.read()

    # Split the file content on closing curly bracket to get a list of selectors+associated rules
    selectors_list = base_css.split("}")

    # Create 2 new lists
    all_selectors = []
    all_declarations = []

    # Loop through all selectors+associated rules items
    for item in selectors_list:
        # Split each item to get selector from one side and associated rules on the other
        selector_declaration_split = item.split("{")
        # Remove excess blank characters from the selector part
        selector = selector_declaration_split[0].strip()

        # If selector is not an empty string
        if selector:
            # Store selector rules as a string
            declarations_string = selector_declaration_split[-1]
            # Add current selector to all_selectors list
            all_selectors.append(selector)

            # Split each declarations string on ';' character and remove the linebreaks.
            clean_declaration = declarations_string.strip("\n").split(";")

            # Store in a new list each property-value pair for the current selector after removing whitespaces.
            clean_declarations_list = [
                declaration.strip()
                for declaration in clean_declaration
                if declaration.strip()
            ]

            # Add the current list of property-value pairs to the final list (list of lists)
            all_declarations.append(clean_declarations_list)

    # Create a final list where all selectors declarations lists are alphabetically sorted
    sorted_all_declarations = [sorted(selector_declarations) for selector_declarations in all_declarations]

    # Create an empty string to store the end result
    final_css_code = ""
    # Loop through 2 lists at the same time
    for selector, declarations in zip(all_selectors, sorted_all_declarations):
        # For each selector add it to the result string and add space, opening curly bracket and linebreak
        final_css_code += selector + " {\n"

        # For each declaration for the current selector
        for declaration in declarations:
            # Add to the result string 4 spaces, the declaration, a ";" character and a linebreak
            final_css_code += "    " + declaration + ";\n"

        # When we have added all property-value pairs for the current selector
        # Add closing bracket and 2 linebreaks
        final_css_code += "}\n\n"

    # Save file in the same folder with a new name
    with open(f"{filename}_formatted.{file_ext}", "w") as f:
        f.write(final_css_code)
    print(f"Saving formatted CSS file as {filename}_formatted.{file_ext}")


if __name__ == "__main__":
    format_css("styles.css")
