import subprocess
import sys

import joblib
from joblib import delayed

VERBOSITY = 100000

try:
    duration = sys.argv[1]
except IndexError:
    duration = 10000

try:
    jobs = sys.argv[2]
except IndexError:
    jobs = 8


def run_subprocess():
    print('START')
    subprocess.run(['./sample', str(duration)])
    print('END')


if __name__ == '__main__':
    with joblib.Parallel(n_jobs=jobs, verbose=VERBOSITY) as parallel:
        parallel_jobs = [delayed(run_subprocess)() for i in range(6)]

        parallel(parallel_jobs)
