from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
# 'Nottinghamfolk send $10 to the ditch fund.'

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-2-76a3651bb772> in <cell line: 3>()
      1 t = Template('Return the $item to $owner.')
      2 d = dict(item='unladen swallow')
----> 3 t.substitute(d)
# /usr/lib/python3.10/string.py in substitute(self, mapping, **kws)
    119             raise ValueError('Unrecognized named group in pattern',
    120                              self.pattern)
--> 121         return self.pattern.sub(convert, self.template)
    122 
    123     def safe_substitute(self, mapping=_sentinel_dict, /, **kws):
# /usr/lib/python3.10/string.py in convert(mo)
    112             named = mo.group('named') or mo.group('braced')
    113             if named is not None:
--> 114                 return str(mapping[named])
    115             if mo.group('escaped') is not None:
    116                 return self.delimiter
# KeyError: 'owner'

t.safe_substitute(d)
# 'Return the unladen swallow to $owner.'

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
# img_1074.jpg --> Ashley_0.jpg
# img_1076.jpg --> Ashley_1.jpg
# img_1077.jpg --> Ashley_2.jpg

