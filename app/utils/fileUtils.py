import aioshutil
import aiofiles
import aiofiles.os as aiofiles_os


class FileUtils(object):
    @staticmethod
    async def is_exists(path: str) -> bool:
        return await aiofiles_os.path.exists(path)

    @staticmethod
    async def copy(file_from: str, file_to: str) -> None:
        await aioshutil.copy(file_from, file_to)

    @staticmethod
    def open(filename: str, mode: str, *args, **kwargs):
        return aiofiles.open(filename, mode, *args, **kwargs)

    @staticmethod
    async def create_dirs(path: str) -> None:
        await aiofiles.os.makedirs(path, exist_ok=True)

    @classmethod
    async def delete_file(cls, path: str) -> None:
        if await cls.is_exists(path):
            await aiofiles.os.remove(path)
