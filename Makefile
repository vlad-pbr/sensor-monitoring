run:
	python .

smtp:
	python -m smtpd -c DebuggingServer -n localhost:1025

tests:
	python -m unittest discover -s test