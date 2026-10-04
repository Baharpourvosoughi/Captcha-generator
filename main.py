import secrets
import string
from pathlib import Path
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha


def generate_random_captcha_text(length: int = 6, digits_only: bool = False) -> str:
    """Generate a secure random text for CAPTCHA."""
    characters = string.digits if digits_only else (string.ascii_uppercase + string.digits)
    return "".join(secrets.choice(characters) for _ in range(length))


def generate_image_captcha(text: str, output_path: str = "captcha.png") -> str:
    """Generate an image CAPTCHA challenge."""
    image_captcha = ImageCaptcha(width=280, height=90)
    image_captcha.write(text, output_path)
    return output_path


def generate_audio_captcha(text: str, output_path: str = "captcha.wav") -> str:
    """
    Generate an audio CAPTCHA challenge.
    Note: captcha library audio supports digit strings.
    """
    audio_captcha = AudioCaptcha()
    audio_captcha.write(text, output_path)
    return output_path


def main():
    # Create an output directory for clean organization
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Audio CAPTCHA (requires numeric values)
    audio_code = generate_random_captcha_text(length=6, digits_only=True)
    audio_file = output_dir / f"audio_{audio_code}.wav"
    generate_audio_captcha(audio_code, str(audio_file))
    print(f"Generated Audio CAPTCHA -> Code: {audio_code} | Saved: {audio_file}")

    # Image CAPTCHA (alphanumeric)
    image_code = generate_random_captcha_text(length=6, digits_only=False)
    image_file = output_dir / f"image_{image_code}.png"
    generate_image_captcha(image_code, str(image_file))
    print(f"Generated Image CAPTCHA -> Code: {image_code} | Saved: {image_file}")


if __name__ == "__main__":
    main()
