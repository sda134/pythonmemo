import tarfile

with tarfile.open(os.path.join(dir_name, file_name), 'r:gz') as tar:
    members: list[tarfile.TarInfo] = tar.getmembers()
    for tar_info in members:
        print(tar_info.name):
