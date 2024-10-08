import gdown
import os
import shutil


    
def organize_folders(dir):
    for filename in os.listdir(dir):
        if filename.endswith((".png", ".csv", ".raw", ".bag")):
            parts = filename.split('_')
            if len(parts) == 4:
                testing = parts[0]
                gesture = parts[1]
                modality = parts[2]
                distance = parts[3].rsplit('.', 1)[0]
                folder_structure = os.path.join(dir, testing, gesture, modality, distance)
            elif len(parts) == 5:
                testing = parts[0]
                gesture = parts[1]
                modality = parts[2]
                distance = parts[3]
                modality2 = parts[4].rsplit('.', 1)[0]
                folder_structure = os.path.join(dir, testing, gesture, modality, distance, modality2)
            elif len(parts) == 6:
                testing = parts[0]
                gesture = parts[1]
                modality = parts[2]
                distance = parts[3]
                modality2 = parts[4]
                metadata = parts[5].rsplit('.', 1)[0]
                folder_structure = os.path.join(dir, testing, gesture, modality, distance, modality2, metadata)
            else:
                print(f"{filename} Did not match any regular expression")
                continue  # Skip further processing for this file
            
            os.makedirs(folder_structure, exist_ok=True)
            source_file = os.path.join(dir, filename)
            destination_file = os.path.join(folder_structure, filename)
            shutil.move(source_file, destination_file)
        else:
            print(f"{filename} was not of a valid extension")
    print("All files have been sorted.")


def main():
    #Link to shared folder. Folder must be set to "Anyone with link can view"
    URL = 'https://drive.google.com/drive/folders/1kJ0spE-iRtF-LJUwpMAPJ2C3Md20n5-P?usp=drive_link'
    NAME_OF_FOLDER_TO_DOWNLOAD = '/Orbbec_Playback'
    folder_directory = os.getcwd() + NAME_OF_FOLDER_TO_DOWNLOAD
    #Check if folder has been downloaded already. If not, download it
    if os.path.exists(folder_directory):
        print("Folder already downloaded. If you meant to download a different folder, please change the URL and name of folder to download.")
    else:
        print("Downloading folder from Google Drive, please wait...")
        gdown.download_folder(URL, quiet = True, use_cookies= False)
        print("Download Complete")
    organize_folders(folder_directory)

if __name__ == "__main__":
    main()
