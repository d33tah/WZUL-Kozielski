#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Analizuje wyniki prac z Podstaw Marketingu zadanych przez
prof. Roberta Kozielskiego na WZ UŁ.

BY d33tah, LICENSED UNDER WTFPL.

TODO: 
  * zakładamy, że nazwisko składa się z 2 członów
  * brak autodetekcji liczby wpisów
  * liczenie wyników poszczególnych prac?
"""

import pyPdf
from sys import argv

#liczba_wpisow = 99

class Student:
  def __init__(self, nazwisko, merytoryczna, rzetelnosc, kreatywnosc,
	       formalna, razem_proc, total):
    self.nazwisko = nazwisko
    self.merytoryczna = merytoryczna
    self.rzetelnosc = rzetelnosc
    self.kreatywnosc = kreatywnosc
    self.formalna = formalna
    self.razem_proc = razem_proc
    self.total = total
    
  def __repr__(self):
    return repr((self.nazwisko,    self.merytoryczna, self.rzetelnosc,
		self.kreatywnosc, self.formalna, self.razem_proc, self.total))

def getPDFContent(path):
    content = ""
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText()
    return content

def parseResultsFile(filename):
  contents = getPDFContent(filename)
  print contents
  results = contents.rstrip().split(' ')
  ret = []
  i_id = 0
  while 1:
      shift = i_id*8
      entry = results [ -8-shift : len(results)-shift ]
      #print entry
      try:
	for i in entry[2:]: int(i)
      except:
	break
      nazwisko = ' '.join(entry[0:2])
      ret.append(Student( *(nazwisko, ) + tuple(int(a) for a in entry[2:]) ))
      i_id+=1
  return ret

if __name__ == "__main__":
    students = parseResultsFile(argv[1])
    lp = 0
    for a in reversed(sorted(students, key=lambda student: student.total)):
     lp += 1
     print "%3d: %s" % (lp, a)
