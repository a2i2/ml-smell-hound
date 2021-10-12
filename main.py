# 1. TODO: pre-learn some things about the context.


# 2. classification based on ML/non-ML.
# 2.1. read/define imports used for ML files.


# Source: https://github.com/boalang/MSR19-DataShowcase/blob/master/info.txt
ml_imports = [
    "theano",
    "pytorch", # Corrected typo "pytroch" in MSR19 info.txt
    "caffe",
    "keras",
    "tensorflow",
    "sklearn",
    "numpy",
    "scipy",
    "pandas",
    "statsmodels",
    "matplotlib",
    "seaborn",
    "plotly",
    "bokeh",
    "pydot",
    "xgboost",
    "catboost",
    "lightgbm",
    "eli5",
    "elephas",
    "spark",
    "nltk",
    "cntk",
    "scrapy",
    "gensim",
    "pybrain",
    "lightning",
    "spacy",
    "pylearn2",
    "nupic",
    "pattern",
    "imblearn",
    "pyenv",
]


# 2.2. classify the files based upon the imports as ML/non-ML by reading file content.


def list_files():
    return ["example-src/ml.py", "example-src/non_ml.py"]


def is_ml_file(file_name):
    print("-------------")
    file1 = open(file_name, "r")
    lines = file1.readlines()

    count = 0
    # Strips the newline character.
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        print("type(line):", type(line))
        for ml_import in ml_imports:
            if ml_import in line.strip():
                print("file_name:", file_name)
                print("line_number:", count)
                print("ml_import:", ml_import)
                return True

    # If no valid import was found, return False.
    return False


# 3. results? do we even need this?
# 3.1. TODO: modify pylint configurations based upon the files and learned context.
# 3.2. TODO: run pylint using the configuration (can probably do it with shell itself).


def modify_pylint():
    print("modify_pylint")


def run_pylint():
    print("run_pylint")


# main execution.
if __name__ == "__main__":
    print("__main__")
    file_names = list_files()
    classification = {}
    for file_name in file_names:
        classification[file_name] = "ML" if is_ml_file(file_name) else "Non-ML"

    print("classification:")
    print(classification)
