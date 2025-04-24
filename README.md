# Rozar-SMP-New-Beginnings-1.20.1
we are so back

## Pack Build & Setup
This modpack repository structure is not typical, but was what the owners agreed on. There are python scripts to setup the folder for playing from the repository, and for building modpack files for sharing.

### Setup
```python
python modpack/pack_build.py <parameters>
```
Completes folder setup to play from the repository

Parameters:
- `client` adds only client and common mods to the `mods` folder
- `server` adds only server and common mods to the `mods` folder
- `common` (or no parameter) adds all mods to the `mods` folder

### Build
Output filenames depend on values in [`modpack/pack_info.json`](modpack/pack_info.json)
```json
{
    "file_name": "rozar-smp-nb",
    "version": "version.number.here"
}
```
You can then build the pack, resulting in client, common, and server `.zip` files
```python
python modpack/pack_build.py <parameters>
```