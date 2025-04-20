import os
import shutil
import json
import zipfile

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODPACK = os.path.join(BASE, "modpack")
BUILD = os.path.join(BASE, "build")
CONFIG = os.path.join(BASE, "config")
CLIENT_MODS = os.path.join(BASE, "_mods_client")
COMMON_MODS = os.path.join(BASE, "_mods_common")
SERVER_MODS = os.path.join(BASE, "_mods_server")
SERVER_RESOURCE_PACKS = os.path.join(BASE, "server-resource-packs")

with open(os.path.join(MODPACK, "pack_info.json"), encoding="utf-8") as f:
    info = json.load(f)
file_name = info["file_name"]
version = info["version"]

def add_folder_to_zip(zipf, folder, arc_prefix=""):
    if not os.path.exists(folder):
        return
    for root, dirs, files in os.walk(folder):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, folder)
            arcname = os.path.join(arc_prefix, rel_path)
            zipf.write(abs_path, arcname)

def build_zip(zip_path, mods_srcs, include_resourcepacks=False):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add config
        add_folder_to_zip(zipf, CONFIG, "config")
        # Add mods
        for src in mods_srcs:
            add_folder_to_zip(zipf, src, "mods")
        # Add resourcepacks
        if include_resourcepacks:
            add_folder_to_zip(zipf, SERVER_RESOURCE_PACKS, "resourcepacks")

def build_server_zip(zip_path, mods_srcs):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add config
        add_folder_to_zip(zipf, CONFIG, "config")
        # Add mods
        for src in mods_srcs:
            add_folder_to_zip(zipf, src, "mods")
        # Add server-resource-packs
        add_folder_to_zip(zipf, SERVER_RESOURCE_PACKS, "server-resource-pack")

def main():
    print("Starting build...")
    os.makedirs(BUILD, exist_ok=True)

    print("Building client pack...")
    client_zip = os.path.join(BUILD, f"{file_name}_{version}_client.zip")
    build_zip(client_zip, [CLIENT_MODS, COMMON_MODS], include_resourcepacks=True)

    print("Building common pack...")
    common_zip = os.path.join(BUILD, f"{file_name}_{version}.zip")
    build_zip(common_zip, [CLIENT_MODS, COMMON_MODS, SERVER_MODS], include_resourcepacks=True)

    print("Building server pack...")
    server_zip = os.path.join(BUILD, f"{file_name}_{version}_server.zip")
    build_server_zip(server_zip, [COMMON_MODS, SERVER_MODS])

    print("Build complete.")

if __name__ == "__main__":
    main()