from PIL import Image
import os

# Path ke folder dataset
data_dir = r"C:\Users\HP\Downloads\dataset\validation_data"

# Format file gambar yang didukung
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Periksa file korup
for root, dirs, files in os.walk(data_dir):
    for file in files:
        file_path = os.path.join(root, file)
        if file.lower().endswith(valid_extensions):  # Hanya periksa file gambar
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verifikasi file gambar
            except (IOError, SyntaxError):
                print(f"Corrupted file detected: {file_path}")
                # Uncomment baris di bawah untuk menghapus file korup
                # os.remove(file_path)
