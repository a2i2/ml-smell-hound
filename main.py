import os
import sys
import glob
import json
from datetime import datetime
from shell_util import *
from operations.reprioritise import Reprioritise
from operations.remessage import Remessage

# Source: https://github.com/boalang/MSR19-DataShowcase/blob/master/info.txt
ml_imports = [
    "theano",
    "pytorch",  # Corrected typo "pytroch" in MSR19 info.txt
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

output_suffix = ".pylint.json"
default_pylint_text_format = "{path}:{line}:{column}: {msg_id}: {msg} ({symbol})\n"


class Runner:
    @staticmethod
    def is_ml_file(file_name):
        """
        Classify the file_name based upon the imports as ML/non-ML by reading file content.
        """

        # print("-------------")
        file1 = open(file_name, "r")
        lines = file1.readlines()

        count = 0
        # Strips the newline character.
        for line in lines:
            count += 1
            # print("Line{}: {}".format(count, line.strip()))
            # print("type(line):", type(line))
            for ml_import in ml_imports:
                if ml_import in line.strip():
                    # print("file_name:", file_name)
                    # print("line_number:", count)
                    # print("ml_import:", ml_import)
                    return True

        # If no valid import was found, return False.
        return False

    def __init__(self, dir_path: str, metamodel: str):
        self.dir_path = dir_path
        self.metamodel = metamodel
        self.ml_config_path = os.path.join(dir_path, "configs/ml.pylintrc")
        self.non_ml_config_path = os.path.join(dir_path, "configs/non_ml.pylintrc")

        script_dir = os.path.dirname(os.path.realpath(__file__))
        time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.output_path = os.path.join(script_dir, "outputs", time)
        os.makedirs(self.output_path, mode=0o755)
        self.audit_report_path = os.path.join(self.output_path, f"lint-{metamodel}.txt")

    def process_file(self, file_path: str):
        # Process each file individually, which will:
        #   1. run pylint on that file based upon context with JSON output.
        base_path, file_name = os.path.split(file_path)

        if self.metamodel == "non_ml":
            config_path = self.non_ml_config_path
        elif self.metamodel == "ml":
            config_path = self.ml_config_path
        else:
            # Context aware.
            config_path = (
                self.ml_config_path
                if Runner.is_ml_file(file_path)
                else self.non_ml_config_path
            )

        cmd = f"pylint --rcfile={config_path} -f json {file_path}"
        print("Executing command:", cmd)

        output_location = os.path.join(self.output_path, f"{file_name}{output_suffix}")
        #   2. Run operations on the file.
        with open(output_location, "w") as out_file:
            get_command_output(cmd, stdout=out_file)

        #   2.1 Reprioritise
        print("==== Running operation Reprioritise")
        Reprioritise.exec(output_location)

        #   2.2 Remessage
        print("==== Running operation Remessage")
        Remessage.exec(output_location)

        lines: list = []
        #   3. Finally transform the json output to text.
        with open(output_location, "r") as json_file:
            json_array = json.load(json_file)

            lines.append(f'************* Module {json_array[0]["module"]}\n')
            for obj in json_array:
                lines.append(
                    default_pylint_text_format.format(
                        path=obj["path"],
                        line=obj["line"],
                        column=obj["column"],
                        msg_id=obj["message-id"],
                        msg=obj["message"],
                        symbol=obj["symbol"],
                    )
                )

        with open(self.audit_report_path, "a") as audit_report_file:
            audit_report_file.writelines(lines)

    def exec(self):

        # List all files in directory.
        files = glob.glob(f"{self.dir_path}/**/*.py", recursive=True)
        print(files)
        # Process each file individually.
        for f in files:
            self.process_file(f)


# # # main execution.
# # # Usage: python3 main.py example-src/ml.py context
# # Outputs: pylint configuration file to use
# def old_way():
#     if len(sys.argv) > 1:
#         # Classify a single file
#         file_name = sys.argv[1]
#         script_dir = os.path.dirname(os.path.realpath(__file__))
#         ml_config_path = os.path.join(script_dir, "example-src/configs/ml.pylintrc")
#         non_ml_config_path = os.path.join(
#             script_dir, "example-src/configs/non_ml.pylintrc"
#         )

#         if len(sys.argv) > 2:
#             mode = sys.argv[2]
#         else:
#             mode = "context"

#         if mode == "non_ml":
#             config_path = non_ml_config_path
#         elif mode == "ml":
#             config_path = ml_config_path
#         else:
#             # context aware
#             config_path = (
#                 ml_config_path if Runner.is_ml_file(file_name) else non_ml_config_path
#             )

#         print(config_path)
