# Basic selectors only (no media query or anything else)

with open("styles.css", "r") as f:
    base_css = f.read()

selectors_list = base_css.split('}')

all_selectors = []
all_declarations = []

for _id, item in enumerate(selectors_list):
    _id2 = 0
    selector_declaration_split = item.split('{')
    selector = selector_declaration_split[0].strip()
    declarations_list = selector_declaration_split[1:]
    if selector:

        all_selectors.append(selector)
        for declarations_bloc in declarations_list:

            clean_declaration = declarations_bloc.strip('\n').split(";")
            clean_declarations_list = []
            for declaration in clean_declaration:

                if declaration.strip():
                    clean_declarations_list.append(declaration.strip())
                    _id2 += 1

            all_declarations.append(clean_declarations_list)

sorted_all_declarations = [sorted(css) for css in all_declarations]

final_css_code = ''
for selector, declarations in zip(all_selectors, sorted_all_declarations):

    final_css_code += selector + " {\n"

    for declaration in declarations:
        final_css_code += "    " + declaration + ";\n"
    final_css_code += "}\n\n"

print(final_css_code)

with open("styles_formatted.css", "w") as f:
    f.write(final_css_code)