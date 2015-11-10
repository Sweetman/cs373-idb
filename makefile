FILES :=                              						\
  apiary.apib                      						\
  IDB.log                      						\
  model.html                           						\
  models.py                         						\
  tests.py                          						\
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
	pydoc3 -w models.py

IDB.log:
	git log > IDB.log

test: TestHardcarry.out

TestHardcarry.out: tests.py
	coverage run --branch tests.py
	coverage report --include=models.py