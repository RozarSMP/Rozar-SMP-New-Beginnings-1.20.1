import os
import shutil
import sys

def copy_mods(src_dirs, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    for src in src_dirs:
        if not os.path.exists(src):
            continue
        for file in os.listdir(src):
            src_file = os.path.join(src, file)
            dest_file = os.path.join(dest_dir, file)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dest_file)

def copy_resourcepacks(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        return
    os.makedirs(dest_dir, exist_ok=True)
    for file in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file)
        dest_file = os.path.join(dest_dir, file)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dest_file)

def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    client_dir = os.path.join(base, "_mods_client")
    common_dir = os.path.join(base, "_mods_common")
    server_dir = os.path.join(base, "_mods_server")
    mods_dir = os.path.join(base, "mods")
    server_resourcepacks_dir = os.path.join(base, "server-resource-packs")
    resourcepacks_dir = os.path.join(base, "resourcepacks")

    # Clean mods folder before copying
    if os.path.exists(mods_dir):
        for f in os.listdir(mods_dir):
            file_path = os.path.join(mods_dir, f)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # Clean resourcepacks folder before copying
    if os.path.exists(resourcepacks_dir):
        for f in os.listdir(resourcepacks_dir):
            file_path = os.path.join(resourcepacks_dir, f)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # Accept "common" or no parameter for all mods
    if len(sys.argv) < 2 or sys.argv[1].lower() == "common":
        copy_mods([client_dir, common_dir, server_dir], mods_dir)
    elif sys.argv[1].lower() == "client":
        copy_mods([client_dir, common_dir], mods_dir)
    elif sys.argv[1].lower() == "server":
        copy_mods([common_dir, server_dir], mods_dir)
    else:
        print("\033[91mUsage: python pack_setup.py [client|server|common]\033[0m")
        sys.exit(1)

    # Always copy server-resource-packs to resourcepacks
    copy_resourcepacks(server_resourcepacks_dir, resourcepacks_dir)

if __name__ == "__main__":
    main()