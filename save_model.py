import torch
model = torch.load("output_dir_base_h_coco_22/checkpoint-latest.pth")
y1 = model['model']
torch.save({
            'model': y1,
            }, "output_dir_base_h_coco_22/my_pretrain_vit_bath_coco_sim_h.pth")