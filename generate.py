import torch
from diffusers import StableDiffusionPipeline
import argparse
from PIL import Image

def generate_image(prompt, output_path):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    image = pipe(prompt).images[0]
    image.save(output_path)
    print(f"图片已保存到 {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    generate_image(args.prompt, args.output)