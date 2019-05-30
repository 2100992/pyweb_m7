#encoding: utf-8

from my_logging import get_logger

logger = get_logger('plots_analyser')

class AreaRecord:
    def __init__(self, line):
        try:
            plot_id, _, xy, _, lw = line.split()
            _, plot_id = plot_id.split('#')
            x, y = xy.split(',')
            l, w = lw.split('x')
            self.id = plot_id
            self.x = int(x)
            self.y = int(y)
            self.long = int(l)
            self.width = int(w)
        except Exception as err:
            logger.error(f'Error ({err}) in parsing in line - : {line}')
            self.id = '_'
            self.x = 0
            self.y = 0
            self.long = 0
            self.width = 0

    def get_elongation(self):
        if (self.long * self.width) == 0:
            e = 0
        else:
            e = self.long / self.width
            if e < 1:
                e = 1 / e
        return e

    def get_area(self):
        a = self.long * self.width
        return a


def get_max_area(record, last_list):
    if record.get_area() > last_list[0].get_area():
        return [record]
    elif record.get_area() == last_list[0].get_area():
        last_list.append(record)
        return last_list
    else:
        return last_list

def get_max_elongation(record, last_list):
    if record.get_elongation() > last_list[0].get_elongation():
        return [record]
    elif record.get_elongation() == last_list[0].get_elongation():
        last_list.append(record)
        return last_list
    else:
        return last_list


def main():

    files = [
        'm7-map-1.txt',
        'm7-map-2.txt',
        'm7-map-3.txt'
    ]

    max_area_records = [AreaRecord('_')]
    max_elongation_records = [AreaRecord('_')]
    summ_area = 0
    counter = 0

    for reading_file in files:
        try:
            with open(reading_file) as f:
                line = f.readline()
                record = AreaRecord(line)
                
                while len(line) != 0:

                    max_area_records = get_max_area(record, max_area_records)
                    
                    max_elongation_records = get_max_elongation(record, max_elongation_records)
                    
                    summ_area += record.get_area()
                    
                    if record.id != '_':
                        counter += 1
                
                    line = f.readline()
                    record = AreaRecord(line)
        
        except Exception as err:
            logger.error(f'Error ({err}) in reading file -  {reading_file}')

    max_area_records_ids = []
    max_elongation_records_ids = []

    for a in max_area_records:
        max_area_records_ids.append(a.id)

    for e in max_elongation_records:
        max_elongation_records_ids.append(e.id)


    print(f'Средняя площадь участков - {summ_area / counter}')
    print(f'Число корректных записей - {counter}')
    print(f'Участок/участки ({max_area_records_ids}) с максимальной площадью -  {max_area_records[0].get_area()}')
    print(f'Участок/участки ({max_elongation_records_ids}) с максимальной вытянутостью - {max_elongation_records[0].get_elongation()}')

    pass

if __name__ == "__main__":
    main()
 



