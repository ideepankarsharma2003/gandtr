import os
import requests
import urllib.request

# Create a folder to store all models
os.makedirs("dark_side_models", exist_ok=True)

# Model URLs from the paper
MODEL_URLS = {
    # Day-to-night generators
    "cyclegan_generator_X.pth": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/cyclegan_generator_X.pth",
    "hedngan_generator_X.pth": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/hedngan_generator_X.pth",

    # Embedding models - VGG16
    "cyclegan_embed_vgg16.pth": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/cyclegan_embed_vgg16.pth",
    "cyclegan_embed_vgg16_lw.pkl": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/cyclegan_embed_vgg16_lw.pkl",
    "hedngan_embed_vgg16.pth": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/hedngan_embed_vgg16.pth",
    "hedngan_embed_vgg16_lw.pkl": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/hedngan_embed_vgg16_lw.pkl",

    # Embedding models - ResNet101
    "cyclegan_embed_resnet101.pth": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/cyclegan_embed_resnet101.pth",
    "cyclegan_embed_resnet101_lw.pkl": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/cyclegan_embed_resnet101_lw.pkl",
    "hedngan_embed_resnet101.pth": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/hedngan_embed_resnet101.pth",
    "hedngan_embed_resnet101_lw.pkl": "http://ptak.felk.cvut.cz/personal/jenicto2/download/iccv23_gan/hedngan_embed_resnet101_lw.pkl",
}

def download_file(url, dest):
    """Download file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 8192
    progress = 0

    with open(dest, 'wb') as f:
        for data in response.iter_content(block_size):
            progress += len(data)
            f.write(data)
            done = int(50 * progress / total_size) if total_size else 0
            print(f"\r[{'=' * done}{' ' * (50-done)}] {progress/1024/1024:.2f} MB", end='')

    print(f"\n✅ Downloaded: {dest}")

# Download all models
for filename, url in MODEL_URLS.items():
    dest_path = os.path.join("dark_side_models", filename)
    if os.path.exists(dest_path):
        print(f"⏩ Skipping (already exists): {filename}")
        continue
    print(f"⬇️  Downloading {filename} ...")
    download_file(url, dest_path)

print("\n🎉 All models downloaded into 'dark_side_models/'")


