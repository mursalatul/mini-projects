class BabyConda:
    def __init__(self):
        self.main_op = None
        self.command = None

    def main_operation(self):
        while True:
            try:
                print('Enter main operation for conda:')
                print('''
                1. List environments
                2. Create environment
                3. Activate environment
                4. Deactivate environment
                ''')
                self.main_op = int(input(f': '))
                if self.main_op == 1 or self.main_op == 2:
                    break
                else:
                    print('Invalid input. Please select a number from above number (1 or 2)')
            except ValueError:
                print('Please select a number.')

        if self.main_op == 1:
            self.list_env()
        elif self.main_op == 2:
            env_path = input('Enter environment path(default): ')
            python_version = float(input('Enter python path(default=3.12): '))
            self.create_env(env_path=env_path, python_version=python_version)
        elif self.main_op == 3:
            env_path = input('Enter environment path(default): ')
            self.activate_env(env_path=env_path)
        else:
            self.deactivate_env()

    def create_env(self, env_path='default', python_version=3.12):
        """
        create a python environment on specific path and python version. If nothing is
        provided, default to 3.12, and env will be created on conda directory.
        :param env_path:
        :param python_version:
        """
        self.command = f'conda create --prefix "{env_path}" python={python_version}'.strip()

        # if env is default, the env will be created in the default conda location
        if env_path == 'default':
            command = self.command.replace('--prefix default', '')

        # execute the command
        self.command_execute()

    def list_env(self):
        """
        show att the available environments.
        """
        print('All the environments are listed bellow:')
        self.command = 'conda env list'

        # execute the command
        self.command_execute()

    def activate_env(self, env_path):
        self.command = f'conda activate "{env_path}"'.strip()

        # execute the command
        self.command_execute()

    def deactivate_env(self):
        self.command = f'conda deactivate'.strip()

        # execute the command
        self.command_execute()

    def command_execute(self):
        import subprocess

        output = subprocess.check_output("g++ --version", shell=True, text=True)
        print(output)


