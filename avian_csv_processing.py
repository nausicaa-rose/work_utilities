"""
Some quick and dirty functions for comparing dates in various fields in CSV 
exports from avIAn. 
"""
import re
import csv

def read_it_in(f_handle):
    base = 'C:/path/to/file.csv'
    with open(f'{base}/{f_handle}', 'r') as fh:
        data = list(csv.reader(fh))
        return data


def print_it_out(data):
    year_match = re.compile('[0-9]{4}')
    for x in data[1:]:
        print(f'{x[0]} {year_match.search(x[4]).group()} {year_match.search(x[17]).group()} {year_match.search(x[15]).group()}')


def print_it_out2(data):
    das_pattern = re.compile('((January|February|March|April|May|June|July|August|September|October|November|December|Winter|Spring||summer|Fall)? ?([0-9]+ )?[0-9]{4})', re.IGNORECASE)
    for x in data[1:]:
        print(f'{x[0]} {das_pattern.search(x[4]).group()} | {das_pattern.search(x[17]).group()} | {das_pattern.search(x[15]).group()}')


def print_it_out3(data):
    das_pattern = re.compile('((January|February|March|April|May|June|July|August|September|October|November|December|Winter|Spring||summer|Fall)? ?([0-9]+ )?[0-9]{4})', re.IGNORECASE)
    for x in data[1:]:
        date = das_pattern.search(x[15]).group() if das_pattern.search(x[15]) is not None else None
        description = das_pattern.search(x[17]).group() if das_pattern.search(x[17]) is not None else None
        title = das_pattern.search(x[4]).group() if das_pattern.search(x[4]) is not None else None
        if title is None or description is None or date is None:
            print(f'{x[0]} | {x[4]}') 
        else:
            print(f'{x[0]},{das_pattern.search(x[4]).group()},{das_pattern.search(x[17]).group()},{das_pattern.search(x[15]).group()}')

            
def print_it_out4(data):
      das_pattern = re.compile('((January|February|March|April|May|June|July|August|September|October|November|December|Winter|Spring||summer|Fall)? ?([0-9]+ )?[0-9]{4})', re.IGNORECASE)
      for x in data[1:]:
           if x[4] != 'DELETE':
               print(f'{x[0]} {das_pattern.search(x[4]).group()} | {das_pattern.search(x[17]).group()} | {das_pattern.search(x[15]).group()}')


def print_it_out5(data):               
      das_pattern = re.compile('((January|February|March|April|May|June|July|August|September|October|November|December|Winter|Spring||summer|Fall)? ?([0-9]+ )?[0-9]{4})', re.IGNORECASE)
      for x in data[1:]:
           date = das_pattern.search(x[15]).group() if das_pattern.search(x[15]) is not None else None
           description = das_pattern.search(x[17]).group() if das_pattern.search(x[17]) is not None else None
           title = das_pattern.search(x[4]).group() if das_pattern.search(x[4]) is not None else None
           if title is None or description is None or date is None:
               if x[4] != 'DELETE':
                  print(f'{x[0]} | {x[4]}') 
           else:
               print(f'{x[0]} {das_pattern.search(x[4]).group()} | {das_pattern.search(x[17]).group()} | {das_pattern.search(x[15]).group()}')


def group_it_out3(data):
    output = []
    das_pattern = re.compile('((January|February|March|April|May|June|July|August|September|October|November|December|Winter|Spring||summer|Fall)? ?([0-9]+ )?[0-9]{4})', re.IGNORECASE)
    for x in data[1:]:
        date = das_pattern.search(x[15]).group() if das_pattern.search(x[15]) is not None else None
        description = das_pattern.search(x[17]).group() if das_pattern.search(x[17]) is not None else None
        title = das_pattern.search(x[4]).group() if das_pattern.search(x[4]) is not None else None
        if title is None or description is None or date is None:
            output.append([x[0], x[4]])          
        else:
            output.append([x[0], das_pattern.search(x[4]).group().strip(),das_pattern.search(x[17]).group().strip(),das_pattern.search(x[15]).group().strip()])
    return output


def group_it_out4(data):               
      das_pattern = re.compile('((January|February|March|April|May|June|July|August|September|October|November|December|Winter|Spring||summer|Fall)? ?([0-9]+ )?[0-9]{4})', re.IGNORECASE)
      outarray = []
      for x in data[1:]:
           date = das_pattern.search(x[15]).group() if das_pattern.search(x[15]) is not None else None
           description = das_pattern.search(x[17]).group() if das_pattern.search(x[17]) is not None else None
           title = das_pattern.search(x[4]).group() if das_pattern.search(x[4]) is not None else None
           if title is None or description is None or date is None:
               if x[4] != 'DELETE':
                  outarray.append([x[0], x[4]])
           else:
               outarray.append([das_pattern.search(x[0]).group(), das_pattern.search(x[4]).group(), das_pattern.search(x[17]).group(), das_pattern.search(x[15]).group()])
      return outarray        


def write_it_out4(data, outfile):               
      das_pattern = re.compile('((January|February|March|April|May|June|July|August|September|October|November|December|Winter|Spring||summer|Fall)? ?([0-9]+ )?[0-9]{4})', re.IGNORECASE)
      file_base = '/home/wt/Downloads/avian_csv'
      
      with open(f'{file_base}/{outfile}', 'w') as fh:
          for x in data[1:]:
               date = das_pattern.search(x[15]).group() if das_pattern.search(x[15]) is not None else None
               description = das_pattern.search(x[17]).group() if das_pattern.search(x[17]) is not None else None
               title = das_pattern.search(x[4]).group() if das_pattern.search(x[4]) is not None else None
               if title is None or description is None or date is None:
                   if x[4] != 'DELETE':
                      fh.write(f'{x[0]} | {x[4]}\n') 
               else:
                   fh.write(f'{x[0]} {das_pattern.search(x[4]).group()} | {das_pattern.search(x[17]).group()} | {das_pattern.search(x[15]).group()}\n')