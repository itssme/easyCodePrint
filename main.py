import argparse
import os
import shutil

from jinja2 import Environment, select_autoescape, FileSystemLoader


def code2pdf(template, challenge_name, author_name, input_folder, output_folder):
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
                             meta={"docname": challenge_name.replace("_", "\_"),
                                   "author": author_name.replace("_", "\_")})
    with open(tex_file, "w") as w:
        w.write(output)

    os.system(f"pdflatex -shell-escape -output-directory=tmp {tex_file} ")
    shutil.move(os.path.join("tmp", pdf_file), os.path.join(output_folder, pdf_file))
    os.remove(tex_file)


def main():
    parser = argparse.ArgumentParser(description='Convert code submissions to PDF with minted as syntax highlighter.')
    parser.add_argument('--challenge-name', type=str,
                        help='Name of the challenge. For example "Python Exercise 1"', required=True)
    parser.add_argument('--input', type=str,
                        help='Input folder of the code files.', default="input")
    parser.add_argument('--output', type=str,
                        help='Output folder to which the pdfs will be written.', default="output")
    parser.add_argument('--template', type=str,
                        help='Template which should be used to create the pdf files.', default="code_minted.tex")
    parser.add_argument('--template-folder', type=str,
                        help='Path to the folder containing all latex templates.', default="templates")
    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output
    challenge_name = args.challenge_name

    env = Environment(
        loader=FileSystemLoader(args.template_folder),
        autoescape=select_autoescape()
    )

    template = env.get_template(args.template)
    os.makedirs(output_folder, exist_ok=True)

    for folder in os.listdir(input_folder):
        code2pdf(template, challenge_name, folder, os.path.join(input_folder, folder), os.path.join(output_folder, folder))


if __name__ == '__main__':
    main()
