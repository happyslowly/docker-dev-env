#!/usr/bin/env python

import tempfile
import shutil
import tarfile
import os

must = ['manifest.json', 'repositories']


def create_diff(base_file, derived_file):
    with tarfile.open(base_file) as base_tar, tarfile.open(derived_file) as derived_tar:
        diff = {}

        base = get_tar_entries(base_tar)
        derived = get_tar_entries(derived_tar)

        for k in derived:
            if k not in base:
                diff[k] = derived[k]
            else:
                if derived[k].size != base[k].size:
                    diff[k] = derived[k]

        for m in must: diff[m] = derived[m]

        tempd = tempfile.mkdtemp()

        for e in diff.values():
            derived_tar.extract(e, tempd)

        with open(os.path.join(tempd, 'remove.txt'), 'w') as fout:
            for k in base:
                if k not in derived:
                    fout.write(k + '\n')

        pwd = os.path.dirname(os.path.realpath(__file__))
        os.chdir(tempd)
        with tarfile.open('diff.tar', 'w') as diff_tar:
            for f in os.listdir('.'):
                diff_tar.add(f)

        shutil.copyfile(os.path.join(tempd, 'diff.tar'),
                os.path.join(pwd, 'diff.tar'))

        shutil.rmtree(tempd)


def get_tar_entries(tar_file):
    return dict([ (e.name, e) for e in tar_file ])


if __name__ == '__main__':
    import sys
    base_file = sys.argv[1]
    derived_file = sys.argv[2]
    create_diff(base_file, derived_file)
