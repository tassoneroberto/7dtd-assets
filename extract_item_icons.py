#!/usr/bin/env python3

from PIL import Image

path = "./alpha12.5/"

itemIconsImage = Image.open(path + "bundle/ItemIcons.png")

with open(path + 'bundle/ItemIcons.txt') as file:
    w, h = file.readline().split('\t')
    h = int(h)
    w = int(w)

    lines = file.readlines()

    for line in lines:
        itemName, x1, y1 = line.split('\t')
        x1 = int(x1)
        y1 = int(y1)
        x2 = x1 + w
        y2 = y1 + h

        extracted = itemIconsImage.crop((x1, y1, x2, y2))
        extracted.save(path + "./ItemIcons/" + itemName + ".png")
