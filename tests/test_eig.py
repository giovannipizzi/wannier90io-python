import pathlib

import numpy as np
import pytest
import w90io


@pytest.mark.parametrize('example', ['example02', 'example03', 'example04'])
def test_read_eig(wannier90, example):
    with open(pathlib.Path(wannier90)/f'examples/{example}/wannier.eig', 'r') as fh:
        eig = w90io.read_eig(fh)

        fh.seek(0)
        for line in fh.readlines():
            [n_idx, k_idx, e1] = np.fromstring(line, sep=' ')
            k_idx = int(k_idx) - 1
            n_idx = int(n_idx) - 1

            assert(abs(eig[k_idx, n_idx] - e1) < 1e-12)