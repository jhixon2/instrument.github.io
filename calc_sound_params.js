/* fun get_freqs(shapeDict):                                                // maybe just do brightness if this doesn't work
    frewqs = []
    for shape in shapeDict:
        counter = {}    // default dict to 0 if possible to just += 1
        for point in points:
            if point[0] in counter.keys():
                counter[point[0]] += 1
            else:
                counter[point[0]] = 1
        total = len(counter.keys())
        amts = []
        for key in keys:
            amts.append(counter[keys])
        amts.sort()
        if total % 2 == 0:
            median = (amts[total / 2] + amts[(total / 2) - 1]) / 2
        else:
            median = amts[total / 2] / 2
        prev = counter[counter.keys()[0]]
        crosses = 0
        for key in counter.keys():
            if prev > median != counter[key] > median:
                crosses += 1
        freqs.append(map(crosses / total, 0, 1, 10, 10000))
    return freqs
*/

/* fun get_volume(shapeDict):
    volumes = []
    for shape in shapeDict:
        numPixels = len(shape[0]) * len(shape)
        volumes.append(map(numPixels, 1 4096, ?, ?))
    return volumes
*/

/* fun get_timbres(shapeDict):
    timbres = []
    for shape in shapeDict:
        colorVal = (color[0]) * 65536 + (color[1] * 256) + color[2]
        timbres.append(...)
    return timbres
*/