class carla_config(object):
    weights = [ 4.927 , 6.8403, 31.216 , 46.7649, 30.7612,
                27.56,33.7536, 3.3284, 27.56 , 27.56,
                27.9024, 27.56, 27.56 , 17.6963, 17.6963,
                17.6963, 17.6963, 17.6963, 8.714]
    ignore_index=250
    num_classes = 19
    color_classes = [
        ('road', (128, 64, 128), 0),
        ('sidewalk', (244, 35, 232), 8),
        ('building', (70, 70, 70), 1),
        ('wall', (102, 102, 156), 11),
        ('fence', (100, 40, 40), 2),
        ('pole', (153, 153, 153), 5),
        ('traffic_light', (250, 170, 30), 18),
        ('traffic_sign', (220, 220, 0), 12),
        ('vegetation', (107, 142, 35), 9),
        ('terrain', (145, 170, 100), 22),
        ('sky', (70, 130, 180), 13),
        ('person', (220, 20, 60), 4),
        ('rider', (220, 20, 60), 4),
        ('car', (0, 0, 142), 10),
        ('truck', (0, 0, 142), 10),
        ('bus', (0, 0, 142), 10),
        ('train', (0, 0, 142), 10),
        ('motorcycle', (0, 0, 142), 10),
        ('bicycle', (0, 0, 142), 10),
        ('void', (0, 0, 0), ignore_index)
    ] 

    swnet_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-swnet-R18.pt'
    bsnet_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-bisenet-R18.pth'
    bisenet_resume_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/gsvnet_bisenet_r18.tar'
    swnet_resume_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/gsvnet_swnet_r18.tar'
    optical_flow_network_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/flownet.pth.tar'
    data_path = '/gpfs1/dlocal/home/2018015/PARTAGE/dataset/carla/carla_0.2/' # put your data path here
