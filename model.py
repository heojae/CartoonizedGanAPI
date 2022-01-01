import numpy as np
import torch
import PIL

from torchvision.transforms import transforms

from PIL import Image

from config.exception import InvalidImageModeException


class JitCycleGANModel:
    # i extract transform condition from original cycle gan repo
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # if you want to apply mlops, you need to get model from aws s3 or google drive
    jit_path = "./weight/jit_real_to_cartoon.pth"

    def __init__(self):
        self.model = torch.jit.load(self.jit_path)
        self.model.eval()

    @staticmethod
    def convert_pil_to_tensor(pil_image: PIL.Image.Image) -> torch.Tensor:

        if pil_image.mode == "RGB":
            pass
        elif pil_image.mode in ("L", "RGBA"):
            pil_image = pil_image.convert("RGB")
        else:
            raise InvalidImageModeException

        image: torch.Tensor = JitCycleGANModel.transform(pil_image)  # [3, 224, 224]
        return image.unsqueeze(dim=0)  # [1, 3, 224, 224]

    @staticmethod
    def convert_tensor_to_pil(tensor_image: torch.Tensor) -> PIL.Image.Image:
        # tensor_image : [1, 3, 256, 256]
        image_numpy = tensor_image[0].cpu().float().numpy()
        image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 255.0  # post-processing: transpose and scaling
        return Image.fromarray(image_numpy.astype(np.uint8))

    def inference(self, pil_image: PIL.Image.Image) -> PIL.Image.Image:
        tensor_image = self.convert_pil_to_tensor(pil_image)

        with torch.no_grad():
            output_tensor: torch.Tensor = self.model(tensor_image)  # [1, 3, 256, 256]

        return self.convert_tensor_to_pil(output_tensor)


if __name__ == '__main__':
    load_path = "./sample/a.png"
    output_path = "./sample/jit_cg_a.jpeg"
    input_pil_image = Image.open(load_path)

    jit_cg_model = JitCycleGANModel()
    output_pil_image = jit_cg_model.inference(input_pil_image)
    output_pil_image.save(output_path)
