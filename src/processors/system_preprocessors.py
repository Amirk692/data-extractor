import json
import os
import logging

logging.basicConfig(
    filename = "system_preprocessor.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class SystemPreprocessor:
    def __init__(self, config_path):
        self.config_path = config_path


    def load_config(self):
        logging.info(f"Trying to load config from: {self.config_path}")

        try:
            with open(self.config_path) as file:            
                config = json.load(file)
                logging.info(f"Config loaded successfully: {config}")
                self.config = config
                return self.config
            
        except FileNotFoundError:
            logging.error(f"File not found: {self.config_path}")
        except json.JSONDecodeError as e:
            logging.error(f"Invalid json in config file : {e}")        
        
    def validate_config(self):
        required_keys = ["SOURCE_TYPE", "SYSTEM_NAME", "FILE_FORMAT", "BASE_URL", "CONNECTION_NAME"]
        for key in required_keys:
            if key not in self.config:
                raise KeyError(f"Missing required key : {required_keys}")
        
    def create_working_directory(self, base_dir):
          system_name = self.config["SYSTEM_NAME"]
          working_directory = os.path.join(base_dir, system_name)
          folders_name = ["input", "output", "inbound", "outbound", "metadata", "logs", "error"]
          """Creating the folders"""
        #   input = os.path.join(base_dir, system_name, "input")
        #   output = os.path.join(base_dir, system_name, "output")
        #   inbound = os.path.join(base_dir, system_name, "inbound")
        #   outbound = os.path.join(base_dir, system_name, "outbound")
        #   metadata = os.path.join(base_dir, system_name, "metadata")
        #   logs = os.path.join(base_dir, system_name, "logs")
        #   error = os.path.join(base_dir, system_name, "error")

          for folder_name in folders_name:
              full_path = os.path.join(base_dir, system_name, folder_name)
              # create the folder if it doesn't exist
              if not os.path.exists(full_path):
                  os.makedirs(full_path)
                  print(f"Created folder : {folder_name}")

              else:
                  print(f"Folder already exist : {folder_name}")  

    def create_system_master_param(self, base_dir):
        system_name = self.config["SYSTEM_NAME"]
        working_directory = os.path.join(base_dir, system_name)

        system_master_param = self.config.copy()
        system_master_param["WORKING_DIR"] = working_directory

        # system_master_param_path = os.path.join(base_dir, system_name)
        param_file_path = os.path.join(working_directory, "system_master_config.json")

        with open(param_file_path, "w") as file:
            json.dump(system_master_param, file, indent=4)
            print(f"System master config saved at : {param_file_path}")


        
        
preprocessor = SystemPreprocessor("D:/my-projects/python-projects/data-extractor/configs/system_configs.json")
config = preprocessor.load_config()

if config:  # Proceed only if config loaded successfully
    preprocessor.validate_config()
    preprocessor.create_working_directory("D:/my-projects/python-projects/data-extractor")
    preprocessor.create_system_master_param("D:/my-projects/python-projects/data-extractor")
else:
    logging.error("Aborting execution because config could not be loaded.")

print("Code ran successfully")    