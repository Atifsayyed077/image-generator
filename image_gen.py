from diffusers import StableDiffusionPipeline
import torch

# Load model (first time download will be ~4GB)
model_id = "runwayml/stable-diffusion-v1-5"

import torch

if torch.cuda.is_available():
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
else:
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe = pipe.to("cpu")

# Prompt for image generation
prompt = "a girl with a red hat, sitting on a bench in a park, sunny day" \
"with a clear blue sky, surrounded by trees and flowers"

# Generate image
image = pipe(prompt).images[0]

# Save image
image.save("generated_image.png")

print("✅ Image saved as generated_image.png")
