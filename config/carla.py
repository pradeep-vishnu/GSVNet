class carla_config(object):
    weights = [ 3.03871497 , 13.01999212, 4.53008444 , 38.00898985, 35.35990217,
                31.14247824, 45.82106668, 39.44451896, 6.00002668 , 32.64759009,
                17.34725897, 31.45715227, 47.0853521 , 11.70166965, 44.50966853,
                44.80501487, 45.63057065, 48.21080448, 41.21912833]
    ignore_index=0
    num_classes = 19
    color_classes = [
        ('road', (128, 64, 128), 7),
        ('sidewalk', (244, 35, 232), 8),
        ('building', (70, 70, 70), 1),
        ('wall', (102, 102, 156), 11),
        ('fence', (100, 40, 40), 2),
        ('pole', (153, 153, 153), 5),
        ('traffic_light', (250, 170, 30), 18),
        ('traffic_sign', (220, 220, 0), 12),
        ('vegetation', (107, 142, 35), 9),
        ('terrain', (170, 120, 50), 22),
        ('sky', (70, 130, 180), 13),
        ('person', (220, 20, 60), 4),
        ('dynamic_objects', (170, 120, 50), 20),
        ('car', (0, 0, 142), 10),
        ('static_objects', (110, 190, 160), 19),
        ('gaurdRail', (180, 165, 180), 17),
        ('water', (45, 60, 150), 21),
        ('roadlines', (157, 234, 50), 6),
        ('others', (55, 90, 80), 3),
        ('void', (0, 0, 0), ignore_index)
    ] 

    swnet_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-swnet-R18.pt'
    bsnet_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-bisenet-R18.pth'

    bsnet_x39_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-bisenet-X39.pth'
    bsnet_r101_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-bisenet-R101.pth'
    dfn_r101_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-dfn-R101_v1c.ohem.pth'
    dfn_raw_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/voc-dfn-R101_v1c.pth'


    bisenet_resume_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/gsvnet_bisenet_r18.tar'
    swnet_resume_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/gsvnet_swnet_r18.tar'
    optical_flow_network_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/flownet.pth.tar'
    data_path = '/gpfs1/dlocal/home/2018015/PARTAGE/dataset/carla/carla_0.2/' # put your data path here
