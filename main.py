import os
import shutil

from jinja2 import Environment, select_autoescape, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)


def code2pdf(template, author_name, input_folder, output_folder):
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    os.makedirs("tmp", exist_ok=True)

    tex_file = os.path.join(output_folder, f"{author_name}.tex")
    pdf_file = f"{author_name}.pdf"

    os.makedirs(output_folder)

    code = []
    for file in os.listdir(input_folder):
        with open(os.path.join(input_folder, file)) as r:
            code.append({"text": r.read(), "filename": file.replace("_", "\_")})

    output = template.render(code_input=code,
                             meta={"docname": "Coding Challenge 2", "author": author_name.replace("_", "\_")})
    with open(tex_file, "w") as w:
        w.write(output)

    os.system(f"pdflatex -shell-escape -output-directory=tmp {tex_file} ")
    shutil.move(os.path.join("tmp", pdf_file), os.path.join(output_folder, pdf_file))
    os.remove(tex_file)


def main():
    template = env.get_template("code_minted.tex")
    os.makedirs("output", exist_ok=True)

    for folder in os.listdir("input"):
        code2pdf(template, folder, os.path.join("input", folder), os.path.join("output", folder))


if __name__ == '__main__':
    main()
