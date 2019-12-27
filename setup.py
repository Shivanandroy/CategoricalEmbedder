import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    #Here is the module name.
    name="categorical_embedder",

    #version of the module
    version="0.1",

    #Name of Author
    author="Shivanand Roy",

    #your Email address
    author_email="Shivanandroy.official@gmail.com",

    #Small Description about module
    description="Categorical Embedder is a python package that let's you convert your categorical variables into numeric via Neural Networks",

    long_description=long_description,

    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
    url="https://github.com/Shivanandroy/CategoricalEmbedder/",
    packages=setuptools.find_packages(),

    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy','pandas','tensorflow','keras','tqdm','keras-tqdm','sklearn']
)
