import os
from uuid import uuid4

from fastapi import UploadFile

from app.utils.fileUtils import FileUtils


class TemporaryFile:
    def __init__(self, file: UploadFile):
        self._upload_file = file
        self.filename_path = self._get_unique_filename_path()

    def __enter__(self):
        self._create_temporary_file()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.filename_path)

    async def __aenter__(self):
        await self._create_temporary_file_async()
        return self

    async def __aexit__(self, *args, **kwargs):
        await FileUtils.delete_file(self.filename_path)

    def _create_temporary_file(self):
        with open(self.filename_path, 'wb') as temporary_file:
            while contents := self._upload_file.file.read(1024 * 1024):
                temporary_file.write(contents)

    async def _create_temporary_file_async(self):
        async with FileUtils.open(self.filename_path, 'wb') as temporary_file:
            while contents := self._upload_file.file.read(1024 * 1024):
                await temporary_file.write(contents)

    def _get_unique_filename_path(self) -> str:
        filename = f'{uuid4().hex}.{self._upload_file.filename.split(".")[-1]}'
        return os.path.join('temporary_buffer', filename)
