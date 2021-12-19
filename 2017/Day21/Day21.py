infile = open("Day21.txt", "r")

rotate2 = {0:1, 1:4, 4:3, 3:0}
rotate3 = {0:2, 1:6, 2:10, 4:1, 5:5, 6:9, 8:0, 9:4, 10:8}

def flip(img):
    if len(img) == 5:
        return img[3:] + "/" + img[:2]
    else:
        return img[8:] + img[3:8] + img[:3]

def rotate(img):
    newImg = img
    if len(img) == 5:
        for i in range(len(img)):
            if img[i] != "/":
                index = rotate2[i]
                newImg = newImg[:index] + img[i] + newImg[index + 1:]
    else:
        for i in range(len(img)):
            if img[i] != "/":
                index = rotate3[i]
                newImg = newImg[:index] + img[i] + newImg[index + 1:]
    return newImg

def enhance(img, enhancements):
    size = img.index("/")
    if size % 2 == 0:
        iters = size // 2
        newSize = iters * 3
        rows = ["" for i in range(newSize)]
        for r in range(iters):
            for c in range(iters):
                start = r * 2 * (size + 1) + c * 2
                imgPart = enhancements[img[start:start + 2] + "/" + img[start + size + 1:start + size + 3]]
                for i in range(3):
                    rows[r * 3 + i] += imgPart[i * 4:i * 4 + 3]
        return '/'.join(rows)
    elif size % 3 == 0:
        iters = size // 3
        newSize = iters * 4
        rows = ["" for i in range(newSize)]
        for r in range(iters):
            for c in range(iters):
                start = r * 3 * (size + 1) + c * 3
                imgPart = enhancements[img[start:start + 3] + "/" + img[start + size + 1:start + size + 4] + "/" + img[start + (size + 1) * 2:start + (size + 1) * 2 + 3]]
                for i in range(4):
                    rows[r * 4 + i] += imgPart[i * 5:i * 5 + 4]
        return '/'.join(rows)

enhancements = {}
for line in infile.readlines():
    img, enhancement = line.rstrip().split(" => ")
    enhancements[img] = enhancement
    for i in range(3):
        img = rotate(img)
        enhancements[img] = enhancement
    img = flip(img)
    enhancements[img] = enhancement
    for i in range(3):
        img = rotate(img)
        enhancements[img] = enhancement

img = ".#./..#/###"
for i in range(18):
    img = enhance(img, enhancements)
print(img.count("#"))