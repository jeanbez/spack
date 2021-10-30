# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class H5bench(CMakePackage):
    """A benchmark suite for measuring HDF5 performance."""

    homepage = 'https://github.com/hpc-io/h5bench'
    git      = 'https://github.com/hpc-io/h5bench.git'
    url      = 'https://github.com/hpc-io/h5bench/archive/refs/tags/1.0.tar.gz'

    maintainers = ['jeanbez', 'sbyna']

    version('master', branch='master')
    version('develop', branch='develop')

    version('1.0', sha256='c9151d0c138990f7fc684501f7a7e99d8727317b5169809ddbb63d8e84c9fa3f', deprecated=True)
    version('1.1', sha256='8d7ba7d835a9a08d88b1a9c6289eafbf67e3a1ea87435799f276809db9df3d77')

    depends_on('cmake@3.10:', type='build')
    depends_on('mpi')
    depends_on('hdf5+mpi@1.12.0:1,develop-1.12:')

    @run_after('install')
    def install_config(self):
        install_tree('h5bench_patterns/sample_config',
                     self.prefix.share.patterns)
        install('metadata_stress/hdf5_iotest.ini',
                self.prefix.share)

    def setup_build_environment(self, env):
        env.set('HDF5_HOME', self.spec['hdf5'].prefix)
