# easyCodePrint

Simple tool for converting a bunch of code submission in python into multiple PDFs (one per submission).

# Usage

## Exercise Name (REQUIRED)

The name of the exercise, which will be written in the header of each .pdf file, can be specified by `--challenge-name NAME`.


## Input Directory

Default: `input`

The input directory can be specified with `--input DIRECTORY`. It should contain all code submission formatted like:

```
/DIRECTORY
    /authorName1
        main.py
        hello_world.py
    /authorName2
        main.py
        something.py
    .
    .
    .   
```

The author names as specified by the folder (for example `authorName1`) will be used as the author name in the generated .pdf file.

## Output Directory

The input directory can be specified with `--output DIRECTORY`. It will contain the .pdf files of all code submissions formatted like:

Default: `output`

```
/DIRECTORY
    /authorName1
        authorName1.pdf
    /authorName2
        authorName2.pdf
    .
    .
    .   
```

## Template

Default: `code_minted.tex`

A different latex template for code formatting may be used. The template must be placed withing the template directory. If can be specified with `--template TEMPLATE_FILE`.

### User Defined Templates

Jinja2 is used as templating language. If a new template file is specified, the following variables can be used:

+ meta
    + .docname - Name of the exercise.
    + .author - Name of the author.
+ code_input list of code
+ code
    + .filename - Filename of the code file.
    + .text - Content of the code file.

## Template Directory

Default: `templates`

A directory which contains all latex templates. If can be specified with `--template-folder DIRECTORY`.
