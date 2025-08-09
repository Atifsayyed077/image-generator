# image-generator
AI Image Generator – Stable Diffusion Powered A Python-based image generation tool using Stable Diffusion via Hugging Face Diffusers. Generate stunning, high-quality art from text prompts – supports CPU & GPU, customizable prompts, and model fine-tuning (LoRA/DreamBooth). Perfect for experimenting with AI-powered creativity.
🖼️ AI Image Generator
Turn your words into art!
This project uses Stable Diffusion with the Hugging Face Diffusers library to generate high-quality, detailed images from text prompts.
It works on Windows, Mac, and Linux, and supports both CPU and GPU execution.

✨ Features
Text-to-Image Generation – Create art from simple text prompts.

CPU & GPU Support – Works even without a GPU (slower on CPU).

Custom Prompts – Describe anything you can imagine.

Model Flexibility – Easily switch between Stable Diffusion versions.

Fine-Tuning Ready – Supports LoRA & DreamBooth for personalized models.

Lightweight Code – Minimal dependencies, easy to set up in VS Code.

🚀 Quick Start
bash
Copy
Edit
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install diffusers transformers accelerate safetensors pillow

# Run the script
python image_gen.py
📝 Example Prompt
python
Copy
Edit
prompt = "A muscular Batman in a dark graveyard, cinematic lighting, highly detailed, digital art"
📸 Example Output
