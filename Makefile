root_dir		= $(realpath .)
src_dir			= ${root_dir}/trote_game

install:
	@pip install -r requirements.txt

install_local:
	@pip install -r requirements-local.txt

clean:
	@find . -type f -name "*.pyc" -exec rm -rf {} \;

kill_run:
	@ps aux | awk '(make run && $$0 !~ /awk/){ system("kill -9 "$$2) }'

run: clean
	@python ${src_dir}/app.py
