import os

os.system('CUDA_VISIBLE_DEVICES=0,1 python -m torch.distributed.launch --master_port 1111 --nproc_per_node 2 main.py --segnet swiftnet --optical-flow-network light --checkname GSV_0.2 --dataset carla --valdataset cityscapes')
