python -u experiment.py -N 100000 -m 4000 -n 256 -s 2 | tee 256.txt
python -u experiment.py -N 100000 -m 4000 -n 512 -s 2 | tee 512.txt
python -u experiment.py -N 100000 -m 4000 -n 1024 -s 2 | tee 1024.txt
python -u experiment.py -N 100000 -m 4000 -n 2048 -s 2 | tee 2048.txt
python -u experiment.py -N 100000 -m 4000 -n 4096 -s 2 | tee 4096.txt
