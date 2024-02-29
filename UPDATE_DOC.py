import os
from UPDATE_DOC_DATA import content, git_info

class CreateDocumentation:
    def writedoc(self, folder_file: list):
        # writing the datas to doc
        with open("DOCUMENTATION.md", "w") as doc:
            doc.write(f"# {content['title']}\n\
{content["text"]}\n\n")

            doc.write(f"## {content['sub_title']}\n")

            # sorting the folders before adding to doc
            folder_file = sorted(folder_file)

            # getting folder name and file list
            for files in folder_file:
                # writing folder name to doc
                doc.write(f"- [{files}]({content['path']}tree/{git_info['root_branch']}/{self.manage_space(files)})\n")
    
    def manage_space(self, file_name):
        # if there is any space in file name it will replace it by %20 as this is supported by github
        return file_name.strip().replace(" ", "%20")



class Files:
    def get_all_valid_folder_files_dict(self):
        all_files = []
        # getting repository location
        cwd = os.getcwd()
        for f in os.listdir(cwd):
            # check if the file/dir is in ignore section or not.
            # ignore files wont be counted
            if f not in content['ignore']:
                # append if it is a file and show_file=True
                if content['show_file'] and os.path.isfile(f):
                    all_files.append(f)
                # append if it is a folder and show_folder=True
                elif content['show_folder'] and os.path.isdir(f):
                    all_files.append(f)
        # return (all_files)
        return all_files

# indipendent function
def check_yml():
    # check if in the yml file, selected branch is the provided branch in UPDATE_DOC_DATA.py or not
    
    # reading data and checking if in the yml file the branch is same as the root branch of UPDATE_DOC_DATE.py
    all_data_in_yml = []
    with open('.github/workflows/run_update_doc_script.yml', 'r') as yml:
        # get all the data in a list
        all_data_in_yml = yml.readlines()

        # if is is already the setted branch then not need to change.
        # 6th line contains branch name
        all_data_in_yml[5] = f'      - {git_info['root_branch']}\n\n' if all_data_in_yml[5].strip() != git_info['root_branch'] else all_data_in_yml[5]

    # writing changes(if branch name changed)
    with open('.github/workflows/run_update_doc_script.yml', 'w') as yml:
        yml.writelines(all_data_in_yml)
def main():
    # check if run_update_doc_script.yml has the currect root branch name or not
    check_yml()
    # getting file data
    ff = Files()
    data = ff.get_all_valid_folder_files_dict()

    # writing to Documentation.md
    doc = CreateDocumentation()
    doc.writedoc(data) # documentation will be written in the repo home

    
if __name__ == '__main__':
    main()