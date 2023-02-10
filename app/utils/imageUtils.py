from PIL import Image

from app.constances.image_params import IMAGE_COMPRESSION_QUALITY
from app.utils.run_async import run_async


class ImageUtils:
    @run_async
    def get_size(self, file_path: str) -> tuple[int, int]:
        with Image.open(file_path) as img:
            return img.size

    @run_async
    def resize_with_ratio_save(self, src_path: str, dst_path: str, max_size: int):
        with Image.open(src_path) as img:
            width, height = self._get_sizes_params_with_ratio_save(img, max_size)

            img = img.resize((width, height))
            img.save(dst_path, quality=IMAGE_COMPRESSION_QUALITY)

    @run_async
    def resize_and_crop_with_ratio_save(self, src_path: str, dst_path: str, tmb_width: int, tmb_height: int):
        with Image.open(src_path) as img:
            bigger_side = tmb_width if tmb_width > tmb_height else tmb_height
            width, height = self._get_sizes_params_with_ratio_save(img, bigger_side)

            img = img.resize((width, height))
            img = self._crop_by_center(img, tmb_width, tmb_height)
            img.save(dst_path, quality=IMAGE_COMPRESSION_QUALITY)

    def _crop_by_center(self, img: Image, width: int, height: int) -> Image:
        if self._is_horizontal_photo(width, height):
            top = (img.height - height) / 2
            bottom = img.height - top
            left = 0
            right = img.width
        else:
            top = 0
            bottom = img.height
            left = (img.width - width) / 2
            right = img.width - left
        return img.crop((left, top, right, bottom))

    def _is_horizontal_photo(self, width: int, height: int) -> bool:
        return width >= height

    def _is_valid_photo_size(self, width: int, height: int, max_size: int) -> bool:
        return width <= max_size and height <= max_size

    def _get_sizes_params_with_ratio_save(self, image: Image, max_size: int) -> tuple[int, int]:
        width, height = image.size

        if self._is_valid_photo_size(width, height, max_size):
            return width, height

        if self._is_horizontal_photo(width, height):
            times_less = max_size / width
        else:
            times_less = max_size / height

        return int(width * times_less), int(height * times_less)
