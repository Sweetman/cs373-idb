FILES :=                              						\
  apiary.apib                      						\
  IDB1.log                      						\
  model.html                           						\
  idb/models.py                         						\
  idb/tests.py                          						\
  UML.pdf		  
\

all:

check:
	@for i in $(FILES);                                         		\
    do                                                          		\
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; 		\
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  models.html
	rm -f  IDB1.log
	rm -rf __pycache__

models.html:
	pydoc3 -w idb/models.py

IDB.log:
	git log > IDB1.log

test: TestHardcarry.out

TestHardcarry.out: tests.py
	coverage3 run --branch tests.py > tests.out 2>&1
	coverage3 report -m             >> tests.out