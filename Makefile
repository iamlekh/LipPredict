clean:
	@rm -rfv */*/__pycache__
	@rm -rfv */__pycache__
	@rm -rfv *__pycache__
	@find . -type f -name "*.log" -exec rm -f {} \;
	@rm -rf mlruns
	@clear
format:
	@python -m black -l 100 */*/*.py
	@python -m black -l 100 */*.py
	@python -m black -l 100 *.py
git_add:
	git add .
git_commit_d:
	git commit -m "--"
git_push:
	git push origin main
git: clean format git_add git_commit_d git_push

utest:
	@python -m pytest bank/tests/basic_test.py

condaenv:
	@conda activate /Users/darpan/Documents/code/bank_term_deposit/env
doc:
	mkdocs serve





