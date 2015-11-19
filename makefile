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

database: scrap_db.sql setup_db.py getChampionData.py getChampYoutube.py getFeaturedGames.py getTxtFeaturedGames.py
	psql -f scrap_db.sql
	python setup_db.py 
	python getChampionData.py 
	python getChampYoutube.py
	python getFeaturedGames.py
	python getTxtFeaturedGames.py

models.html:
	pydoc3 -w models.py

IDB.log:
	git log > IDB3.log

test: TestHardcarry.out

TestHardcarry.out: tests.py
	coverage run tests.py
	coverage report --include=models.py