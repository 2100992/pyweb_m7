from my_logging import get_logger

logger = get_logger('plots_analysis')


def find_area(record):
    a = int(record['l']) * int(record['w'])
    return a


def find_max_area(record1, record2):
    if find_area(record1) > find_area(record2):
        return record1
    else:
        return record2


def elongation(l, w):
    if (l * w) == 0:
        e = 0
    else:
        e = l / w
        if e < 1:
            e = 1 / e
    return e


def find_max_elongation(record1, record2):
    if elongation(int(record1['l']), int(record1['w'])) > elongation(int(record2['l']), int(record2['w'])):
        return record1
    else:
        return record2


def record_parser(record):
    try:
        plot_id, _, xy, _, lw = record.split()
        _, plot_id = plot_id.split('#')
        x, y = xy.split(',')
        l, w = lw.split('x')
        return {'id': plot_id, 'x': x, 'y': y, 'l':l, 'w': w}
    except Exception as err:
        logger.error(f'Ошибка {err} в парсинге строки: {record}')
        return {'id': '_', 'x': 0, 'y': 0, 'l':0, 'w': 0}


def file_analysis(path_file):
    with open(path_file) as f:
        summ_area = 0
        counter = 0
        line = f.readline()
        record = record_parser(line)
        max_area = record
        max_elongation = record
        while len(line) != 0:
            max_area = find_max_area(record, max_area)
            max_elongation = find_max_elongation(record, max_elongation)
            summ_area += int(record['l']) * int(record['w'])
            if record['id'] != '_':
                counter +=1
            
            line = f.readline()
            record = record_parser(line)
    return {'max_area': max_area, 'max_elongation': max_elongation, 'summ_area':summ_area, 'counter': counter}

def main():
    file1parser = file_analysis('m7-map-1.txt')
    file2parser = file_analysis('m7-map-2.txt')
    max_area = find_max_area(file1parser['max_area'], file2parser['max_area'])
    max_elongation = find_max_elongation(file1parser['max_elongation'], file2parser['max_elongation'])
    counter = file1parser['counter'] + file2parser['counter']
    summ_area = file1parser['summ_area'] + file2parser['summ_area']
    print(f'Средняя площадь участков - {summ_area / counter}')

    print(file1parser)
    print(file2parser)


    print(f'Участок ({max_area["id"]}) с максимальной площадью -  {int(max_area["l"]) * int(max_area["w"])}')
    print(f'Участок ({max_elongation["id"]}) с максимальной вытянутостью - {elongation(int(max_elongation["l"]), int(max_elongation["w"]))}')
    pass

if __name__ == "__main__":
    main()