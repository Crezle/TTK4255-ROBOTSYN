import os
import zipfile


def query(question, options):
    print(question)
    to_write = ["\n\t{}: {}".format(key, val) for key, val in options.items()]
    to_write = "".join(to_write)
    print("Options to select:" + to_write)
    answer = None
    while answer not in ("yes", "no"):
        answer_alternatives = ", ".join([str(key) for key in options.keys()])
        answer = input("Select an option [{}]:".format(answer_alternatives))
        answer = answer.strip()
        if answer not in options.keys():
            print("Answer is not in: {}".format(list(options.keys())))
            continue
        return options[answer]


# If you create other files, edit this list to include them in the .zip file.
files_to_include = {
    "A5/python/task2": [".py"],
    "A5/python/task4": [".py"],
    "A5/python/show_calibration_results": [".py"],
}
zipfile_path = "A5/A5_code.zip"
print("-"*80)


def select_file(filename, extension):
    if len(extensions) == 1:
        return filename + extensions[0]
    options = {str(i): filename + extensions[i]
               for i in range(len(extensions))}
    filename = query("Which file would you like to add?", options)
    return filename


files_added = []
with zipfile.ZipFile(zipfile_path, "w") as fp:
    for filename, extensions in files_to_include.items():
        filepath = select_file(filename, extensions)
        assert os.path.isfile(filepath),\
            f"Did not find path: {filepath}"
        fp.write(filepath)
        files_added.append(filepath)

print("-"*80)
print("Files added to zip:")
print("\t" + "\n\t".join(files_added))
print("Zipfile saved to: {}".format(zipfile_path))